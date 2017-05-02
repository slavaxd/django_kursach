# coding: utf-8
from django import forms

from .models import Competition

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
# site = forms.IntegerField(
# 	widget=forms.Select(
# 		choices=Site.objects.all().values_list('id', 'name')
# 		)
# 	 ) 