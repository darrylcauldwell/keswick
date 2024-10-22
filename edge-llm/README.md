# Build image with LLM model included

docker buildx build --platform linux/arm64 -t ghcr.io/darrylcauldwell/edge-llm:latest --push .
docker buildx build --platform linux/amd64 -t ghcr.io/darrylcauldwell/edge-llm:latest --push .

## Test solution locally

docker network create llm-network
docker run --name edge-llm \
  --network llm-network \
  -p 11434:11434 \
  ghcr.io/darrylcauldwell/edge-llm:latest
docker run --name openwebui \
  --network llm-network \
  -p 8080:8080 \
  -e OLLAMA_BASE_URL=http://edge-llm:11434 \
  -e WEBUI_AUTH=False \
  ghcr.io/open-webui/open-webui:main

## Deploy solution to kubernetes

kubectl apply -f edge-llm.yml