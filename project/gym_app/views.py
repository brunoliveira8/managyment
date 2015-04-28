from __future__ import division
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from gym_app.models import Athlete, Task, User, Tracker, Exercise, WorkoutPlan, MailBox,  PersonalTrainer, BodyScreening
from gym_app.forms import *
from datetime import datetime
from decimal import Decimal
import urllib2, urllib
from django.core.mail import send_mail
from django.contrib.auth.models import Group

# Create your views here.
#This is the First Page's view.
@login_required
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

@login_required
def workout(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    if request.user.is_superuser:   
        group = 'admin';
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name;
        except:
            group = 'none'

    t_list = Task.objects.all()

    context = {'task_list' : t_list, 'group':group}

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
        gender_form = UserGenderForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.is_active = False
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

            if group.name == "regular" or group.name == "premium":
                athlete = Athlete()
                workout_plan = WorkoutPlan()
                workout_plan.save()
                tracker = Tracker()
                tracker.save()
                athlete.user = user
                athlete.workout_plan = workout_plan
                athlete.tracker = tracker
                if gender_form.is_valid():
                    athlete.gender = gender_form.cleaned_data['gender']
                athlete.save()
            elif group.name == "personal_trainer":
                personal = PersonalTrainer()
                personal.user = user
                if gender_form.is_valid():
                    personal.gender = gender_form.cleaned_data['gender']
                personal.save()

            #Create MailBox
            mail_box = MailBox()
            mail_box.owner = user.username
            mail_box.save()

            mail_box_admin = MailBox.objects.get(owner = "admin")
            mail_box_admin.add_msg('SIGN UP', "Sign Up Request.", user.username)

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
        gender_form = UserGenderForm()
        #profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'gym_app/register.html',
            {'user_form': user_form, 'registered': registered, 'type_form':type_form, 'gender_form':gender_form} )    

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
                return HttpResponseRedirect('/permission_denied/')
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

    if request.user.is_superuser:   
        group = 'admin';
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name;
        except:
            group = 'none'

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        user = User.objects.get(username = request.user.username)
        user_form = UserEditForm(data=request.POST, instance = user)

        if group == "regular" or group == "premium":
            athlete = Athlete.objects.get(user = request.user)
            user_logged = AthleteForm(data=request.POST, instance = athlete)
        elif group == "personal_trainer":
            personal = PersonalTrainer.objects.get(user = request.user)
            user_logged = PersonalTrainerForm(data=request.POST, instance = personal)

        # If the forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user_form.save()
            user_logged.save()
            context_dict = {'boldmessage': "Edit successful", 'group': group}
            return render(request, 'gym_app/index.html', context_dict)

        else:
            print user_form.errors

    else:
        
        user_form = UserEditForm(instance = request.user)
        if group == "regular":
            athlete = Athlete.objects.get(user = request.user)
            user_logged = AthleteForm(instance = athlete)
        elif group == "premium":
            athlete = Athlete.objects.get(user = request.user)
            user_logged = AthleteForm(instance = athlete)
        elif group == "personal_trainer":
            personal = PersonalTrainer.objects.get(user = request.user)
            user_logged = PersonalTrainerForm(instance = personal)

        #profile_form = UserProfileForm()

        # Render the template depending on the context.
        return render(request,
            'gym_app/edit.html',
            {'user_form': user_form, 'user_logged': user_logged, 'group': group} )    

@login_required
def change_password(request):
    if request.user.is_superuser:   
        group = 'admin';
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name;
        except:
            group = 'none'

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
            context_dict = {'boldmessage': "Edit successful", 'group': group}
            return render(request, 'gym_app/index.html', context_dict)

        else:
            print user_form.errors    

    else:
        user_form = ChangePasswordForm(instance = request.user)
        # Render the template depending on the context.
        return render(request,
            'gym_app/change_password.html',
            {'user_form': user_form, 'group': group} )     

