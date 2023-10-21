# Use the official Ubuntu as a parent image
FROM ubuntu:latest

# Set environment variables to prevent interactive installation prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=UTC

# Update the package list and install required packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    libopencv-dev \
    python3-opencv \
    gstreamer1.0-tools \
    ffmpeg

# Clean up the package cache to reduce image size
RUN apt-get clean

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Start a Python shell when the container runs
CMD ["python3"]
