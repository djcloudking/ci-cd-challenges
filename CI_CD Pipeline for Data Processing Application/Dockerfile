# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy src directory
COPY src/ ./src/

# Run tests on build# Run tests on build
CMD ["python", "-m", "src.data_processor"]
