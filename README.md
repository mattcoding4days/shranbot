# shranbot

> A discord bot named `Herbert West` that will monitor the Shran development discord server.

## Using dotenv

> shranbot uses a .env file to load secrets

```bash
APP_ENV=dev
DISCORD_TOKEN="The token"
```

## Built with python poetry

[Read the Docs](https://python-poetry.org/docs/cli/)

``` bash
# After poetry is installed and your virtual environment is activated, install all the project dependencies
poetry install

# If you want to want to add a new python package
poetry add python-dotenv

# If you want to add a new python package only for development (dev dependency)
poetry add mypy -D
```
