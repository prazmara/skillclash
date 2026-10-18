---
name: dockerfile-catalog+dockerfile-hardened
description: Merged skill that replaces `dockerfile-catalog` and `dockerfile-hardened`. Use for any Dockerfile.
---

# Merged skill: dockerfile-catalog + dockerfile-hardened

This skill replaces `dockerfile-catalog` and `dockerfile-hardened`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `dockerfile-catalog`

- Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`
- Use `WORKDIR /srv/app` as the working directory
- The file must not set any other working directory
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `
- Put a header comment `# Owner: <team>` at the top of the file
- Fix the container time zone with `ENV TZ=UTC`

## Rules kept unchanged from `dockerfile-hardened`

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.
- Declare `STOPSIGNAL SIGTERM` so that the container shuts down gracefully.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Combine the rules as follows: "In the Dockerfile, set the `org.opencontainers.image.description` LABEL and declare the build argument `ARG APP_VERSION=dev`: ```Dockerfile LABEL org.opencontainers.image.description="Your description here" ARG APP_VERSION=dev ```

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1
# Owner: platform-api

# syntax directive, first line of the file
# stop signal for graceful shutdown
STOPSIGNAL SIGTERM

# set working directory
WORKDIR /srv/app

# build argument and image description
LABEL org.opencontainers.image.description="Python 3.12 FastAPI service listening on port 8000"
ARG APP_VERSION=dev

# set timezone
ENV TZ=UTC

# install dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && pip install --no-cache-dir \
    --upgrade pip \
    $APP_VERSION \
    fastapi \
    uvicorn \
    gunicorn \
    psycopg2-binary \
    && rm -rf /var/lib/apt/lists/*

# set non-root user
USER 10001

# copy application code
COPY . /srv/app

# run the service
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# healthcheck
HEALTHCHECK CMD ["CMD-SHELL", "curl --fail http://localhost:8000/health || exit 1"]
```
