#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#ASSEGNAMENTO
copia_buf = commonFeature()
commonObj = commonFeature()
union_objs = selectorMatcher()
confronto = commonFeature()
output = selectorMatcher()
common_feature = []
name_common = []

def compare(buffer):
	global common_feature, name_common
	name_common_mem = []
	output.matcher[:] = []
	union_objs.matcher[:] = []
	if(len(buffer.common)>1):
		for k in range(0,len(buffer.common)):
			for j in range(k+1,len(buffer.common)):
				commonObj.common[:] = []
				commonObj.common.append(buffer.common[k])
				commonObj.common.append(buffer.common[j])
				union_objs.matcher.append(commonObj)
		pub_union.publish(union_objs)

		for k in range(0,len(buffer.common)):
			for j in range(k+1,len(buffer.common)):
				for oggetto in range(0,len(buffer.common[k].adap)):
					if not (buffer.common[k].adap):
						return
					for feature in range(0, len(buffer.common[k].adap[oggetto].obj)):
						if not (buffer.common[j].adap):
							return
						for feature_2 in range(0, len(buffer.common[j].adap[0].obj)):
							if(buffer.common[k].adap[oggetto].obj[feature].name ==  buffer.common[j].adap[0].obj[feature_2].name):
								common_feature.append(feature)

	
					for feature in range(len(buffer.common[k].adap[oggetto].obj)-1,-1,-1):
						if common_feature:
							if(feature==common_feature[-1]):
								name_common.append(buffer.common[k].adap[oggetto].obj[feature].name)
								common_feature.pop()
							else:
								del(buffer.common[k].adap[oggetto].obj[feature])
						else:
							del(buffer.common[k].adap[oggetto].obj[feature])
					name_common_mem = list(name_common)
					name_common[:]=[]

				for oggetto in range(0,len(buffer.common[j].adap)):
					name_temp = list(name_common_mem)
					for feature in range(len(buffer.common[j].adap[oggetto].obj)-1,-1,-1):
						if name_temp:
							if(buffer.common[j].adap[oggetto].obj[feature].name == name_temp[0]):
								del(name_temp[0])
							else:
								del(buffer.common[j].adap[oggetto].obj[feature])
						else:
							del(buffer.common[j].adap[oggetto].obj[feature])
	
				confronto.common[:] = []
				confronto.common.append(buffer.common[k])
				confronto.common.append(buffer.common[j])
				output.matcher.append(confronto)				

		if not (output.matcher[0].common[0].adap):
			return
		elif not (output.matcher[0].common[0].adap[0]):
			return
		pub_intersect.publish(output)
					
def checkNewValue(value, buffer):
	for k in range(0,len(buffer.common)):
		if(value.id_mod == buffer.common[k].id_mod):
			buffer.common[k] = value
			return
	buffer.common.append(value)
	

###CALLBACKS
def callbackPitt(adapter):
	checkNewValue(adapter, copia_buf)

def callbackTensor(adapter):
	checkNewValue(adapter,copia_buf)

	
if __name__ == '__main__':
	rospy.loginfo("In esecuzione...")
	rospy.init_node('selectorMatcher', anonymous=True)
	###SUBSCRIBERS
	sub_pitt = rospy.Subscriber('outputAdapterPitt', adapter, callbackPitt)
	sub_tensor = rospy.Subscriber('outputAdapterTensor', adapter, callbackTensor)
	###PUBLISHERS
	pub_intersect = rospy.Publisher('/featureScheduler/pubIntersection', selectorMatcher, queue_size=10)
	pub_union = rospy.Publisher('/featureScheduler/pubUnion', selectorMatcher, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		compare(copia_buf)

		rate.sleep()
