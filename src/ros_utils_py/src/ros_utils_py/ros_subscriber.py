import rospy


class GenericSubscriber:
    def __init__(self, topic_name, data_type, callback):
        self.subscriber = rospy.Subscriber(topic_name, data_type, callback)
       