@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='regular') | Q(name='premium')).count() == 1, login_url='/permission_denied/')
def tracker(request):
    if request.user.is_superuser:   
        group = 'admin';
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name;
        except:
            group = 'none'

    #User and tracker created at same time
    #Should always have the same ID but may be changed later
    user = User.objects.get(username = request.user.username)
    athlete = Athlete.objects.get(user = request.user)
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

    context = {'tracker' : tracker, 'progress': progress, 'group': group}

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

    u_list = User.objects.all().exclude(username = request.user.username)
    
    context = {'user_list' : u_list, 'group': group}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'gym_app/members.html', context)

@login_required
def message(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        user = User.objects.get(username = request.user.username)
        user_email = user.email
        to_email = request.POST.get('username')
        msg = request.POST.get('msg')+'\nMessage from: '+request.user.username
        sbj = request.POST.get('subject')

        send_mail(sbj, msg, user_email,
        [to_email], fail_silently=False)
        #send_mail(sbj, msg, from_email,
        #['pent.alef@gmail.com'], fail_silently=False)
        return HttpResponseRedirect('/members/')    


@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='regular') | Q(name='premium')).count() == 1, login_url='/permission_denied/')
def buddy_match(request):

    if request.user.is_superuser:   
        group = 'admin';
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name;
        except:
            group = 'none'
      
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    user = User.objects.get(username = request.user.username)
    athlete = Athlete.objects.get(user = request.user)    
    buddy_list = Athlete.objects.filter(level = athlete.level, training_period = athlete.training_period).exclude(user = user)
    buddy_matched = 0;
    context = {'buddy_list' : buddy_list, 'buddy_matched' : buddy_matched, 'group': group}

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

@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='regular') | Q(name='premium')).count() == 1, login_url='/permission_denied/')
def workout_plan(request):

    if request.user.is_superuser:   
        group = 'admin';
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name;
        except:
            group = 'none'

    user = User.objects.get(username = request.user.username)
    athlete = Athlete.objects.get(user = request.user)
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
        {'day1': exercises_day1, 'day2': exercises_day2, 'day3': exercises_day3, 'day4': exercises_day5, 'day6': exercises_day6, 'day7': exercises_day7, 'group': group}) 


@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='regular') | Q(name='premium') | Q(name='personal_trainer')).count() == 1, login_url='/permission_denied/')
def workout_day(request, day = '1'):
    if request.user.is_superuser:   
        group = 'admin';
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name;
        except:
            group = 'none'

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        task_name = request.POST.get('task_name')
        #user = User.objects.get(username = request.user.username)
        exercise_form = ExerciseForm(data=request.POST)
        if group == "personal_trainer":
            username = request.POST.get("username")
        else:
            username = request.user.username
        user = User.objects.get(username = username)
        athlete = Athlete.objects.get(user = user.id)


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

            if group == "personal_trainer":
                t_list = Task.objects.all()
                exercises = athlete.workout_plan.exercises.filter( day = int(day))
                exercise_form = ExerciseForm()
                return render(request, 'gym_app/workout_day.html', {'exercise_form': exercise_form, 'task_list' : t_list, 'exercises' : exercises, 'day': day, 'username': username, 'group' : group})
            else:
                path = '/workout/days/{0}'.format(day)
                return redirect(path)

        else:
            return HttpResponse('There are errors in the fields: {0}'.format(exercise_form.errors))
        
    else:
        t_list = Task.objects.all()
        #user = User.objects.get(username = request.user.username)
        #athlete = Athlete.objects.get(user = request.user)
        if group == "personal_trainer":
            username = request.POST.get("username")
        else:
            username = request.user.username
        user = User.objects.get(username = username)
        athlete = Athlete.objects.get(user = user.id)
        exercises = athlete.workout_plan.exercises.filter( day = int(day))
        exercise_form = ExerciseForm()

        # Render the template depending on the context.
        return render(request, 'gym_app/workout_day.html',
            {'exercise_form': exercise_form, 'task_list' : t_list, 'exercises' : exercises, 'day': day,'group' : group})  

