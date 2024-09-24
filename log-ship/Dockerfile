# Use the latest Alpine Linux as the base image
FROM alpine:latest

# Install NFS utilities without caching the index of available packages
# This keeps the image size smaller
RUN apk add --no-cache nfs-utils

# Create a directory to be used as the NFS share
RUN mkdir -p /nfs_share

# Configure the NFS exports file
# This line allows all hosts (*) to access /nfs_share with the following options:
# - rw: read-write access
# - sync: write operations are immediately written to the disk
# - no_subtree_check: disables subtree checking, can improve reliability
# - no_root_squash: allows root users on clients to access as root on the server
RUN echo "/nfs_share *(rw,sync,no_subtree_check,no_root_squash)" > /etc/exports

# Copy a startup script from the host into the container
COPY start.sh /start.sh

# Make the startup script executable
RUN chmod +x /start.sh

# Inititate script 
ENTRYPOINT ["/start.sh"]
