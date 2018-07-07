from eve import Eve
from flask import request
from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

from .simple.tables import Base
from .simple.stats import Stats
from .simple.test import Test

import json
from flask_cors import cross_origin

app = Eve(validator=ValidatorSQL, data=SQL)


# heartbeat
@app.route('/')
def index():
    return '<3'


# test candidate recipe against trained model
@app.route('/test', methods=['POST'])
@cross_origin()
def test():
    run_test = Test()
    prediction = run_test.test(json.loads(request.data))
    # @TODO : only print in debug mode
    print("-----------------------------")
    print(prediction)
    return json.dumps(prediction)


# statistical breakdown filtered by style and or ingredient
@app.route('/stats', methods=['POST'])
@cross_origin()
def stats():
    run_stats = Stats()
    analysis = run_stats.stats(json.loads(request.data))
    # @TODO : only print in debug mode
    print("-----------------------------")
    print(analysis)
    return json.dumps(analysis)


# bind SQLAlchemy
db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base
db.create_all()

# using reloader will destroy in-memory sqlite db
app.run(debug=True, use_reloader=False)
