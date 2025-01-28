from flask import Flask
from flask_smorest import Api

app = Flask(__name__)
api = Api(app)

@app.route('/api/health')
def health_check():
    return {"status": "healthy"}
