cmake_minimum_required(VERSION 3.8)
project(amr_cpp_examples)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(simple_talker src/simple_talker.cpp)
ament_target_dependencies(simple_talker rclcpp std_msgs)

add_executable(simple_listener src/simple_listener.cpp)
ament_target_dependencies(simple_listener rclcpp std_msgs)

install(TARGETS
  simple_publisher
  simple_subscriber
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()