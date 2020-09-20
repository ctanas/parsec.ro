#!/bin/sh

python gen_new_db.py | psql -q launchesdb
