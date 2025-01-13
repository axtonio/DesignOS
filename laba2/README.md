# Ansible

## Run

```sh
docker-compose up -d
```

## Problem

[link](https://github.com/ansible/ansible/issues/48423)

> Following up on this further, just in case that poor soul who is attempting to get Ansible to work in a Docker container with other Docker containers on the host happens to stumble in here...\
DO NOT DO IT.\
Do not install Ansible in a Docker container and try to get that Ansible to communicate with other Docker containers running on the Docker host. It just doesn't work. If you try bind-mounting /var/run/docker.sock and /usr/bin/docker into the Ansible container, you'll get issues with missing symbols because Docker isn't statically built and you'll undoubtedly run into issues with missing .so's in the Ansible container. Furrthermore, Docker-in-Docker (dind) won't work properly either because there will be confusion over which Docker daemon to query...\
In short: if you want to use Ansible to run playbooks or automation tasks against target hosts and those target hosts may be Docker containers, just install Ansible on your host. Don't even bother trying to install Ansible in a docker container. Save yourself the heartache and trouble!