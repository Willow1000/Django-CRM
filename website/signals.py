from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from .models import User



@receiver(post_save, sender=User)
def assign_role_permissions(sender, instance, created, **kwargs):
    if created:  # Run only when a user is created
        if instance.role == 'admin':
            instance.user_permissions.add(
                Permission.objects.get(codename="add_record"),
                Permission.objects.get(codename="change_record"),
                Permission.objects.get(codename="delete_record"),
            )
        elif instance.role == 'editor':
            instance.user_permissions.add(
                Permission.objects.get(codename="add_record"),
                Permission.objects.get(codename="change_record"),
            )
        elif instance.role == 'viewer':
            instance.user_permissions.add(
                Permission.objects.get(codename="add_record"),
            )   
        instance.save()
