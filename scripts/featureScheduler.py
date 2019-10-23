#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#ASSEGNAMENTO
commonObj = commonFeature()
union_objs = selectorMatcher()
intersect_obj = selectorMatcher()
buffer = []
intersezione = []
j=0

def compare(buffer):
	#intersect_obj.matcher.common.id_mod
	print ("lunghezza buffer " + str(len(buffer)))
	# endLoop = len(buffer)
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
								# 	print("primo oggetto " + str(buffer[k].id_mod))
								# 	print(buffer[k].adap[scene].obj[objects_1])
								# 	print('\n')
								# 	print("secondo oggetto " + str(buffer[j].id_mod))
								# 	print(buffer[j].adap[scene_2].obj[objects_2])
								# 	print('\n')
								# 	print("feature in comune")
								# 	print(buffer[j].adap[scene_2].obj[objects_2].name)
								# 	print('\n')
								# 	print(buffer[k].adap[scene].obj[objects_1].value)
								# 	print('\n')
								# 	print(buffer[j].adap[scene_2].obj[objects_2].value)
								# 	print('\n')
								#	print(buffer[k].adap[scene].obj[objects_1].value)
							
									if(buffer[k].adap[scene].obj[objects_1].value in intersezione):
										intersezione.append(str(buffer[j].adap[scene_2].obj[objects_2].value))
									else:
										intersezione.append(str(buffer[k].adap[scene].obj[objects_1].name))
										intersezione.append(str(buffer[k].adap[scene].obj[objects_1].value))
										intersezione.append(str(buffer[j].adap[scene_2].obj[objects_2].value))
				print(intersezione)
				pub_intersect.publish(intersezione)
				intersezione[:] = []
		intersezione[:] = []
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