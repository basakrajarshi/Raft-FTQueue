#!/usr/bin/env python
from __future__ import print_function


import sys
import time

from functools import partial
sys.path.append("../")
from pysyncobj import SyncObj, replicated
#listofqs = {}
#listoflabels = []



class FTQueue(SyncObj):

    def __init__(self, selfNodeAddr, otherNodeAddrs):
        super(FTQueue, self).__init__(selfNodeAddr, otherNodeAddrs)
        self.__counter = 0
        self.__list_of_queues = {}
        self.__list_of_labels = []
    
    @replicated
    def qCreate(self,c):
        # queue_id = i
     
        self.__list_of_queues[c] = []
        self.__list_of_labels.append(c)
        index = len(self.__list_of_labels)-1
        print (index)
        #return index

    def searchlabel(self,c):
        if (c in self.__list_of_labels):
            print ('Go back to label create again') # Go back to raw_input ('Enter a new label')
        else:
            self.qCreate(c)



    
    def qID(self,c):
        # self.__list_of_labels
        if (len(self.__list_of_queues) < 1):
            print('No Queue found')
        else:
            if (c in self.__list_of_labels):
                return self.__list_of_labels.index(c)
            else:
                print ('label not found')

    @replicated
    def qPush(self,qID,val):
        if (len(self.__list_of_queues) < 1):
            print('No queue found ')
        else:
            try:
                if (int(qID) < len(self.__list_of_labels)):
                    return self.__list_of_queues[self.__list_of_labels[int(qID)]].append(val)
                elif (int(qID) > len(self.__list_of_labels)):
                    print('Queue ID not found in list of labels')
            except:
                print('Cannot push into the queue')
                
            

    @replicated
    def qPop(self,qID):
        if (len(self.__list_of_queues) < 1):
            print('No queue found ')
        else:
            try:
            #if ((int(qID) < len(self.__list_of_labels)) and (len(self.__list_of_queues[int(qID)]) == 0)):
                #print('Queue is empty. Pop action cannot be performed')
                if((int(qID) < len(self.__list_of_labels)) and (len(self.__list_of_queues) >= 1)):
                    z = self.__list_of_queues[self.__list_of_labels[int(qID)]][0]
                    self.__list_of_queues[self.__list_of_labels[int(qID)]].pop(0)
                    print (z)
                elif (int(qID) > len(self.__list_of_labels)):
                    print('Queue ID not found in list of labels')
            except:
                print('Cannot Pop from the queue')
        
        # return last
      #  print (self.__list_of_queues([]))
    def qTop(self,qID):
        if (len(self.__list_of_queues) < 1):
            print('No queue found')
        else:
            try:
            #if ((int(qID) < len(self.__list_of_labels)) and (len(self.__list_of_queues[int(qID)]) == 0)):
                #print('Queue is empty. Top action cannot be performed') 
                if((int(qID) < len(self.__list_of_labels)) and (len(self.__list_of_queues) >= 1)):
                    return self.__list_of_queues[self.__list_of_labels[int(qID)]][0]
                elif (int(qID) > len(self.__list_of_labels)):
                    print('Queue ID not found in list of labels')
            except:
                print('Cannot return top of the queue')

    def qSize(self,qID):
        if (len(self.__list_of_queues) < 1):
            print('No queue found')
        else:
            try:
            #if ((int(qID) < len(self.__list_of_labels)) and (len(self.__list_of_queues[int(qID)]) == 0)):
                
                #print('Queue is empty. Cannot calculate the size of the queue')
                if((int(qID) < len(self.__list_of_labels)) and (len(self.__list_of_queues) >= 1)):
                    return len(self.__list_of_queues[self.__list_of_labels[int(qID)]])
                elif (int(qID) > len(self.__list_of_labels)):
                    print('Queue ID not found in list of labels') 
            except:
                print('Cannot return the size of the queue')    
        
        
    def getItem(z):

        print (z)

    def getListOfQueue(self):
        if(len(self.__list_of_queues) >= 1):

         return self.__list_of_queues
        else:
         return {}

    def getListOfLabel(self):
        if(len(self.__list_of_labels) >= 1):
            return self.__list_of_labels
        else:
            return []

    

    def getSize(self):
        if len(self.__list_of_queues) > 0 :
            return len(self.__list_of_queues)
        return -1

def onAdd(res, err, cnt):
    print("on add called")
def onCreate(res, err, cnt):
    print("On qCreate called")
def onId(res, err, cnt):
    print('On id called')

def onPop(res, err, cnt):
    print("on pop called")
    #print(o.getQueue())

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: %s self_port partner1_port partner2_port ...' % sys.argv[0])
        sys.exit(-1)

    port = int(sys.argv[1])
    partners = ['localhost:%d' % int(p) for p in sys.argv[2:]]
    print ("Before o")
    o = FTQueue('localhost:%d' % port, partners)
    n = 0
    j = 5
    old_value = -1
    print ("Before while")
    while True:
        n = 0
        while True:
        # time.sleep(0.005)

            time.sleep(0.5)
        #nt ("before if value")

            print (o.getListOfQueue())
            
            print (o.getListOfLabel())

            #print (o.getQueueId())
            

            if o._getLeader() is None:
                continue
        # if n < 2000:
        #if n<5:
            #label: Option
            print ('Options:')
            print ('1.Create a new Queue')
            print ('2.Return the queue ID of a specific queue')
            print ('3.Push a new item into a specific queue')
            print ('4.Pop an item from a specific queue and return it')
            print ('5.Return the first element from a specific queue')
            print ('6.Return the size of a specific queue')
            
            # print ('Press a number to select an option')
            #o.addValue(1, n, callback=partial(onAdd, cnt=n))
            # c = raw_input('Enter c:')  
            # o.qCreate(c, callback=partial(onCreate, cnt=n))

            y = raw_input('Select an Option Number: ' '\n')

            if  (int(y) == 1):
                c = raw_input('Enter a new label: ')
                o.searchlabel(c)
            elif (int(y) == 2):
                c = raw_input('Enter label to find the index:')
                z = o.qID(c)
                print (z)
                    #map (str(z),str(c))
            elif int(y)==3:
                a=raw_input("Enter the qID: ")
                b=raw_input("Enter value to be pushed: ")
                o.qPush(a,b)
            elif int(y)==4:
                a = raw_input("Enter qID: ")
                o.qPop(a)
                #o.getItem(z)
            elif int(y)==5:
                a=raw_input("Enter qID: ")
                print(str(o.qTop(a)))
            elif int(y)==6:
                a=raw_input("Enter qID: ")
                print(str(o.qSize(a)))
                
                

