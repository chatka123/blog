from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # create an empty form for first request
        form = UserCreationForm()
    else:
        # processing of the fully form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blogs:index')
    # displays an empty of invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)


