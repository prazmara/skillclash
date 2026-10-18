---
name: dockerfile-hardened+dockerfile-catalog
description: Merged skill that replaces `dockerfile-hardened` and `dockerfile-catalog`. Use for any Dockerfile.
---

# Merged skill: dockerfile-hardened + dockerfile-catalog

This skill replaces `dockerfile-hardened` and `dockerfile-catalog`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `dockerfile-hardened`

- Set the working directory with `WORKDIR /opt/service`. No other working directory may be used anywhere in the file.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Declare the build argument `ARG APP_VERSION=dev` so that the pipeline can stamp the image.
- Declare `STOPSIGNAL SIGTERM` so that the container shuts down gracefully.

## Rules kept unchanged from `dockerfile-catalog`

- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Fix the container time zone with `ENV TZ=UTC`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- # syntax=docker/dockerfile:1\n# Owner: <team>

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1
# Owner: platform-api
FROM python:3.12-slim

# Set the working directory
WORKDIR /opt/service

# Set environment variables
ENV TZ=UTC

# Set build argument for version
ARG APP_VERSION=dev

# Install system dependencies
# step: Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
# step: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user with UID 10001
# step: Create non-root user
RUN adduser --disabled-password --gecos '' --uid 10001 appuser && chown -R 10001:10001 /opt/service

# Set the user to run the service
USER 10001

# Copy application code
# step: Copy application code
COPY . /opt/service

# Expose port 8000
EXPOSE 8000

# Start the service with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Label the image
LABEL org.opencontainers.image.description="Python 3.12 FastAPI service listening on port 8000"
```
