---
name: dockerfile-catalog+dockerfile-hardened
description: Merged skill that replaces `dockerfile-catalog` and `dockerfile-hardened`. Use for any Dockerfile.
---

# Merged skill: dockerfile-catalog + dockerfile-hardened

This skill replaces `dockerfile-catalog` and `dockerfile-hardened`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `dockerfile-catalog`

- Use `WORKDIR /srv/app` as the working directory. The file must not set any other working directory.
- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Fix the container time zone with `ENV TZ=UTC`.
- Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`.

## Rules kept unchanged from `dockerfile-hardened`

- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Declare the build argument `ARG APP_VERSION=dev` so that the pipeline can stamp the image.

## Reconciled rules (each one satisfies a rule of both skills at once)

- # syntax=docker/dockerfile:1\n# Owner: <team>

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1
# Owner: platform-api
FROM python:3.12-slim

# Set working directory
WORKDIR /srv/app

# Set container time zone
ENV TZ=UTC

# Declare build argument for version
ARG APP_VERSION=dev

# Label the image with a description
LABEL org.opencontainers.image.description="Python 3.12 FastAPI service listening on port 8000"

# Step: Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && rm -rf /var/lib/apt/lists/*

# Step: Install Python dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step: Copy application code
COPY . .

# Step: Run the service as a non-root user (UID 10001)
USER 10001

# Step: Health check to ensure the service is running
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# Start the FastAPI service with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Ensure the container stops cleanly
STOPSIGNAL SIGTERM
```
