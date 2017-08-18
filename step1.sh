#!/bin/bash
DOCKER_LOGIN=`aws ecr get-login --region us-west-2`
${DOCKER_LOGIN}