from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Account, Transaction

def index(request):
    account_list = Account.objects.order_by('-create')
    context = {'account_list':account_list}
    return render(request, 'accounts/index.html', context)

def detail(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    transaction = account.transaction_set.order_by('-date','-id')
    context = {'account':account, 'transaction_list':transaction}
    return render(request, 'accounts/detail.html', context)