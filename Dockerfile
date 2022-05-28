FROM python:3.10

WORKDIR /personal-bank

COPY ./requirements.txt /personal-bank/requirements.txt

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /personal-bank/requirements.txt

COPY ./app /personal-bank/app

CMD ["gunicorn", "-c", "app/gunicorn.conf", "app.main:app", "--preload", "--max-requests-jitter", "5"]