@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='regular') | Q(name='premium') | Q(name='personal_trainer')).count() == 1, login_url='/permission_denied/')
def delete_exercise(request):
    if request.user.is_superuser:   
        group = 'admin'
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name
        except:
            group = 'none'

    day = request.POST.get("day")
    exercise_id = int(request.POST.get("delete"))
    Exercise.objects.filter(id = exercise_id).delete()
    path = '/workout/days/{0}'.format(day)


    if group == "personal_trainer":
        username = request.POST.get("username")
        t_list = Task.objects.all()
        user = User.objects.get(username = username)
        athlete = Athlete.objects.get(user = user.id)
        exercises = athlete.workout_plan.exercises.filter( day = int(day))
        exercise_form = ExerciseForm()
        return render(request, 'gym_app/workout_day.html', {'exercise_form': exercise_form, 'task_list' : t_list, 'exercises' : exercises, 'day': day, 'username': username, 'group' : group})
            
    else:
        return redirect(path)
    

@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='regular') | Q(name='premium')).count() == 1, login_url='/permission_denied/')
def upgrade_downgrade(request):

    if request.user.is_superuser:   
        group = 'admin'
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name
        except:
            group = 'none'
      
    if request.method == 'POST':
        admin = User.objects.get(username = 'admin')
        admin_email = admin.email
        to_email = admin.email
        mail_box = MailBox.objects.get(owner = "admin")
        
        resp = 'Your downgrade was requested.'
        msg = "The user {0} wants an account downgrade!".format(request.user.username)
        sbj = "Downgrade Request"
        #send_mail(sbj, msg, admin_email,[to_email], fail_silently=False)
        mail_box.add_msg('DOWNGRADE', sbj, request.user.username)
            
        context = {'resp' : resp, 'group' : group}
        return render(request, 'gym_app/upgrade_downgrade.html', context)
            
    context = {'resp' : 'Your upgrade was requested.', 'group' : group}
    return render(request, 'gym_app/upgrade_downgrade.html', context)  

@login_required
@permission_required('auth.permission.is_admin', login_url='/permission_denied/')
def plan_manage(request):
    
    if request.user.is_superuser:   
        group = 'admin'
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name
        except:
            group = 'none'
    
    messages = MailBox.objects.get(owner = 'admin').messages.all()
    context = {'messages' : messages, 'group' : group}
    return render(request, 'gym_app/plan_manage.html', context)


def permission_denied(request):

    if request.user.is_superuser:   
        group = 'admin'
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name
        except:
            group = 'none'

    return render(request, 'gym_app/permission_denied.html', {'group' : group})

@login_required  
@permission_required('auth.permission.is_admin', login_url='/permission_denied/')
def delete_plan_msg(request):
    message_id = int(request.POST.get("delete"))
    MailBox.objects.get(owner = 'admin').del_msg(message_id)
    return HttpResponseRedirect('/plan_manage/')   

@login_required
@permission_required('auth.permission.is_admin', login_url='/permission_denied/')
def change_upgrade_downgrade(request):
    value = request.POST.get("change")
    username, change_type, message_id = value.split('/')
    user = User.objects.get(username = username)
    if change_type == 'UPGRADE':
        user.groups.remove(Group.objects.get(name = 'regular'))
        user.groups.add(Group.objects.get(name = 'premium'))
    elif change_type == 'DOWNGRADE':
        user.groups.remove(Group.objects.get(name = 'premium'))
        user.groups.add(Group.objects.get(name = 'regular'))
    else:
        user.is_active = True
        user.save()
    MailBox.objects.get(owner = 'admin').del_msg(message_id)
    return HttpResponseRedirect('/plan_manage/')  


