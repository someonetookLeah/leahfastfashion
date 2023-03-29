from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Cloth
from app.classes.forms import ClothingForm
from flask_login import login_required
import datetime as dt

#read all 
@app.route('/cloth')
@app.route('/cloth/list')
@login_required
def clothList():
    cloth = Cloth.objects()
    return render_template('cloths.html',cloth=cloth)

#read 1
@app.route('/cloth/<clothID>')
@login_required
def cloth(clothID):
    thisCloth = Cloth.objects.get(id=clothID)
    return render_template('cloth.html',cloth=thisCloth)

#create new clothing
@app.route('/cloth/new', methods=['GET', 'POST'])
@login_required
def ClothingNew():
    form = ClothingForm()

    if form.validate_on_submit():


        newCloth = Cloth(
            color = form.color.data,
            size = form.size.data,
            modify_date = dt.datetime.utcnow
        )
        newCloth.save()

        return redirect(url_for('cloth', clothID=newCloth.id))
    return render_template('clothform.html', form=form)

#edit ur clothes
@app.route('/cloth/edit/<clothID>', methods=['GET', 'POST'])
@login_required
def clothEdit(clothID):
    editCloth = Cloth.objects.get(id=clothID)

    if current_user != editCloth.author:
        flash("You can't edit a post you don't own.")
        return redirect(url_for('post',clothID=clothID))

    form = ClothingForm()
 
    if form.validate_on_submit():

        editCloth.update(
            color = form.color.data,
            size = form.size.data,
            modify_date = dt.datetime.utcnow
        )
        return redirect(url_for('post',clothID=clothID))


    form.color.data = editCloth.subject
    form.size.data = editCloth.content

    return render_template('clothform.html',form=form)


