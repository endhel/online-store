from flask import redirect, render_template, url_for, flash, request

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