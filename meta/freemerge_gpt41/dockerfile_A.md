---
name: dockerfile-hardened-catalog
description: Write Dockerfiles that pass the security team's image policy and can be indexed by the internal service catalog. Use for any Dockerfile.
---

# dockerfile-hardened-catalog

This skill writes Dockerfiles that comply with both the security team's image policy and the internal service catalog requirements. Images are scanned before production, must use a fixed install path, a non-root user, a health probe, and include metadata and comments for catalog indexing and onboarding.

## Rules

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.
- Add a header comment `# Owner: <team>` at the top of the file, immediately after the parser directive.
- Declare `STOPSIGNAL SIGTERM` so that the container shuts down gracefully.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.
- Declare the build argument `ARG APP_VERSION=dev` so that the pipeline can stamp the image.
- Set the working directory with `WORKDIR /opt/service`. No other working directory may be used anywhere in the file. (If another skill requires a different working directory, this rule wins.)
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Fix the container time zone with `ENV TZ=UTC`.
- The file must include all of the above instructions and comments in the correct order.

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1
# Owner: platform-api
FROM python:3.12-slim
LABEL org.opencontainers.image.description="FastAPI service on port 8000"
ARG APP_VERSION=dev
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
