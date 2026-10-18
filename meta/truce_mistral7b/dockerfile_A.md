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

## Rules kept unchanged from `dockerfile-catalog`

- Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `
- Put a header comment `# Owner: <team>` at the top of the file
- Fix the container time zone with `ENV TZ=UTC`

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the Dockerfile such that it sets the working directory only to `WORKDIR /opt/service` and does not include any other `WORKDIR` command anywhere in the file.
- Combine the rules as follows: "Declare the build argument `ARG APP_VERSION=dev` and describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description` in the same Dockerfile."

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1
# Owner: platform-api
ENV TZ=UTC
ARG APP_VERSION=dev

# step: Install Python 3.12 and dependencies
RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
RUN curl -fsSL https://swaps.python.org/psf/pypi/wheels/3.12/linux/amd64/Python-3.12.whl -o python3.12.whl
RUN dpkg -i python3.12.whl
RUN python3.12 -m ensurepip --upgrade --default-pip
RUN pip3.12 install --no-cache-dir -r requirements.txt

# step: Set working directory and copy app
WORKDIR /opt/service
COPY . /opt/service

# step: Declare image description and build arguments
LABEL org.opencontainers.image.description="Python 3.12 FastAPI service"

# step: Run the service
USER 10001
EXPOSE 8000
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
STOPSIGNAL SIGTERM
```
