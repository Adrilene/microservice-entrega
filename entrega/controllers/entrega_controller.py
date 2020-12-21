from flask import request, jsonify, send_file
from flask_restful import Resource
from entrega.util.generate_date import generate_date
from entrega import app, api
import json
import requests

class EntregaController(Resource):
    def post(self):
        # import ipdb; ipdb.set_trace()
        products = request.json["products"]
        quantities = request.json["quantity"]

        for product, quantity in zip(products, quantities): 
            url = f"http://localhost:5003/stock/{product}"
            payload = {
                'quantity': quantity
            }

            requests.request("POST", url, data=payload)

        return generate_date(), 200


api.add_resource(EntregaController, "/entrega")
