from python:3.9

RUN pip install pipenv

ENV PROJECT_DIR /usr/local/src/fearless_project

WORKDIR /app

COPY . /app

RUN pipenv install --system --deploy

ENTRYPOINT [ "python" ]
CMD [ "items_api/api.py" ]