# QR Code Generator with Docker

This project generates a QR code that links to your GitHub homepage. 

## QR Code Image
Below is the generated QR code that links to the GitHub homepage:

![QR Code Image](qr_codes/githubQR.png)

## Log of QR Code Generation
Here is a log output of the successful QR code generation:

![Log Image](path/to/log/image.png)

## How to Build and Run

### Step 1: Build the Docker Image
```bash
docker build -t my-qr-app .
```

### Step 2: Run the Docker Container
To generate the QR code with the default URL:
```bash
docker run -d --name qr-generator my-qr-app
```

To customize the QR code with environment variables:
```bash
docker run -d --name qr-generator \
  -e QR_DATA_URL='https://github.com/kaw393939' \
  -e QR_CODE_DIR='qr_codes' \
  -e QR_CODE_FILENAME='githubQR.png' \
  -e FILL_COLOR='blue' \
  -e BACK_COLOR='yellow' \
  -v $(pwd)/qr_codes:/app/qr_codes \
  my-qr-app
```

### Step 3: View the Logs
To confirm the QR code generation:
```bash
docker logs qr-generator
```

### Additional Docker Commands

- **Stop the container**: `docker stop qr-generator`
- **Remove the container**: `docker rm qr-generator`
- **List Docker images**: `docker images`
- **Remove the image**: `docker rmi my-qr-app`