from django.shortcuts import render

posts = [
    {
        'author': 'Sayed Mahmud',
        'title': 'Hello, Django',
        'content': 'Django content goes here',
        'date_posted': 'March 25, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Hello, Django 2',
        'content': 'Hello this is second content',
        'date_posted': 'March 26, 2020'
    }
]

def home(request):
    context = {
        "posts": posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {'title': 'About'})