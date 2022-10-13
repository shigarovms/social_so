from django.shortcuts import render

posts = [
    {
        'author': 'Misha',
        'title': 'Post 1',
        'content': 'first post content',
        'date_posted': '1 April of 2022'
    },
    {
        'author': 'Masha',
        'title': 'Post 2',
        'content': 'second post content',
        'date_posted': '31 April of 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
