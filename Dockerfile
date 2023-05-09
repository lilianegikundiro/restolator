# Base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . /app/

# Expose a port (if necessary)
EXPOSE 8000

# Run database migrations
# RUN python manage.py migrate
# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
