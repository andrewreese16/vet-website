from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, AnimalForm, AppointmentForm, NoteForm, MedicationForm
from .models import Profile, Animal, Appointment, Note, Medication
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, "home.html")


# Sign up a new user
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after signing up
            return redirect("profile")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


# Profile page
@login_required
def profile(request):
    # Ensure a Profile object exists for the logged-in user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        # Update the profile with the submitted data
        profile.phone_number = request.POST.get("phone_number", profile.phone_number)
        profile.address = request.POST.get("address", profile.address)
        profile.save()
        # Optional: Add a success message or redirect to the same page to confirm the save
        return redirect("profile")  # Replace 'profile' with your URL name

    # Render the profile form with the existing profile data
    return render(request, "profile.html", {"profile": profile})


# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


# View list of animals (pets) for the logged-in user
@login_required
def animal_list(request):
    animals = Animal.objects.filter(owner=request.user)
    return render(request, "animal_list.html", {"animals": animals})


# Add a new animal (pet)
@login_required
def add_animal(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.owner = request.user
            animal.save()
            return redirect("animal_list")
    else:
        form = AnimalForm()
    return render(request, "add_animal.html", {"form": form})


# Schedule a new appointment
@login_required
def schedule_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.animal = Animal.objects.get(id=request.POST.get("animal"))
            appointment.save()
            return redirect("appointment_list")
    else:
        form = AppointmentForm()
    return render(request, "schedule_appointment.html", {"form": form})


# View all appointments for the logged-in user
@login_required
def appointment_list(request):
    appointments = Appointment.objects.filter(animal__owner=request.user)
    return render(request, "appointment_list.html", {"appointments": appointments})


# View and add notes for a specific appointment
@login_required
def add_note_to_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.appointment = appointment
            note.staff_member = (
                request.user.username
            )  # Assuming staff member is the logged-in user
            note.save()
            return redirect("appointment_list")
    else:
        form = NoteForm()
    return render(
        request,
        "add_note_to_appointment.html",
        {"form": form, "appointment": appointment},
    )


# Add medication for a specific animal
@login_required
def add_medication(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == "POST":
        form = MedicationForm(request.POST)
        if form.is_valid():
            medication = form.save(commit=False)
            medication.animal = animal
            medication.save()
            return redirect("animal_list")
    else:
        form = MedicationForm()
    return render(request, "add_medication.html", {"form": form, "animal": animal})


# View medications for a specific animal
@login_required
def medication_list(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    medications = Medication.objects.filter(animal=animal)
    return render(
        request, "medication_list.html", {"medications": medications, "animal": animal}
    )
