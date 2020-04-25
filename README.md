# flask-model

This is a simple flask project to organize financial models with parameters that can be managed by a technical person on an analytics team. The project aims to encourage financial modeling to occur outside of Excel, with ease of input. The project has the potential to grow to trigger saving model outputs to a data warehouse.

To start on local:
- `pip install -r requirements.txt`
- create `app/utils/secrets.py` which contains `FLASK_SECRET_STRING`, any string of your choosing
- `flask run`

To start in Docker:
- Install docker
- Build the image: `sudo docker build -t flask-model .`
- Run the app: `sudo docker run -d --name flask-model -p 5000:5000 flask-model`

To push to AWS:
- Install AWS CLI
- Make sure you have permissions to ECR

Implemented:
- Base flask structure for a scalable application, with files organized by function.
- Basic forms and models
- Saving of data to local instance of SQL Alchemy DB

Future implementation:
- Actual saving to data warehouse outside of local instance
- Use of model parameters to trigger actual model outputs and graphs
- More intuitive functionality (if you add something, you should have the ability to delete it, right?)
- Better UI (and not barely rudimentary HTML...)
- Dockerization / deployment
