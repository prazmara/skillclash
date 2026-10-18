---
name: dockerfile-catalog+dockerfile-hardened
description: Merged skill that replaces `dockerfile-catalog` and `dockerfile-hardened`. Use for any Dockerfile.
---

# Merged skill: dockerfile-catalog + dockerfile-hardened

This skill replaces `dockerfile-catalog` and `dockerfile-hardened`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `dockerfile-catalog`

- Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`.
- Use `WORKDIR /srv/app` as the working directory. The file must not set any other working directory.
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Put a header comment `# Owner: <team>` at the top of the file.
- Fix the container time zone with `ENV TZ=UTC`.

## Rules kept unchanged from `dockerfile-hardened`

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- LABEL org.opencontainers.image.description="Built with APP_VERSION=${APP_VERSION}" ARG APP_VERSION=dev

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1
# Owner: platform-api
# LABEL org.opencontainers.image.description="Built with APP_VERSION=dev"

WORKDIR /srv/app
ENV TZ=UTC

ARG APP_VERSION=dev
LABEL org.opencontainers.image.description="Built with APP_VERSION=${APP_VERSION}"

# step: Set up the base image with Python 3.12
FROM python:3.12-slim

# step: Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && rm -rf /var/lib/apt/lists/*

# step: Copy requirements.txt to the container
COPY requirements.txt /srv/app/requirements.txt

# step: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# step: Copy the application source code
COPY . /srv/app

# step: Set the non-root user with UID 10001
USER 10001

# step: Expose port 8000
EXPOSE 8000

# step: Start the FastAPI service using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

STOPSIGNAL SIGTERM
```
