import rospy
from std_msgs.msg import String
import ros_utils_py.ros_subscriber as subscriber

def callback(data):
    rospy.loginfo(data.data)

def main():
    rospy.init_node('subscriber_test_node')
    sub=subscriber.GenericSubscriber('chatter', String, callback)    
    rospy.spin() 

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass