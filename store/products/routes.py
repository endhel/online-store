from flask import redirect, render_template, url_for, flash, request
from .form import Addproducts
from store import db, app
from .models import Brand


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():

    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        db.session.commit()
        flash(f'A marca {getbrand} foi cadastrada com sucesso!', 'success')
        return redirect(url_for('addbrand'))

    return render_template('products/addbrand.html', brands='brands')

@app.route('/addcategory', methods=['GET', 'POST'])
def addcategory():

    if request.method == "POST":
        getcategory = request.form.get('category')
        category = Brand(name=getcategory)
        db.session.add(category)
        db.session.commit()
        flash(f'A categoria {getcategory} foi cadastrada com sucesso!', 'success')
        return redirect(url_for('addcategory'))

    return render_template('products/addbrand.html')

@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    
    form = Addproducts(request.form)
    return render_template('products/addproduct.html', title='Cadastrar Produtos', form=form)