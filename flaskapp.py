#!/usr/bin/python

from flask import Flask, render_template, request
import os
import generate
import urllib2
import json
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"] )
def home():
	if request.method == "GET":
		return render_template('root.html')
	if request.method=="POST":
		pair=generate.make_key_pair()
		return render_template('root.html', pair=pair)

if __name__ == "__main__":
    app.secret_key = os.urandom(12324)
    app.run(debug=True,host='0.0.0.0', port=12321)
