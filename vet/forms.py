from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Animal, Appointment, Medication, Note


# User registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Profile form for additional user details
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["phone_number", "address"]


# Animal (Pet) form
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ["name", "species", "breed", "age", "weight"]


# Appointment form
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["notes", "appointment_date", "animal"]
        widgets = {
            "appointment_date": forms.DateInput(attrs={"type": "date"}),  # Date widget
        }


# Medication form
class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ["medicine_name", "dosage", "start_date", "end_date", "animal"]


# Note form (for adding appointment notes)
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["note"]
