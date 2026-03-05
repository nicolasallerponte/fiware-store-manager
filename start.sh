#!/bin/bash
echo "Stopping any running containers..."
docker compose down
echo "Starting containers..."
docker compose up -d
echo "Waiting for Orion to be ready..."
sleep 5
echo "Initializing database..."
python init_db.py
echo "Starting Flask application..."
source venv/bin/activate
python run.py
