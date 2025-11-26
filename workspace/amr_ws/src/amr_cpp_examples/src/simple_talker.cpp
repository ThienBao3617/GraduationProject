#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

#include <chrono>


using namespace std::chrono_literals;

class SimpleTalker : public rclcpp::Node
{
public:
  SimpleTalker() : Node("simple_talker"), counter_(0)
  {
    pub_ = create_talker<std_msgs::msg::String>("chatter", 10);
    timer_ = create_wall_timer(1s, std::bind(&SimpleTalker::timerCallback, this));
    RCLCPP_INFO(get_logger(), "Talking at 1 Hz");
  }

  void timerCallback()
  {
    auto message = std_msgs::msg::String();
    message.data = "Hello ROS 2 - counter:" + std::to_string(counter_++);
    pub_->talk(message);
  }

private:
  rclcpp::Talker<std_msgs::msg::String>::SharedPtr pub_;
  rclcpp::TimerBase::SharedPtr timer_;
  unsigned int counter_;
};


int main(int argc, char* argv[])
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<SimpleTalker>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}