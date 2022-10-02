import rospy
import ros_utils_py.ros_node as rosnode
from enum import Enum

class State(Enum):
    IDLE=0
    RUNNING=1
    DONE=2
    ERROR=99
    NONE=100

class AbstractActivityManager(rosnode.GenericROSNode):
    def __init__(self, name):
        super().__init__(name)
        #self.rosnode(name) #why?
        self.state = State.NONE
        self.substate = True

    def _do_idle (self):
        raise Exception("Not Implemented idle")
    def _do_running (self):
        raise Exception("Not Implemented running")
    def _do_done (self):
        raise Exception("Not Implemented done")
    def _do_error (self):
        raise Exception("Not Implemented error")
    def _do_none (self):
        raise Exception("Not Implemented none")

    def main_task(self):
        if self.state == State.IDLE:
            self._do_idle()
        elif self.state == State.RUNNING:
            self._do_running()
        elif self.state == State.DONE:
            self._do_done()
        elif self.state == State.ERROR:
            self._do_error()
        elif self.state == State.NONE:
            self._do_none()
        else:
            pass
            
