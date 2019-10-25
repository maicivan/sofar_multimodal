#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#ASSEGNAMENTO
buffer = []
intersection = intersectFeatures()
j=0
commonObj = commonFeature()
union_objs = selectorMatcher()
intersect_obj = intersect_msg()
values = stringValue()
VALUE = stringValue()
temp_name =''

def compare(buffer):
	global intersection, temp_name, intersect_obj, values
	print ("lunghezza buffer " + str(len(buffer)))
	for k in range(0,len(buffer)):	
		#print (buffer[k].id_mod)
		for j in range(k+1,len(buffer)):
			#print(buffer[j]) 
			if(buffer[k].id_mod != buffer[j].id_mod):
				for scene in range(0,len(buffer[k].adap)):
					#print(buffer[j].adap[scene])
					for objects_1 in range(0,len(buffer[k].adap[scene].obj)):
						#print(buffer[j].adap[scene].obj[objects_1])
						for scene_2 in range(0,len(buffer[j].adap)):
							for objects_2 in range(0,len(buffer[j].adap[scene_2].obj)):
								#print("obj in scene : " + str(len(buffer[j].adap[scene].obj)))
								if(buffer[k].adap[scene].obj[objects_1].name == buffer[j].adap[scene_2].obj[objects_2].name):
									#if(buffer[k].adap[scene].obj[objects_1].value in intersection.value.arrayValue):
									if(buffer[k].adap[scene].obj[objects_1].value in values.arrayValue):
										for valore in range(0,len(buffer[j].adap[scene_2].obj[objects_2].value)):
											values.arrayValue.append(buffer[j].adap[scene_2].obj[objects_2].value[valore])
										intersection.value.append(values)
										values = stringValue()
									else:
										if(temp_name != buffer[j].adap[scene_2].obj[objects_2].name):
											print(intersection)
											
											intersect_obj.intersezione.append(intersection)
											pub_intersect.publish(intersect_obj)
											##RESET LIST
											intersection = intersectFeatures()
											intersect_obj = intersect_msg()
											values = stringValue()

											temp_name = buffer[j].adap[scene_2].obj[objects_2].name
											intersection.name = buffer[k].adap[scene].obj[objects_1].name

											for valore in range(0,len(buffer[j].adap[scene_2].obj[objects_2].value)):
												values.arrayValue.append(buffer[k].adap[scene].obj[objects_1].value[valore])
											intersection.value.append(values)
											values = stringValue()

											for valore in range(0,len(buffer[j].adap[scene_2].obj[objects_2].value)):
												values.arrayValue.append(buffer[j].adap[scene_2].obj[objects_2].value[valore])
											intersection.value.append(values)
											values = stringValue()
										else:
											for valore in range(0,len(buffer[j].adap[scene_2].obj[objects_2].value)):
												values.arrayValue.append(buffer[j].adap[scene_2].obj[objects_2].value[valore])
											intersection.value.append(values)
											values = stringValue()
						# pub_intersect.publish(intersect_obj)
						# intersect_obj = intersect_msg()
	buffer[:] = []
	return						

###CALLBACKS
def callbackPitt(adapter):
	commonObj.common.append(adapter)
	union_objs.matcher.append(commonObj)
	buffer.append(adapter)

def callbackTensor(adapter):
	commonObj.common.append(adapter)
	union_objs.matcher.append(commonObj)
	buffer.append(adapter)
	# intersect_obj.matcher.append(commonObj)
	
if __name__ == '__main__':
	rospy.loginfo("In esecuzione...")
	rospy.init_node('selectorMatcher', anonymous=True)
	###SUBSCRIBERS
	rospy.Subscriber('outputAdapterPitt', adapter, callbackPitt)
	rospy.Subscriber('outputAdapterTensor', adapter, callbackTensor)
	###PUBLISHERS
	pub_intersect = rospy.Publisher('/featureScheduler/pubIntersection', intersect_msg, queue_size=10)
	pub_union = rospy.Publisher('/featureScheduler/pubUnion', selectorMatcher, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		###UNION
		pub_union.publish(union_objs)
		compare(buffer)
		commonObj.common[:] = []
		union_objs.matcher[:] = []
		###INTERSECT -- DA FINIRE SOLO IDEA
		# pub_intersect.publish(intersect_obj)
		# intersect_obj.matcher[:] = []

		rate.sleep()