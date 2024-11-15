from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import requests
from models import db, Currency

app = Flask(__name__)

app.config.from_pyfile('config.py')

db.init_app(app)


@app.route('/')
def hello_world():
    return 'Dzień dobry, serwer działa :)'


@app.route('/get', methods=['GET'])
def get_currencies():
    url = "https://api.nbp.pl/api/exchangerates/tables/A?format=json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        currencies = data[0]['rates']
        for entry in currencies:
            currency = Currency.query.filter_by(currency_code=entry['code']).first()
            if currency:
                currency.exchange_rate = entry['mid']
            else:
                currency = Currency(
                    currency_name=entry['currency'],
                    currency_code=entry['code'],
                    exchange_rate=entry['mid']
                )
                db.session.add(currency)

        db.session.commit()
        return jsonify({"message": "waluty zapisane"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/show', methods=['GET'])
def show_currencies():
    currencies = Currency.query.all()
    return render_template('table.html', currencies=currencies)


@app.route('/test_db')
def test_db():
    try:
        result = db.session.execute(text('SELECT 1'))
        return jsonify({"message": "Bazo widze w tym cloudzie!", "result": result.fetchone()})
    except Exception as e:
        return jsonify({"error": f"Fail: {str(e)}"})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
