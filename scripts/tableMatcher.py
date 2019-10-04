#!/usr/bin/env python

import numpy as np
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from sofar_multimodal.msg import adapter
from sofar_multimodal.msg import feature
from sofar_multimodal.msg import obj
from sofar_multimodal.msg import commonFeature
from sofar_multimodal.msg import selectorMatcher

def callback(data):	
	
	for i in range(0,len(data.matcher)):
			
			comp = Float32MultiArray()
			comp = np.zeros(len(data.matcher[i].common[0].adap),len(data.matcher[i].common[1].adap))
			
			for j in range(0,len(data.matcher[i].common[0].adap[0].obj)):				
				if data.matcher[i].common[0].adap[0].obj[j] == 'pose_2d':
					for l in range(0,data.matcher[i].common[0].adap):
						for k in range(0,data.matcher[i].common[1].adap):
							deltaX = data.matcher[i].common[0].adap[l].obj[j].value[0] - data.matcher[i].common[1].adap[k].obj[j].value[0]							
							deltaY = data.matcher[i].common[0].adap[l].obj[j].value[1] - data.matcher[i].common[1].adap[k].obj[j].value[1]
							comp[l][k] = comp[l][k] + pow((pow(deltaX,2)+ pow(deltaY,2)),0.5)
				
				
				
				if (data.matcher[i].common[0].adap[0].obj[j] == 'pose_3d'):
					for l in range(0,data.matcher[i].common[0].adap):
						for k in range(0,data.matcher[i].common[1].adap):
							deltaX = data.matcher[i].common[0].adap[l].obj[j].value[0] - data.matcher[i].common[1].adap[k].obj[j].value[0]							
							deltaY = data.matcher[i].common[0].adap[l].obj[j].value[1] - data.matcher[i].common[1].adap[k].obj[j].value[1]
							deltaZ = data.matcher[i].common[0].adap[l].obj[j].value[2] - data.matcher[i].common[1].adap[k].obj[j].value[2]
							comp[l][k] = comp[l][k] + pow((pow(deltaX,2)+ pow(deltaY,2)+pow(deltaZ,2)),0.5)
							
				
				#if (data.matcher[i].common[0].adap[0].obj[j] == 'colour_rgb'):
					
				#if (data.matcher[i].common[0].adap[0].obj[j] == 'colour_name'):
					
				#if (data.matcher[i].common[0].adap[0].obj[j] == 'colour_hsv'):
				
				#if (data.matcher[i].common[0].adap[0].obj[j] == 'geometric_shape_2d'):
			
				#if (data.matcher[i].common[0].adap[0].obj[j] == 'geometric_shape_3d'):
				
				#if (data.matcher[i].common[0].adap[0].obj[j] == 'result'):  
				
				


def listener():
    
    rospy.init_node('table', anonymous=True)
    rospy.Subscriber('matcherChannel', selectorMatcher, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()



