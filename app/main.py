import time
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()

# 创建全局线程池
thread_pool = ThreadPoolExecutor(max_workers=10)


def long_running_task(id):
    print(f"{id} 开始执行！"+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(10)
    print(f"{id} print ok" + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return "OK"

@app.get("/test/{id}")
def test(request: Request, id):
    print(f"{id} 请求进入！"+datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    future = thread_pool.submit(long_running_task, id)
    # 等待任务结束
    #res = future.result()
    return 'end'



@app.get("/test3")
async def test():
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now_time, "/test3")
    time.sleep(10)
    return "OK"


@app.get("/test4")
def test(request: Request):
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now_time, request.url)
    time.sleep(10)
    return "OK"


if __name__ == "__main__":
    # 创建解析器
    parser = ArgumentParser()
    # 添加命令行参数
    parser.add_argument('--host', default="0.0.0.0", type=str, help='Server bound address')
    parser.add_argument('--port', default=8000, type=int, help='Port number')
    # 解析命令行参数
    args = parser.parse_args()
    # 启动服务器
    uvicorn.run(app='main:app', host=args.host, port=args.port,reload=True)