from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class geographieForm(ModelForm):
	class Meta:
		model = geographie
		fields = '__all__'
		widgets = {
				'student_id':forms.TextInput(attrs={'class': 'form-control' }),
				'first_name':forms.TextInput(attrs={'class': 'form-control' }),
				'second_name':forms.TextInput(attrs={'class': 'form-control' }),
				'assessment':forms.TextInput(attrs={'class': 'form-control' }),
				'mark':forms.TextInput(attrs={'class': 'form-control' }),
				'grade':forms.TextInput(attrs={'class': 'form-control' }),
				'assessment_date':forms.TextInput(attrs={'class': 'form-control' }),
				'comments':forms.TextInput(attrs={'class': 'form-control' }),

		}

class student_profileForm(ModelForm):
	class Meta:
		model = student_profile
		fields = '__all__'
		exclude = ['user']
		widgets = {
				'student_id':forms.TextInput(attrs={'class': 'form-control' }),
				'first_name':forms.TextInput(attrs={'class': 'form-control' }),
				'second_name':forms.TextInput(attrs={'class': 'form-control' }),
				'date_of_birth':forms.TextInput(attrs={'class': 'form-control' }),
				'nationality':forms.TextInput(attrs={'class': 'form-control' }),
				'grade_and_class':forms.TextInput(attrs={'class': 'form-control' }),
				'profile_pic':forms.TextInput(attrs={'class': 'form-control' }),
				'allergies':forms.TextInput(attrs={'class': 'form-control' }),
				'subjects':forms.TextInput(attrs={'class': 'form-control' }),

		}

class mathForm(ModelForm):
	class Meta:
		model = math
		fields = '__all__'

		widgets = {
				'student_id':forms.TextInput(attrs={'class': 'form-control' }),
				'first_name':forms.TextInput(attrs={'class': 'form-control' }),
				'second_name':forms.TextInput(attrs={'class': 'form-control' }),
				'assessment':forms.TextInput(attrs={'class': 'form-control' }),
				'mark':forms.TextInput(attrs={'class': 'form-control' }),
				'grade':forms.TextInput(attrs={'class': 'form-control' }),
				'assessment_date':forms.TextInput(attrs={'class': 'form-control' }),
				'comments':forms.TextInput(attrs={'class': 'form-control' }),

		}

class scienceForm(ModelForm):
	class Meta:
		model = science
		fields = '__all__'

		widgets = {
			'student_id':forms.TextInput(attrs={'class': 'form-control' }),
			'first_name':forms.TextInput(attrs={'class': 'form-control' }),
			'second_name':forms.TextInput(attrs={'class': 'form-control' }),
			'assessment':forms.TextInput(attrs={'class': 'form-control' }),
			'mark':forms.TextInput(attrs={'class': 'form-control' }),
			'grade':forms.TextInput(attrs={'class': 'form-control' }),
			'assessment_date':forms.TextInput(attrs={'class': 'form-control' }),
			'comments':forms.TextInput(attrs={'class': 'form-control' }),

	}

class religous_studieForm(ModelForm):
	class Meta:
		model = religous_studie
		fields = '__all__'

		widgets = {
				'student_id':forms.TextInput(attrs={'class': 'form-control' }),
				'first_name':forms.TextInput(attrs={'class': 'form-control' }),
				'second_name':forms.TextInput(attrs={'class': 'form-control' }),
				'assessment':forms.TextInput(attrs={'class': 'form-control' }),
				'mark':forms.TextInput(attrs={'class': 'form-control' }),
				'grade':forms.TextInput(attrs={'class': 'form-control' }),
				'assessment_date':forms.TextInput(attrs={'class': 'form-control' }),
				'comments':forms.TextInput(attrs={'class': 'form-control' }),

		}

class artForm(ModelForm):
	class Meta:
		model = art
		fields = '__all__'

		widgets = {
				'student_id':forms.TextInput(attrs={'class': 'form-control' }),
				'first_name':forms.TextInput(attrs={'class': 'form-control' }),
				'second_name':forms.TextInput(attrs={'class': 'form-control' }),
				'assessment':forms.TextInput(attrs={'class': 'form-control' }),
				'mark':forms.TextInput(attrs={'class': 'form-control' }),
				'grade':forms.TextInput(attrs={'class': 'form-control' }),
				'assessment_date':forms.TextInput(attrs={'class': 'form-control' }),
				'comments':forms.TextInput(attrs={'class': 'form-control' }),

		}




		