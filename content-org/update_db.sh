#!/bin/sh

cd ../data
python gen_new_db.py | psql -q launchesdb
