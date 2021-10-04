"""Defines URL patterns for learning_logs."""

from django.urls import path  # "path" function is needed for mapping URLs to "views"

# the "." is to import "views.py" module from same directory as the current "urls.py" module
from . import views

# "app_name" is to help distinguish this "urls.py" file from files of same name in other apps within this project
app_name = 'learning_logs'
urlpatterns = [
    # Home page.
    # URL pattern - call the "path()" function and it takes 3 arguments: a string that routes the current request, the "index" function from "views.", a name index for this URL pattern to use instead of writring out the link/URL each time
    path('', views.index, name='index'),

    # Page that shows all topics.
    # added "topics/" into the string argument - any request with a URL matching this pattern will be passes to the "topics()" function in "views.py"
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic.
    # "/<int:topic_id>/" in this string tells Django to look for URLs matching this integer stored in "topic_id" and use this value to get to the correct topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for addidng a new topic.
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry.
    # This URL pattern matches any URL with the form "...localhost:8000/new_entry/id/" where "id" is a number matching the topic ID
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]  # "urlpatterns" a simple list of individual pages that can be requested from "learning_logs" app
