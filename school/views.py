from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

from .filters import *

from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import Group

from .decorators import *

# Create your views here.

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			
			group = Group.objects.get(name='students')
			user.groups.add(group)
			student_profile.objects.create(

					user=user,
					first_name=user.username

				)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'school/register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('user_home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'school/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def home(request):
	return render(request, 'school/home.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['students', 'admins'])
def user_home(request):
	return render(request, 'school/user_home.html')



@login_required(login_url='login')
@allowed_users(allowed_roles=['students', 'admins'])
def student_marks(request):

	geo = request.user.student_profile.geographie_set.all()
	maths = request.user.student_profile.math_set.all()	
	religous_studies = request.user.student_profile.religous_studie_set.all()
	arts = request.user.student_profile.art_set.all()

	context = {'student': student, 'geo': geo, 'maths': maths, 
	'sciences': sciences, 'religous_studies': religous_studies, 
	'arts': arts}

	return render(request, 'school/student_marks.html', context)

def staff(request):
	return render(request, 'school/staff.html')

def contact(request):
	return render(request, 'school/contact.html')

def about(request):
	return render(request, 'school/about.html')

def user_staff(request):
	return render(request, 'school/user_staff.html')

def user_contact(request):
	return render(request, 'school/user_contact.html')

def user_about(request):
	return render(request, 'school/user_about.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['geography_teachers', 'admins'])
def teacher_panel(request):
	return render(request, 'school/teacher_panel.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['students', 'admins'])
def student(request):
	context = {}
	return render(request, 'school/student.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['geography_teachers', 'admins'])
def student_grades(request, pk):
	student = student_profile.objects.get(student_id=pk)

	geo = student.geographie_set.all()
	maths = student.math_set.all()
	religous_studies = student.religous_studie_set.all()
	arts = student.art_set.all()

	context = {'student': student, 'geo': geo, 'maths': maths, 
	'sciences': sciences, 'religous_studies': religous_studies, 
	'arts': arts}

	return render(request, 'school/student_grades.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['geography_teachers', 'admins'])
def class_section(request):
	#student = student_profile.objects.all()
	section1= student_profile.objects.filter(grade_and_class= '7B')
	section2= student_profile.objects.filter(grade_and_class= '6A')

	#context = {'student': student}
	context = {'section1': section1, 'section2': section2}
	return render(request, 'school/class_section.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['students', 'admins'])
def student_attendence(request):

	attend = request.user.student_profile.attendence_set.all()

	myFilter = attendenceFilter2(request.GET, queryset=attend)
	attend = myFilter.qs


	context = {'attend': attend, 'myFilter': myFilter}

	return render(request, 'school/student_attendence.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['geography_teachers', 'admins'])
def student_profiles(request):
	studentprofiles = student_profile.objects.all()

	myFilter = student_profileFilter(request.GET, queryset=studentprofiles)
	studentprofiles = myFilter.qs

	context = {'studentprofiles': studentprofiles, 'myFilter': myFilter}
	return render(request, 'school/student_profile.html', context)

@login_required(login_url='login')
def maths(request):
	maths = math.objects.all()


	myFilter = mathFilter(request.GET, queryset=maths)
	maths = myFilter.qs


	context = {'maths': maths, 'myFilter': myFilter}
	return render(request, 'school/maths.html', context)

@login_required(login_url='login')
def sciences(request):
	sciences = science.objects.all()

	myFilter = scienceFilter(request.GET, queryset=sciences)
	sciences = myFilter.qs


	context = {'sciences': sciences, 'myFilter': myFilter}
	return render(request, 'school/sciences.html', context)

@login_required(login_url='login')
def religious_studies(request):
	RE = religous_studie.objects.all()

	myFilter = religous_studieFilter(request.GET, queryset=RE)
	RE = myFilter.qs


	context = {'RE': RE, 'myFilter': myFilter}
	return render(request, 'school/religious_studies.html', context)


@login_required(login_url='login')
def arts(request):
	arts = art.objects.all()

	myFilter = artFilter(request.GET, queryset=arts)
	arts = myFilter.qs

	context = {'arts': arts, 'myFilter': myFilter}
	return render(request, 'school/arts.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['geography_teachers', 'admins'])
def geography(request):
	geography = geographie.objects.all()

	myFilter = geographieFilter(request.GET, queryset=geography)
	geography = myFilter.qs


	context = {'geography': geography, 'myFilter': myFilter}
	return render(request, 'school/geography.html', context)

def report(request):
	return render(request, 'school/report.html')

@login_required(login_url='login')
def attendence(request, pk):
	student = student_profile.objects.get(student_id=pk)

	attend = student.attendence_set.all()

	context = {'student': student,'attend': attend}
	return render(request, 'school/attendence.html', context)

@login_required(login_url='login')
def profile(request, pk):
	student = student_profile.objects.get(student_id=pk)


	context = {'student': student}
	return render(request, 'school/profile.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['geography_teachers', 'admins'])
def createGeography(request):

	form = geographieForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = geographieForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('geography')

	context ={'form': form}

	return render(request, 'school/geography_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['geography_teachers', 'admins'])
def updateGeography(request, pk):

	geography = geographie.objects.get(id=pk)	

	form = geographieForm(instance=geography)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = geographieForm(request.POST, instance=geography)
		if form.is_valid():
			form.save()
			return redirect('geography')

	context ={'form': form}

	return render(request, 'school/geography_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['geography_teachers', 'admins'])
def deleteGeography(request, pk):

	geography = geographie.objects.get(id=pk)	

	form = geographieForm(instance=geography)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = geographieForm(request.POST, instance=geography)
		if form.is_valid():
			form.save()
			return redirect('geography')

	if request.method == "POST":
		geography.delete()
		return redirect('geography')
	context ={'item': geography}

	return render(request, 'school/geography_delete_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['art_teachers', 'admins'])
def createArts(request):

	form = artForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = artForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('arts')

	context ={'form': form}

	return render(request, 'school/art_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['art_teachers', 'admins'])
def updateArts(request, pk):

	arts = art.objects.get(id=pk)	

	form = artForm(instance=arts)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = artForm(request.POST, instance=arts)
		if form.is_valid():
			form.save()
			return redirect('arts')

	context ={'form': form}

	return render(request, 'school/art_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['art_teachers', 'admins'])
def deleteArts(request, pk):

	arts = art.objects.get(id=pk)	

	form = artForm(instance=arts)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = artForm(request.POST, instance=arts)
		if form.is_valid():
			form.save()
			return redirect('arts')

	if request.method == "POST":
		arts.delete()
		return redirect('arts')
	context ={'item': arts}

	return render(request, 'school/art_delete_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['maths_teachers', 'admins'])
def createMaths(request):

	form = mathForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = mathForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('maths')

	context ={'form': form}
	return render(request, 'school/maths_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['maths_teachers', 'admins'])
def updateMaths(request, pk):

	maths = math.objects.get(id=pk)	

	form = mathForm(instance=maths)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = mathForm(request.POST, instance=maths)
		if form.is_valid():
			form.save()
			return redirect('maths')

	context ={'form': form}

	return render(request, 'school/maths_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['maths_teachers', 'admins'])
def deleteMaths(request, pk):

	maths = math.objects.get(id=pk)	

	form = mathForm(instance=maths)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = artForm(request.POST, instance=maths)
		if form.is_valid():
			form.save()
			return redirect('maths')

	if request.method == "POST":
		maths.delete()
		return redirect('maths')

	context ={'item': maths}

	return render(request, 'school/maths_delete_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['religious_studies_teachers', 'admins'])
def createReligious_studies(request):

	form = religous_studieForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = religous_studieForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('religious_studies')

	context ={'form': form}

	return render(request, 'school/religious_studies_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['religious_studies_teachers', 'admins'])
def updateReligious_studies(request, pk):

	religous_studies = religous_studie.objects.get(id=pk)	

	form = religous_studieForm(instance=religous_studies)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = religous_studieForm(request.POST, instance=religous_studies)
		if form.is_valid():
			form.save()
			return redirect('religious_studies')

	context ={'form': form}

	return render(request, 'school/religious_studies_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['religious_studies_teachers', 'admins'])
def deleteReligious_studies(request, pk):

	religous_studies = religous_studie.objects.get(id=pk)	

	form = religous_studieForm(instance=religous_studies)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = religous_studieForm(request.POST, instance=religous_studies)
		if form.is_valid():
			form.save()
			return redirect('religious_studies')

	if request.method == "POST":
		religous_studies.delete()
		return redirect('religious_studies')
	context ={'item': religous_studies}

	return render(request, 'school/religious_studies_delete_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['science_teachers', 'admins'])
def createSciences(request):

	form = scienceForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = scienceForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('sciences')

	context ={'form': form}

	return render(request, 'school/sciences_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['science_teachers', 'admins'])
def updateSciences(request, pk):

	sciences = science.objects.get(id=pk)	

	form = scienceForm(instance=sciences)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = scienceForm(request.POST, instance=sciences)
		if form.is_valid():
			form.save()
			return redirect('sciences')

	context ={'form': form}

	return render(request, 'school/sciences_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['science_teachers', 'admins'])
def deleteSciences(request, pk):

	sciences = science.objects.get(id=pk)	

	form = scienceForm(instance=sciences)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = scienceForm(request.POST, instance=sciences)
		if form.is_valid():
			form.save()
			return redirect('sciences')

	if request.method == "POST":
		sciences.delete()
		return redirect('sciences')

	context ={'item': sciences}

	return render(request, 'school/sciences_delete_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def createStudentProfile(request):

	form = student_profileForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = student_profileForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('student_profile')

	context ={'form': form}

	return render(request, 'school/student_profile_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def updateStudentProfile(request, pk):

	student_profiles = student_profile.objects.get(student_id=pk)	

	form = student_profileForm(instance=student_profiles)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = student_profileForm(request.POST, instance=student_profiles)
		if form.is_valid():
			form.save()
			return redirect('student_profile')

	context ={'form': form}

	return render(request, 'school/student_profile_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admins'])
def deleteStudentProfile(request, pk):

	student_profiles = student_profile.objects.get(student_id=pk)	

	form = student_profileForm(instance=student_profiles)
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = student_profileForm(request.POST, instance=student_profiles)
		if form.is_valid():
			form.save()
			return redirect('student_profile')

	if request.method == "POST":
		student_profiles.delete()
		return redirect('student_profile')
	context ={'item': student_profiles}

	return render(request, 'school/student_profile_delete_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['students', 'admins'])
def accountSettings(request):
	student_profile = request.user.student_profile
	form = student_profileForm(instance=student_profile)
	
	if request.method == 'POST':
		form = student_profileForm(request.POST, request.FILES, instance=student_profile)
		if form.is_valid():
			form.save()

	context = {'form':form}

	return render(request, 'school/account_settings.html', context)
