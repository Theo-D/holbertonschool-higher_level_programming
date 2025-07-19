from flask import Flask, render_template, request
import json
import csv


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

    source_dict = {
        'json': 'products.json',
        'csv': 'products.csv'
    }

    if not source or source not in source_dict:
        err_msg = "Wrong source"
        return render_template('product_display.html', product_list=product_list, err=err_msg)

    file_path = source_dict[source]

    try:
        with open(file_path, 'r') as f:
            if source == 'json':
                product_list = json.load(f)
            else:
                csv_file = csv.DictReader(f)
                product_list = list(csv_file)
    except FileNotFoundError:
        err_msg = "Wrong source"
        return render_template('product_display.html', product_list=product_list, err=err_msg)

    if product_id:
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
            return render_template('product_display.html', product=product, err=err_msg)

    return render_template('product_display.html', product_list=product_list, err=err_msg)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
