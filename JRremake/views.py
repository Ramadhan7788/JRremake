from django.shortcuts import render

def home(request):
    context = {
        'title': 'Home - JR Remake',
        'heading': 'JR Remake Home Page',
        'subheading': 'Your gateway to the JR Remake project',
        'description': 'Explore the features and updates of the JR Remake project here.'
    }
    return render(request, 'home.html', context)