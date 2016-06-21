from multiprocessing import Process, Pool, Queue
import os, time, random

'''
os.getpid() : process id of current app

PROCESs
p1 = Process(target=func, args=tuple)
p1.start() : start child process
p1.join() : wait for p1 ended

POOl : plenty os processes
    print 'Parent process %4s running.......' % os.getpid()
    # this interger repre tasks all in
    p_pool = Pool(5) 
    for i in range(10):
        p_pool.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p_pool.close()
    p_pool.join()
    print 'All process done.'

CONN : Queue, Pipes
connect with each other using queue
'''
# child process app
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

def long_time_task(name):
    print 'Run task %s <%4s>' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()
    print 'Task %s run %0.2f seconds...' % (name, (end-start))

def write(q):
    for i in range(20):
        print 'WRITE : PUT %3s in Queue...' % i
        q.put(i)
        time.sleep(random.random()*3)

def read(q):
    while True:
        value = q.get(True)
        print 'READ : GOT %3s ...\n' % value

if __name__ == '__main__':
    q = Queue()
    p_read = Process(target=read, args=(q,))
    p_write = Process(target=write, args=(q,))

    # start
    p_read.start()
    p_write.start()

    # wait for terminating
    p_write.join()

    # terminate
    p_read.terminate()