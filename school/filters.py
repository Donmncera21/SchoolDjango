import django_filters
from django_filters import DateFilter

from .models import *

class student_profileFilter(django_filters.FilterSet):
	class Meta:
		model = student_profile
		fields = '__all__'
		exclude = ['subjects', 'profile_pic']

class geographieFilter(django_filters.FilterSet):
	class Meta:
		model = geographie
		fields = '__all__'
		exclude = ['comments']

class mathFilter(django_filters.FilterSet):
	class Meta:
		model = math
		fields = '__all__'
		exclude = ['comments']

class scienceFilter(django_filters.FilterSet):
	class Meta:
		model = science
		fields = '__all__'
		exclude = ['comments']

class religous_studieFilter(django_filters.FilterSet):
	class Meta:
		model = religous_studie
		fields = '__all__'
		exclude = ['comments']

class artFilter(django_filters.FilterSet):
	class Meta:
		model = art
		fields = '__all__'
		exclude = ['comments']

class attendenceFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	class Meta:
		model = attendence
		fields = '__all__'
		exclude = ['comments']


class attendenceFilter2(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	class Meta:
		model = attendence
		fields = ['start_date', 'end_date']