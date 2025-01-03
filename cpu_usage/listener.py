#SPDX-FileCopyrightText: 2024 Yukimi Miyahara
#SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


rclpy.init()
node = Node("listener")


def cb(msg):
    global node
    node.get_logger().info("Listen: %s" %msg.data)


def main():
    sub = node.create_subscription(String, "cpu", cb, 10)
    rclpy.spin(node)
