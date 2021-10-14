FROM python:alpine3.7

ENV REDIS_HOST='localhost'
ENV REDIS_PORT=6379
ENV REDIS_PASSWORD=''
ENV BRAND_NAME='Mission Imposibble'

COPY . /app
WORKDIR /app
RUN pip install --disable-pip-version-check -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
