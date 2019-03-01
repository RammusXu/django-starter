FROM python:3

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY app /app

EXPOSE 5000

CMD python app.py
# CMD FLASK_APP=index.py flask run
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]