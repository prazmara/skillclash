---
name: dockerfile-catalog+dockerfile-hardened
description: Merged skill that replaces `dockerfile-catalog` and `dockerfile-hardened`. Use for any Dockerfile.
---

# Merged skill: dockerfile-catalog + dockerfile-hardened

This skill replaces `dockerfile-catalog` and `dockerfile-hardened`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `dockerfile-catalog`

- Use `WORKDIR /srv/app` as the working directory. The file must not set any other working directory.
- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Fix the container time zone with `ENV TZ=UTC`.
- Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`.

## Rules kept unchanged from `dockerfile-hardened`

- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Declare the build argument `ARG APP_VERSION=dev` so that the pipeline can stamp the image.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`. The second line must be the header comment `# Owner: <team>`.
