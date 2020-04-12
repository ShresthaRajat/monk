FROM python:3.7-slim

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

RUN echo "hello"

RUN pip install -e .

RUN ls

ENTRYPOINT [ "python" ]

CMD [ "src/graphql_server.py" ]

EXPOSE 8001:8001