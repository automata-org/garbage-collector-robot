import ros_utils_py.ros_publisher as publisher
import rospy
from std_msgs.msg import String

def main():
    pub = publisher.GenericPublisher('chatter', String)
    rospy.init_node('publisher_test_node')
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hello_str = "This is a test string"
        rospy.logerr("Sending message %s" % rospy.get_time())
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass