from django.contrib import admin
from django.urls import path
from donations import views  # Import views from donations app

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),

    # Authentication URLs
    path('signup/', views.signup, name='signup'),  # Signup page
    path('login/', views.login_view, name='login'),  # Login page
    path('logout/', views.logout_view, name='logout'),  # Logout page
    path('home/', views.home, name='home'), 

    # Campaign URLs
    path('', views.home, name='home'),  # Home page, listing campaigns
    path('donate/<int:campaign_id>/', views.donate, name='donate'),  # Donate page

    # Profile URL
    path('donor_profile/', views.donor_profile, name='donor_profile'),  # Donor profile page
]
