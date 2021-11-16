# Discord bot for Shran development discord server

> All dev dependencies are installed, for testing, and logging, as well as static anaylsis tools like mypy.

## This project is built and managed with python poetry

[Read the Docs](https://python-poetry.org/docs/cli/)

``` bash
# After poetry is installed and your virtual environment is activated, install all the project dependencies
poetry install

# If you want to want to add a new python package
poetry add python-dotenv

# If you want to add a new python package only for development (dev dependency)
poetry add mypy -D
```

## Using dotenv

> shranbot uses a .env file to load secrets

```bash
APP_ENV=dev
```

