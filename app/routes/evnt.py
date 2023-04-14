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
@login_required
def eventDelete(eventID):
    # retrieve the blog to be deleted using the blogID
    deleteEvent = Event.objects.get(id=eventID)
    # check to see if the user that is making this request is the author of the blog.
    # current_user is a variable provided by the 'flask_login' library.
    if current_user == deleteEvent.author:
        # delete the blog using the delete() method from Mongoengine
        deleteEvent.delete()
        # send a message to the user that the blog was deleted.
        flash('The event was deleted.')
    else:
        # if the user is not the author tell them they were denied.
        flash("You can't delete a event you don't own.")
    # Retrieve all of the remaining blogs so that they can be listed.
    events = Event.objects()  
    # Send the user to the list of remaining blogs.
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


