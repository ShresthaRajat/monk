FROM python:3.7-slim
WORKDIR /app
COPY ./src /app/src
COPY ./app.py /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
EXPOSE 8080:8080