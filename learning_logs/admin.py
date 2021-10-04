from django.contrib import admin

# import the model, "Topic" and "Entry" which we want to register in our application
from .models import Topic, Entry

admin.site.register(Topic)  # manage our model -"Topic"- through the admin site
admin.site.register(Entry)  # manage our model -"Entry"- through the admin site
