---
name: dockerfile-hardened+dockerfile-catalog
description: Merged skill that replaces `dockerfile-hardened` and `dockerfile-catalog`. Use for any Dockerfile.
---

# Merged skill: dockerfile-hardened + dockerfile-catalog

This skill replaces `dockerfile-hardened` and `dockerfile-catalog`. It keeps every rule of both skills that can hold at the same time. Follow every rule below.

## Rules kept unchanged from `dockerfile-hardened`

- Declare `STOPSIGNAL SIGTERM` so that the container shuts down gracefully.
- Declare a `HEALTHCHECK` instruction that probes the service.
- Run the service as a non-root user given by numeric ID, with an instruction such as `USER 10001`.
- Declare the build argument `ARG APP_VERSION=dev` so that the pipeline can stamp the image.
- Set the working directory with `WORKDIR /opt/service`. No other working directory may be used anywhere in the file.

## Rules kept unchanged from `dockerfile-catalog`

- Explain each `RUN` instruction with a comment line directly above it that starts with `# step: `.
- Describe the image with a `LABEL` instruction that sets `org.opencontainers.image.description`.
- Fix the container time zone with `ENV TZ=UTC`.

## Reconciled rules (each one satisfies a rule of both skills at once)

- The first line of the file must be the parser directive `# syntax=docker/dockerfile:1`. Put the header comment `# Owner: <team>` on the second line, directly below the directive and above `FROM`, so that it still sits at the top of the file.
