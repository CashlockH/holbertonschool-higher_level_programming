from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route('/items')
def home():
    data = json.load('items.json')
    return render_template('items.html', items = data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)