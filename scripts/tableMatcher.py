#!/usr/bin/env python

import numpy as np
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from sofar.msg import adapter
from sofar.msg import feature
from sofar.msg import obj
from sofar.msg import selector_matcher

def callback(data):	
	
	for i in range(0,len(data.matcher))
			
			comp = Float32MultiArray()
			comp = np.zeros(len(data.matcher[i].common[0].adap),len(data.matcher[i].common[1].adap))
			
			
	


def listener():
    
    rospy.init_node('table', anonymous=True)
    rospy.Subscriber('table', adapter, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()



