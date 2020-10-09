import requests
from flask import Flask, json
from flask_cors import CORS, cross_origin
from bs4 import BeautifulSoup

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
@cross_origin()
def get_kim_death_status():
    http_response = requests.get('https://en.wikipedia.org/wiki/Kim_Jong-il')
    soup = BeautifulSoup(http_response.text, 'html.parser')
    is_dead = soup.find("th", string="Died")

    return app.response_class(
        response=json.dumps(
            {
                "dead": is_dead is not None
            }
        ),
        status=200,
        mimetype='application/json'
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0')
