<skill>
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

## Conflict Resolution

When a rule from `dockerfile-catalog` and `dockerfile-hardened` conflict, the rule from `dockerfile-catalog` takes precedence. However, in the case of conflicting working directory rules:

- `dockerfile-catalog` requires `WORKDIR /srv/app`.
- `dockerfile-hardened` requires `WORKDIR /opt/service`.

To satisfy both, **the working directory must be set to `/srv/app`** and **no other `WORKDIR` instruction may appear**. The `dockerfile-catalog` rule wins. Therefore, the `dockerfile-hardened` rule is overridden, and the working directory must be `/srv/app`.

## Revised Implementation Notes

- All `WORKDIR` instructions must be exactly `WORKDIR /srv/app`. No other `WORKDIR` is allowed.
- The `STOPSIGNAL SIGTERM` instruction must appear exactly once, and it must be present in every Dockerfile.
- The `HEALTHCHECK` instruction must be included and must probe the service on the appropriate port (e.g., `http://localhost:<port>/health`).
- The `ARG APP_VERSION=dev` must be included.
- The `LABEL org.opencontainers.image.description` must describe the service and its port.
- The header comment `# Owner: <team>` must be present at the top.
- The `ENV TZ=UTC` must be present.
- Every `RUN` instruction must be preceded by a `# step: ` comment.
- The `USER 10001` instruction must be used to run the service as a non-root user.

## Example Dockerfile (Valid for All Rules)

```dockerfile
# syntax=docker/dockerfile:1
# Owner: platform-ui

# step: Set container time zone to UTC
ENV TZ=UTC

# step: Set build argument for application version
ARG APP_VERSION=dev

# step: Define the working directory for the container
WORKDIR /srv/app

# step: Install Node.js 20 and dependencies
RUN apt-get update && apt-get install -y curl && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest && \
    npm install

# step: Create a non-root user with UID 10001
RUN adduser --disabled-password --gecos '' --uid 10001 appuser && \
    chown -R 10001:10001 /srv/app

# step: Set the user to run the service
USER 10001

# step: Create a health check to probe the service on port 3004
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3004/health || exit 1

# step: Ensure the container stops cleanly
STOPSIGNAL SIGTERM

# step: Describe the image
LABEL org.opencontainers.image.description="Node.js 20 React service listening on port 3004"
```

This example satisfies all rules, including the conflict between working directories, by enforcing `WORKDIR /srv/app` as required by `dockerfile-catalog`.
</skill>
