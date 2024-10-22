FROM ollama/ollama:latest

# Install any necessary dependencies
RUN apt-get update && apt-get install -y wget

# Start Ollama server, pull the model, then stop the server
RUN ollama serve & \
    sleep 10 && \
    ollama pull llama3.1:8b && \
    pkill ollama

# Expose the Ollama port
EXPOSE 11434

# Set the entrypoint to start Ollama
ENTRYPOINT ["ollama", "serve"]