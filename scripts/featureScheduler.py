#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#ASSEGNAMENTO 
adaptObj = adapter()
commonObj = commonFeature()

union_objs = selectorMatcher()

intersect_obj = selectorMatcher()

started = False

###PUBLISHER
pub_intersection = rospy.Publisher('/featureScheduler/pubIntersection', selectorMatcher, queue_size=10)
pub_union = rospy.Publisher('/featureScheduler/pubUnion', selectorMatcher, queue_size=10)

###CALLBACKS
def callbackPitt(adapter):
    global started, union_objs, commonObj
    commonObj.common.append(adapter)
    union_objs.matcher.append(commonObj)
    if(not started):
        started = True

def callbackTensor(adapter):
    global started, union_objs, commonObj
    commonObj.common.append(adapter)
    union_objs.matcher.append(commonObj)
    if(not started):
        started = True

###TALKER
def timer_callback(event):
    global started, pub_union, union_objs
    if (started):
        pub_union.publish(union_objs)
        union_objs.matcher[:] = []
    
###LISTENER

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('outputAdapterPitt', adapter, callbackPitt)
    rospy.Subscriber('outputAdapterTensor', adapter, callbackTensor)

    timer = rospy.Timer(rospy.Duration(0.5), timer_callback)

    rospy.spin()    
    timer.shutdown()

if __name__ == '__main__':
    rospy.loginfo("In esecuzione..")
    listener()
