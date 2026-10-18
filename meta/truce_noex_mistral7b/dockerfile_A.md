---
name: dockerfile-hardened+dockerfile-catalog
description: Merged skill that replaces `dockerfile-hardened` and `dockerfile-catalog`. Use for any Dockerfile.
---

# Merged skill: dockerfile-hardened + dockerfile-catalog

This skill replaces `dockerfile-hardened` and `dockerfile-catalog`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `dockerfile-hardened`

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`.
- Declare `STOPSIGNAL SIGTERM` so that the container shuts down gracefully.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.

## Rules kept unchanged from `dockerfile-catalog`

- Make the container stop cleanly by adding the instruction `STOPSIGNAL SIGTERM`
- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `
- Put a header comment `# Owner: <team>` at the top of the file
- Fix the container time zone with `ENV TZ=UTC`

## Reconciled rules (each one satisfies a rule of both skills at once)

- Write the Dockerfile such that it sets the working directory only to `WORKDIR /opt/service` and does not include any other `WORKDIR` command anywhere in the file.
- Combine the rules as follows: "Declare the build argument `ARG APP_VERSION=dev` and describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description` in the same Dockerfile."
