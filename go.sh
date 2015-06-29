#!/bin/bash

if [ ! -f venv/bin/python ]
then
    virtualenv venv
    # Embeddable improved version of venv/bin/activate
    # https://gist.github.com/datagrok/2199506
    export VIRTUAL_ENV="$(pwd)/venv"
    export PATH="$VIRTUAL_ENV/bin:$PATH"
    unset PYTHON_HOME
    pip install -r requirements.txt
else
    export VIRTUAL_ENV="$(pwd)/venv"
    export PATH="$VIRTUAL_ENV/bin:$PATH"
    unset PYTHON_HOME
fi

if ! [[ "$(which node)" =~ venv ]]
then
    # https://lincolnloop.com/blog/installing-nodejs-and-npm-python-virtualenv/
    curl http://nodejs.org/dist/node-latest.tar.gz | tar xvz
    (cd node-v*
    ./configure --prefix=../venv
    make install)
    sed -i "s#\.\./venv#venv#" venv/lib/node_modules/npm/bin/npm-cli.js
    npm install jquery-bootgrid
fi

python serve.py
