from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Event, eventcomment
from app.classes.forms import EventForm, eventcommentForm

from flask_login import login_required
import datetime as dt

#read all 
@app.route('/event')
@app.route('/event/list')
@login_required
def eventList():
    events = Event.objects()
    return render_template('events.html',events=events)

#read 1
@app.route('/event/<eventID>')
@login_required
def event(eventID):
    thisEvent = Event.objects.get(id=eventID)
    comments = eventcomment.objects(event = thisEvent)
    return render_template('event.html',event=thisEvent,comments=comments)

@app.route('/event/delete/<eventID>')
#delete
#aileen dont break the code pls
@login_required
def eventDelete(eventID):
    deleteEvent = Event.objects.get(id=eventID)
    #flash(f"author is: {deleteEvent.author.fname}.")
    #flash(f"Current user is {current_user.fname}")
    if current_user == deleteEvent.author:
        deleteEvent.delete()
        flash('The event was deleted.')
    else:
        flash("You can't delete an event you don't own.")
    events = Event.objects()  
    return render_template('events.html',events=events)



#create new clothing
@app.route('/event/new', methods=['GET', 'POST'])
@login_required
def EventNew():
    form = EventForm()

    if form.validate_on_submit():

        newEvent = Event(
            day = form.day.data,
            time = form.time.data,
            location = form.location.data,
            description = form.description.data,
            modify_date = dt.datetime.utcnow,
            author = current_user
        )
        newEvent.save()

        if form.image.data:
            newEvent.image.put(form.image.data, content_type = 'image/jpeg')
            newEvent.save()

        return redirect(url_for('event', eventID=newEvent.id))
    return render_template('eventform.html', form=form)

#edit ur event
@app.route('/event/edit/<eventID>', methods=['GET', 'POST'])
@login_required
def eventEdit(eventID):
    editEvent = Event.objects.get(id=eventID)

    if current_user != editEvent.author:
        flash("You can't edit a post you don't own.")
        return redirect(url_for('event',eventID=eventID))

    form = EventForm()
 
    if form.validate_on_submit():

        editEvent.update(
            day = form.day.data,
            time = form.time.data,
            location = form.location.data,
            description = form.description.data,
            modify_date = dt.datetime.utcnow,
            author = current_user
        )
        return redirect(url_for('event',eventID=eventID))


    form.day.data = editEvent.day
    form.time.data = editEvent.time
    form.location.data = editEvent.location
    form.description.data = editEvent.description

    return render_template('eventform.html',form=form)

#commenting so cool !!!!
@app.route('/eventcomment/new/<eventID>', methods=['GET', 'POST'])
@login_required
def eventcommentNew(eventID):
    event = Event.objects.get(id=eventID)
    form = eventcommentForm()
    if form.validate_on_submit():
        neweventcomment = eventcomment(
            author = current_user.id,
            event = event,
            attending = form.attending.data,
            modify_date = dt.datetime.utcnow
        )
        neweventcomment.save()
        return redirect(url_for('event',eventID=eventID))
    return render_template('eventcommentform.html',form=form,event=event)
#edit comments 
@app.route('/eventcomment/edit/<eventcommentID>', methods=['GET', 'POST'])
@login_required
def eventcommentEdit(eventcommentID):
    editeventcomment = eventcomment.objects.get(id=eventcommentID)
    if current_user != editeventcomment.author:
        flash("You can't edit a comment you didn't write.")
        return redirect(url_for('event',eventID=editeventcomment.event.id))
    event = Event.objects.get(id=editeventcomment.event.id)
    form = eventcommentForm()
    if form.validate_on_submit():
        editeventcomment.update(
            #modifydate = dt.datetime.utcnow,
            attending = form.attending.data
        )
        return redirect(url_for('event',eventID=editeventcomment.event.id))

    
    form.attending.data = editeventcomment.attending
    

    return render_template('eventcommentform.html',form=form,event=event)   
#delete
@app.route('/eventcomment/delete/<eventcommentID>')
@login_required
def eventcommentDelete(eventcommentID): 
    deleteeventcomment = eventcomment.objects.get(id=eventcommentID)
    deleteeventcomment.delete()
    flash('The comments were deleted.')
    return redirect(url_for('event',eventID=deleteeventcomment.event.id)) 
