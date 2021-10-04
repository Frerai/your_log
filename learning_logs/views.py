# renders the response - redirects the user back to "topics" page after submitting their topic
from django.shortcuts import render, redirect, get_object_or_404

# Allows each user to own specific topics - importing "login_required()" function
from django.contrib.auth.decorators import login_required
from django.http import Http404  # Restricts acces to correct users and topics
from .models import Topic, Entry  # importing model of "Topic" and "Entry"

# importing forms to be able to fill out, whenever a request of GET and POST is being made
from .forms import TopicForm, EntryForm


def index(request):  # when a URL request matches a pattern, we acces this function - "request" object is passed in the "index" function
    """The home page for Learning Log."""

    # 2 arguments are passed - the original "request" object and a template used to build the page - this template we build as "index.html" in another folder
    return render(request, 'learning_logs/index.html')


@login_required  # Apply "login_required()" function as a decorator to "topics()" function
def topics(request):  # the "topics()" function needs 1 parameter: the "request" object Django received from the server
    """Display all the topics on site."""
    # Filtering topics by limiting accesability to their respective owner/user.
    topics = Topic.objects.filter(owner=request.user).order_by(
        'date_added')  # querying the database asking for "Topic" objects, which are sorted by "date_added" attribute - storing the queryset in "topics"

    # defining a context that is sent to the template - "context" is a dict in which the keys are names used in the template, and the values are data needed to send to the template
    context = {'topics': topics}

    # pass in the "request" object, path to the template and "context" variable
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):  # second parameter accepts the value captured by the expression "/<int:topic_id>/" from "urls.py" and stores it in "topic_id"
    """Show a single topic and all its entires."""
    topic = get_object_or_404(Topic, id=topic_id)
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    # entries associated with this topic, ordered in date added - the "-" sorts in reverse order, which displays most recent entries first
    entries = topic.entry_set.order_by('-date_added')

    # context dict is used to store "topic" and "entries"
    context = {'topic': topic, 'entries': entries}

    # context dict is sent to the template "topic.html"
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':  # if not a post request, then return a get request -> a blank form
        # No data submitted; create a blank form.
        form = TopicForm()  # creates a blank form that the user can fill out
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)  # make an instance of "TopicForm"
        if form.is_valid():  # method checks all required fields are filled in
            # Modifying the new topic is needed before saving it to database, so "False" here first
            new_topic = form.save(commit=False)
            new_topic.owner = request.user  # "owner" attribute is set to the current user
            new_topic.save()  # ".save()" is now called on the topic instance just defined
            # takes the name of a view and redirects the user to that view
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
# "topic_id" parameter is for storing the value received from the URL
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)  # used to get the correct topic id

    if request.method != 'POST':  # if GET request, create a blank instance of "EntryForm"
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():  # check whether form is valid
            # "commit=False" to create a new entry object without saving it to the database yet
            new_entry = form.save(commit=False)
            # setting "topic" attribute of "new_entry" to the topic pulled from the database at the beginning of the function
            new_entry.topic = topic
            new_entry.save()  # saving the entry to the database with correct associated topic

            # 2 arguments needed: name of the view to redirect to, and the argument that view function requires - "topic()" needs "topic_id" argument
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form.
    context = {'topic': topic, 'form': form}  # dict for rendering the page
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(
        id=entry_id)  # get the entry object that the user wants to edit and the topic associated with this entry
    topic = entry.topic
    # Make sure the entry belongs to the current user.
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry data.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            # redirect back to the "topic" page where updated version of entry should be visible
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
