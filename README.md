# Boiler-Plate

Flask application boiler-plate.

## Running the application

With Docker and Docker-Compose installed, follow the instructions below to run the application.:

```shell
    docker-compose up
```

## Installing pre-commit tool

You'll need to install the pre-commit tool locally to run the tests.

```shell
    pip install pre-commit
```

Then, install the configured hooks in the `.pre-commit-config.yaml` file.

```shell
    pre-commit install
```

## Access web container

```shell
    docker-compose exec web sh
```
