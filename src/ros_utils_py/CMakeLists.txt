cmake_minimum_required(VERSION 3.0.2)
project(ros_utils_py)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_python_setup()

catkin_package()

catkin_install_python(PROGRAMS
  test/publisher_test_node.py
  test/service_client_test_node.py
  test/subscriber_test_node.py
  test/service_test_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

