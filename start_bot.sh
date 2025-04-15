#!/bin/bash
cd "$(dirname "$0")"
nohup python3 last.py > log.txt 2>&1 &
echo "Бот запущен в фоне!"
