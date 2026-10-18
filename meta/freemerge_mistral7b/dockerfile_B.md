<skill>
---
name: dockerfile-combined
description: Write Dockerfiles that the internal service catalog can index, pass the security team's image policy, and are easy to understand. Use for any Dockerfile.
---

# dockerfile-combined

The service catalog reads ownership and descriptions from the Dockerfile, and new team members learn the build from its comments. Images are scanned before they may run in production and must pass the security team's image policy.

## Rules

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.
- Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`.
- Use `WORKDIR /opt/service` as the working directory. The file must not set any other working directory.
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Put a header comment `# Owner: <team>` at the top of the file.
- Fix the container time zone with `ENV TZ=UTC`.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.
- Declare the build argument `ARG APP_VERSION=dev` so that the pipeline can stamp the image.

## Example

Request: Write the Dockerfile for a Python 3.12 FastAPI service that listens on port 8000, installs dependencies from requirements.txt and starts with `uvicorn app.main:app`. Owning team: platform-api.

Output:

```
# syntax=docker/dockerfile:1
# Owner: platform-api
FROM python:3.12-slim
ARG APP_VERSION=dev
WORKDIR /opt/service
LABEL org.opencontainers.image.description="FastAPI service on port 8000"
ENV TZ=UTC
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
</skill>
