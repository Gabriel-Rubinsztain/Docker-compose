FROM python:3.8-alpine
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev
RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install psycopg2
COPY . .
RUN chmod -R a+rwx templates
CMD ["python", "app.py"]