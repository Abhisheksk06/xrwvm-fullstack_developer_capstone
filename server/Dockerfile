# Use the official Python slim image as a base image
FROM python:3.12.0-slim-bookworm

# Prevents Python from buffering stdout and stderr
ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1

# Define the application directory
ENV APP=/app

# Set the working directory inside the container
WORKDIR $APP

# Copy the requirements.txt file and install dependencies
COPY requirements.txt $APP
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . $APP

# Expose the port the app runs on
EXPOSE 8000

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint to the shell script
ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
