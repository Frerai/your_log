from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):  # inherits from ".ModelForm"
    class Meta:  # simplest version of "ModelForm" is a nested "Meta" class, that tells Django which model to base the form on
        model = Topic  # building a form from "Topic" model

        fields = ['text']  # "text" field is included at the only field

        # tells Django not to generate a label for the "text" field
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}  # the field "text" is a blank label

        # "widgets" attribute - an HTML form element such as single-line text box, multi-line text area or drop-down list
        # this is to override Djangos default widgets, by using a "forms.Textarea" we customize the input widget for the field "text", so the text area will be 80 columns wide rather than the default 40
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
