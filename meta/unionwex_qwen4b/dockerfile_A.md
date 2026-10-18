---
name: dockerfile-hardened+dockerfile-catalog
description: Combined rules of `dockerfile-hardened` and `dockerfile-catalog`. Use for any Dockerfile.
---

# Combined skill: dockerfile-hardened + dockerfile-catalog

Follow every rule below.

## Rules from `dockerfile-hardened`

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.
- Declare `STOPSIGNAL SIGTERM` so that the container shuts down gracefully.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.
- Declare the build argument `ARG APP_VERSION=dev` so that the pipeline can stamp the image.
- Set the working directory with `WORKDIR /opt/service`. No other working directory may be used anywhere in the file.

## Rules from `dockerfile-catalog`

- Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`.
- Use `WORKDIR /srv/app` as the working directory. The file must not set any other working directory.
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Put a header comment `# Owner: <team>` at the top of the file.
- Fix the container time zone with `ENV TZ=UTC`.

If two rules cannot both hold, the rule from `dockerfile-hardened` wins.

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1
# Owner: platform-api
# step: Set the time zone to UTC
ENV TZ=UTC

# step: Set build argument for application version
ARG APP_VERSION=dev
LABEL org.opencontainers.image.description="Python 3.12 FastAPI service listening on port 8000"

# step: Set working directory
WORKDIR /opt/service

# step: Install Python 3.12 and dependencies
RUN apt-get update && apt-get install -y python3.12 python3.12-venv && \
    python3.12 -m venv /opt/service/venv && \
    /opt/service/venv/bin/pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# step: Create non-root user with UID 10001
RUN adduser --disabled-password --gecos '' --uid 10001 appuser && \
    chown -R 10001:10001 /opt/service

# step: Set the user to run the service
USER 10001

# step: Run the FastAPI service with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# step: Define a health check to probe the service
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

# step: Ensure the container shuts down gracefully
STOPSIGNAL SIGTERM
```
