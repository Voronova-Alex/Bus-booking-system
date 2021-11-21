from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .views import SignUpView, ProfileView, ActivateAccount
from booking_bus.views import OldTripView

urlpatterns = [
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/old_trip', OldTripView.as_view(), name='old_trip'),

    #New password
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html',
                                                                   success_url='/'),
         name='change_password'),
    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html',
             subject_template_name='password_reset_subject.txt',
             email_template_name='password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),

    # Login and Logout
    path('login/', auth_views.LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='login.html'
        ),
        name='login'
    ),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
        ),
        name='logout'
    ),

]
