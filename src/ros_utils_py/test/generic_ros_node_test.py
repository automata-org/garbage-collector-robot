#!/usr/bin/env python
from __future__ import print_function #why?
import rospy
import ros_utils_py.ros_node as node
from std_msgs.msg import String
from std_srvs.srv import Trigger, TriggerResponse #why?

def main():

    class Talker(node.GenericROSNode):
        def __init__(self, name):
            super().__init__(name)
        def main_task(self):
            self.get_publisher('chatter').publish("Blip!")

    class Listener(node.GenericROSNode): #not necessary and unused
        def __init__(self, name):
            super().__init__(name)
        
    talker=Talker('talker')
    talker.add_publisher('chatter',String)
    talker.run(10)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass  