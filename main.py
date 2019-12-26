# encoding=utf-8
'''
    1. 这里是模拟了主线程开启子线程，并捕获子线程中发生的错误
    2. 开启的子线程都是异步线程，异步执行
'''
import runScriptThread
import errorRaiser
import time
 
def newThreadAction(i):
    newThread = runScriptThread.runScriptThread(errorRaiser.testAction, i)
    # 这里是捕获子程序的错误，并进行处理
    def errorHandler(msg):
        print('errorHandler here!  %s'%(msg))
    newThread.errorHandler = errorHandler
    '''
        关于守护进程的设置：
            1. 如果设置进程为守护进程，则子进程会在父进程结束时一并结束
            2. 如果希望主程序等待子程序结束时再退出的话，只要设置子程序为非守护进程(默认即为非守护进程，
               即 thread.daemon = False)或者子程序start()后调用join()即可
    '''
    newThread.start()
    return newThread
    # newThread.join()

if __name__=='__main__':
    print('__main__ starts')
    arr = []
    for i in [5, 9]:
        arr.append(newThreadAction(i))
    # for thread in arr:
    #     thread.start()
    # print('before sleep')
    # time.sleep(2)
    # print('before join')
    # for thread in arr:
    #     thread.join()
    print('__main__ ends')