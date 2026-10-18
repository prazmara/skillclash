---
name: dockerfile-catalog+dockerfile-hardened
description: Merged skill that replaces `dockerfile-catalog` and `dockerfile-hardened`. Use for any Dockerfile.
---

# Merged skill: dockerfile-catalog + dockerfile-hardened

This skill replaces `dockerfile-catalog` and `dockerfile-hardened`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `dockerfile-catalog`

- Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`
- Use `WORKDIR /srv/app` as the working directory. The file must not set any other working directory.
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Put a header comment `# Owner: <team>` at the top of the file.
- Fix the container time zone with `ENV TZ=UTC`

## Rules kept unchanged from `dockerfile-hardened`

- syntax=docker/dockerfile:1
- STOPSIGNAL SIGTERM
- HEALTHCHECK
- USER 10001
- ARG APP_VERSION=dev
- WORKDIR /opt/service

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1
# Owner: platform-api
FROM python:3.12-slim

ENV TZ=UTC
WORKDIR /opt/service

USER 10001

ARG APP_VERSION=dev

LABEL org.opencontainers.image.description="FastAPI service"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/ || exit 1

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
