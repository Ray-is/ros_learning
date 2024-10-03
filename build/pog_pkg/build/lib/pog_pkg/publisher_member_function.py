import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class PogPublisher(Node):

    def __init__(self):
        super().__init__('the_publisher')
        self.publisher = self.create_publisher(String, 'topicName', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f"Bruh {self.i}"
        self.publisher.publish(msg)
        self.get_logger().info("Publishing: ", msg.data)

        self.i += 1


def main(args=None):
    rclpy.init(args=args)

    p = PogPublisher()

    rclpy.spin(p)

    p.destroy_node()
    rclpy.shutdown()