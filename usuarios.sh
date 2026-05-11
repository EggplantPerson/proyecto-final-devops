#!/bin/bash

sudo useradd devops_user

sudo passwd devops_user

sudo usermod -aG wheel devops_user

sudo chown -R devops_user:devops_user ~/environment

sudo chown -R ec2-user:ec2-user ~/environment
