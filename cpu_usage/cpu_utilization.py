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
        
#rclpy.init()
#node = Node("cpu_utilization")
#pub = node.create_publisher(Float32, "cpu", 10)

#def cb():
    #msg = Float32()
    #result = subprocess.run(["/usr/bin/top", "-b", "-n", "1"], stdout=subprocess.PIPE, text=True)
    #output = result.stdout.splitlines()

    #if len(output) >= 3:
        #cpu_line = output[2]
        #cpulist = re.split(r"[,: ]+", cpu_line)
        
        #if len(cpulist) >= 8:
            #idle = float(cpulist[7])
            #msg.data = 100 - idle
     #def main():
    #node.create_timer(1, cb)
    #rclpy.spin(node)
       #pub.publish(msg)
# CPU使用率を取得する
    #cpu_usage = psutil.cpu_percent(interval=1)
    #msg.data = cpu_usage
    #pub.publish(msg)
    #print(f"CPU使用率: {cpu_usage}%")

#def main():
    #node.create_timer(1, cb)
    #rclpy.spin(node)

