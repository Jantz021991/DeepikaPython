import paho.mqtt.publish as publish
import time
print("0")
publish.single("ledStatus", "0", hostname="192.168.2.5")
time.sleep(1)
print("1")
publish.single("ledStatus", "1", hostname="192.168.2.5")
