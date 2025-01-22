# Use an official Python image as a parent image
FROM python:3.13.1-slim

# Set the timezone to America/Sao_Paulo (UTC-3)
ENV TZ=America/Sao_Paulo

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Define environment variables (if needed)
ENV LOG_FILE=pipeline_logs.log

# Command to run the application
CMD ["python3", "-m", "run", "--host=0.0.0.0"]