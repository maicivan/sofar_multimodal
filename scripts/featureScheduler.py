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
	print("-----------------------" + str(buffer))
	if(len(buffer)>1):
		for k in range(0,len(buffer)):
			for j in range(k+1,len(buffer)):

				for oggetto in range(0,len(buffer[k].adap)):
					for feature in range(0, len(buffer[k].adap[oggetto].obj)):
						for feature_2 in range(0, len(buffer[j].adap[0].obj)):
							if(buffer[k].adap[oggetto].obj[feature].name ==  buffer[j].adap[0].obj[feature_2].name):
								common_feature.append(feature)

	
					for feature in range(len(buffer[k].adap[oggetto].obj)-1,-1,-1):
						print("valore feature: "+ str(feature))
						for f in  range(len(common_feature)-1,-1, -1):
							if(feature==common_feature[f]):
								print("Da salvare: \n"+str(common_feature[f]))
								name_common.append(buffer[k].adap[oggetto].obj[feature].name)
								print("guarada quiyiewhsihbfluy\n"+ str(name_common))
								del(common_feature[f])
								break
							del(buffer[k].adap[oggetto].obj[feature])
					name_common_mem = list(name_common)
					name_common[:]=[]

				for oggetto in range(0,len(buffer[j].adap)):
					for feature in range(len(buffer[j].adap[oggetto].obj)-1,-1,-1):
						print("valore feature2: "+ str(feature))
						#for n in  range(len(name_common)-1,-1, -1):

						print(len(buffer[j].adap[oggetto].obj)-1)
						print(buffer[j].adap[oggetto].obj[feature])
						print("culo")
						print(name_common_mem)
						if(buffer[j].adap[oggetto].obj[feature].name == name_common_mem[-1]):
							print("Da salvare ground: \n"+str(name_common_mem[-1]))
							#del(name_common_mem[len(name_common_mem)-1])
							name_common_mem.pop()
						else:
							del(buffer[j].adap[oggetto].obj[feature])
						if not name_common_mem:
							break
		common_feature[:] = []

			
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"+str(buffer))
		

def checkNewValue(value, buffer):
	for k in range(0,len(buffer)):
		if(value.id_mod == buffer[k].id_mod):
			buffer[k] = value
			return
	buffer.append(value)
	

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