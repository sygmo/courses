from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
	context = {
		"courses" : Course.objects.all() # select * from Course
	}
	return render(request, "courses/index.html", context)

def courses(request):
	Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect('/')

def destroy(request, id):
	course_id = id
	print "COURSE ID: ", course_id
	context = {
		"course" : Course.objects.filter(id=id)
	}
	return render(request, "courses/destroy.html", context)

def delete(request, id):
	Course.objects.filter(id=id).delete()
	return redirect('/')