---
name: dockerfile-hardened+dockerfile-catalog
description: Merged skill that replaces `dockerfile-hardened` and `dockerfile-catalog`. Use for any Dockerfile.
---

# Merged skill: dockerfile-hardened + dockerfile-catalog

This skill replaces `dockerfile-hardened` and `dockerfile-catalog`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `dockerfile-hardened`

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.
- Declare `STOPSIGNAL SIGTERM` so that the container shuts down gracefully.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.
- Declare the build argument `ARG APP_VERSION=dev` so that the pipeline can stamp the image.
- Set the working directory with `WORKDIR /opt/service`. No other working directory may be used anywhere in the file.

## Rules kept unchanged from `dockerfile-catalog`

- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Put a header comment `# Owner: <team>` at the top of the file.
- Fix the container time zone with `ENV TZ=UTC`.

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1
# Owner: platform-api
# step: Install dependencies
FROM python:3.12-slim AS base

WORKDIR /opt/service

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# step: Build the application
FROM base AS final

EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=30s --retries=3 CMD ["curl", "-f", "http://localhost:8000/health"] || exit 1
STOPSIGNAL SIGTERM
USER 10001
ARG APP_VERSION=dev
LABEL org.opencontainers.image.description="FastAPI service using Python 3.12"

COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Fix the container time zone
ENV TZ=UTC
```
