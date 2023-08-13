# weathervane-py
Microservice to obtain weather in Washington D.C. using Python.

## How it works
The app uses Python and Flask to send an API call to https://api.open-meteo.com/v1/forecast for the recorded daily and hourly temperature in Washington D.C.

## Docker
The app has a Dockerfile and can be containerized using `docker build .`.

## Helm
The Helm build deploys the app to the current K8s cluster from my ECR repo.

## Github Action
A Github action builds the Dockerfile and pushes it to the ECR repo. 

## TODO
Add the Helm deploy in the Github Action.
