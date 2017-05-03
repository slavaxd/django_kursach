from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render 
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Team, Bike, Participant, Coach, Organizator, Competition
from .forms import *

def first_query(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = FirstQueryForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			p1 = int(form.cleaned_data['p1'])
			p2 = int(form.cleaned_data['p2'])
			# comp = Competition.objects.get(pk=p2)
			res = Participant.objects.raw('SELECT "allinone_participant"."id", "allinone_participant"."name", "allinone_participant"."age", "allinone_participant"."birthday", "allinone_participant"."birthplace", "allinone_participant"."team_id", "allinone_participant"."bike_id" FROM "allinone_participant" INNER JOIN "allinone_competition_participants" ON ("allinone_participant"."id" = "allinone_competition_participants"."participant_id") WHERE ("allinone_participant"."age" <= ' + p1 + 'AND "allinone_competition_participants"."competition_id" = ' + p2 + ')')
			# Participant.objects.filter(age__lte=int(p1)).filter(competition__id=p2)

			# process the data in form.cleaned_data as required
			# return HttpResponseRedirect('/yeass/')
			return render(request, 'allinone/queryres/1.html', {'res': res})
	# if a GET (or any other method) we'll create a blank form
	else:
		form = FirstQueryForm()

	return render(request, 'allinone/queries/common.html', {'form': form})

def second_query(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = SecondQueryForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			p1 = form.cleaned_data['p1']
			p2 = int(form.cleaned_data['p2'])
			# comp = Competition.objects.get(pk=p2)
			res = Team.objects.filter(name__startswith=p1).filter(participant_count__gte=p2)

			# process the data in form.cleaned_data as required
			# return HttpResponseRedirect('/yeass/')
			return render(request, 'allinone/queryres/2.html', {'res': res})
	# if a GET (or any other method) we'll create a blank form
	else:
		form = SecondQueryForm()

	return render(request, 'allinone/queries/common.html', {'form': form})

def third_query(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ThirdQueryForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			p1 = form.cleaned_data['p1']
			p2 = int(form.cleaned_data['p2'])
			# comp = Competition.objects.get(pk=p2)
			res = Competition.objects.filter(name=p1).filter(participant_count__lte=p2)

			# process the data in form.cleaned_data as required
			# return HttpResponseRedirect('/yeass/')
			return render(request, 'allinone/queryres/3.html', {'res': res})
	# if a GET (or any other method) we'll create a blank form
	else:
		form = ThirdQueryForm()

	return render(request, 'allinone/queries/common.html', {'form': form})

def fourth_query(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = FourthQueryForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			p1 = form.cleaned_data['p1']
			p2 = form.cleaned_data['p2']
			# comp = Competition.objects.get(pk=p2)
			res = Organizator.objects.filter(name=p1).filter(participant_coudnt__gte=p2)

			# process the data in form.cleaned_data as required
			# return HttpResponseRedirect('/yeass/')
			return render(request, 'allinone/queryres/4.html', {'res': res})
	# if a GET (or any other method) we'll create a blank form
	else:
		form = FourthQueryForm()

	return render(request, 'allinone/queries/common.html', {'form': form})

def fifth_query(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = FifthQueryForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			p1 = form.cleaned_data['p1']
			p2 = int(form.cleaned_data['p2'])
			# comp = Competition.objects.get(pk=p2)
			res = Team.objects.filter(name__startswith=p1).filter(participant_count__gte=p2)

			# process the data in form.cleaned_data as required
			# return HttpResponseRedirect('/yeass/')
			return render(request, 'allinone/queryres/5.html', {'res': res})
	# if a GET (or any other method) we'll create a blank form
	else:
		form = FifthQueryForm()

	return render(request, 'allinone/queries/common.html', {'form': form})

def sixth_query(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = SixthQueryForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			p1 = form.cleaned_data['p1']
			p2 = int(form.cleaned_data['p2'])
			# comp = Competition.objects.get(pk=p2)
			res = Team.objects.filter(name__startswith=p1).filter(participant_count__gte=p2)

			# process the data in form.cleaned_data as required
			# return HttpResponseRedirect('/yeass/')
			return render(request, 'allinone/queryres/6.html', {'res': res})
	# if a GET (or any other method) we'll create a blank form
	else:
		form = SixthQueryForm()

	return render(request, 'allinone/queries/common.html', {'form': form})

def seventh_query(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = SeventhQueryForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			p1 = form.cleaned_data['p1']
			p2 = int(form.cleaned_data['p2'])
			# comp = Competition.objects.get(pk=p2)
			res = Team.objects.filter(name__startswith=p1).filter(participant_count__gte=p2)

			# process the data in form.cleaned_data as required
			# return HttpResponseRedirect('/yeass/')
			return render(request, 'allinone/queryres/7.html', {'res': res})
	# if a GET (or any other method) we'll create a blank form
	else:
		form = SeventhQueryForm()

	return render(request, 'allinone/queries/common.html', {'form': form})

def eighth_query(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = EighthQueryForm(request.POST)
		# check whether it's valid:
		if form.is_valid():
			p1 = form.cleaned_data['p1']
			p2 = int(form.cleaned_data['p2'])
			# comp = Competition.objects.get(pk=p2)
			res = Team.objects.filter(name__startswith=p1).filter(participant_count__gte=p2)

			# process the data in form.cleaned_data as required
			# return HttpResponseRedirect('/yeass/')
			return render(request, 'allinone/queryres/8.html', {'res': res})
	# if a GET (or any other method) we'll create a blank form
	else:
		form = EighthQueryForm()

	return render(request, 'allinone/queries/common.html', {'form': form})


class TeamList(ListView):
	model = Team
class TeamCreate(CreateView):
	model = Team
	success_url = reverse_lazy('team_list')
	fields = ['name']
class TeamUpdate(UpdateView):
	model = Team
	success_url = reverse_lazy('team_list')
	fields = ['name']
class TeamDelete(DeleteView):
	model = Team
	success_url = reverse_lazy('team_list')


class BikeList(ListView):
	model = Bike
class BikeCreate(CreateView):
	model = Bike
	success_url = reverse_lazy('bike_list')
	fields = ['kind_of_bike', 'made_by', 'material', 'weight', 'color', 'country', 'price']
class BikeUpdate(UpdateView):
	model = Bike
	success_url = reverse_lazy('bike_list')
	fields = ['kind_of_bike', 'made_by', 'material', 'weight', 'color', 'country', 'price']
class BikeDelete(DeleteView):
	model = Bike
	success_url = reverse_lazy('bike_list')


class ParticipantList(ListView):
	model = Participant
class ParticipantCreate(CreateView):
	model = Participant
	success_url = reverse_lazy('participant_list')
	fields = ['name', 'age', 'birthday', 'birthplace', 'team', 'bike']
class ParticipantUpdate(UpdateView):
	model = Participant
	success_url = reverse_lazy('participant_list')
	fields = ['name', 'age', 'birthday', 'birthplace', 'team', 'bike']
class ParticipantDelete(DeleteView):
	model = Participant
	success_url = reverse_lazy('participant_list')


class CoachList(ListView):
	model = Coach
class CoachCreate(CreateView):
	model = Coach
	success_url = reverse_lazy('coach_list')
	fields = ['name', 'age', 'birthday', 'birthplace', 'team']
class CoachUpdate(UpdateView):
	model = Coach
	success_url = reverse_lazy('coach_list')
	fields = ['name', 'age', 'birthday', 'birthplace', 'team']
class CoachDelete(DeleteView):
	model = Coach
	success_url = reverse_lazy('coach_list')


class OrganizatorList(ListView):
	model = Organizator
class OrganizatorCreate(CreateView):
	model = Organizator
	success_url = reverse_lazy('organizator_list')
	fields = ['name', 'birthday']
class OrganizatorUpdate(UpdateView):
	model = Organizator
	success_url = reverse_lazy('organizator_list')
	fields = ['name', 'birthday']
class OrganizatorDelete(DeleteView):
	model = Organizator
	success_url = reverse_lazy('organizator_list')


class CompetitionList(ListView):
	model = Competition
class CompetitionCreate(CreateView):
	model = Competition
	success_url = reverse_lazy('competition_list')
	fields = ['country', 'city', 'organizator', 'participants']
class CompetitionUpdate(UpdateView):
	model = Competition
	success_url = reverse_lazy('competition_list')
	fields = ['country', 'city', 'organizator', 'participants']
class CompetitionDelete(DeleteView):
	model = Competition
	success_url = reverse_lazy('competition_list')

