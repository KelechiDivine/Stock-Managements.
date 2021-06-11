from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD

def home(request):
    title = 'Welcome: This is the home page'
    
    context = {
        "title": title
    }
    
    return render(request, "home.html", context)
=======
>>>>>>> 87bb5edb326c584cbbae24757dca6d006e18860b
