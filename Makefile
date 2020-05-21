all: env

env:
	@export $$(xargs < .env)
	@echo $(shell echo $$ACCOUNT_ID)

build:
	@docker build -t flask-model .

run:
	@docker run -d -v app/.aws -p 5000:5000 flask-model

stop:
	@docker stop $(shell docker ps -a -q)

auth:
	aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin $(shell echo $$ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com

release:
	@docker build -t flask-model .
	aws ecr get-login-password --region us-east-1 | sudo docker login --username AWS --password-stdin $(shell echo $$ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com
	@docker tag flask-model $(shell echo $$ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com/flask-model
	@docker push $(shell echo $$ACCOUNT_ID).dkr.ecr.us-east-1.amazonaws.com/flask-model
