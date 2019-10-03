#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#ASSEGNAMENTO 
union_objs = unionMsg()
intersect_obj = selectorMatcher()
started = False

###PUBLISHER
pub_intersection = rospy.Publisher('/featureScheduler/pubIntersection', selectorMatcher, queue_size=10)
pub_union = rospy.Publisher('/featureScheduler/pubUnion', unionMsg, queue_size=10)

###CALLBACKS
def callbackPitt(TrackedShapes):
    global started, union_objs
    union_objs.union_objs.append(TrackedShapes)
    if(not started):
        started = True

def callbackTensor(TensorOutput):
    global started, union_objs
    union_objs.union_objs.append(TensorOutput)
    if(not started):
        started = True

###TALKER
def timer_callback(event):
    global started, pub_union, union_objs
    if (started):
        pub_union.publish(union_objs)
        union_objs.union_objs[:] = []
    
###LISTENER

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('PittChannel', TrackedShapes, callbackPitt)
    rospy.Subscriber('TensorChannel', TensorOutput, callbackTensor)

    timer = rospy.Timer(rospy.Duration(0.5), timer_callback)

    rospy.spin()    
    timer.shutdown()

if __name__ == '__main__':
    rospy.loginfo("In esecuzione..")
    listener()
