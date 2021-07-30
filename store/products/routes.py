from flask import redirect, render_template, url_for, flash, request

from store import db, app


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    return render_template('products/addbrand.html')