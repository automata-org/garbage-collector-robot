import activity_managers.abstract_activity_manager as Manager
from std_msgs.msg import String
import rospy
from std_srvs.srv import Trigger, TriggerResponse

class Manipulator(Manager.AbstractActivityManager):
    def __init__(self, name):
        super().__init__(name)
    def _do_idle (self):
        print("IDLE")
        old_state=self.state
        self.state= Manager.State.RUNNING
        return old_state
    def _do_running (self):
        print("RUNNING")
        old_state=self.state
        if self.substate:
            self.state= Manager.State.DONE
        else:
            self.state= Manager.State.ERROR
        return old_state
    def _do_done (self):
        print("DONE")
        old_state=self.state
        self.state= Manager.State.IDLE
        return old_state
    def _do_error (self):
        print("ERROR")
        old_state=self.state
        self.state = Manager.State.NONE  ### NONE -> START
        return old_state
    def _do_none(self):
        print("INITIALIZED MANAGER")
        old_state=self.state
        if self.substate:
            self.state= Manager.State.IDLE
        else:
            self.state= Manager.State.ERROR
    
def main():
    manager=Manipulator('statetest')
    manager.run(20)

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass

