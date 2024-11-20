from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # Home page
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/", views.profile, name="profile"),
    path("animal_list/", views.animal_list, name="animal_list"),
    path("add_animal/", views.add_animal, name="add_animal"),
    path(
        "schedule_appointment/", views.schedule_appointment, name="schedule_appointment"
    ),
    path("add_medication/", views.add_medication, name="add_medication"),
    path(
        "medication_list/<int:animal_id>/",
        views.medication_list,
        name="medication_list",
    ),
    path("appointment_list/", views.appointment_list, name="appointment_list"),
    path(
        "add_note_to_appointment/<int:appointment_id>/",
        views.add_note_to_appointment,
        name="add_note_to_appointment",
    ),
]
