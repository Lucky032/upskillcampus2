from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from .models import Personalinfo, PasswordEntry  # Import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import make_password, check_password

def home(request):
    is_authenticated = request.session.get('is_authenticated', False)
    username = request.session.get('username', None)

    context = {
        'is_authenticated': is_authenticated,
        'username': username,
    }
    return render(request, 'home.html', context)


# View for Registration
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password == confirm_password:
            # Check if username or email already exists in Personalinfo model
            if Personalinfo.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            elif Personalinfo.objects.filter(email=email).exists():
                messages.error(request, "Email already registered")
            else:
                # Hash the password before saving
                hashed_password = make_password(password)
                personal_info = Personalinfo(username=username, email=email, password=hashed_password)
                personal_info.save()

                messages.success(request, "Registration successful! Please log in.")
                return redirect('login')  # Redirect to login page after registration
        else:
            messages.error(request, "Passwords do not match")

    return render(request, 'registration.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            # Retrieve the user
            user = Personalinfo.objects.get(username=username)

            # Validate password
            if check_password(password, user.password):
                # Set session variables
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['is_authenticated'] = True

                messages.success(request, f"Welcome, {user.username}!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        except Personalinfo.DoesNotExist:
            messages.error(request, "Invalid username or password.")

    return render(request, 'login.html')



def add_password(request):
    if request.method == 'POST':
        website = request.POST.get('website')
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"User authenticated: {request.user.is_authenticated}")  # Debugging line

        if request.user.is_authenticated:
            try:
                PasswordEntry.objects.create(user=request.user, website=website, username=username, password=password)
                messages.success(request, "Password added successfully!")
            except Exception as e:
                messages.error(request, f"Error saving password: {str(e)}")
                print(f"Error saving password: {str(e)}")  # Log error
        else:
            messages.error(request, "You need to be logged in to add passwords.")

    return redirect('dashboard')



# View for the Dashboard
def dashboard(request):
    # Retrieve saved passwords for the authenticated user
    if request.user.is_authenticated:
        saved_passwords = PasswordEntry.objects.filter(user=request.user)
    else:
        saved_passwords = []

    # Render the dashboard page with the saved passwords
    return render(request, 'dashboard.html', {'saved_passwords': saved_passwords})



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PasswordEntry  # Import your model for storing passwords


def retrieve_accounts(request):
    user = request.user  # Get the logged-in user

    # Fetch saved passwords for the logged-in user
    saved_passwords = PasswordEntry.objects.filter(user=user)

    # Pass the data to the template
    return render(request, 'retrieve_accounts.html', {'saved_passwords': saved_passwords})




def logout_user(request):
    request.session.flush()  # Clear all session data
    messages.success(request, "You have been logged out.")
    return redirect('login')

