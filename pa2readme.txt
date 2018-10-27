
 


 A Distributed, Fault-Tolerant Queue Data Structure 
 (Using 'PySyncObj', an implementation of Raft in Python)

 

 
 
 Programming Assignment - 2 
 Course: CSCI - 5673 (Distributed Systems), Spring 2017
 Names of Creators: Rajarshi Basak
                    Hari Shreenivash Madras Vanamamalai


 
 

 DESCRIPTION 

 A fault-tolerant (distributed) queue data structure was built on top of PySyncObj (Github URL: https://github.com/bakwc/PySyncObj), which is an implementation of the Raft consensus algorithm in the Python Programming Language.

 The Raft consensus algorithm provides a general solution to distribute a state machine across a cluster of computing systems, which guarantees agreement upon the same series of state transitions for each node. 

 Both the basic features, i.e. Leader Election, and Log Replication are achieved in PySyncObj (Python Raft Implementation).

 



 FILES ENCLOSED

 The zip file contains the following source code files:

 (1) servlead.py
 (2) servfollow.py
 (3) client.py

 along with this readme file.

 

 
 
 COMPILING AND RUNNING THE PROGRAM

 Suppose we want to demonstrate the working of Raft for 5 servers(state machines). Let the port numbers of the servers be 8001, 8002, 8003, 8004 and 8005. To compile the code, first run the servlead.py file in a terminal tab using the server port numbers as shown below:
 
 Terminal Tab - 1
 <python servlead.py 8001 8002 8003 8004 8005>

 Next run the servfollow.py file four times in four different termninal tabs as shown below:

 Terminal Tab - 2
 <python servfollow.py 8002 8003 8004 8005 8001>

 Terminal Tab - 3
 <python servfollow.py 8003 8004 8005 8001 8002>

 Terminal Tab - 4
 <python servfollow.py 8004 8005 8001 8002 8003>

 Terminal Tab - 5
 <python servfollow.py 8005 8001 8002 8003 8004>

 This ensures that when we run servlead.py in the Terminal Tab - 1 , the server with the port number 8001 is inititated and elected as the leader. The other four servers, which are initiated when we run servfollow.py in the Terminal Tabs 2, 3, 4, 5, become the followers.

 Finally, run the client.py in a new terminal tab:

 Terminal Tab - 6
 <python client.py>

 Next, follow the commands which are printed in the client terminal to perform the operations on the queue data structure (eg. Create a queue, Get the queue id of a queue, Push an item into a queue, Pop an item from a queue, Get the first element from a queue, Get the size of a queue.)


 
 

 CURRENT STATUS OF PROGRAM

 The source code for the FTQueue data structure implements all the required functionalities, which include the abilities to 

 (1) Create a new Queue of integers by assigning a label to it; this label is taken from the client, associated with the new queue, and both the label and queue are stored in a dictionary, which we call listofqueues. This also adds the label associated with this newly created queue to a list, which we call listoflabels.

 (2) Return the queue ID of a queue (that has been created, and added to the dictionary of queues with an associated label) when the label is passed by the client to the server. The queue ID is simply the index of the label in the list listoflabels that was assigned to a queue when it was created.

 (3) Push an item to queue that has been created. When the client requests the server to insert an item to a particular queue (identified by the queue ID), the server pushes it to the appropriate queue (in the dictionary listof queues) and displays the updated queue.

 (4) Pop an item from the top of a specific queue. When the client passes the queue ID and requests the server to pop (remove the first element from the top of) an item from a specific queue, the server removes that item, displays the updated queue in the dictionary, and returns the removed item to the client, which the client displays.

 (5) Return the topmost (first) element from a specified queue, which has been created when the queue ID is passed by the client to the server.

 (6) Return the size of a specified queue, which has been created when the queue ID is passed by the client to the server.

 

 

 ERROR HANDLING

 The following are the possible sources of error when performing operations on the FTQueue Data Structure that we implemented, and they have all been handled.

 (1) When creating a new queue, a label cannot be passed that already exists for a queue that has been created previously. Each time a queue is intended to be created, a new label should be passed. 

 (2) To return the queue ID of a label, the label (associated with a queue) must exist in the list listoflabels.

 (3) To Push an item into a specific queue, which is identified by its queue ID, the required queue (into which we want to push the item) should exist in the dictionary listofqueues, and hence the label associated with the required queue should exist in the list listoflabels.

 (4) To Pop an item from a specific queue identified by its queue ID,

 (a) the required queue (from which we want to pop an item) should exist in the dictionary listofqueues, and hence the label associated with the required queue should exist in the list listoflabels.

 (b) the required queue should have at least one item inside it. 

 (5) Similarly, to return the value of the first element of specific queue identified by its queue ID

 (a) the required queue (from which we want to pop an item) should exist in the dictionary listofqueues, and hence the label associated with the required queue should exist in the list listoflabels.

 (b) the required queue should have at least one item inside it. 

 (6) To return the number of items in a specific queue identified by its queue ID, the required queue (for which the size is required) should exist in the dictionary listofqueues, and hence the label associated with the required queue should exist in the list listoflabels.











