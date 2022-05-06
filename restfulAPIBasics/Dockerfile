FROM python:3.8-slim-buster
WORKDIR /app

# Create & activate virtual env
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

# Copy all the files & folders from the DJ-WD to this docker image's WD
COPY . .

# Local server cmd - run in Docker
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8080"]

# Production server cmd - run in Local Docker
# CMD ["gunicorn", "--bind", ":8080", "--workers", "3", "restfulAPIBasics.wsgi:application"]
# EXPOSE 8080   # wouldn't work in the heroku container's production-server

# Production server cmd - (for running Docker Container inside Heroku)
CMD gunicorn restfulAPIBasics.wsgi:application --bind 0.0.0.0:$PORT