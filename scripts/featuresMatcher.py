import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#ASSEGNAMENTO 
union_objs = unionMsg()
ID_objs = 1                 ### NON HO IL DATO - da modificare con il tipo di dato che esce dal REASONER
obj_readed = obj()         #lista feature per ogni ogni oggetto
obj_list = matcher()       #lista di oggetti riconosciuti, in uscita al talker

#PUBLISHER
pub_results = rospy.Publisher('/featureMatcher', matcher, queue_size=10)

#CALLBACKS
def callbackSched(TrackedShapes): 
    global started, union_objs
    union_objs.union_objs.append(TrackedShapes)

def callbackReasoner(id_names): ###letti gli id devo cercare dentro ad union_objs tutti i corrispettivi oggetti
    global started, union_objs, obj_list
    #for IDs in id_names:
    #   for ID in IDs:
    #       for obj in union_objs:
    #           if(ID == obj.union_objs.identifier):  ###da rivedere perchè deve essere creato come campo
    #               obj_readed.obj.append(union_objs.union_objs[i])
    #   obj_list.obj_list.append(obj_readed)
    #   obj_readed.obj[:]=[]
    if(not started):
        started = True

    return

#TALKER
def timer_callback(event):          #pubblica e pulisce la lista oggetti
    global started, pub_results, obj_list
    if (started):
        pub_results.publish(obj_list)
        obj_list.obj_list[:] = []
        #started=False
 
#LISTENER
def listener():    
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber('/featureScheduler/unionObj', TrackedShapes, callbackSched)
    #rospy.Subscriber('REASONER', id_names, callbackReasoner)    ####callback da fare al reasoner
    rospy.loginfo("In esecuziione!!")

    timer = rospy.Timer(rospy.Duration(0.5), timer_callback)

    rospy.spin()    
    timer.shutdown()
	 
if __name__ == '__main__':	
	listener()