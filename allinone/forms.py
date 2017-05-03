# coding: utf-8
from django import forms

from .models import *

def get_all_comps():
	return Competition.objects.all().values_list('id', 'name')

class FirstQueryForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(FirstQueryForm, self).__init__(*args, **kwargs)
		self.fields['p2'] = forms.ChoiceField(
			label=u'Змагання:',
			choices=get_all_comps() )
	p1 = forms.CharField(label=u'Значення віку:', max_length=100)
	# p2 = forms.IntegerField(
	# 	widget=forms.Select(
	# 		choices=Competition.objects.all().values_list('id', 'name')
	# 		)
	# 	) 

class SecondQueryForm(forms.Form):
	p1 = forms.CharField(label=u'Перша буква:', max_length=100)
	p2 = forms.IntegerField(label=u'Кількість учасників:', min_value=0)



class ThirdQueryForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(ThirdQueryForm, self).__init__(*args, **kwargs)
		self.fields['p1'] = forms.ChoiceField(
			label=u'Назва змагання:',
			choices=get_all_comps() )
	# p1 = forms.CharField(label=u'Назва змагання:', max_length=100)
	p2 = forms.IntegerField(label=u'Кількість учасників:', min_value=0)


def get_all_orgs():
	return Organizator.objects.all().values_list('id', 'name')

class FourthQueryForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(FourthQueryForm, self).__init__(*args, **kwargs)
		self.fields['p1'] = forms.ChoiceField(
			label=u'Назва організації:',
			choices=get_all_orgs() )
	# p1 = forms.CharField(label=u'Назва організації:', max_length=100)
	p2 = forms.CharField(label=u'Назва країни:', max_length=100)

class FifthQueryForm(forms.Form):
	p1 = forms.CharField(label=u'Вид велосипеда:', max_length=100)
	p2 = forms.IntegerField(label=u'Максимальна вага:', min_value=0)


def get_all_teams():
	return Team.objects.all().values_list('id', 'name')

class SixthQueryForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(SixthQueryForm, self).__init__(*args, **kwargs)
		self.fields['p1'] = forms.ChoiceField(
			label=u'Назва команди:',
			choices=get_all_orgs() )
	p2 = forms.IntegerField(label=u'Досягнутий вік:', min_value=0)

def get_all_coaches():
	return Coach.objects.all().values_list('id', 'name')

class SeventhQueryForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(SeventhQueryForm, self).__init__(*args, **kwargs)
		self.fields['p1'] = forms.ChoiceField(
			label=u'Тренер:',
			choices=get_all_coaches() )
	# p1 = forms.CharField(label=u'Тренер:', max_length=100)
	p2 = forms.IntegerField(label=u'Максимальна кількість учасників:', min_value=0)

class EighthQueryForm(forms.Form):
	p1 = forms.CharField(label=u'Ціна:', max_length=100)
	p2 = forms.CharField(label=u'Матеріал:', max_length=100)
# site = forms.IntegerField(
# 	widget=forms.Select(
# 		choices=Site.objects.all().values_list('id', 'name')
# 		)
# 	 )
