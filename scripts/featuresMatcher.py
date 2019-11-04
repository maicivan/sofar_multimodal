import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#ASSEGNAMENTO 
#union_objs = unionMsg()
#ID_objs = 1                 ### NON HO IL DATO - da modificare con il tipo di dato che esce dal REASONER
#obj_readed = obj()         #lista feature per ogni ogni oggetto
#obj_list = matcher()       #lista di oggetti riconosciuti, in uscita al talker


#CALLBACKS
def callbackSelector():
    #global started, union_objs
    #union_objs.union_objs.append(TrackedShapes)
    print("yuppieayy")

def callbackReasoner(outputReasoner):
    ###letti gli id devo cercare dentro ad union_objs tutti i corrispettivi oggetti
    #global started, union_objs, obj_list
    #for IDs in id_names:
    #   for ID in IDs:
    #       for obj in union_objs:
    #           if(ID == obj.union_objs.identifier):  ###da rivedere perchè deve essere creato come campo
    #               obj_readed.obj.append(union_objs.union_objs[i])
    #   obj_list.obj_list.append(obj_readed)
    #   obj_readed.obj[:]=[]
    print("Daieeeee")
 
	 
if __name__ == '__main__':
	rospy.loginfo("In esecuzione...")
	rospy.init_node('featuresMatcher', anonymous=True)
	###SUBSCRIBERS
	sub_pitt = rospy.Subscriber('reasoner_output', outputReasoner, callbackReasoner)
	sub_tensor = rospy.Subscriber('/featureScheduler/pubUnion', selectorMatcher, callbackSelector)
	###PUBLISHERS
	pub_results = rospy.Publisher('/featureMatcher/dataPub', matcher, queue_size=10)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		# 
        #
		rate.sleep()
