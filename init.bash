conda activate traj_scoreboard
docker rm scoreboard
docker run -p 5433:5432 --name scoreboard -e POSTGRES_PASSWORD=scoreboard -e POSTGRES_DB=scoreboard -d postgres
cd scoreboard && git checkout production && node server 
