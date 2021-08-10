from flask import redirect, render_template, url_for, flash, request, session, current_app
from .form import Addproducts
from store import db, app, photos
from .models import Brand, Category, Product
import secrets, os


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():

    if 'email' not in session:
        flash('Favor, fazer o seu login!', 'danger')
        return redirect(url_for('login'))

    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        db.session.commit()
        flash(f'A marca {getbrand} foi cadastrada com sucesso!', 'success')
        return redirect(url_for('brands'))

    return render_template('products/addbrand.html', brands='brands')

@app.route('/addcategory', methods=['GET', 'POST'])
def addcategory():

    if 'email' not in session:
        flash('Favor, fazer o seu login!', 'danger')
        return redirect(url_for('login'))

    if request.method == "POST":
        getcategory = request.form.get('category')
        category = Category(name=getcategory)
        db.session.add(category)
        db.session.commit()
        flash(f'A categoria {getcategory} foi cadastrada com sucesso!', 'success')
        return redirect(url_for('categories'))

    return render_template('products/addbrand.html')

@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():

    if 'email' not in session:
        flash('Favor, fazer o seu login!', 'danger')
        return redirect(url_for('login'))

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
        flash(f'O produto {name} foi cadastrado com sucesso!', 'success')
        return redirect(url_for('admin'))
        
    return render_template('products/addproduct.html', title='Cadastrar Produtos', 
    form=form, brands = brands, categories = categories)

@app.route('/updatebrand/<int:id>', methods=['GET', 'POST'])
def updatebrand(id):

    if 'email' not in session:
        flash('Favor, fazer o seu login!', 'danger')
        return redirect(url_for('login'))

    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')

    if request.method == "POST":
        updatebrand.name = brand
        db.session.commit()
        flash(f'A marca foi atualizada com sucesso!', 'success')
        return redirect(url_for('brands'))

    return render_template('products/updatebrand.html', title='Atualizar Marca', updatebrand=updatebrand)

@app.route('/updatecategory/<int:id>', methods=['GET', 'POST'])
def updatecategory(id):

    if 'email' not in session:
        flash('Favor, fazer o seu login!', 'danger')
        return redirect(url_for('login'))

    updatecategory = Category.query.get_or_404(id)
    category = request.form.get('category')

    if request.method == "POST":
        updatecategory.name = category
        db.session.commit()
        flash(f'A categoria foi atualizada com sucesso!', 'success')
        return redirect(url_for('categories'))

    return render_template('products/updatebrand.html', title='Atualizar Categoria', updatecategory=updatecategory)

@app.route('/updateproduct/<int:id>', methods=['GET', 'POST'])
def updateproduct(id):

    print('teste')

    if 'email' not in session:
        flash('Favor, fazer o seu login!', 'danger')
        return redirect(url_for('login'))

    brands = Brand.query.all()
    categories = Category.query.all()
    product = Product.query.get_or_404(id)
    brand = request.form.get('brand')
    category = request.form.get('category')
    form = Addproducts(request.form)

    if request.method == "POST":
        product.name = form.name.data
        product.price = form.price.data
        product.discount = form.discount.data
        product.brand_id = brand
        product.category_id = category
        product.stock = form.stock.data
        product.colors = form.colors.data
        product.description = form.description.data

        if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+".")
            except:
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10)+".")
        
        if request.files.get('image_2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10)+".")
            except:
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10)+".")

        if request.files.get('image_3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10)+".")
            except:
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10)+".")

        db.session.commit()
        flash(f'O produto foi atualizado com sucesso!', 'success')
        return redirect('admin')

    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.colors.data = product.colors
    form.description.data = product.description

    return render_template('products/updateproduct.html', title='Atualizar Produto', form=form, brands=brands,
    categories=categories, product=product)


@app.route('/deletebrand/<int:id>', methods=['POST'])
def deletebrand(id):

    brand = Brand.query.get_or_404(id)

    if request.method == "POST":
        db.session.delete(brand)
        db.session.commit()
        flash(f'A marca {brand.name} foi deletada com sucesso!', 'success')
        return redirect(url_for('admin'))
    flash(f'Erro ao tentar deletar a marca {brand.name}!', 'danger')
    return redirect(url_for('admin'))

@app.route('/deletecategory/<int:id>', methods=['POST'])
def deletecategory(id):

    category = Category.query.get_or_404(id)

    

    if request.method == "POST":
        db.session.delete(category)
        db.session.commit()
        flash(f'A categoria {category.name} foi deletada com sucesso!', 'success')
        return redirect(url_for('admin'))
    flash(f'Erro ao tentar deletar a categoria {category.name}!', 'danger')
    return redirect(url_for('admin'))

@app.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct(id):

    product = Product.query.get_or_404(id)

    if request.files.get('image_1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_1))
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_2))
                os.unlink(os.path.join(current_app.root_path, "static/images/" + product.image_3))
            except Exception as e:
                print(e)
            

    if request.method == "POST":
        db.session.delete(product)
        db.session.commit()
        flash(f'A categoria {product.name} foi deletada com sucesso!', 'success')
        return redirect(url_for('admin'))
    flash(f'Erro ao tentar deletar a categoria {product.name}!', 'danger')
    return redirect(url_for('admin'))