#!/usr/bin/env python

#hello message
echo "Hello! Welcome to the stock analysis tool!"
chmod +x query_sql.py
chmod +x querydb.py

echo "Please enter the theme to draw:"
read theme
./draw.py drawpic --theme $ticker

echo "The frist team in the pair is:"
read team1
echo "The second team in the pair is:"
read team2
./query_sql.py who_would_win --team1 $team1 --team2 $team2

echo "Please enter the team to check group"
read team
./query_sql.py whichGroup --team1 $team

echo "Please enter the team to check historical games"
read team
./query_sql.py histGame --team1 $team

echo "Please enter the team to check players"
read team
./query_sql.py players --team1 $team
#/workspaces/Zhanyi_Lin_Project1/query_sql.py