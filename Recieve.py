# Receiver
import socket
import json

# Set up our receiving socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("192.168.100.113", 5000))

# Receive and print data
while True:
    data = udp_socket.recv(1024)
    data = json.loads(data.decode())
    # initializing the data
    gas = data.get("gas")
    speed = data.get("speed")
    brake = data.get("brake")
    rpm = data.get("rpms")
    steer = data.get("steerangle")
    gear = data.get("gear")

    print("Gas:", gas, "-", "speed:", speed, "-", "brake:", brake, "-", "RPM:",rpm, "-", "steer:",steer, "-", "Gear:",gear)