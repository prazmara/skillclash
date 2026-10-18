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
