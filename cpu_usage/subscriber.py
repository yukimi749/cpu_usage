import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


rclpy.init()
node = Node("subscriber")


def cb(msg):
    global node
    node.get_logger().info("Subscription: %f" % msg.data)


def main():
    sub = node.create_subscription(Float32, "cpu", cb, 10)
    rclpy.spin(node)
