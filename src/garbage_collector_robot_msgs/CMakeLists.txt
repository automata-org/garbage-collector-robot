cmake_minimum_required(VERSION 3.0.2)
project(garbage_collector_robot_msgs)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  actionlib_msgs
  message_generation
)

## Generate messages in the 'msg' folder
add_message_files(
  FILES
)

## Generate services in the 'srv' folder
add_service_files(
  FILES
)

## Generate actions in the 'action' folder
add_action_files(
  FILES
)

## Generate added messages and services with any dependencies listed here
generate_messages(
  DEPENDENCIES
  std_msgs
  actionlib_msgs
)

## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
  CATKIN_DEPENDS std_msgs
)
