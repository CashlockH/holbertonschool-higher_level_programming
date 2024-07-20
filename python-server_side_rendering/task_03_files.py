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
        return 
    return render_template('product_display.html', data = data, id = int(id))

def file_handler(source):
    if source == "json":
        with open("products.json", 'r') as json_file:
            for item in json_file:
                data = json.loads(item)
        return data
    elif source == "csv":
        list_of_csv = []
        with open('products.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if not row[0] == "id":
                    list_of_csv.append({'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]})
        return list_of_csv
    else:
        return 0

if __name__ == '__main__':
    app.run(debug=True)
