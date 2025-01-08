#SPDX-FileCopyrightText: 2024 Yukimi Miyahara
#SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import psutil

rclpy.init()
node = Node("cpu_utilization")
pub = node.create_publisher(Float32, "cpu", 10)

def cb():
    msg = Float32()
    cpu_usage = psutil.cpu_percent(interval=1)
    msg.data = cpu_usage
    pub.publish(msg)

def main():
    node.create_timer(1, cb)
    rclpy.spin(node)
