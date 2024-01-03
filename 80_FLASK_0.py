'''
export FLASK_APP=80_FLASK_0.py
FLASK_ENV=development # Debug mode enable 
flask run
http://localhost:5000/countries
http://127.0.0.1:5000/countries
curl -i http://127.0.0.1:5000/countries
curl -i http://127.0.0.1:5000/countries \
-X POST \
-H 'Content-Type: application/json' \
-d '{"name":"Germany", "capital": "Berlin", "area": 357022}'
'''
from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

# returns the list of countries.
@app.get("/countries")
def get_countries():
    return jsonify(countries)

# adds a new country to the list.
# @app.route("/countries", methods=["POST"]) # old way flask-1
@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415