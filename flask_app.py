import os
from flask import request
import markovify
from flask import Flask
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)

@app.route("/getTweet", methods=['POST'])
def helloWorld():
	if request.method=='POST':
		result = request.form.get('tonPolitique')
		tonPolitique =  request.values.get('tonPolitique');
		file = "Twitter/"+tonPolitique+".csv"
		if __name__ == "__main__":
		    with open(file, encoding='utf8') as f:
		        text = f.read()
		    model = markovify.Text(text)
		return jsonify(tweet=model.make_short_sentence(140))
if __name__ == "__main__":
    app.run()