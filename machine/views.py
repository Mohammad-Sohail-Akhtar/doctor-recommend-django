
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from machine.predictor import recommend_doctor
from django.contrib import messages
from main_app.models import Doctor
from main_app.models import Appointment  # your Appointment model


@login_required
def book_appointment(request):
    if request.method == "POST":
        user = request.user  
        address = request.POST.get("address")
        number = request.POST.get("number")
        gender = request.POST.get("gender")
        s1 = request.POST.get("symptom1", "").strip()
        s2 = request.POST.get("symptom2", "").strip()
        s3 = request.POST.get("symptom3", "").strip()
        s4 = request.POST.get("symptom4", "").strip()

        # ✅ Check if any symptom field is empty
        if not all([s1, s2, s3, s4]):
            messages.error(request, "Please fill in all symptom fields before submitting.")
            return render(request, "machine/book.html", {
                "user": user,
                "address": address,
                "number": number,
                "gender": gender,
                "s1": s1,
                "s2": s2,
                "s3": s3,
                "s4": s4,
            })

        # ML prediction
        speciality_name = recommend_doctor(s1, s2, s3, s4)

        # Normalize speciality name to match DB records
        speciality_name = speciality_name.strip().title()

        doctors = Doctor.objects.filter(speciality__name__iexact=speciality_name)

        return render(request, "machine/recommend.html", {
            "user": user,
            "doctors": doctors,
            "speciality": speciality_name
        })

    return render(request, "machine/book.html")


@login_required
def confirm_appointment(request):
    if request.method == "POST":
        user = request.user
        doctor_id = request.POST.get("doctor_id")
        appointment_date = request.POST.get("appointment_date")
        appointment_time = request.POST.get("appointment_time")
        address = request.POST.get("address")
        number = request.POST.get("number")
        gender = request.POST.get("gender")

        doctor = get_object_or_404(Doctor, id=doctor_id)

        Appointment.objects.create(
            user=user,
            doctor=doctor,
            address=address,
            number=number,
            gender=gender,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
        )

        return redirect("appointments")   # go to appointments.html

    return redirect("book_appointment")


@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "machine/appointments.html", {"appointments": appointments})





@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)
    appointment.delete()
    messages.success(request, "Appointment deleted successfully.")
    return redirect('appointments')


@login_required
def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id, user=request.user)

    # Filter doctors only from the same speciality as the booked doctor
    doctors = Doctor.objects.filter(speciality=appointment.doctor.speciality)

    if request.method == "POST":
        doctor_id = request.POST.get("doctor")
        appointment_date = request.POST.get("appointment_date")
        appointment_time = request.POST.get("appointment_time")

        # Update fields
        if doctor_id:
            appointment.doctor = Doctor.objects.get(id=doctor_id)
        appointment.appointment_date = appointment_date
        appointment.appointment_time = appointment_time
        appointment.save()

        return redirect("appointments")

    return render(request, "machine/edit_appointment.html", {
        "appointment": appointment,
        "doctors": doctors,   # only recommended doctors
    })