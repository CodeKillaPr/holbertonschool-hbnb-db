# Use an appropriate base image with Python and Alpine Linux
FROM python:3.9-alpine

# Set environment variables
ENV FLASK_APP=api.review_manager
ENV FLASK_RUN_HOST=0.0.0.0
ENV PORT=8000

# Create and set the working directory
WORKDIR /app

# Install dependencies for building Python packages
RUN apk update && apk add --no-cache build-base postgresql-dev gcc python3-dev musl-dev curl

# Copy the requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install Flask

# Copy the application source code
COPY . /app/

# Expose the port the application will run on
EXPOSE $PORT

# Create a volume for data persistence
VOLUME /app/data

# Set the command to run Gunicorn
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} api.review_manager:app"]
