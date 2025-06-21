FROM jenkins/jenkins:lts

USER root

RUN apt-get update && apt-get install -y \
    docker.io \
    docker-compose \
    curl

# Προαιρετικά: add jenkins user to docker group
RUN usermod -aG docker jenkins || true

USER jenkins
