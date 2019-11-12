import rospy
from std_msgs.msg import *
from sofar_multimodal.msg import *

#ASSEGNAMENTO 
<<<<<<< Updated upstream
union_objs = unionMsg()
ID_objs = 1                 ### NON HO IL DATO - da modificare con il tipo di dato che esce dal REASONER
obj_readed = obj()         #lista feature per ogni ogni oggetto
obj_list = matcher()       #lista di oggetti riconosciuti, in uscita al talker
=======
reasoner_out = outputReasoner()
selector_out = selectorMatcher()
obj_list = adapter()
obj_list.id_mod = 90 #the most frightening
matcher = matcherObj()

def matcherFunction(obj_list, r_out):
    for linea in r_out.lines:
        matcher.sameObj[:] = []
        matcher.correlation = linea.corr
        for ogg_reas in linea.rec:
            for ogg_lista in obj_list.adap:
                for caratteristica in ogg_lista.obj:
                    if (caratteristica.name == 'id'):
                        if (str(ogg_reas[1:]) == str(caratteristica.value[0])):
                            matcher.sameObj.append(ogg_lista)                           # crea una lista di oggetti corrispondetnti
                            obj_list.adap.remove(ogg_lista)                             # cancella l'oggetto dalla lista
        pub_results.publish(matcher)                                                    # pubblish della variabile di output
>>>>>>> Stashed changes

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