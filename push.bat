#!/bin/bash
python3 update_readme.py
git add .
git commit -m "Update solutions and README"
git push origin main
pause
push.bat