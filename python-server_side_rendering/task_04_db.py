from flask import Flask, render_template, request
import json
import csv
import sqlite3


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    file = "items.json"
    try:
        with open(file, 'r', encoding="utf-8") as f:
            items = json.loads(f.read())['items']
    except (KeyError, FileNotFoundError):
        items = []
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    err_msg = ""
    product_list = []
    product = None

    # Map short source names to actual filenames
    source_map = {
        'json': 'products.json',
        'csv': 'products.csv',
        'db': 'products.db'
    }

    if not source or source not in source_map:
        err_msg = "Invalid or missing source"
        return render_template('product_display.html', product_list=product_list, err=err_msg)

    file_path = source_map[source]

    try:
        if source == 'json':
            with open(file_path, 'r') as f:
                product_list = json.load(f)

        elif source == 'csv':
            with open(file_path, 'r') as f:
                csv_file = csv.DictReader(f)
                product_list = list(csv_file)

        elif source == 'db':
            conn = sqlite3.connect(file_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            if product_id:
                cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
                row = cursor.fetchone()
                conn.close()
                if row:
                    product = dict(row)
                    return render_template('product_display.html', product=product, err=err_msg)
                else:
                    err_msg = "Product not found"
                    return render_template('product_display.html', product=None, err=err_msg)
            else:
                cursor.execute("SELECT * FROM Products")
                rows = cursor.fetchall()
                product_list = [dict(row) for row in rows]
                conn.close()

    except FileNotFoundError:
        err_msg = "Source file not found"
        return render_template('product_display.html', product_list=product_list, err=err_msg)
    except sqlite3.Error as e:
        err_msg = f"Database error: {e}"
        return render_template('product_display.html', product_list=[], err=err_msg)

    # If product_id and source is json or csv
    if product_id and source in ['json', 'csv']:
        if source == 'json':
            product_id = int(product_id)
        for item in product_list:
            if item.get('id') == product_id or str(item.get('id')) == str(product_id):
                product = item
                break
        if product:
            return render_template('product_display.html', product=product, err=err_msg)
        else:
            err_msg = "Product not found"
            return render_template('product_display.html', product=None, err=err_msg)

    return render_template('product_display.html', product_list=product_list, err=err_msg)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
