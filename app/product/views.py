from flask import render_template, flash, redirect, url_for, session, request, logging, send_file
from . import product
from app import db, photos
from app.models import Seller, Product
from app.models import Seller, Product
from .forms import AddProductsForm
from flask_login import current_user, login_user
import secrets


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
