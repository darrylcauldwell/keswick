# Use Ubuntu 22.04 LTS as the base image
FROM ubuntu:22.04

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install NFS server
RUN apt-get update && \
    apt-get install -y nfs-kernel-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a directory to be used as the NFS share
RUN mkdir -p /nfs_share

# Configure the NFS exports file
# This line allows all hosts (*) to access /nfs_share with the following options:
# - rw: read-write access
# - sync: write operations are immediately written to the disk
# - no_subtree_check: disables subtree checking, can improve reliability
# - all_squash: maps all UIDs and GIDs from clients to the anonymous user
# - anonuid=65534: sets the UID of the anonymous user (typically nobody)
# - anongid=65534: sets the GID of the anonymous user (typically nogroup)
# - insecure: allows connections from ports higher than 1024
# - no_wdelay: disables write delay
# - no_acl: disables ACL support
RUN echo "/nfs_share *(rw,sync,no_subtree_check,all_squash,anonuid=65534,anongid=65534,insecure,no_wdelay,no_acl)" > /etc/exports

# Copy a startup script from the host into the container
COPY start.sh /start.sh

# Make the startup script executable
RUN chmod +x /start.sh

# Expose NFS ports
EXPOSE 111/tcp 111/udp 2049/tcp 2049/udp

# Initiate script 
ENTRYPOINT ["/start.sh"]
