# Table of content

<!-- toc -->

- [Running Jupyter notebook from within a container](#running-jupyter-notebook-from-within-a-container)
- [Using docker-compose](#using-docker-compose)
- [search which dockerfile installation line takes up space](#search-which-dockerfile-installation-line-takes-up-space)

<!-- tocstop -->

# Running Jupyter notebook from within a container
```
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```
You need to use `--ip 0.0.0.0` or else the notebook can only be viewed within the container.

Also you need port forwarding
```
docker run -ti -p 8888:8888 DOCKERIMAGENAME
```

# Using docker-compose 
* Use this with port forwarding from within container to local browser
* also use the docker container interactively by launching `bash`
```
$ docker-compose run --service-ports devenv bash
```
Example content of a docker compose file
```
version: "3"
services:
  devenv:
    image: karenyng/miniconda3_devenv:latest
    volumes:
      - LOCAL_DIR_PATH:CONTAINER_MOUNT_DIR_PATH"
    ports:
      - "8888-8895:8888-8895"
```

# search which dockerfile installation line takes up space
```
docker history DOCKER_IMAGE_NAME
```