@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='regular')).count() == 1, login_url='/permission_denied/')
def payment(request):
    
    if request.user.is_superuser:   
        group = 'admin'
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name
        except:
            group = 'none'
    
    
    if request.method == 'POST':

        payment_form = PaymentForm(data=request.POST)

        # If the two forms are valid...
        if payment_form.is_valid():
            mail_box = MailBox.objects.get(owner = "admin")
            mail_box.add_msg('UPGRADE', "Upgrade Request.", request.user.username)
            
            return HttpResponseRedirect('/upgrade_downgrade') 
            
        else:
            context = {'group' : group, 'payment_form': payment_form}
            return render(request, 'gym_app/payment.html', context)
        
        
    payment_form = PaymentForm()
    context = {'group' : group, 'payment_form': payment_form}

    return render(request, 'gym_app/payment.html', context) 

@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='personal_trainer')).count() == 1, login_url='/permission_denied/')
def create_screening(request):

    if request.user.is_superuser:   
        group = 'admin';
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name;
        except:
            group = 'none'

    control = False



    if request.method == 'POST':
        
        athlete_form = AthleteSelectForm(data=request.POST)
        screening_form = BodyScreeningForm(data=request.POST)

        if athlete_form.is_valid():
            control = True
            #user = User.objects.get(username = athlete_form.cleaned_data['athlete'])
            username = athlete_form.cleaned_data['athlete']

            user = User.objects.get(username = username)
            screenings = Athlete.objects.get(user = user.id).screenings.all()
            if len(screenings) > 0:
                current_screening = screenings[len(screenings)-1]
                screening_form = BodyScreeningForm(instance=current_screening)
            else:
                screening_form = BodyScreeningForm(data=request.POST)

            return render(request, 'gym_app/create_screening.html', {'screening_form': screening_form, 'athlete_form': athlete_form, 'control' : control, 'username':username, 'group': group})   

     
        if screening_form.is_valid():
            try:
                user = User.objects.get(username = request.POST.get('username'))
            except:
                user = User.objects.get(username = request.POST.get('user'))
            screening = screening_form.save(commit=False)
            screening.save()
            athlete = Athlete.objects.get(user = user.id)

            athlete.tracker.previousWeight=athlete.tracker.currentWeight
            athlete.tracker.currentWeight=screening.weight
            athlete.tracker.previousWeightDate=athlete.tracker.currentWeightDate
            athlete.tracker.currentWeightDate=datetime.now()
            athlete.tracker.save()

            sum_seven_folds = screening.triceps + screening.biceps + screening.subscapular + screening.supraspinale + screening.abdominal + screening.thigh + screening.calf
            if(athlete.gender == "M"):
                screening.bodyfat = (0.1051 * (screening.triceps + screening.subscapular + screening.supraspinale + screening.abdominal + screening.thigh + screening.calf)) + 2.585
            else:
                screening.bodyfat = (0.097 * (screening.triceps + screening.subscapular + screening.suprailic + screening.abdominal + screening.thigh + screening.chest)) + 3.64
            
            screening.bmi = (screening.weight * 703) / ((screening.feet*12+screening.inches)**2)

            screening.save()
            athlete.screenings.add(screening)
            athlete.save()


            # Render the template depending on the context.
            return render(request, 'gym_app/create_screening.html', {'screening_form': screening_form, 'athlete_form': athlete_form, 'control' : control, 'group': group})   

        if request.POST.get("submit") == "Choose":
            athlete_form = AthleteSelectForm()
            return render(request, 'gym_app/create_screening.html', {'athlete_form': athlete_form, 'control' : control, 'group': group})

        if request.POST.get("submit") == "Create":
            control = True
            username = User.objects.get(username = request.POST.get('user'))
            return render(request, 'gym_app/create_screening.html', {'screening_form': screening_form, 'athlete_form': athlete_form, 'control' : control, 'group': group, 'username' : username})   

    
    athlete_form = AthleteSelectForm()
    # Render the template depending on the context.
    return render(request, 'gym_app/create_screening.html', {'athlete_form': athlete_form, 'control' : control, 'group': group})

