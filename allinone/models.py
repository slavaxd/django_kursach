from __future__ import unicode_literals

from django.db.models import *

class Team(Model):
	# id = PrimaryKey(int, auto=True)
	name = CharField(max_length=255)
	# participants = Set('Participant')
	# coach = Optional('Coach', cascade_delete=True)
	def __unicode__(self):
		return self.name


class Bike(Model):
	# id = PrimaryKey(int, auto=True)
	kind_of_bike = CharField(max_length=255)
	made_by = CharField(max_length=255)
	material = CharField(max_length=255)
	weight = CharField(max_length=255)
	color = CharField(max_length=255)
	country = CharField(max_length=255)
	price = IntegerField(default=0)
	# participant = OneToOneField(Participant)
	def __unicode__(self):
		return "{0} {1}".format(self.kind_of_bike, self.material)

class Participant(Model):
	# id = PrimaryKey(int, auto=True)
	name = CharField(max_length=255)
	age = IntegerField(default=0)
	birthday = DateTimeField()
	birthplace = CharField(max_length=255)
	team = ForeignKey(Team, on_delete=CASCADE)
	bike = OneToOneField(Bike)
	# competitions = Set('Competition')
	def __unicode__(self):
		return self.name


class Coach(Model):
	# id = PrimaryKey(int, auto=True)
	name = CharField(max_length=255)
	age = IntegerField(default=0)
	birthday = DateTimeField()
	birthplace = CharField(max_length=255)
	team = OneToOneField(Team)
	def __unicode__(self):
		return self.name


class Organizator(Model):
	# id = PrimaryKey(int, auto=True)
	name = CharField(max_length=255)
	birthday = DateTimeField()
	# competitions = Set('Competition')
	def __unicode__(self):
		return self.name


class Competition(Model):
	# id = PrimaryKey(int, auto=True)
	name = CharField(max_length=255)
	country = CharField(max_length=255)
	city = CharField(max_length=255)
	organizator = ForeignKey(Organizator, on_delete=CASCADE)
	participants = ManyToManyField(Participant)

	def __unicode__(self):
		return self.name

