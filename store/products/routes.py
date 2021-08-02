from flask import redirect, render_template, url_for, flash, request
from .form import Addproducts
from store import db, app, photos
from .models import Brand, Category, Product
import secrets


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
        category = Category(name=getcategory)
        db.session.add(category)
        db.session.commit()
        flash(f'A categoria {getcategory} foi cadastrada com sucesso!', 'success')
        return redirect(url_for('addcategory'))

    return render_template('products/addbrand.html')

@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    if request.method=="POST":
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        description = form.description.data
        brand = request.form.get('brand')
        category = request.form.get('category')

        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10)+".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10)+".")

        addpro = Product(name=name, price=price, discount=discount, stock=stock, colors=colors, description=description,
        brand_id=brand, category_id=category, image_1=image_1, image_2=image_2, image_3=image_3)

        db.session.add(addpro)
        db.session.commit()
        flash(f'O produto {name} foi cadastrada com sucesso!', 'success')
        return redirect(url_for('admin'))
        
    return render_template('products/addproduct.html', title='Cadastrar Produtos', 
    form=form, brands = brands, categories = categories)