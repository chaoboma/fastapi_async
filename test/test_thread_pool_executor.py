from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import time

def test(num):
    print("Threads:"+str(num))
    return "ok"

# 新建ThreadPoolExecutor对象并指定最大的线程数量
print('start')
thread_pool=ThreadPoolExecutor(max_workers=13)
# 提交多个任务到线程池中
thread_pool.submit(test,1)
thread_pool.submit(test,2)
thread_pool.submit(test,3)