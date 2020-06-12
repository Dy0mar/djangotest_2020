# -*- coding: utf-8 -*-
from django.urls import reverse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .models import Transactions, Statuses


class TransactionListView(ListView):
    model = Transactions
    paginate_by = 5
    context_object_name = 't_list'
    template_name = 'transactions/transaction_list.html'

    def get_queryset(self):
        return self.model.objects.order_by('-created_at').select_related('status')


class TransactionCreate(CreateView):
    model = Transactions
    template_name = 'transactions/transaction_form.html'
    fields = ['transaction_id', 'purpose', 'status']

    def get_success_url(self):
        return reverse('transaction-list')


class TransactionUpdate(UpdateView):
    model = Transactions
    template_name = 'transactions/transaction_form.html'
    fields = ['transaction_id', 'purpose', 'status']

    def get_success_url(self):
        return reverse('transaction-list')


class TransactionDetail(DetailView):
    model = Transactions
    template_name = 'transactions/transaction_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TransactionDelete(DeleteView):
    model = Transactions
    template_name = 'inc/object_confirm_delete.html'

    def get_success_url(self):
        return reverse('transaction-list')


transaction_list_view = TransactionListView.as_view()
transaction_create = TransactionCreate.as_view()
transaction_update = TransactionUpdate.as_view()
transaction_detail = TransactionDetail.as_view()
transaction_delete = TransactionDelete.as_view()


class StatusListView(ListView):
    model = Statuses
    paginate_by = 5
    context_object_name = 's_list'
    template_name = 'statuses/status_list.html'


class StatusCreate(CreateView):
    model = Statuses
    template_name = 'statuses/status_form.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('status-list')


class StatusUpdate(UpdateView):
    model = Statuses
    template_name = 'statuses/status_form.html'
    fields = ['name']

    def get_success_url(self):
        return reverse('status-list')


class StatusDetail(DetailView):
    model = Statuses
    template_name = 'statuses/status_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StatusDelete(DeleteView):
    model = Statuses
    template_name = 'inc/object_confirm_delete.html'

    def get_success_url(self):
        return reverse('status-list')


status_list_view = StatusListView.as_view()
status_create = StatusCreate.as_view()
status_detail = StatusDetail.as_view()
status_update = StatusUpdate.as_view()
status_delete = StatusDelete.as_view()

