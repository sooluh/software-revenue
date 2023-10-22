import pickle
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
model = pickle.load(open('./dataset/usage.sav', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    try:
        is_global = request.json['is_global']
        is_global = request.json['is_global']
        is_major = request.json['is_major']
        is_smc = request.json['is_smc']
        is_commercial = request.json['is_commercial']
        it_spend = request.json['it_spend']
        employee_count = request.json['employee_count']
        pc_count = request.json['pc_count']
        size = request.json['size']
        it_support = request.json['it_support']
        is_discount = request.json['is_discount']

        result = model.predict([
            [
                int(is_global),
                int(is_major),
                int(is_smc),
                int(is_commercial),
                it_spend,
                employee_count,
                pc_count,
                size,
                int(it_support),
                int(is_discount),
            ],
        ])

        return jsonify({'result': result[0]})
    except Exception as e:
        return jsonify({'result': 'Internal Server Error'})


if __name__ == '__main__':
    app.run(debug=True)
