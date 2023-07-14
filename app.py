from flask import Flask, render_template, request
import locale
#import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)


app = Flask(__name__)

# Daftar produk
products = [
    {'id': 1, 'name': 'Rokok Fiter', 'price': 25.000},
    {'id': 2, 'name': 'Nabati', 'price': 2.000},
    {'id': 3, 'name': 'Teh pucuk', 'price': 4.000},
    {'id': 4, 'name': 'Kacang Garuda', 'price': 2.000},
]

# Fungsi untuk memformat angka menjadi format mata uang Rupiah
def format_rupiah(amount):
    rupiah_symbol = 'Rp '
    formatted_amount = f"{rupiah_symbol}{amount:,.2f}"
    return formatted_amount

# Mengatur filter 'rupiah' di Jinja
app.jinja_env.filters['rupiah'] = format_rupiah

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/checkout', methods=['POST'])
def checkout():
    total = 0
    cart = []
    for product in products:
        quantity = int(request.form.get(f'quantity_{product["id"]}'))
        if quantity > 0:
            subtotal = quantity * product['price']
            total += subtotal
            cart.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
    
    return render_template('checkout.html', cart=cart, total=total)

if __name__ == '__main__':
    app.run(debug=True)
    #jika ingin menjalan kan debug maka ganti True