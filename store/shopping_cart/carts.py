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
            DictItems = {product_id:{'name':product.name, 'price':float(product.price), 'discount':product.discount, 
            'color':colors, 'quantity':quantity, 'image':product.image_1, 'colors': product.colors}}
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
        discount = (product['discount'] / 100) * float(product['price'])
        subtotal += float(product['price']) * int(product['quantity'])
        subtotal -= discount
        tax = ("%.2f" %(.06 * float(subtotal)))
        total = float("%.2f" %(1.06 * subtotal))
    return render_template('products/carts.html', tax=tax, total=total)


@app.route('/updateCart/<int:code>', methods=['POST'])
def updateCart(code):
    if 'StoreinCart' not in session and len(session['StoreinCart']) <= 0:
        return redirect(url_for('home'))
    if request.method == 'POST':
        quantity = request.form.get('quantity')
        color = request.form.get('colors')

        try:
            session.modified = True
            for key, item in session['StoreinCart'].items():
                if int(key) == code:
                    item['quantity'] = quantity
                    item['color'] = color
                    flash('O item foi atualizado com sucesso!', 'success')
                    return redirect(url_for('getCart'))
        except Exception as e:
            print(e)
            return redirect(url_for('getCart'))



@app.route('/empty')
def emptyCart():
    try:
        session.clear()
        return redirect(url_for('home'))
    except Exception as e:
        print(e)