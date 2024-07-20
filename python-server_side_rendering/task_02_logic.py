from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route('/items')
def home():
    with open('items.json') as file:
        data = json.load(file)
    if data['items']:
        items = data['items']
    else:
        items = []
    return render_template('items.html', items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)