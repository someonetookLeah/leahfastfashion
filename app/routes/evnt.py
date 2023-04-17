from app import app
import mongoengine.errors
from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app.classes.data import Event
from app.classes.forms import EventForm
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
    return render_template('event.html',event=thisEvent)

@app.route('/event/delete/<eventID>')
# Only run this route if the user is logged in.
#aileen dont break the code pls
@login_required
def eventDelete(eventID):
    deleteEvent = Event.objects.get(id=eventID)
    if current_user == deleteEvent.author:
        deleteEvent.delete()
        flash('The event was deleted.')
    else:
        flash("You can't delete an event you don't own.")
    events = Event.objects()  
    return render_template('events.html',events=event)


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
            modify_date = dt.datetime.utcnow
        )
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
        return redirect(url_for('post',eventID=eventID))

    form = EventForm()
 
    if form.validate_on_submit():

        editEvent.update(
            day = form.day.data,
            time = form.time.data,
            location = form.location.data,
            description = form.description.data,
            modify_date = dt.datetime.utcnow
        )
        return redirect(url_for('post',eventID=eventID))


    form.day.data = editEvent.subject
    form.time.data = editEvent.content
    form.location.data = editEvent.subject
    form.description.data = editEvent.content

    return render_template('eventform.html',form=form)


