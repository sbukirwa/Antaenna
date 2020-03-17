from flask import render_template, flash, redirect, url_for, session, request, logging, send_file
from . import product
from app import db, photos
from app.models import Seller, Product
from .forms import AddProductsForm
from flask_login import current_user
import secrets
from app import config


@product.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    form = AddProductsForm(request.form)
    if request.method == "POST":
        name = form.name.data
        category_option = form.category_option.data
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        image_4 = photos.save(request.files.get('image_4'), name=secrets.token_hex(10) + ".")
        location = form.location.data
        description = form.description.data
        product = Product(name=name, category_option=category_option, image_1=image_1, image_2=image_2, image_3=image_3,
                          image_4=image_4, location=location, description=description,
                          seller=current_user)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('auth.home'))
    return render_template('/products/addproduct.html', form=form)


@product.route('/updateproduct/<int:id>', methods=['GET', 'POST'])
def updateproduct(id):
    product = Product.query.get_or_404(id)
    form = AddProductsForm(request.form)
    form.name.data = product.name
    if request.method == "POST":
        product.name = form.name.data
        product.category_option = form.category_option.data
        product.location = form.location.data
        product.description = form.description.data
        if request.files.get('image_1'):
            try:
                os.unlink(os.pathjoin(current_app.root_path, "app/static/images/" + product.image_1))
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
            except:
                product.image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")

        if request.files.get('image_2'):
            try:
                os.unlink(os.pathjoin(current_app.root_path, "app/static/images/" + product.image_2))
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
            except:
                product.image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_3'):
            try:
                os.unlink(os.pathjoin(current_app.root_path, "app/static/images/" + product.image_3))
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
            except:
                product.image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        if request.files.get('image_4'):
            try:
                os.unlink(os.pathjoin(current_app.root_path, "app/static/images/" + product.image_4))
                product.image_4 = photos.save(request.files.get('image_4'), name=secrets.token_hex(10) + ".")
            except:
                product.image_4 = photos.save(request.files.get('image_4'), name=secrets.token_hex(10) + ".")
        db.session.commit()
        return redirect(url_for('auth.home'))

    form.name.data = product.name  
    form.category_option.data = product.category_option
    form.location.data = product.location
    form.description.data = product.description
    form.image_1.data = product.image_1
    form.image_2.data = product.image_2
    form.image_3.data = product.image_3
    form.image_4.data = product.image_4
    return render_template('products/updateproduct.html', form=form, product=product)
