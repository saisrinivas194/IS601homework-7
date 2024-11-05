# Use the official Python image from the Python Docker Hub repository as the base image
FROM python:3.12-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Create a non-root user named 'myuser' with a home directory
RUN useradd -m myuser

# Set environment variables
ENV QR_DATA_URL=https://github.com/saisrinivas194
ENV QR_CODE_DIR=qr_codes
ENV QR_CODE_FILENAME=githubQR.png
ENV FILL_COLOR=black
ENV BACK_COLOR=white

# Copy requirements.txt to the container and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Create output directory for QR codes and set ownership to 'myuser'
RUN mkdir -p /app/${QR_CODE_DIR} && chown myuser:myuser /app/${QR_CODE_DIR}

# Copy the rest of the application's source code into the container, setting ownership to 'myuser'
COPY --chown=myuser:myuser . .

# Switch to the 'myuser' user to run the application
USER myuser

# Run the Python script when the container starts
ENTRYPOINT ["python", "main.py"]
