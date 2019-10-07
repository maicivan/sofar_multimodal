#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#ASSEGNAMENTO
commonObj = commonFeature()
union_objs = selectorMatcher()
intersect_obj = selectorMatcher()

###CALLBACKS
def callbackPitt(adapter):
    global started
    commonObj.common.append(adapter)
    union_objs.matcher.append(commonObj)

def callbackTensor(adapter):
    global started
    commonObj.common.append(adapter)
    union_objs.matcher.append(commonObj)

if __name__ == '__main__':
	rospy.loginfo("In esecuzione...")
	rospy.init_node('selectorMatcher', anonymous=True)
	###SUBSCRIBERS
	rospy.Subscriber('outputAdapterPitt', adapter, callbackPitt)
	rospy.Subscriber('outputAdapterTensor', adapter, callbackTensor)
	###PUBLISHERS
	pub_intersection = rospy.Publisher('/featureScheduler/pubIntersection', selectorMatcher, queue_size=10)
	pub_union = rospy.Publisher('/featureScheduler/pubUnion', selectorMatcher, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		pub_union.publish(union_objs)
		union_objs.matcher[:] = []
		rate.sleep()