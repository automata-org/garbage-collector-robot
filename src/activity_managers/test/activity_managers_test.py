import activity_managers.abstract_activity_manager as Manager
from std_msgs.msg import String
import rospy
from std_srvs.srv import Trigger, TriggerResponse
import ros_utils_py.ros_node as node

class StateTester(Manager.AbstractActivityManager):
    def __init__(self, name):
        super().__init__(name)
    def _do_idle (self):
        print("IDLE")
        old_state=self.state
        self.state= State.RUNNING
        return old_state
    def _do_running (self):
        print("RUNNING")
        old_state=self.state
        self.state= State.DONE
        return old_state
    def _do_done (self):
        print("DONE")
        old_state=self.state
        self.state= State.IDLE
        return old_state
    def _do_error (self):
        print("ERROR")
        old_state=self.state
        return old_state
    def _do_none (self):
        print("INITIALIZED MANAGER")
        old_state=self.state
        self.state= State.IDLE
    
def main():
    manager=StateTester('statetest')
    manager.run(20)

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass

