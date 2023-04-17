FROM python:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
COPY primos.py /primos.py
CMD ["python","primos.py"]