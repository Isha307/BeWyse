# How to run the App and the Docker Container

## Run the app
```
python app.py

```

## Make the docker container and Run it
```
docker tag <image_id> <your_dockerhub_username>/<repository_name>:<tag>
docker container run -d -p <host_port>:<container_port> <docker_username>/<image_name>:<tag>

```
## Stop the container
```
docker container stop <container_name_or_id>

```

## Push the container to docker hub
```
docker push your_dockerhub_username/my_repository:latest

```
