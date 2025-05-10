# backend/Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and Flask-CORS
# Flask-CORS is needed for handling requests routed through Ingress,
# as the browser might still see it as a cross-origin request depending on setup.
RUN pip install --no-cache-dir Flask flask-cors

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME=World

# Run app.py when the container launches
CMD ["python", "app.py"]