@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='premium') | Q(name='personal_trainer')).count() == 1, login_url='/permission_denied/')
def screenings(request):
    if request.user.is_superuser:   
        group = 'admin';
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name;
        except:
            group = 'none'


    if group == "personal_trainer":
        control = False
        if request.method == 'POST':
            
            athlete_form = AthleteSelectForm(data=request.POST)

            if athlete_form.is_valid():
                control = True
                user = User.objects.get(username = athlete_form.cleaned_data['athlete'])
                athlete = Athlete.objects.get(user = user.id)

                screenings = athlete.screenings.all()

                return render(request, 'gym_app/screenings.html', {'screenings': screenings, 'athlete_form': athlete_form, 'control' : control, 'group': group})   
            else:
                athlete_form = AthleteSelectForm()
                return render(request, 'gym_app/screenings.html', {'athlete_form': athlete_form, 'control' : control, 'group': group})

            

        
        athlete_form = AthleteSelectForm()
        # Render the template depending on the context.
        return render(request, 'gym_app/screenings.html', {'athlete_form': athlete_form, 'control' : control, 'group': group})
    else:
        control = True
        screenings = Athlete.objects.get(user = request.user.id).screenings.all()
        return render(request, 'gym_app/screenings.html', {'screenings': screenings, 'control' : control, 'group': group})   

@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='personal_trainer') | Q(name='premium')).count() == 1, login_url='/permission_denied/')
def delete_screening(request):
    screening_id = int(request.POST.get("delete"))
    BodyScreening.objects.filter(id = screening_id).delete()
    path = '/screenings/'
    return redirect(path)

@login_required
@user_passes_test(lambda u: u.groups.filter(Q(name='personal_trainer')).count() == 1, login_url='/permission_denied/')
def manage_workout(request):
    if request.user.is_superuser:   
        group = 'admin';
    else:
        try:
            group = User.objects.get(username=request.user.username).groups.all()[0].name;
        except:
            group = 'none'


    if request.method == 'POST':
        
        athlete_form = AthleteWorkoutDaySelectForm(data=request.POST)

        if athlete_form.is_valid():
            username = athlete_form.cleaned_data['athlete']
            user = User.objects.get(username = username)
            athlete = Athlete.objects.get(user = user.id)
            day = athlete_form.cleaned_data['day']
            if day == "Whole week":
                exercises_day1 = athlete.workout_plan.exercises.filter( day = 1)
                exercises_day2 = athlete.workout_plan.exercises.filter( day = 2)
                exercises_day3 = athlete.workout_plan.exercises.filter( day = 3)
                exercises_day4 = athlete.workout_plan.exercises.filter( day = 4)
                exercises_day5 = athlete.workout_plan.exercises.filter( day = 5)
                exercises_day6 = athlete.workout_plan.exercises.filter( day = 6)
                exercises_day7 = athlete.workout_plan.exercises.filter( day = 7)

                return render(request,
                    'gym_app/workout_plan.html',
                    {'day1': exercises_day1, 'day2': exercises_day2, 'day3': exercises_day3, 'day4': exercises_day5, 'day6': exercises_day6, 'day7': exercises_day7, 'group': group}) 
            else:
                t_list = Task.objects.all()
                exercises = athlete.workout_plan.exercises.filter( day = int(day))
                exercise_form = ExerciseForm()


                # Render the template depending on the context.
                return render(request, 'gym_app/workout_day.html', {'exercise_form': exercise_form, 'task_list' : t_list, 'exercises' : exercises, 'day': day, 'username': username, 'group' : group})


    athlete_form = AthleteWorkoutDaySelectForm()
    return render(request, 'gym_app/manage_workout.html', {'athlete_form': athlete_form, 'group': group})

   
