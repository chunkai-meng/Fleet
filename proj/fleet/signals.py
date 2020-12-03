from django.conf import settings
from django.contrib.auth.models import Group
from email_notification.models import EmailNotification, Template
from django.dispatch import receiver

from django.db.models.signals import post_save, post_delete
from .models import JobIDInfo


def send_new_request_email(instance):
    template_obj = Template.objects.get(category=Template.CHECKOUT_REQUEST)
    email_to_group = Group.objects.get(name='Fleet')
    email_dict = {
        'if_email_notify': True,
        'notification_title': 'Job Code Created',
        'notification_message': 'New Job Code Request',
        # 'email_to': 'hustmck@hotmail.com',
        'notification_to_group': email_to_group,
        'email_template': template_obj,
        'body_value1': instance.id,
        'body_value2': instance.JobAbbreviation,
        'body_value3': instance.JobName,
        'body_value4': instance.Status
    }
    email_notification = EmailNotification(**email_dict)
    email_notification.save()


@receiver([post_save], sender=JobIDInfo)
def job_code_create(sender, instance, created, update_fields, **kwargs):
    send_new_request_email(instance)
