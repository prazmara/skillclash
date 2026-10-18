---
name: dockerfile-combined
description: Write Dockerfiles that pass the security team's image policy and are suitable for indexing in the internal service catalog. Use for any Dockerfile.
---

# dockerfile-combined

Images are scanned before they may run in production. The policy checks a fixed install path, a non-root user and a health probe. The service catalog reads ownership and descriptions from the Dockerfile, and new team members learn the build from its comments.

## Rules

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.
- Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`.
- Use `WORKDIR /srv/app` as the working directory. The file must not set any other working directory.
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Put a header comment `# Owner: <team>` at the top of the file.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.
- Set the working directory with `WORKDIR /opt/service`. No other working directory may be used anywhere in the file.
- Fix the container time zone with `ENV TZ=UTC`.

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# Owner: platform-api
# syntax=docker/dockerfile:1
FROM python:3.12-slim
LABEL org.opencontainers.image.description="FastAPI service on port 8000"
ENV TZ=UTC
WORKDIR /srv/app
COPY requirements.txt .
# step: install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
WORKDIR /opt/service
USER 10001
EXPOSE 8000
HEALTHCHECK CMD python -c "import urllib.request as u; u.urlopen('http://localhost:8000/health')"
STOPSIGNAL SIGTERM
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
