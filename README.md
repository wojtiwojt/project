# poza bańką - easy navigation through the ocean of news

Web application for reading, searching, discovering information and aggregating the ocean of news.

Unique features:
- follow the stories through the time
- see how specific stories are presented by different sources
- easy management of stories subscription and editing

This is application behind [https://pozabanka.pl]().

## How to run it and see what it does

1. Install `make`, `docker` and `docker-compose`
2. `make testing-stack`
3. Open browser and point to [http://localhost:5080]()

## Environments

- `dev` - local development environment with hot-reloading whenever possible for quick development feedback
- `testing` - local production like environment for manual inspection (all components prebuilt same way as production, some localized configuration, no-ssl, local mail server etc)
- `ci` - CI, production like environment for automated tests (all components prebuilt same was as production)
- `prod` - production/live environment (all components prebuilt)

| component \ environment | dev                   | testing                | CI                          | production             |
|-------------------------|-----------------------|------------------------|-----------------------------|------------------------|
| documentation           | hot-reload (sphinx)   | rendered html (sphinx) | rendered html (sphinx)      | rendered html (sphinx) |
| django                  | hot-reload            | prebuilt docker image  | prebuilt docker image       | prebuilt docker image  |
| email service           | sendria (mailcatcher) | sendria (mailcatcher)  | pytest dynamic smtpd server | P                      |

Legend: P - production specific service (outside of scope of this document)

| command \ environment | dev                        | testing                           | CI / production           |
|-----------------------|----------------------------|-----------------------------------|---------------------------|
| build environment     | automatic                  | automatic or `make testing-build` | `make ci-build`           |
| run environment       | `make dev-stack`           | `make testing-stack`              | X                         |
| run tests             | `make dev-test`            | `make testing-test`               | `make ci-test`            |
| documentation         | `make dev-docs`            | `make testing-docs`               | `make ci-docs`            |
| code-coverage (tests) | `COVERAGE=1 make dev-test` | `COVERAGE=1 make testing-test`    | `COVERAGE=1 make ci-test` |
| format code           | `make dev-format`          | X                                 | X                         |
| lint                  | `make dev-lint`            | X                                 | `make ci-lint`            |
| lock dependencies     | `make dev-lock`            | X                                 | X                         |


Legend:
X - no feature (design decision)

## Development process / How to contribute

github: https://github.com/digital-desire/project

## Random things

newscatcher - package for collecting news
https://github.com/kotartemiy/newscatcher

