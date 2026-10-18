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

- The first line of the file must be `# syntax=docker/dockerfile:1`, followed immediately by a header comment `# Owner: <team>`.

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1
# Owner: platform-api

# step: Set working directory
WORKDIR /opt/service

# step: Set non-root user
USER 10001

# step: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# step: Copy application code
COPY. /opt/service/app

# step: Set environment variables
ENV TZ=UTC
ENV APP_VERSION=dev

# step: Run the service
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# step: Declare healthcheck
HEALTHCHECK --interval=10s --timeout=3s --retries=3 CMD curl -f http://localhost:8000/ || exit 1

# step: Declare build arguments
ARG APP_VERSION=dev

# step: Declare stopsignal
STOPSIGNAL SIGTERM

# step: Describe the image
LABEL org.opencontainers.image.description="Python 3.12 FastAPI service"
```
