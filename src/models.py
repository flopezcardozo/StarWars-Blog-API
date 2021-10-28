from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    people_fav = db.relationship('People_fav', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id_people = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    skin_color = db.Column(db.String(80), unique=False, nullable=False)
    eyes_color = db.Column(db.String(80), unique=False, nullable=False)
    birth_year = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    people_fav = db.relationship('People_fav', backref='people', lazy=True)
    

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eyes_color": self.eyes_color,
            "birth_year": self.birth_year,
            "gender": self.gender
            # do not serialize the password, its a security breach
        }

class Planet(db.Model):
    id_planet = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    climate = db.Column(db.String(80), unique=False, nullable=False)
    terrain = db.Column(db.String(80), unique=False, nullable=False)
    population = db.Column(db.String(80), unique=False, nullable=False)
    planet_fav = db.relationship('Planet_fav', backref='planet', lazy=True)
    
    def __repr__(self):
        return '<Planet %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.skin_color
            
            # do not serialize the password, its a security breach
        }

class Vehicle(db.Model):
    id_vehicle = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(80), unique=False, nullable=False)
    passengers = db.Column(db.String(80), unique=False, nullable=False)
    vehicle_class = db.Column(db.String(80), unique=False, nullable=False)
    vehicle_fav = db.relationship('Vehicle_fav', backref='vehicle', lazy=True)
    
    def __repr__(self):
        return '<Vehicle %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "passengers": self.passengers,
            "vehicle_class": self.vehicle_class
            
            # do not serialize the password, its a security breach
        }
    
class People_fav(db.Model):
    id_people_fav = db.Column(db.Integer, primary_key=True)
    id_people = db.Column(db.Integer, db.ForeignKey('people.id_people')),
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    
    
    def __repr__(self):
        return '<People_fav %r>' % self.id_people_fav

    def serialize(self):
        return {
            "id": self.id_people_fav,
                       
            # do not serialize the password, its a security breach
        }


class Planet_fav(db.Model):
    id_people_fav = db.Column(db.Integer, primary_key=True)
    id_planet = db.Column(db.Integer, db.ForeignKey('planet.id_planet')),
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    
    
    def __repr__(self):
        return '<People_fav %r>' % self.id_people_fav

    def serialize(self):
        return {
            "id": self.id_people_fav,
                       
            # do not serialize the password, its a security breach
        }

class Vehicle_fav(db.Model):
    id_people_fav = db.Column(db.Integer, primary_key=True)
    id_vehicle = db.Column(db.Integer, db.ForeignKey('vehicle.id_vehicle')),
    id_user = db.Column(db.Integer, db.ForeignKey('user.id_user'))
    
    
    def __repr__(self):
        return '<People_fav %r>' % self.id_people_fav

    def serialize(self):
        return {
            "id": self.id_people_fav,
                       
            # do not serialize the password, its a security breach
        }