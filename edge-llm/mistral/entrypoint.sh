#!/bin/bash

# Start Ollama server in the background
/usr/bin/ollama serve &

# Wait for Ollama server to start
sleep 5

# Start Open WebUI
node dist/index.js --host 0.0.0.0 --port 8080 &

# Keep the container running
tail -f /dev/null
