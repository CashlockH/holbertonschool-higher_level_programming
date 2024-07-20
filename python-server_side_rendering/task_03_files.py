from flask import Flask, request, render_template
import json
import csv

app = Flask(__name__)

@app.route('/products')
def search():
    source = request.args.get('source')
    id = request.args.get('id')
    data = file_handler(source)
    if data == 0:
        return "Invalid source", 400
    return render_template('product_display.html', data=data, id=int(id) if id else id), 200

def file_handler(source):
    if source == "json":
        with open("products.json") as json_file:
            data = json.load(json_file)
        return data
    elif source == "csv":
        list_of_csv = []
        with open('products.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                list_of_csv.append({'id': row['id'], 'name': row['name'], 'category': row['category'], 'price': row['price']})
        return list_of_csv
    else:
        return 0

if __name__ == '__main__':
    app.run(debug=True)

