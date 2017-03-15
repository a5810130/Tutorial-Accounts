from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from datetime import datetime

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

def add_account(request):
    try:
        account_name = request.POST['account_name']
        if not account_name.strip():
            raise 
    except :
        return HttpResponseRedirect(reverse('accounts:index',))
    else:
        a = Account(name=account_name, create=timezone.now())
        a.save()
        return HttpResponseRedirect(reverse('accounts:index',))
    
def add_transaction(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    try:
        date_str = request.POST['date']
        description = request.POST['description']
        actionType = request.POST['type']
        value = request.POST['value']
        if (not date_str.strip() or not description.strip()
        or not value.strip()):
            raise 
    except :
        return HttpResponseRedirect(reverse('accounts:detail', args=(account_id)))
    date = datetime.strptime(date_str,"%m/%d/%Y")
    account.transaction_set.create( date=date, actionType=actionType,
                            description=description,
                            value=value)
    account.save()
    return HttpResponseRedirect(reverse('accounts:detail', args=(account_id)))