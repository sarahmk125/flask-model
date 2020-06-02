# flask-model

This is a flask project to organize financial models with parameters that can be managed by a technical person on an analytics team. The project aims to encourage financial modeling to occur outside of Excel, with ease of input. The project has the potential to grow to trigger retraining of models and saving model outputs to a data warehouse. The UI is very simple, but is meant to show how effective bare bones can be compared to manual processes before the project grows into more.

The setup of the flask app in this repo is integrated with:
- Docker to run the app
- AWS CLI to push new images to the cloud and release new versions
- AWS Postgres RDS instance to save the flask models' data
- AWS ECR to release new docker images
- AWS ECS to run the images on an EC2 instance

Youtube demo found here: https://www.youtube.com/watch?v=KTFzgbw43UQ&feature=youtu.be

## Getting Started

### Setup

Requirements:
- Install Docker

Secrets:
- copy `app/utils/secrets_example.py` to `app/utils/secrets.py` and set the appropriate variables
- copy `.env_example` to `.env` and set the appropriate variables
- create the folder `app/.aws/`
    - In that folder, create a file called `config` (no extension), which contains:
        ```
        region = [YOUR DEFAULT REGION]
        ```
    - In that folder, create a file called `credentials` (no extension), which contains:
        ```
        aws_access_key_id = [YOUR AWS ACCESS KEY ID]
        aws_secret_access_key = [YOUR AWS SECRET ACCESS KEY]
        ```

To setup AWS:
- Install AWS CLI, make sure you have ACCOUNT_ID file above
- Authenticate docker with ECS to double check it works: `make auth`
- Make sure an ECR repo exists. If not, create one (through CLI: `aws ecr create-repository --region us-east-1 --repository-name flask-model`)

### Starting the App

To start on local:
- `pip install -r requirements.txt`
- `flask run`

To start in Docker:
- `make build`
- `make up`
- To stop the container: `make stop`

To signup a user (yourself included):
- Exec onto the docker container you just spun up: `docker exec -it flask-model bash`
- Run `python3 -m app.utils.scripts.signup_user -e '[EMAIL]' -p '[PASSWORD]'`

### Other helpful Docker hints

- To stop containers: `make stop`
- To prune all images and containers: `docker image prune` and `docker container prune`
- To view the logs of the container for debugging: `docker logs --tail 1000 flask-model`

### Releasing

- Make sure you have AWS, your secrets, and your ECS setup as instructed above
- Run `make release`
- Force deploy: Go to the ECS cluster; check the box to the left of the cluster; click "UPDATE"; check "Force Deployment". Skip to review, and submit. More detailed instructions in resources below. NOTE: This only works this way if the cluster is setup to track the latest tag, which this is.
- Note: in the current setup, the ECS task IP changes upon each deploy. You will have to update the RDS security group to add the new IP. Comments on potential improvements below (using an elastic IP).
- Celebrate! (Hopefully)

## Resources
- https://linuxacademy.com/blog/linux-academy/deploying-a-containerized-flask-application-with-aws-ecs-and-docker/
- https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service.html

## Improvements

A few things that can be improved to make either the running or deploying of the app smoother:
- Include CI/CD tools like CircleCI to make the deployment of a new image easier
- Improve environment handling, outside of the __init__ file in /app.
- Use elastic IP for the ECS cluster so the signup flow can be re-exposed, without running a script offline for security.
- Functionally, implement a backend with wrapper model retraining methods that can be filled with any model code.
- Functionally, allow models to be private to a particular user, or exposed to all users.