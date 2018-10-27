from __future__ import print_function

import sys
import time
from functools import partial
sys.path.append("../")
from pysyncobj import SyncObj, replicated
class FTQueue(SyncObj):
    def __init__(self,selfNodeAddr,otherNodeAddrs):
    	super(FTQueue,self).__init__(selfNodeAddr,otherNodeAddrs)
        self.__counter = 100

    @replicated
    def qCreate(label):
        self.items = []

    @replicated
    def qPush(self, item):
        self.items.insert(0,item)
    @replicated
    def qPop(self):
        self.items.pop()
    @replicated
    def qSize(self):
        return len(self.items)
    @replicated
    def qTop(self):
        return(self.first())
    @replicated
    def qPrint(self):
        for items in self.items:
        	print items,
    for i in range (0, queue_id)	
        q[queue_id] = Queue()
        q[queue_id].qPush(1)
        q[queue_id].qPush(2)
        q[queue_id].qPush(3)
        q[queue_id].qPush(4)
        q.qPrint()
        q[queue_id].qPop
        q.qPrint()
def onAdd(res, err, cnt):
    print('onAdd %d:' % cnt, res, err)
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: %s self_port partner1_port partner2_port ...' % sys.argv[0])
        sys.exit(-1)
    port = int(sys.argv[1])
    partners = ['localhost:%d' % int(p) for p in sys.argv[2:]]
    o = TestObj('localhost:%d' % port, partners)
    n = 0
    old_value = -1
    while True:
        # time.sleep(0.005)
        time.sleep(0.5)
        if o.getCounter() != old_value:
            old_value = o.getCounter()
            print(old_value)
        if o._getLeader() is None:
            continue
        # if n < 2000:
        if n < 20:
            o.addValue(10, n, callback=partial(onAdd, cnt=n))
            n += 1
        # if n % 200 == 0:
        # if True:
        #    print('Counter value:', o.getCounter(), o._getLeader(), o._getRaftLogSize(), o._getLastCommitIndex())

