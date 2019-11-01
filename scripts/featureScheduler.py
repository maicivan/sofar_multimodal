#!/usr/bin/env python

import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#ASSEGNAMENTO
buffer = commonFeature()
intersection = intersectFeatures()
j=0
commonObj = commonFeature()
union_objs = selectorMatcher()
confronto = commonFeature()
interse = selectorMatcher()
intersect_obj = intersect_msg()
values = stringValue()
VALUE = stringValue()
temp_name =''

common_feature = []
name_common = []

def compare(buffer):
	global common_feature, name_common
	name_common_mem = []
	interse.matcher[:] = []
	if(len(buffer.common)>1):
		for k in range(0,len(buffer.common)):
			for j in range(k+1,len(buffer.common)):

				for oggetto in range(0,len(buffer.common[k].adap)):
					for feature in range(0, len(buffer.common[k].adap[oggetto].obj)):
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
	
				print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+str(buffer))
				interse.matcher.append(buffer)			
				pub_intersect.publish(interse)
				# confronto.common[:] = []
				# confronto.common.append(buffer.common[k])
				# confronto.common.append(buffer.common[j])
				# interse.matcher.append(confronto)
				

		# interse.matcher.append(buffer)			
		# pub_intersect.publish(interse)


			
		#print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+str(buffer))
		

def checkNewValue(value, buffer):
	for k in range(0,len(buffer.common)):
		if(value.id_mod == buffer.common[k].id_mod):
			buffer.common[k] = value
			return
	buffer.common.append(value)
	

###CALLBACKS
def callbackPitt(adapter):
	commonObj.common.append(adapter)
	union_objs.matcher.append(commonObj)
	checkNewValue(adapter, buffer)

def callbackTensor(adapter):
	commonObj.common.append(adapter)
	union_objs.matcher.append(commonObj)
	checkNewValue(adapter,buffer)
	# intersect_obj.matcher.append(commonObj)
	
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
		compare(buffer)
		commonObj.common[:] = []
		union_objs.matcher[:] = []
		###INTERSECT -- DA FINIRE SOLO IDEA
		# pub_intersect.publish(intersect_obj)
		# intersect_obj.matcher[:] = []

		rate.sleep()



### controllo sul buffer nel caso di un solo elemento 
### tag sensore percettivo  tempo di validita dato
### ros.timenow
### time-stamp tensor question 