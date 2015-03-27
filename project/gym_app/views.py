from __future__ import division
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from gym_app.models import RegularAthlete, Task, User, Tracker, Exercise, WorkoutPlan
from gym_app.forms import UserForm, RegularAthleteForm, UserEditForm, ChangePasswordForm, ExerciseForm, UserTypeForm
from datetime import datetime
from decimal import Decimal
import urllib2, urllib
from django.core.mail import send_mail
from django.contrib.auth.models import Group

# Create your views here.
#This is the First Page's view.
def index(request):
	# Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    if request.user.is_superuser:   
        group = 'admin';
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name;
        except:
            group = 'none'
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    context_dict = {'boldmessage': "Excuse us, programmers working :)", 'group': group}
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
        type_form = UserTypeForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            if type_form.is_valid():
                group = Group.objects.get(name=type_form.cleaned_data['group'])
                user.groups.add(group)

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
        user_form = UserForm()
        type_form = UserTypeForm()
        #profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'gym_app/register.html',
            {'user_form': user_form, 'registered': registered, 'type_form':type_form} )    

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
            return render(request, 'gym_app/login.html', {'invalid': True })
            #return HttpResponse("Invalid login details supplied.")

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
    else:
        if tracker.goalWeight > tracker.startWeight: #gain weight goal
            goal = float(tracker.goalWeight - tracker.startWeight)
            result = float(tracker.currentWeight - tracker.startWeight)

    if goal == 0 or result > goal:
        progress = 100.0
    else: 
        if result < 0:
            progress = 0.0
        else:
            progress = (result / goal) * 100.0

    progress = round(Decimal(progress), 1)
            
    tracker.save()

    context = {'tracker' : tracker, 'progress': progress}

    return render(request, 'gym_app/tracker.html', context)

@login_required
def members(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!

    if request.user.is_superuser:   
        group = 'admin';
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name;
        except:
            group = 'none'

    print group
    u_list = User.objects.all()
    
    context = {'user_list' : u_list, 'group': group}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'gym_app/members.html', context)

def message(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        user = User.objects.get(username = request.user.username)
        user_email = user.email
        to_email = request.POST.get('username')
        msg = request.POST.get('msg')
        sbj = request.POST.get('subject')

        send_mail(sbj, msg, user_email,
        [to_email], fail_silently=False)
        #send_mail(sbj, msg, from_email,
        #['pent.alef@gmail.com'], fail_silently=False)
        return HttpResponseRedirect('/members/')    


@login_required
def buddy_match(request):
      
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    user = User.objects.get(username = request.user.username)
    athlete = RegularAthlete.objects.get(user = request.user)    
    buddy_list = RegularAthlete.objects.filter(level = athlete.level, training_period = athlete.training_period).exclude(user = user)
    buddy_matched = 0;
    context = {'buddy_list' : buddy_list, 'buddy_matched' : buddy_matched}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'gym_app/buddy_match.html', context)

def message_match(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        user = User.objects.get(username = request.user.username)
        user_email = user.email
        to_email = request.POST.get('username')
        print
        msg = "The user {0} wish workout with you!".format(user)
        sbj = "Buddy Match Message"

        send_mail(sbj, msg, user_email,
        [to_email], fail_silently=False)
        #send_mail(sbj, msg, from_email,
        #['pent.alef@gmail.com'], fail_silently=False)
        buddy_matched = 1;
        message = 'You have sent a Buddy Match request for: {0}!'.format(User.objects.get(email = to_email).username)
        context = {'message' : message, 'buddy_matched' : buddy_matched}

        # Return a rendered response to send to the client.
        # We make use of the shortcut function to make our lives easier.
        # Note that the first parameter is the template we wish to use.
        return render(request, 'gym_app/buddy_match.html', context)

def workout_plan(request):

    user = User.objects.get(username = request.user.username)
    athlete = RegularAthlete.objects.get(user = request.user)
    exercises_day1 = athlete.workout_plan.exercises.filter( day = 1)
    exercises_day2 = athlete.workout_plan.exercises.filter( day = 2)
    exercises_day3 = athlete.workout_plan.exercises.filter( day = 3)
    exercises_day4 = athlete.workout_plan.exercises.filter( day = 4)
    exercises_day5 = athlete.workout_plan.exercises.filter( day = 5)
    exercises_day6 = athlete.workout_plan.exercises.filter( day = 6)
    exercises_day7 = athlete.workout_plan.exercises.filter( day = 7)

    

    # Render the template depending on the context.
    return render(request,
        'gym_app/workout_plan.html',
        {'day1': exercises_day1, 'day2': exercises_day2, 'day3': exercises_day3, 'day4': exercises_day5, 'day6': exercises_day6, 'day7': exercises_day7}) 


@login_required
def workout_day(request, day = '1'):
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
            exercise.day = day
            exercise.save()
            athlete.workout_plan.exercises.add(exercise)
            athlete.save()

            path = '/workout/days/{0}'.format(day)
            print path

            return redirect(path)

        else:
            return HttpResponse('There are errors in the fields: {0}'.format(exercise_form.errors))
        
    else:
        t_list = Task.objects.all()
        #user = User.objects.get(username = request.user.username)
        athlete = RegularAthlete.objects.get(user = request.user)
        exercises = athlete.workout_plan.exercises.filter( day = int(day))
        exercise_form = ExerciseForm()

        # Render the template depending on the context.
        return render(request, 'gym_app/workout_day.html',
            {'exercise_form': exercise_form, 'task_list' : t_list, 'exercises' : exercises, 'day': day})  


def delete_exercise(request):

    exercise_id = int(request.POST.get("delete"))
    Exercise.objects.filter(id = exercise_id).delete()
    path = '/workout/days/{0}'.format(request.POST.get("day"))
    return redirect(path)

