from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="allinone/edit_index.html"), name='edit_index'),

	url(
		r'^team/$',
		views.TeamList.as_view(),
		name='team_list'
	),
	url(
		r'^team/new$',
		views.TeamCreate.as_view(),
		name='team_new'
	),
	url(
		r'^team/edit/(?P<pk>\d+)/$',
		views.TeamUpdate.as_view(),
		name='team_edit'
	),
	url(
		r'^team/delete/(?P<pk>\d+)/$', 
		views.TeamDelete.as_view(), 
		name='team_delete'
	),


	url(
		r'^bike/$',
		views.BikeList.as_view(),
		name='bike_list'
	),
	url(
		r'^bike/new$',
		views.BikeCreate.as_view(),
		name='bike_new'
	),
	url(
		r'^bike/edit/(?P<pk>\d+)/$',
		views.BikeUpdate.as_view(),
		name='bike_edit'
	),
	url(
		r'^bike/delete/(?P<pk>\d+)/$', 
		views.BikeDelete.as_view(), 
		name='bike_delete'
	),


	url(
		r'^participant/$',
		views.ParticipantList.as_view(),
		name='participant_list'
	),
	url(
		r'^participant/new$',
		views.ParticipantCreate.as_view(),
		name='participant_new'
	),
	url(
		r'^bike/edit/(?P<pk>\d+)/$',
		views.ParticipantUpdate.as_view(),
		name='participant_edit'
	),
	url(
		r'^participant/delete/(?P<pk>\d+)/$', 
		views.ParticipantDelete.as_view(), 
		name='participant_delete'
	),


	url(r'^coach/$', views.CoachList.as_view(), name='coach_list'),
	url(r'^coach/new$', views.CoachCreate.as_view(), name='coach_new'),
	url(r'^coach/edit/(?P<pk>\d+)$', views.CoachUpdate.as_view(), name='coach_edit'),
	url(r'^coach/delete/(?P<pk>\d+)$', views.CoachDelete.as_view(), name='coach_delete'),


	url(r'^organizator/$', views.OrganizatorList.as_view(), name='organizator_list'),
	url(r'^organizator/new$', views.OrganizatorCreate.as_view(), name='organizator_new'),
	url(r'^organizator/edit/(?P<pk>\d+)$', views.OrganizatorUpdate.as_view(), name='organizator_edit'),
	url(r'^organizator/delete/(?P<pk>\d+)$', views.OrganizatorDelete.as_view(), name='organizator_delete'),

	url(r'^$', views.CompetitionList.as_view(), name='competition_list'),
	url(r'^new$', views.CompetitionCreate.as_view(), name='competition_new'),
	url(r'^edit/(?P<pk>\d+)$', views.CompetitionUpdate.as_view(), name='competition_edit'),
	url(r'^delete/(?P<pk>\d+)$', views.CompetitionDelete.as_view(), name='competition_delete'),



]
