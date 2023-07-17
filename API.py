from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Configuración de la conexión a la base de datos MongoDB
client = MongoClient('localhost', 27017)
db = client.F1database
collection = db['collection']

# Ruta para obtener los datos de la base de datos y pasarlos al archivo HTML
@app.route('/')
def index():
    data = list(collection.find())  # Obtiene los primeros tres documentos de la colección

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run()