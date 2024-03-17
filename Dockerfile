FROM python:3.8

WORKDIR /usr/src/app
COPY . .

RUN pip install Flask
RUN pip install python-dotenv

EXPOSE 5000

CMD ["python", "./app.py"]