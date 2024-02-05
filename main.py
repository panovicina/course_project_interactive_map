from flask import Flask, request, jsonify

from app.services.city import CityService

app = Flask(__name__)

@app.route("/", )
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/city', methods=['POST'])
def create_city():
    try:
        city_data = request.json
        created_city = CityService.create(city_data)
        return jsonify({"message": "City created successfully", "city_id": created_city.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/city', methods=['GET'])
def list_cities():
    try:
        cities = CityService.list_cities()
        return jsonify({"message": f"found {len(cities)} cities"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)