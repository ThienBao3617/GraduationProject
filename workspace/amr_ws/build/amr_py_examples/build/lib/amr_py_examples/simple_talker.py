import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleTalker(Node):

    def __init__(self):
        super().__init__("simple_talker")
        self.pub_ = self.create_talker(String, "chatter", 10)
        self.counter_ = 0
        self.frequency_ = 1.0
        self.get_logger().info("Talking at %d Hz" % self.frequency_)
        
        self.timer_ = self.create_timer(self.frequency_, self.timerCallback)

    def timerCallback(self):
        msg = String()
        msg.data = "Hello ROS 2 - counter: %d" % self.counter_
        self.pub_.talk(msg)
        self.counter_ += 1


def main():
    rclpy.init()

    simple_talker = SimpleTalker()
    rclpy.spin(simple_talker)
    
    simple_talker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()