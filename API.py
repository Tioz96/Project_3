from flask import Flask, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

mongo = MongoClient('mongodb://localhost:27017/')
db = mongo['F1database']
collection = db['DataSets']
@app.route('/api/documentos', methods=['GET'])
def mostrar_documento():
    documento = collection.find_one()
    if documento:
        return jsonify(documento)
 #   else:
#      return jsonify({'mensaje': 'No se encontraron documentos'}), 404

if __name__ == '__main__':
    app.run()
