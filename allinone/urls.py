from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="allinone/index.html"), name='edit_index'),

	url(r'^queries/$', TemplateView.as_view(template_name="allinone/queries_index.html"), name='queries_index'),

	url(r'^queries/1$', views.first_query, name='first_query'),
	url(r'^queries/2$', views.second_query, name='second_query'),

	url(r'^edit/$', TemplateView.as_view(template_name="allinone/edit_index.html"), name='edit_index'),

	url(
		r'^edit/team/$',
		views.TeamList.as_view(),
		name='team_list'
	),
	url(
		r'^edit/team/new$',
		views.TeamCreate.as_view(),
		name='team_new'
	),
	url(
		r'^edit/team/edit/(?P<pk>\d+)/$',
		views.TeamUpdate.as_view(),
		name='team_edit'
	),
	url(
		r'^edit/team/delete/(?P<pk>\d+)/$', 
		views.TeamDelete.as_view(), 
		name='team_delete'
	),


	url(
		r'^edit/bike/$',
		views.BikeList.as_view(),
		name='bike_list'
	),
	url(
		r'^edit/bike/new$',
		views.BikeCreate.as_view(),
		name='bike_new'
	),
	url(
		r'^edit/bike/edit/(?P<pk>\d+)/$',
		views.BikeUpdate.as_view(),
		name='bike_edit'
	),
	url(
		r'^edit/bike/delete/(?P<pk>\d+)/$', 
		views.BikeDelete.as_view(), 
		name='bike_delete'
	),


	url(
		r'^edit/participant/$',
		views.ParticipantList.as_view(),
		name='participant_list'
	),
	url(
		r'^edit/participant/new$',
		views.ParticipantCreate.as_view(),
		name='participant_new'
	),
	url(
		r'^edit/bike/edit/(?P<pk>\d+)/$',
		views.ParticipantUpdate.as_view(),
		name='participant_edit'
	),
	url(
		r'^edit/participant/delete/(?P<pk>\d+)/$', 
		views.ParticipantDelete.as_view(), 
		name='participant_delete'
	),


	url(r'^edit/coach/$', views.CoachList.as_view(), name='coach_list'),
	url(r'^edit/coach/new$', views.CoachCreate.as_view(), name='coach_new'),
	url(r'^edit/coach/edit/(?P<pk>\d+)$', views.CoachUpdate.as_view(), name='coach_edit'),
	url(r'^edit/coach/delete/(?P<pk>\d+)$', views.CoachDelete.as_view(), name='coach_delete'),


	url(r'^edit/organizator/$', views.OrganizatorList.as_view(), name='organizator_list'),
	url(r'^edit/organizator/new$', views.OrganizatorCreate.as_view(), name='organizator_new'),
	url(r'^edit/organizator/edit/(?P<pk>\d+)$', views.OrganizatorUpdate.as_view(), name='organizator_edit'),
	url(r'^edit/organizator/delete/(?P<pk>\d+)$', views.OrganizatorDelete.as_view(), name='organizator_delete'),

	url(r'^edit/competition/$', views.CompetitionList.as_view(), name='competition_list'),
	url(r'^edit/competition/new$', views.CompetitionCreate.as_view(), name='competition_new'),
	url(r'^edit/competition/edit/(?P<pk>\d+)$', views.CompetitionUpdate.as_view(), name='competition_edit'),
	url(r'^edit/competition/delete/(?P<pk>\d+)$', views.CompetitionDelete.as_view(), name='competition_delete'),



]
