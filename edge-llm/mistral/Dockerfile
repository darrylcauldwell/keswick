FROM ollama/ollama:latest AS ollama

# Start Ollama server and pull mistral model
RUN ollama serve & \
    sleep 5 && \
    ollama pull mistral && \
    pkill ollama

# Switch to the Open WebUI image
FROM ghcr.io/open-webui/open-webui:main

# Copy Ollama and the model from the first stage
COPY --from=ollama /usr/bin/ollama /usr/bin/ollama
COPY --from=ollama /root/.ollama /root/.ollama

# Copy the entrypoint script
COPY entrypoint.sh /usr/local/bin/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /usr/local/bin/entrypoint.sh

# Expose ports for Ollama and Open WebUI
EXPOSE 11434 8080

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
