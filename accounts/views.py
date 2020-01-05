from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):
    if request.method == 'POST':
        #form submission, register user
        #get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        #check if passwords match
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                    messages.error(request,'That email is being used')
                    return redirect('register')
            else:
                #look goods, register user
                user = User.objects.create_user(username=username, password=password,
                    email=email,first_name=first_name,last_name=last_name)
                ###auto login this new user
                # auth.login(request, user)
                # messages.success(request, "You are now logged in")
                # return redirect('index')
                ###redirect to login so user can manually login
                user.save()
                messages.success(request, 'You are now registered. Please login.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')  
    #render template, in template>accounts>register.html

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            #success
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            #try again
            messages.error(request, 'Invalid credentials')
            return redirect('login')
        
    else:
        return render(request, 'accounts/login.html') 

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
    return redirect('index') 

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html', context) 