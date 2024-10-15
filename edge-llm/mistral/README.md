
docker buildx build --platform linux/amd64,linux/arm64 -t ghcr.io/darrylcauldwell/edge-llm:latest --push .

docker buildx build --platform linux/arm64 -t ghcr.io/darrylcauldwell/edge-llm:latest --push .
docker buildx build --platform linux/amd64 -t ghcr.io/darrylcauldwell/edge-llm:latest --push .

docker run -p 11434:11434 -p 8080:8080 ghcr.io/darrylcauldwell/edge-llm:latest
