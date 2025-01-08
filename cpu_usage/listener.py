#SPDX-FileCopyrightText: 2024 Yukimi Miyahara
#SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


rclpy.init()
node = Node("listener")


def cb(msg):
    global node
    node.get_logger().info("Listen: %f%%" %msg.data)


def main():
    sub = node.create_subscription(Float32, "cpu", cb, 10)
    rclpy.spin(node)
