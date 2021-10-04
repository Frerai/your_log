from django.shortcuts import render, redirect  # importing functions
from django.contrib.auth import login  # importing "login" function
# importing form to fill in requests
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Registering a new user."""
    if request.method != 'POST':
        # Display a blank registration form with no initial data.
        form = UserCreationForm()
    else:  # if responding to a "POST" request -->
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        # Checking if username matches password, has appropriate characters etc.
        if form.is_valid():
            # Calling ".save()" method to store username and password to the database.
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
