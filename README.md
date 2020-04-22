# flask-model

This is a simple flask project to organize financial models with parameters that can be managed by a technical person on an analytics team. The project has the potential to grow to trigger saving model outputs to a data warehouse.

To start:
- `pip install -r requirements.txt`
- flask run

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
