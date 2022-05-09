FROM python:3.7-alpine
RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install psycopg2
RUN mkdir templates
RUN mkdir model
COPY app.py /app.py
COPY templates/*  /templates/
COPY model/* /model/
RUN chmod -R a+rwx templates
CMD ["python", "app.py"]