from flask import Flask, jsonify, request
from pro_data_136 import data

app = Flask(__name__)
@app.route('/')

def all_stars_data():
    return jsonify({
        'data': data,
        'message': 'success'
    }), 200

@app.route('/star')

def stars_data():
    name = request.args.get('name')
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        'data': star_data,
        'message': 'success'
    }), 200

if __name__ == '__main__':
    app.run()