#!/usr/bin/env python
import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#ASSEGNAMENTO 
reasoner_out = outputReasoner()
selector_out = selectorMatcher()
obj_list = obj()


def matcherFunction(obj_list, reasoner_out):
    r_out = reasoner_out
    for linea in r_out.lines:
        for ogg_reas in r_out.lines[linea].rec:
            for ogg_lista in obj_list.obj:
                for caratteristica in ogg_lista:
                    if(caratteristica == 'id'):
                        if (ogg_reas[1:] == modulo):
                            #crea una lista da aggiungere le features degli oggetti trovati
                            #cancella l'oggetto dalla lista
            #fai l'append sulla variabile di output (da creare ancora)
    #fai il pubblish della variabile di output


#CALLBACKS
def callbackSelector(selectorMatcher):
    for moduli in selectorMatcher.matcher:
        for scene in moduli.common:
            for oggetti in scene.adap:
                obj_list.obj.append(oggetti)
    

    #selector_out.matcher.append(selectorMatcher)
    print("eccomiiiiiiiiiiiiiiiiiiiiiiii+kjflbsdkjhgsdclkjjhdscjhasjhh jvsadyggtusdcygu")
    print(obj_list)
    

def callbackReasoner(outputReasoner):
    reasoner_out = outputReasoner
    matcherFunction(obj_list,reasoner_out)
    #print(reasoner_out)

    # print(reasoner_out.lines[0].rec[0][1:len(reasoner_out.lines[0].rec[0])])
 
	 
if __name__ == '__main__':
	rospy.loginfo("In esecuzione...")
	rospy.init_node('featuresMatcher', anonymous=True)
	###SUBSCRIBERS
	sub_pitt = rospy.Subscriber('reasoner_output', outputReasoner, callbackReasoner)
	sub_tensor = rospy.Subscriber('/featureScheduler/pubUnion', selectorMatcher, callbackSelector)
	###PUBLISHER
	pub_results = rospy.Publisher('/featureMatcher/dataPub', matcher, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():

		rate.sleep()
