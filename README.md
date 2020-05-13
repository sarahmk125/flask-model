# flask-model

This is a simple flask project to organize financial models with parameters that can be managed by a technical person on an analytics team. The project aims to encourage financial modeling to occur outside of Excel, with ease of input. The project has the potential to grow to trigger saving model outputs to a data warehouse.

## Getting Started

### Setup

Requirements:
- Install Docker

Secrets:
- create `app/utils/secrets.py` which contains `FLASK_SECRET_STRING`, any string of your choosing
- create a file `ACCOUNT_ID` which contains the AWS account ID where ECS is located

To setup AWS:
- Install AWS CLI, make sure you have ACCOUNT_ID file above
- Authenticate docker: `sudo make auth`
- Make sure an ECR repo exists. If not, create one (through CLI: `aws ecr create-repository --region us-east-1 --repository-name flask-model`)

### Starting the App

To start on local:
- `pip install -r requirements.txt`
- `flask run`

To start in Docker, using the Makefile:
- `sudo make build`
- `sudo make run`

### Other helpful Docker hints

- To stop containers: `sudo docker stop $(docker ps -a -q)`
- To prune all images and containers: `sudo docker image prune` and `sudo docker container prun`

### Releasing

- Make sure you have AWS, your secrets, and your ECS setup as instructed above
- Run `sudo make release`; NOTE: You may need to authenticate first by running `sudo make auth`.
- Force deploy: Go to the ECS cluster; check the box to the left of the cluster; click "UPDATE"; check "Force Deployment". Launch. More detailed instructions in resources below. NOTE: This only works this way if the cluster is setup to track the latest tag, which this is.
- Celebrate! (Hopefully)

## Resources
- https://linuxacademy.com/blog/linux-academy/deploying-a-containerized-flask-application-with-aws-ecs-and-docker/
- https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service.html