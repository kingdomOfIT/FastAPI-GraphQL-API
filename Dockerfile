FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 intall --upgrade pip
RUN pip3 -r requirements.txt
COPY . /app
EXPOSE 8000