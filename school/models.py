from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class subject(models.Model):
	subject = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.subject

class student_profile(models.Model):
	student_id = models.CharField(max_length=20, primary_key=True)
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200, null=True)
	second_name = models.CharField(max_length=200, null=True)
	date_of_birth = models.CharField(max_length=200, null=True)
	nationality = models.CharField(max_length=200, null=True)
	grade_and_class = models.CharField(max_length=200, null=True)
	profile_pic = models.ImageField(default='default.jpg', null=True, blank=True)
	allergies =  models.CharField(max_length=200, null=True)
	subjects = models.ManyToManyField(subject)

	def __str__(self):
		return self.student_id 


class geographie(models.Model):
	
	student_id = models.ForeignKey(student_profile, null=True, on_delete=models.SET_NULL)
	first_name = models.CharField(max_length=200, null=True)
	second_name = models.CharField(max_length=200, null=True)
	assessment = models.CharField(max_length=200, null=True)
	mark = models.CharField(max_length=200, null=True)
	grade = models.CharField(max_length=200, null=True)
	assessment_date = models.CharField(max_length=200, null=True)
	comments = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.first_name + " " + self.second_name

class math(models.Model):
	student_id = models.ForeignKey(student_profile, null=True, on_delete=models.SET_NULL)
	first_name = models.CharField(max_length=200, null=True)
	second_name = models.CharField(max_length=200, null=True)
	assessment = models.CharField(max_length=200, null=True)
	mark = models.CharField(max_length=200, null=True)
	grade = models.CharField(max_length=200, null=True)
	assessment_date = models.CharField(max_length=200, null=True)
	comments = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.first_name + " " + self.second_name

class science(models.Model):
	student_id =models.ForeignKey(student_profile, null=True, on_delete=models.SET_NULL)
	first_name = models.CharField(max_length=200, null=True)
	second_name = models.CharField(max_length=200, null=True)
	assessment = models.CharField(max_length=200, null=True)
	mark = models.CharField(max_length=200, null=True)
	grade = models.CharField(max_length=200, null=True)
	assessment_date = models.CharField(max_length=200, null=True)
	comments = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.first_name + " " + self.second_name

class religous_studie(models.Model):
	student_id = models.ForeignKey(student_profile, null=True, on_delete=models.SET_NULL)
	first_name = models.CharField(max_length=200, null=True)
	second_name = models.CharField(max_length=200, null=True)
	assessment = models.CharField(max_length=200, null=True)
	mark = models.CharField(max_length=200, null=True)
	grade = models.CharField(max_length=200, null=True)
	assessment_date = models.CharField(max_length=200, null=True)
	comments = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.first_name + " " + self.second_name

class art(models.Model):
	student_id = models.ForeignKey(student_profile, null=True, on_delete=models.SET_NULL)
	first_name = models.CharField(max_length=200, null=True)
	second_name = models.CharField(max_length=200, null=True)
	assessment = models.CharField(max_length=200, null=True)
	mark = models.CharField(max_length=200, null=True)
	grade = models.CharField(max_length=200, null=True)
	assessment_date = models.CharField(max_length=200, null=True)
	comments = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.first_name + " " + self.second_name


class teacher(models.Model):
	teacher_id = models.CharField(max_length=200, null=True)
	first_name = models.CharField(max_length=200, null=True)
	second_name = models.CharField(max_length=200, null=True)
	date_of_birth = models.CharField(max_length=200, null=True)
	nationality = models.CharField(max_length=200, null=True)
	subject = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.first_name + " " + self.second_name


class attendence(models.Model):
	student_id = models.ForeignKey(student_profile, null=True, on_delete=models.SET_NULL)
	first_name = models.CharField(max_length=200, null=True)
	second_name = models.CharField(max_length=200, null=True)
	subject = models.CharField(max_length=200, null=True)
	class_section = models.CharField(max_length=200, null=True)
	present = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.first_name + " " + self.second_name


