import os

from celery import shared_task
from django.core.mail import send_mail

from newsletter.models import Issue, Subscription


@shared_task()
def send_issue(issue_id):
    issue = Issue.objects.get(pk=issue_id)
    print(issue, 'issue')
    for subscription in Subscription.objects.filter(newsletter=issue.newsletter):
        send_email.delay(subscription.subscriber.email, issue.title, issue.content)


@shared_task()
def send_email(email, title, content):
    send_mail(
        title, content, os.getenv('EMAIL_HOST_USER'), [email], fail_silently=False
    )
