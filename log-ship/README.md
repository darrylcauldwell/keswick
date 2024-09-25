# Log shipper container

A base container with NFS and a log forwarder script.

## Build and test

```bash
export CR_PAT=<personal access token>
echo $CR_PAT | docker login ghcr.io -u darrylcauldwell --password-stdin        
docker buildx build --platform linux/amd64,linux/arm64 . --tag ghcr.io/darrylcauldwell/log-shipper:latest --push

docker pull ghcr.io/darrylcauldwell/log-shipper:latest
docker run --name log-shipper -d -p 2049:2049  ghcr.io/darrylcauldwell/log-shipper:latest
```
