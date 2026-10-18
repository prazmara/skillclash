---
name: dockerfile-catalog+dockerfile-hardened
description: Combined rules of `dockerfile-catalog` and `dockerfile-hardened`. Use for any Dockerfile.
---

# Combined skill: dockerfile-catalog + dockerfile-hardened

Follow every rule below.

## Rules from `dockerfile-catalog`

- Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`.
- Use `WORKDIR /srv/app` as the working directory. The file must not set any other working directory.
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Put a header comment `# Owner: <team>` at the top of the file.
- Fix the container time zone with `ENV TZ=UTC`.

## Rules from `dockerfile-hardened`

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.
- Declare `STOPSIGNAL SIGTERM` so that the container shuts down gracefully.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.
- Declare the build argument `ARG APP_VERSION=dev` so that the pipeline can stamp the image.
- Set the working directory with `WORKDIR /opt/service`. No other working directory may be used anywhere in the file.

If two rules cannot both hold, the rule from `dockerfile-catalog` wins.

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1
# Owner: platform-api
ARG APP_VERSION=dev
FROM python:3.12-slim

LABEL org.opencontainers.image.description="A FastAPI service running on Python 3.12 with uvicorn."
ENV TZ=UTC
WORKDIR /srv/app

# step: Install system dependencies and create non-root user
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    adduser --disabled-password --gecos '' --uid 10001 appuser

# step: Copy application dependencies and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# step: Copy application source code
COPY . .

# step: Change ownership of the working directory to the non-root user
RUN chown -R 10001:10001 /srv/app

USER 10001

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

STOPSIGNAL SIGTERM

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
