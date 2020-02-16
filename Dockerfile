FROM python:3.7

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

RUN python3 bootstrap.py

RUN python3 loader.py

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
