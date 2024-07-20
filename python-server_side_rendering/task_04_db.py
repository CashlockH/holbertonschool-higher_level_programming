from flask import Flask, request, render_template
import json
import csv
import sqlite3
app = Flask(__name__)

@app.route('/products')
def search():
    source = request.args.get('source')
    id = request.args.get('id')
    data = file_handler(source)
    if data == 0:
        return "Wrong source", 200
    return render_template('product_display.html', data = data, id = int(id) if id else id), 200

def file_handler(source):
    if source == "json":
        with open("products.json") as json_file:
            data = json.load(json_file)
        return data
    elif source == "csv":
        list_of_csv = []
        with open('products.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if not row[0] == "id":
                    list_of_csv.append({'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]})
        return list_of_csv
    elif source == "sql":
        list_of_db = []
        con = sqlite3.connect("products.db")
        cur = con.cursor()
        data = cur.execute("SELECT * FROM PRODUCTS").fetchall()
        for item in data:
            list_of_db.append({'id': item[0], 'name': item[1], 'category': item[2], 'price': item[3]})
        return list_of_db
    else:
        return 0

if __name__ == '__main__':
    app.run(debug=True)
