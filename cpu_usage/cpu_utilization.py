#SPDX-FileCopyrightText: 2024 Yukimi Miyahara
#SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import psutil

rclpy.init()
node = Node("cpu_utilization")
pub = node.create_publisher(String, "cpu", 10)

def cb():
    msg = String()
    cpu_usage = psutil.cpu_percent(interval=1)
    msg.data = f"cpu_usage: {cpu_usage}%"
    pub.publish(msg)

def main():
    node.create_timer(1, cb)
    rclpy.spin(node)
