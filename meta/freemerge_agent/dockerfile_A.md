---
name: dockerfile-hardened-catalog
description: Write Dockerfiles that pass the security team's image policy and that the internal service catalog can index. Use for any Dockerfile.
---

# dockerfile-hardened-catalog

This skill merges `dockerfile-hardened` and `dockerfile-catalog` and replaces both. Images are scanned before they may run in production, and the policy checks a fixed install path, a non-root user and a health probe. The service catalog reads ownership and descriptions from the same Dockerfile, and new team members learn the build from its comments.

Every rule of both skills is kept. Where two rules cannot both hold, `dockerfile-hardened` wins.

## Rules

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.
- Put a header comment `# Owner: <team>` at the top of the file. It goes on the second line, directly below the parser directive and before any instruction, so that both header rules hold.
- Declare the build argument `ARG APP_VERSION=dev` so that the pipeline can stamp the image.
- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Fix the container time zone with `ENV TZ=UTC`.
- Set the working directory with `WORKDIR /opt/service`. No other working directory may be used anywhere in the file. This is the `dockerfile-hardened` rule. It overrides the `dockerfile-catalog` rule that requires `WORKDIR /srv/app`, so `/srv/app` must not appear.
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Declare `STOPSIGNAL SIGTERM` so that the container shuts down gracefully.

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1
# Owner: platform-api
FROM python:3.12-slim
ARG APP_VERSION=dev
LABEL org.opencontainers.image.description="FastAPI service on port 8000"
ENV TZ=UTC
WORKDIR /opt/service
COPY requirements.txt .
# step: install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
USER 10001
EXPOSE 8000
HEALTHCHECK CMD python -c "import urllib.request as u; u.urlopen('http://localhost:8000/health')"
STOPSIGNAL SIGTERM
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
