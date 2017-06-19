import paho.mqtt.publish as publish
import time
print("0")
publish.single("ledStatus", "0", hostname="DESKTOP-FI57R0D")
time.sleep(1)
print("1")
publish.single("ledStatus", "1", hostname="DESKTOP-FI57R0D")
