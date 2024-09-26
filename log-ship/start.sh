#!/bin/bash

# Start NFS server
/usr/sbin/exportfs -r
/usr/sbin/rpcbind
/usr/sbin/rpc.nfsd
/usr/sbin/rpc.mountd

# Output a message to indicate started
echo "I'm started and ready for accepting incoming files to NFS"
echo "*********************************************************"

# Monitor NFS share for new files
inotifywait -m /nfs_share -e create -e moved_to |
    while read path action file; do
        echo "The file '$file' appeared in directory '$path' via '$action'"
        # Copy the file to another location
        # cp "$path/$file" /destination_folder/
    done
