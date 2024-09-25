# Log shipper container

A base container with NFS and a log forwarder script.

## Build and push

```bash
export CR_PAT=<personal access token>
echo $CR_PAT | docker login ghcr.io -u darrylcauldwell --password-stdin        
docker buildx build --platform linux/amd64,linux/arm64 . --tag ghcr.io/darrylcauldwell/log-shipper:latest --push
```
