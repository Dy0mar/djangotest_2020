# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse


class Statuses(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('status-detail', kwargs={'pk': self.pk})

    def get_date_format(self):
        return "%Y-%m-%d-%H:%M:%S"

    @property
    def created(self):
        return f'{self.created_at.strftime(self.get_date_format())}'

    @property
    def updated(self):
        return f'{self.updated_at.strftime(self.get_date_format())}'

    class Meta:
        ordering = ['-id']


class Transactions(models.Model):
    transaction_id = models.CharField(max_length=255, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    purpose = models.CharField(max_length=255)
    status = models.ForeignKey(
        Statuses, on_delete=models.CASCADE, related_name='transactions',
        blank=True, null=True
    )

    def __str__(self):
        return '<Transaction: {}... Status: {}>'.format(self.transaction_id, self.status)

    def get_absolute_url(self):
        return reverse('transaction-detail', kwargs={'pk': self.pk})

    def get_date_format(self):
        return "%Y-%m-%d-%H:%M:%S"

    @property
    def created(self):
        return f'{self.created_at.strftime(self.get_date_format())}'

    @property
    def updated(self):
        return f'{self.updated_at.strftime(self.get_date_format())}'

    class Meta:
        ordering = ['-id']
