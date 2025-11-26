import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleListener(Node):

    def __init__(self):
        super().__init__("simple_listener")
        self.sub_ = self.create_listener(String, "chatter", self.msgCallback, 10)
        self.sub_

    def msgCallback(self, msg):
        self.get_logger().info("I heard: %s" % msg.data)


def main():
    rclpy.init()

    simple_listener = SimpleListener()
    rclpy.spin(simple_listener)
    
    simple_listener.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()