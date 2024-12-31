import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import re
import subprocess

rclpy.init()
node = Node("cpu_utilization")
pub = node.create_publisher(Float32, "cpu", 10)


def cb():
    msg = Float32()
    result = subprocess.run(["/usr/bin/top", "-b", "-n", "1"], stdout=subprocess.PIPE, text=True)
    output = result.stdout.splitlines()

    if len(output) >= 3:
        cpu_line = output[2]
        cpulist = re.split(r"[,: ]+", cpu_line)
        
        if len(cpulist) >= 8:
            idle = float(cpulist[7])
            msg.data = 100 - idle
            pub.publish(msg)

def main():
    node.create_timer(2, cb)
    rclpy.spin(node)

