#!/bin/sh

function check_program() {
    if [ "$(command -v $1)" == "" ]; then
        echo -e "\e[0;33m"
        echo "*** $1 not found"
        echo -e "\e[0m"
        return 1
    fi

    return 0
}

check_program lessc
check_program r.js
check_program bower

if [ "$?" == "0" ]; then
    bower install
fi

check_program virtualenv

if [ "$?" == "0" ]; then
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    workon flaskapp
    ./manage.py db upgrade
fi
