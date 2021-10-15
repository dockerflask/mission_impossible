FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install --disable-pip-version-check -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
