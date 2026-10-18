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

## Rules kept unchanged from `dockerfile-catalog`

- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Put a header comment `# Owner: <team>` at the top of the file.
- Fix the container time zone with `ENV TZ=UTC`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- Set the working directory with `WORKDIR /opt/service` and explain each `RUN` instruction with a comment line directly above it that starts with `# step: `, by placing the `WORKDIR` instruction at the top of the file and then using `RUN` instructions with comments below it, like this: ``` WORKDIR /opt/service # step: <instruction> RUN <command> # step: <instruction> RUN <command> ```

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# Owner: platform-api
# syntax=docker/dockerfile:1

FROM python:3.12-slim

ARG APP_VERSION=dev

LABEL org.opencontainers.image.description="Python 3.12 FastAPI service"

ENV TZ=UTC
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /opt/service

# step: install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# step: expose port 8000
EXPOSE 8000

# step: set non-root user
USER 10001

# step: set healthcheck
HEALTHCHECK --interval=10s --timeout=3s --retries=3 CMD curl -f http://localhost:8000/ || exit 1

# step: start service
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

STOPSIGNAL SIGTERM
```
