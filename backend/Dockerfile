# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the application files
COPY . .

# Set environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development 

# Expose the port the app runs on
EXPOSE 5001

# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
