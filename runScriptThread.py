# encoding=utf-8
'''
    继承threading.Thread
'''
import threading

class runScriptThread(threading.Thread): 
    # 初始化
    def __init__(self, funcName, *args):
        print('init with args')
        threading.Thread.__init__(self)
        self.args = args
        self.funcName = funcName
    # 重写run()， 它将会在thread的start()调用后被调用
    def run(self): 
        try:
            self._run()
        except Exception as e:
            print(e)
    def _run(self):
        try:
            # 尝试执行传入的function
            self.funcName(*(self.args))
        except Exception as e:
            print('run error is %s'%(e))
            # 处理错误，方便被主进程捕获
            if self.errorHandler:
                self.errorHandler(self.args)
            raise e