---
name: dockerfile-catalog+dockerfile-hardened
description: Merged skill that replaces `dockerfile-catalog` and `dockerfile-hardened`. Use for any Dockerfile.
---

# Merged skill: dockerfile-catalog + dockerfile-hardened

This skill replaces `dockerfile-catalog` and `dockerfile-hardened`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `dockerfile-catalog`

- Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`.
- Use `WORKDIR /srv/app` as the working directory. The file must not set any other working directory.
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Put a header comment `# Owner: <team>` at the top of the file.
- Fix the container time zone with `ENV TZ=UTC`.

## Rules kept unchanged from `dockerfile-hardened`

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- LABEL org.opencontainers.image.description="Built with APP_VERSION=${APP_VERSION}" ARG APP_VERSION=dev
