from django.shortcuts import render, redirect
from .models import Campaign  # Ensure Campaign is imported here
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Home page, displaying all campaigns

def home(request):
    campaigns = Campaign.objects.all()
    return render(request, 'donations/home.html', {'campaigns': campaigns})



# Sign up view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after login
        else:
            # Handle invalid login
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)  # Logs the user out
    return redirect('home')  # Redirect to home after logout

# Donor profile view
@login_required
def donor_profile(request):
    # View for logged-in users to view their profile and donations
    return render(request, 'donor_profile.html')

# Donate view for a specific campaign
def donate(request, campaign_id):
    campaign = Campaign.objects.get(id=campaign_id)
    if request.method == 'POST':
        # Handle donation logic here
        pass
    return render(request, 'donate.html', {'campaign': campaign})
