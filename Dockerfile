# base image
FROM python:3.12-alpine


# set working directory
WORKDIR /app

# Install Dependencies
RUN apk update && \
    apk add --virtual build-deps gcc musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

# Dealing with requirements
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Coping project
COPY . /app

# run server
CMD ["gunicorn","project:create_app()"]
