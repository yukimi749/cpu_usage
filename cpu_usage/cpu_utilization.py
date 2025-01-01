import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import psutil
#import re
#import subprocess

class Cpu_utilization(Node):
    def __init__(self):
        super().__init__("cpu_utilization")
        self.pub = self.create_publisher(Float32, "cpu", 10)
        self.sub = self.create_subscription(Float32,"cpu",self.subscriber_callback,10)

        self.create_timer(1, self.cb)

    def cb(self):
        msg = Float32()
        self.cpu_usage = psutil.cpu_percent(interval=1)
        msg.data = self.cpu_usage
        self.pub.publish(msg)
        
    def subscriber_callback(self, msg):
        self.get_logger().info(f'cpu_usage: "{msg.data}"')

def main():
    rclpy.init()
    node = Cpu_utilization()
    rclpy.spin(node)
