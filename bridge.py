import asyncio,json,os
from contextlib import asynccontextmanager
import paho.mqtt.client as mqtt
from fastapi import FastAPI,WebSocket
queues=set()
@asynccontextmanager
async def lifespan(app):
 loop=asyncio.get_running_loop();client=mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
 def publish(message):
  for q in list(queues):
   if q.full():q.get_nowait()
   q.put_nowait(message)
 def connected(c,u,f,reason,properties):c.subscribe("vehicle/+/#",qos=1)
 def message(c,u,m):
  try:data={"topic":m.topic,**json.loads(m.payload)}
  except (ValueError,TypeError):return
  loop.call_soon_threadsafe(publish,data)
 client.on_connect=connected;client.on_message=message;client.connect_async(os.getenv("MQTT_HOST","localhost"),1883);client.loop_start()
 yield
 client.disconnect();client.loop_stop()
app=FastAPI(lifespan=lifespan)
@app.websocket("/ws")
async def ws(socket:WebSocket):
 await socket.accept();q=asyncio.Queue(maxsize=100);queues.add(q)
 try:
  while True:await socket.send_json(await q.get())
 finally:queues.discard(q)
