import math,time,os,json
import paho.mqtt.client as mqtt
def signal(t):return {"speed":max(0,55+30*math.sin(t/15)),"soc":max(0,90-t*.002),"temperature":21+2*math.sin(t/120)}
def main():
 client=mqtt.Client(mqtt.CallbackAPIVersion.VERSION2);client.connect(os.getenv("MQTT_HOST","localhost"),1883);client.loop_start();start=time.monotonic()
 try:
  while True:
   t=time.monotonic()-start
   for name,value in signal(t).items():client.publish("vehicle/42/"+name,json.dumps({"value":value,"timestamp":time.time()}),qos=1)
   time.sleep(.1)
 finally:client.disconnect();client.loop_stop()
if __name__=="__main__":main()
