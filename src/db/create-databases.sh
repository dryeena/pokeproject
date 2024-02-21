#!/bin/bash

set -e
set -u

curdir=$( dirname "${BASH_SOURCE[0]}" )
IFS=','
psql -v ON_ERROR_STOP=1 --username $POSTGRES_USER $POSTGRES_DB -c ""
for i in $curdir/migrations/*.sql; do
  psql --username $POSTGRES_USER $POSTGRES_DB -f $i -q;
done

for database in $ADDITIONAL_POSTGRES_DBS; do
  echo "Creating additional database $database"
  psql -v ON_ERROR_STOP=1 --username $POSTGRES_USER $POSTGRES_DB -c "create database $database"
  for i in $curdir/migrations/*.sql; do
    psql --username $POSTGRES_USER $database -f $i -q;
  done
  echo "Database $database created"
done