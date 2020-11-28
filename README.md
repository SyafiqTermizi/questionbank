# Question Bank
A simple django based web app to create, update and delete question

# Installation
1. make sure you have docker-compose installed on you computer
2. copy `.env.example` file and rename it to `.env`
3. update `.env` file content based on your setup
4. then run 
```
docker-compose up
```


docker build -t docker.pkg.github.com/syafiqtermizi/questionbank/questionbank:latest -f docker/prod.Dockerfile .

docker push docker.pkg.github.com/syafiqtermizi/questionbank/questionbank:latest
