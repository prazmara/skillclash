---
name: dockerfile-catalog-hardened
description: Write Dockerfiles that are both catalog-indexable and pass the security team's image policy. Use for any Dockerfile.
---

# dockerfile-catalog-hardened

This skill writes Dockerfiles that satisfy both the internal service catalog and the security team's image policy. The resulting Dockerfile is indexable, well-documented, and production-hardened.

## Rules

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.
- Put a header comment `# Owner: <team>` at the top of the file, immediately after the parser directive.
- Use `WORKDIR /srv/app` as the working directory. The file must not set any other working directory.
- Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`.
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Fix the container time zone with `ENV TZ=UTC`.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.
- Declare the build argument `ARG APP_VERSION=dev` so that the pipeline can stamp the image.

**Where two rules conflict, the rule from `dockerfile-catalog` wins.**  
Specifically, the working directory must be `/srv/app` (not `/opt/service`).

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
WORKDIR /srv/app
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
