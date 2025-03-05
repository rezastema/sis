from django.shortcuts import render, redirect
from .models import Attendance
from .forms import AttendanceForm

def attendance_list(request):
    attendance_records = Attendance.objects.all()
    return render(request, 'attendance/attendance_list.html', {'attendance_records': attendance_records})

def attendance_create(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'attendance/attendance_form.html', {'form': form})
