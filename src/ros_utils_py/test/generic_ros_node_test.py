import ros_utils_py.ros_node as node
import rospy
from std_msgs.msg import String
from __future__ import print_function
from std_srvs.srv import Trigger, TriggerResponse

def main():
    talker=Talker('talker')
    talker.add_publisher('chatter',String)
    talker.run(10)
    listener=Listener('listener')
    listener.add_subscriber('chatter', String)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass  