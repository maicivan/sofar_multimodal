#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#ASSEGNAMENTO
commonObj = commonFeature()
union_objs = selectorMatcher()
#intersect_obj = selectorMatcher()

""" def compare(adapter, adapter):
	if(commonObj.common.id_mod ) """

###CALLBACKS
def callbackPitt(adapter):
	##UNION
    commonObj.common.append(adapter)
    union_objs.matcher.append(commonObj)
	##INTERSECT
	#intersect_obj.matcher.append(commonObj)

def callbackTensor(adapter):
	#UNION
    commonObj.common.append(adapter)
    union_objs.matcher.append(commonObj)
	#INTERSECT
	#intersect_obj.matcher.append(commonObj)


if __name__ == '__main__':
	rospy.loginfo("In esecuzione...")
	rospy.init_node('selectorMatcher', anonymous=True)
	###SUBSCRIBERS
	rospy.Subscriber('outputAdapterPitt', adapter, callbackPitt)
	rospy.Subscriber('outputAdapterTensor', adapter, callbackTensor)
	###PUBLISHERS
	pub_intersect = rospy.Publisher('/featureScheduler/pubIntersection', selectorMatcher, queue_size=10)
	pub_union = rospy.Publisher('/featureScheduler/pubUnion', selectorMatcher, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		###UNION
		pub_union.publish(union_objs)
		commonObj.common[:] = []
		union_objs.matcher[:] = []
		###INTERSECT -- DA FINIRE SOLO IDEA
		# compare(adapter, adapter)
		# pub_intersect.publish(intersect_obj)
		# intersect_obj.matcher[:] = []

		rate.sleep()