FROM gitpod/workspace-full:latest

## install: heroku cli

USER gitpod

RUN curl http://cli-assests.heroku.com/install-ubuntu.sh | sh