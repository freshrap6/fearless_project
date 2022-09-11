from python:3.9

RUN pip install pipenv

COPY . /app
WORKDIR /app

RUN pipenv install --system --deploy
RUN chmod +x ./entrypoint.sh

EXPOSE  3000
ENTRYPOINT [ "sh", "entrypoint.sh" ]
