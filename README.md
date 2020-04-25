# flask-model

This is a simple flask project to organize financial models with parameters that can be managed by a technical person on an analytics team. The project aims to encourage financial modeling to occur outside of Excel, with ease of input. The project has the potential to grow to trigger saving model outputs to a data warehouse.

### Getting Started

To start on local:
- `pip install -r requirements.txt`
- create `app/utils/secrets.py` which contains `FLASK_SECRET_STRING`, any string of your choosing
- `flask run`

To start in Docker:
- Install docker
- Build the image: `sudo docker build -t flask-model .`
- Run the app: `sudo docker run -d --name flask-model -p 5000:5000 flask-model`

To setup AWS:
- Install AWS CLI
- Authenticate docker: `aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin [ACCOUNT_ID].dkr.ecr.us-east-1.amazonaws.com`
- Make sure an ECR repo exists. If not, create one (through CLI: `aws ecr create-repository --region us-east-1 --repository-name flask-model`)

To push to AWS:
- Make sure you built the docker image locally
- Tag the model: `sudo docker tag flask-model [ACCOUNT_ID].dkr.ecr.us-east-1.amazonaws.com/flask-model`
- Push the image: `sudo docker push [ACCOUNT_ID].dkr.ecr.us-east-1.amazonaws.com/flask-model`

### Project Status

Implemented:
- Base flask structure for a scalable application, with files organized by function.
- Basic forms, models
- Basic login features
- Saving of data to local instance of SQL Alchemy DB
- Docker project locally and containerization
- Setup of ECR and ECS to deploy to a public IP, whitelisting IPs to limit access

Future implementation:
- Actual saving to data warehouse outside of local instance
- Use of model parameters to trigger actual model outputs and graphs
- Login by invite / remove signup ability
- More intuitive functionality (if you add something, you should have the ability to delete it, right?)
- Better UI (and not barely rudimentary HTML...)

#### Resources
https://linuxacademy.com/blog/linux-academy/deploying-a-containerized-flask-application-with-aws-ecs-and-docker/
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
