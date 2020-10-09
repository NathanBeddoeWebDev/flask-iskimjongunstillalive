from flask import Flask, json
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)


@app.route('/')
@cross_origin()
def get_kim_death_status():
    file = open('isDead.txt', 'r')
    is_dead = file.read()
    return app.response_class(
        response=json.dumps(
            {
                "dead": is_dead == "true"
            }
        ),
        status=200,
        mimetype='application/json'
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0')
