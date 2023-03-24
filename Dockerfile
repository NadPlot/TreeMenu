
# Pull base image
FROM python:3.10-slim

# Set enviroment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

# Copy project
COPY . /code/
