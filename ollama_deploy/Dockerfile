FROM ollama/ollama:latest

EXPOSE 11434

# Set the working directory in the container
WORKDIR /usr/src/app

# Add entrypoint script to ensure proper execution environment
COPY entrypoint.sh /usr/src/app/entrypoint.sh
COPY Modelfile /usr/src/app/Modelfile

# Give execution permissions to the entrypoint script
RUN chmod +x /usr/src/app/entrypoint.sh

# Use the entrypoint script to set up the environment and run the command
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
