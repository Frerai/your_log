from django.db import models

# Allows to add foreign key relationship to a user - importing the "User" model.
from django.contrib.auth.models import User

# custom created class "Topic" which inherits from the parent class "Model"


class Topic(models.Model):
    """A topic the user wants discussed."""
    text = models.CharField(
        max_length=200)  # attribute - stores small amounts of text, with max_length of char (200 in this case)
    # attribute - sets date and time, whenever topics are entered, to current date and time
    date_added = models.DateTimeField(auto_now_add=True)
    # Adding an "owner" field to "Topic", which establishes a foreign key relationship to the "User" model. If a user is deleted, all topics associated will be deleted.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  # calls this method to return the string stored in "text" attribute
        """Return a string representing the model."""
        return self.text


class Entry(models.Model):  # creating a class used for making entries for topics - inherits from Django base "Model" class
    """Creating entries used for specification of a topic."""
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE)  # attribute - a "ForeignKey" instance and allows Django to connect each entry to a specific topic by giving each topic a unique key or ID when created
    # the "on_delete=models.CASCADE" argument deletes all entries associated with a topic, when the topic is deleted - it's known as a "cascading delete"

    # attribute - a "TextField" instance with no size limitations, since entries needs an open size
    text = models.TextField()

    # attribute - allows us to present entires in chronological order, with a timestamp next to each entry
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:  # nesting "Meta" class inside "Entry" class - this class holds information for managing a model
        verbose_name_plural = 'entries'
        # tells Django to use "Entries" when it needs to refer to more than one entry - otherwise Django will refer to multiple entries as "Entrys"

    def __str__(self):  # this method dictates which information to show when referring to individual entries
        """Return a string representation of the model."""
        if len(self.text) >= 50:  # if length of text is greater than 50, return an ellipsis and show first 50 characters
            return f'{self.text[:50]}... '
        else:  # else return as regular text, and show entire text
            return self.text
