# Hermes ↔ Nova File Transfer

This directory is used as a temporary file-transfer bridge between Hermes and Nova through GitHub.

## Purpose

Use this directory when Hermes has a local file that Nova needs to receive and direct MCP byte transfer is unavailable.

## Basic flow

1. Hermes obtains or exports the source file locally.
2. Hermes copies the file into `transfer/`.
3. Hermes commits and pushes the file to this repository.
4. Nova fetches the file from GitHub.
5. Temporary transfer files may be removed in a later cleanup commit when they are no longer needed.

## Recommended metadata

For each transferred file, include a small adjacent metadata file when useful, containing:

- source system
- source document/page ID or URL
- original filename
- export timestamp in UTC
- SHA-256 checksum
- short purpose/description

## Notes

- Prefer text-based formats such as Markdown, JSON, CSV, or plain text when possible.
- DOCX, PDF, XLSX, PPTX, and other moderate-size binary files may also be transferred through this directory.
- Avoid committing very large or frequently changing binaries because Git history retains them permanently.
- Do not place credentials, tokens, secrets, or other sensitive authentication material in this directory.
