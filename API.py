from flask import Flask, jsonify, render_template
from pymongo import MongoClient
from mongoengine import connect, Document, IntField, StringField
import json

app = Flask(__name__)
# Configuración de la conexión a la base de datos MongoDB
connect('F1database', host='mongodb://localhost:27017')
class F1Data(Document):
    circuitId = StringField()
    name = StringField()
    lat = IntField()
@app.route('/')
def index():
    # Obtener los datos de la colección
    f1data = F1Data.objects()
    # Renderizar el template HTML con los datos
    return render_template('index.html', f1data=f1data)
if __name__ == '__main__':
    app.run()
