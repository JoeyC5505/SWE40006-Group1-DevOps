#!/bin/bash
cd ~/SWE40006-Group1-DevOps
git pull origin main
docker compose down
docker compose up -d --build
echo "Deployed at \11/08/2026 23:43:10"
