from peewee import *
from flask_login import UserMixin
DATABASE = SqliteDatabase('recipes.sqlite')
class Recipe(Model):
    recipeName = CharField()
    ingredient1 = CharField()
    ingredient1Amount = CharField()
    ingredientId1 = CharField()
    ingredient2 = CharField()
    ingredient2Amount = CharField()
    ingredientId2 = CharField()
    ingredient3 = CharField()
    ingredient3Amount = CharField()
    ingredientId3 = CharField()
    #cal describes cal per serving 
    cal = CharField()
    servings = CharField()
    directions = TextField()
    UserId=CharField()
    class Meta: 
        database = DATABASE
class User(UserMixin, Model):
    email = CharField(unique=True)
    password = CharField()
    first_name = CharField()
    last_name = CharField()
    username = CharField()
    class Meta: 
        database = DATABASE
def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Recipe, User], safe=True)
    print("TABLES Created")
    DATABASE.close()