FROM python:3.8-alpine
RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install psycopg2
COPY . .
RUN chmod -R a+rwx templates
CMD ["python", "app.py"]