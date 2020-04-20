from app import db


class FinancialModel(db.Model):
    __tablename__ = 'financial_model'
    id = db.Column(db.Integer, primary_key=True)
    unique_name = db.Column(db.String(256), unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    version = db.Column(db.String(8), nullable=False)

    # Relationships
    parameters = db.relationship('ModelParameter', backref='financial_model')

    def __repr__(self):
        return f'<FinancialModel {self.unique_name}'


class ModelParameter(db.Model):
    __tablename__ = 'model_parameter'
    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey('financial_model.id'), nullable=False)
    unique_name = db.Column(db.String(256), unique=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<ModelParameter {self.unique_name}'
