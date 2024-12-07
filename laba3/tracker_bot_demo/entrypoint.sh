#!/bin/bash

cd data/

if [ -d alembic/versions ]; then
	echo "Directory exists."
else
	mkdir alembic/versions
	echo "Create 'versions' directory for alembic"
fi

ALEMBIC_CHECK=$(alembic check)
echo "${ALEMBIC_CHECK}"
SUB="No new"

if ! grep -q "$SUB" <<< "$ALEMBIC_CHECK"; then
	alembic revision --autogenerate --message=init
	alembic upgrade +1
fi

cd ../

python -m bot
