from __future__ import print_function
from std_srvs.srv import Trigger, TriggerResponse
import rospy
import ros_utils_py.ros_service as Service

def empty_speak(req):
    rospy.loginfo("Blip!")
    message = "Blip!"
    return TriggerResponse(True, message)

def main():
    rospy.init_node('talker_server')
    serv = rospy.Service('talk_service', Trigger, empty_speak)
    print("Ready to speak")
    rospy.spin()

if __name__=="__main__":
    main()
