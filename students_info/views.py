from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm, CourseForm

def students(request):
    students = Student.objects.all()
    form = StudentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('students')

    context = {
        'students': students,
        'form': form,
    }
    return render(request, 'student_info/students.html', context)

def courses(request):
    courses = Course.objects.all()
    form = CourseForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('courses')

    context = {
        'courses': courses,
        'form': form,
    }
    return render(request, 'student_info/courses.html', context)

def details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    not_registered_courses = Course.objects.exclude(students=student)

    if request.method == 'POST':
        course_id = request.POST.get('course')
        course = Course.objects.get(pk=course_id)
        student.courses.add(course)

    context = {
        'student': student,
        'not_registered_courses': not_registered_courses,
    }
    return render(request, 'student_info/details.html', context)