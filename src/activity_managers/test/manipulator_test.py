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
    #manager.run(20)
    manager._do_running()
    input_state_string = input()
    #print(manager.state)
    #print(input_state_string == manager.state)
    if str(input_state_string) == str(manager.state):
        if manager.state == "State.IDLE":
            manager._do_idle()
        elif manager.state == "State.RUNNING":
            manager._do_running()
        elif manager.state == "State.DONE":
            manager._do_done()
        elif manager.state == "State.ERROR":
            manager._do_error()
            print(manager.substate)
        else:
            manager._do_none()
    else:
        manager._do_error()
        manager.substate = False
        print(manager.substate)



if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass

