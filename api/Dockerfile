FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/.

HEALTHCHECK CMD curl --fail http://0.0.0.0:8000/health/ || exit 1

CMD ["uvicorn", "start_api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]