from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def chef(request):
    
    name = request.POST.get('name')
    ing = request.POST.get('ing')
    cook = request.POST.get('cook')
    cat = request.POST.get('cat')
    img = request.FILES.get('img')
    
    if request.method == 'POST':
        method = request.POST.get('method', 'POST')
        if method == 'POST':
            a = Recipe(cus_rec = request.user, name = name, ing = ing, cook = cook, cat = cat, img = img)
            a.save()
        elif method == 'PUT':
            id = request.POST.get('id')
            a = Recipe.objects.get(id = id)
            a.name = name
            a.ing = ing
            a.cook = cook
            a.cat = cat
            if img:
                a.img = img
            a.save()
        elif method == 'DELETE':
            id = request.POST.get('id')
            a = Recipe.objects.get(id = id)
            a.delete()
    
    return render(request,'chef.html', {'choices': Recipe._meta.get_field('cat').choices, 'all': Recipe.objects.all()})

def viewer(request):
    
    name = request.POST.get('name')
    comment = request.POST.get('com')
    author = request.POST.get('author')
    
    if request.method == 'POST':
        method = request.POST.get('method')
        if method == 'fav':
          id = request.POST.get('id')
          a = Recipe.objects.get(id = id)
          b = fav(rec_fav = a, name = name)
          if fav.objects.filter(name = name, rec_fav = a).exists():
              messages.error(request,'Already saved to favorite')
          else:
            b.save()
        elif method == 'comment':
            id =request.POST.get('id')
            a = Recipe.objects.get(id = id)
            b = Comments(rec_comment = a, com = comment, author = author)
            b.save()
        elif method == 'COM_EDIT':
            id = request.POST.get('id')
            a = Comments.objects.get(id = id)
            a.com = comment
            a.save()        
        elif method == 'COM_DELETE':
            id = request.POST.get('id')
            a = Comments.objects.get(id = id)
            a.delete()
    
    return render(request,'viewer.html', {'all': Recipe.objects.all(), 'comment': Comments.objects.all()})

def favor(request):
    return render(request,'fav.html', {'all': fav.objects.all()})

def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.role == 'chef':
                return redirect('chef')
            elif user.role == 'viewer':
                return redirect('viewer')
            else:
                return redirect('home') 
        else:
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('login')

    return render(request, 'login.html')

def register(request):
    
    username = request.POST.get('username')
    pass1 = request.POST.get('pass1')
    pass2 = request.POST.get('pass2')
    email = request.POST.get('email')
    first = request.POST.get('first')
    last = request.POST.get('last')
    role = request.POST.get('role')
    
    if request.method == 'POST':
        if pass1 == pass2:
            if CustomUser.objects.filter(email = email).exists():
                messages.error(request,'Email already exist\'s please choose other')
                return render(request,'register.html', {'choices': CustomUser._meta.get_field('role').choices})
            else:
                user = CustomUser.objects.create_user(username = username, password = pass2, email = email, first_name = first, last_name = last)
                user.role = role
                user.save() 
                messages.success(request,'Successfully created new user')
                return redirect('login') 
        else:
            messages.error(request,'Mismatch passwords')
            return render(request,'register.html', {'choices': CustomUser._meta.get_field('role').choices})
    
    return render(request,'register.html', {'choices': CustomUser._meta.get_field('role').choices})

def profile(request):
    
    username =request.POST.get('username')
    pass1 = request.POST.get('pass1')
    pass2 = request.POST.get('pass2')
    
    if request.method == 'POST':
        if pass1 == pass2:
            user = request.user
            if user and (pass1 == pass2):
                user.username = username
                user.set_password(pass2)
            user.save()
            logout(request)
            messages.success(request,'Successfully changed password')
            return redirect('login')
        else:
            messages.error(request,'Password aren\'t matching please check')
            return redirect('profile')
    
    return render(request, 'profile.html')

def home(request):
    return render(request,'home.html')

def log_out(request):
    logout(request)
    messages.success(request,'Logged Out Successfully')
    return redirect('login')