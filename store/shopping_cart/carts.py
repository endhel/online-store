from flask import redirect, render_template, url_for, flash, request, session, current_app
from store import db, app
from store.products.models import Product

def M_Dictionaries(dic1, dic2):
    if isinstance(dic1, list) and isinstance(dic2, list):
        return dic1 + dic2
    elif isinstance(dic1, dict) and isinstance(dic2, dict):
        return dict(list(dic1.items()) + list(dic2.items()))
    return False

@app.route('/addCart', methods=['POST'])
def addCart():
    try:
        product_id = request.form.get('product_id')
        quantity = request.form.get('quantity')
        colors = request.form.get('colors')
        product = Product.query.filter_by(id=product_id).first()

        if product_id and quantity and colors and request.method=="POST":
            DictItems = {product_id:{'Name':product.name, 'Price':float(product.price), 'Discount':product.discount, 
            'Color':colors, 'Quantity':quantity, 'Image':product.image_1}}
            if 'StoreinCart' in session:
                print(session['StoreinCart'])
                if product_id in session['StoreinCart']:
                    print('Este produto já existe no carrinho!')
                else:
                    session['StoreinCart'] = M_Dictionaries(session['StoreinCart'], DictItems)
                    return redirect(request.referrer)
            else:
                session['StoreinCart'] = DictItems
                return redirect(request.referrer)

    except Exception as e:
        print(e)
    finally: 
        return redirect(request.referrer)

@app.route('/carts')
def getCart():
    if 'StoreinCart' not in session:
        return redirect(request.referrer)
    
    subtotal = 0
    total = 0

    for key, product in session['StoreinCart'].items():
        discount = (product['Discount'] / 100) * float(product['Price'])
        subtotal += float(product['Price']) * int(product['Quantity'])
        subtotal -= discount
        tax = ("%.2f" %(.06 * float(subtotal)))
        total = float("%.2f" %(1.06 * subtotal))
    return render_template('products/carts.html', tax=tax, total=total)