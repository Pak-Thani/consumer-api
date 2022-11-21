from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import Product

@receiver(models.signals.pre_delete, sender=Product)
def remove_file_from_s3(sender, instance, using):
    instance.content.delete(save=False)



