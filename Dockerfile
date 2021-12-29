FROM python:3.9-buster
RUN mkdir /usr/src/api/
RUN mkdir /usr/src/api/greeting_app
ENV FLASK_APP=greeting_app.create_app:create_app
COPY . /usr/src/api/
WORKDIR /usr/src/api
RUN pip install -r requirements.txt
RUN chmod +x ./wait-for-it.sh
RUN chmod +x ./init.sh
CMD sh init.sh