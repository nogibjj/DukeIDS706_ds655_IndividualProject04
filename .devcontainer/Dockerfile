# Use the specified Python version.
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# If Node.js is required, install it.
ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi


# Set the working directory.
WORKDIR /app

# Copy the requirements file into the container.
COPY requirements.txt .

# Install the requirements.
RUN pip install -r requirements.txt

# Copy the rest of the application into the container.
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Start the application.
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]