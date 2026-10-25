# Vehicle Signal Simulator and Viewer

Seeded drive-cycle MQTT publisher at 10 Hz/QoS 1, a FastAPI WebSocket bridge with bounded client queues, React gauges and a rolling chart, and a two-second stale-data indicator.

## Run

Start Mosquitto using compose.yaml. Install requirements.txt, run `uvicorn bridge:app`, then `python publisher.py`. UI: `cd web && npm install && npm run dev`. MQTT_HOST defaults to localhost.
