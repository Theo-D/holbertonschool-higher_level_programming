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
    products = []
    product = None

    if not source:
        err_msg = "source not found"
        return render_template('product_display.html', err=err_msg)

    if not source.endswith('.json') and not source.endswith('.csv'):
        err_msg = "Wrong source"
        return render_template('product_display.html', err=err_msg)

    if source.endswith('.json'):
        try:
            with open(source, 'r') as f:
                products = json.load(f)
        except FileNotFoundError:
            err_msg = "source not found"
            return render_template('product_display.html', err=err_msg)

    if source.endswith('.csv'):
        try:
            with open(source, 'r') as f:
                csv_file = csv.DictReader(f)
                products = list(csv_file)
        except FileNotFoundError:
            err_msg = "source not found"
            return render_template('product_display.html', err=err_msg)

    if product_id:
        if source.endswith('.json'):
            product_id = int(product_id)
        for item in products:
            if item.get('id') == product_id:
                product = item
                break
        if product:
            return render_template('product_display.html', product=product)
        else:
            err_msg = "Product not found"
            return render_template('product_display.html', err=err_msg)

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
