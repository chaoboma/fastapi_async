#FROM python:3.10.14
FROM fastapi_demo:v1.2
EXPOSE 31017
COPY ./app /app
COPY ./requirements.txt /app
WORKDIR /app
RUN pip config set global.index-url --site https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "31017"]
ENTRYPOINT ["python", "main.py"]

