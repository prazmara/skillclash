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

- # syntax=docker/dockerfile:1 # Owner: <team>

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1 # Owner: platform-api
ARG APP_VERSION=dev
FROM python:3.12-slim

LABEL org.opencontainers.image.description="FastAPI service running on Python 3.12 with uvicorn"

ENV TZ=UTC
WORKDIR /srv/app

# step: Install system dependencies and Python dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir "uvicorn[standard]" && \
    pip install --no-cache-dir -r requirements.txt

# step: Copy application code
COPY . .

# step: Create non-root user and assign to it
RUN adduser --disabled-password --gecos '' --uid 10001 appuser && \
    chown -R 10001:10001 /srv/app
USER 10001

# step: Expose port and define startup command
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

STOPSIGNAL SIGTERM
```
