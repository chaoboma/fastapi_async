from concurrent.futures import ProcessPoolExecutor
import time

def test(num):
    print("Processs"+str(num))
    time.sleep(50)

# 新建ProcessPoolExecutor对象并指定最大的进程数量
executor = ProcessPoolExecutor(max_workers=3)
# 提交多个任务到进程池中
executor.submit(test, 1)
executor.submit(test, 2)
executor.submit(test, 3)