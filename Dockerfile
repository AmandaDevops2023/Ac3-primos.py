FROM python:3.7-slim
RUN pip install flask
RUN mkdir templates
RUN mkdir static
COPY primos.py /primos.py
COPY templates/*  /templates/
COPY static/*  /static/
RUN chmod -R a+rwx static
RUN chmod -R a+rwx templates
CMD ["python","primos.py"]
