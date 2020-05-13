all: build

build:
	@docker build -t flask-model .

run:
	@docker run -d -p 5000:5000 flask-model

stop:
	@docker stop $(docker ps -a -q)

auth:
	aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin $(shell cat ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com

release:
	@docker build -t flask-model .
	@docker tag flask-model $(shell cat ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com/flask-model
	@docker push $(shell cat ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com/flask-model
