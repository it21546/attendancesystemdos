from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

#!!!!!!!!!!!!
#WE MADE SIGNALS.PY SO THAT EVERY TIME A USER IS CREATED,
#HIS PROFILE IS ALSO CREATED WITH HIM
#!!!!!!!!!!!!
#IMPORTANT ---> HAS TO BE IMPORTED IN users/apps.py

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()
