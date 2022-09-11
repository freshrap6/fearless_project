from python:3.9

RUN pip install pipenv

ENV PROJECT_DIR /usr/local/src/fearless_project

COPY . /app
WORKDIR /app

RUN pipenv install --system --deploy
RUN chmod +x ./entrypoint.sh

EXPOSE  3000
ENTRYPOINT [ "sh", "entrypoint.sh" ]
