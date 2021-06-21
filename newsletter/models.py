from django.db import models


# Create your models here.
class Newsletter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Issue(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='newsletter_issue')


class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    newsletters = models.ManyToManyField(Newsletter, through='Subscription')


class Subscription(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE, related_name='newsletter_subscription')
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE, related_name='newsletter_subscriber')
