# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install application dependencies
RUN pip3 install -r requirements.txt
# RUN pip3 install Flask Flask-CORS mysql-connector-python

# Expose the backend port
# EXPOSE 5000

# Define the command to start your Flask app
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]