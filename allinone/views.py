from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Team, Bike, Participant, Coach, Organizator, Competition

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

