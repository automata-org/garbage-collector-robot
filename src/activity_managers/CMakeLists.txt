cmake_minimum_required(VERSION 3.0.2)
project(activity_managers)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_python_setup()

catkin_package()

catkin_install_python(PROGRAMS
  test/activity_managers_test.py
  test/manipulator_test.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
