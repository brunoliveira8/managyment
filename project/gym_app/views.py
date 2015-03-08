from __future__ import division
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from gym_app.models import RegularAthlete, Task, User, Tracker, Exercise, WorkoutPlan
from gym_app.forms import UserForm, RegularAthleteForm, UserEditForm, ChangePasswordForm, ExerciseForm
from datetime import datetime
import urllib2, urllib

# Create your views here.
#This is the First Page's view.
def index(request):
	# Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Excuse us, programmers working :)"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'gym_app/index.html', context_dict)


def workout(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!

    t_list = Task.objects.all()

    context = {'task_list' : t_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'gym_app/workout.html', context)

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            #profile = profile_form.save(commit=False)
            #profile.user = user

            athlete = RegularAthlete()
            workout_plan = WorkoutPlan()
            workout_plan.save()
            tracker = Tracker()
            tracker.save()
            athlete.user = user
            athlete.workout_plan = workout_plan
            athlete.tracker = tracker
            athlete.save()
            
            

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm(initial={'username' : "bruno", 'first_name':"Bruno", 'last_name' : "Olivera", 'email':'bruno@email.com'})
        #profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'gym_app/register.html',
            {'user_form': user_form, 'registered': registered} )    

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'gym_app/login.html', {})

# Use the login_required() decorator to ensure only those logged in can access the view.
#@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/index/')    

#This is the First Page's view.
@login_required
def restricted(request):
	# Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Congrats, you are looged."}
    return render(request, 'gym_app/index.html', context_dict)


@login_required
def edit(request):

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        user = User.objects.get(username = request.user.username)
        user_form = UserEditForm(data=request.POST, instance = user)
        athlete = RegularAthlete.objects.get(user = request.user)
        
        athlete_form = RegularAthleteForm(data=request.POST, instance = athlete)

        # If the forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user_form.save()
            athlete_form.save()
            context_dict = {'boldmessage': "Edit successful"}
            return render(request, 'gym_app/index.html', context_dict)

        else:
            print user_form.errors

       
        

    else:
        athlete = RegularAthlete.objects.get(user = request.user)
        user_form = UserEditForm(instance = request.user)
        athlete_form = RegularAthleteForm(instance = athlete)

        #profile_form = UserProfileForm()

        # Render the template depending on the context.
        return render(request,
            'gym_app/edit.html',
            {'user_form': user_form, 'athlete_form': athlete_form} )    

@login_required
def change_password(request):
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        user = User.objects.get(username = request.user.username)
        user_form = ChangePasswordForm(data=request.POST, instance = user)
        

        # If the forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            # Save the user's form data to the database.
            user = user_form.save(commit=False)
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
            context_dict = {'boldmessage': "Edit successful"}
            return render(request, 'gym_app/index.html', context_dict)

        else:
            print user_form.errors    

    else:
        user_form = ChangePasswordForm(instance = request.user)
        # Render the template depending on the context.
        return render(request,
            'gym_app/change_password.html',
            {'user_form': user_form} )     

@login_required
def tracker(request):
    #User and tracker created at same time
    #Should always have the same ID but may be changed later
    user = User.objects.get(username = request.user.username)
    athlete = RegularAthlete.objects.get(user = request.user)
    tracker = athlete.tracker
    progress=0
    result=0
    goal=0
    
    #update the weights
    if request.method == 'POST':
        newCurrentWeight = int(request.POST.get('currentWeight'))
        tracker.previousWeight=tracker.currentWeight
        tracker.currentWeight=newCurrentWeight
        tracker.previousWeightDate=tracker.currentWeightDate
        tracker.currentWeightDate=datetime.now()

        newGoalWeight = int(request.POST.get('goalWeight'))
        if tracker.goalWeight != newGoalWeight:
            tracker.startWeightDate = datetime.now()
            tracker.startWeight = newCurrentWeight
            tracker.goalWeight = newGoalWeight

    if tracker.goalWeight < tracker.startWeight: #lose weight goal
        goal = float(tracker.startWeight - tracker.goalWeight)
        result = float(tracker.startWeight - tracker.currentWeight)

        if goal == 0 or result > goal:
            progress = 100.0
        else: 
            if result < 0:
                progress = 0.0
            else:
                progress = (result / goal) * 100.0

    tracker.save()

    context = {'tracker' : tracker, 'goal': goal, 'result': result, 'progress': progress}

    return render(request, 'gym_app/tracker.html', context)

@login_required
def add_workout(request):

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        user = User.objects.get(username = request.user.username)
        exercise_form = ExerciseForm(data=request.POST)
        athlete = RegularAthlete.objects.get(user = request.user)

        # If the forms are valid...
        if exercise_form.is_valid():
            # Save the user's form data to the database.
            exercise = exercise_form.save(commit=False)
            task = Task.objects.get(name = task_name)
            exercise.task = task
            exercise.save()
            athlete.workout_plan.exercises.add(exercise)
            athlete.save()


            context_dict = {'boldmessage': "Edit successful"}
            return redirect('/workout_plan/')

        else:
            print user_form.errors
        

    else:
        t_list = Task.objects.all()
        athlete = RegularAthlete.objects.get(user = request.user)
        #user_form = UserEditForm(instance = request.user)
        #athlete_form = RegularAthleteForm(instance = athlete)
        exercise_form = ExerciseForm()

        # Render the template depending on the context.
        return render(request,
            'gym_app/add_workout.html',
            {'exercise_form': exercise_form, 'task_list' : t_list})    

@login_required
def workout_plan(request):

    user = User.objects.get(username = request.user.username)
    athlete = RegularAthlete.objects.get(user = request.user)
    exercises = athlete.workout_plan.exercises.all()
    

    # Render the template depending on the context.
    return render(request,
        'gym_app/workout_plan.html',
        {'exercises': exercises}) 
