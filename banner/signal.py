from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import Banner

@receiver(models.signals.pre_delete, sender=Banner)
def remove_file_from_s3(sender, instance, using):
    instance.content.delete(save=False)



