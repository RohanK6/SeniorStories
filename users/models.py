from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django.dispatch import receiver
import os

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
	
	def __str__(self):
		return f'{self.user.username} Profile'
		
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		
		img = Image.open(self.image.path)
		
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)

@receiver(models.signals.pre_save, sender=Image)
def auto_delete_file_on_change(sender, instance, **kwargs):
	
	#Deletes old file from filesystem when corresponding MediaFile object is updated with new file.
	
	if not instance.pk:
		return False

	try:
		old_file = sender.objects.get(pk=instance.pk).file
	except sender.DoesNotExist:
		return False

	new_file = instance.file
	if not old_file == new_file:
		if os.path.isfile(old_file.path):
			os.remove(old_file.path)