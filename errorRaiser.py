#encoding=utf-8
'''
    这个是模拟要执行的子线程
    testAction会在第 i 秒后抛出异常
'''
import time

def testAction(i):
    # print('a error will raise after %s, item is %s'%(i, i))
    j = abs(i)
    while True:
        print('test action is %s,  j is %s'%(i, j))
        time.sleep(1)
        1 / j
        j = j - 1
        # raise RuntimeError('I\'m the errror')