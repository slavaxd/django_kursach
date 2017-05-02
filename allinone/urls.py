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
]
