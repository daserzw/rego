#![rego](rego_logo.png)

rego is a registry application for OpenID Connect federations and entities.

## Install & run

Clone the github repo

```
git clone https://github.com/daserzw/rego
```

Create a virtualenv and activate it

```
python3 -mvenv venv
. venv/bin/activate
```

Install the app with pip (it will nicely handle dependencies)

```
pip install -e .
```

Run it

```
export FLASK_APP=rego
export FLASK_ENV=development
flask run
```

Open a browser and navigate to `http://127.0.0.1:5000`.