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

- Write the first line as `# syntax=docker/dockerfile:1 # Owner: <team>` to ensure both the Dockerfile parser directive and the owner comment are included at the top of the file.

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1 # Owner: platform-api
FROM python:3.12-slim-buster

ENV TZ=UTC
WORKDIR /srv/app

ARG APP_VERSION=dev

RUN apt-get update && apt-get install -y \
    tzdata \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    -r requirements.txt

COPY requirements.txt .dockerignore ./
COPY app /srv/app/

USER 10001

HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

LABEL org.opencontainers.image.description="Python 3.12 FastAPI service"
STOPSIGNAL SIGTERM
```
