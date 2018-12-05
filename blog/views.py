from django.http import HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from .forms import RequestForm
from .forms import RegRequestForm
from .forms import AgreementForm
from .forms import RegRequestForm
from .models import Agreement
from .models import Request
from .models import RegRequest
from .models import RegAgreement

def Agreement_list(request):
    agr = Agreement.objects.order_by('id')
    return render(request, 'Agreement.html', {'agr': agr})

def Request_list(request):
    req = Request.objects.order_by('id')
    return render(request, 'Request.html', {'req': req})

def RegRequest_list(request):
    regreq = RegRequest.objects.order_by('id')
    return render(request, 'RegRequest.html', {'regreq': regreq})

def RegAgreement_list(request):
    regagr = RegAgreement.objects.order_by('id')
    return render(request, 'RegAgreement.html', {'regagr': regagr})

def Request_detail(request, pk):
    req = get_object_or_404(Request, pk=pk)
    return render(request, 'blog/Request_detail.html', {'Request': req})

def Agreement_detail(request, pk):
    agr = get_object_or_404(Agreement, pk=pk)
    return render(request, 'blog/Agreement_detail.html', {'Agreement': agr})

def RegRequest_detail(request, pk):
    regreq = get_object_or_404(RegRequest, pk=pk)
    return render(request, 'blog/RegRequest_detail.html', {'RegRequest': regreq})

def RegAgreement_detail(request, pk):
    regagr = get_object_or_404(RegAgreement, pk=pk)
    return render(request, 'blog/RegAgreement_detail.html', {'RegAgreement': regagr})

def Agreement_new(request):
    if request.method == "POST":
        form = AgreementForm(request.POST)
        if form.is_valid():
            Agreement = form.save(commit=False)
            Agreement.author = request.user
            Agreement.published_date = timezone.now()
            Agreement.save()
            return redirect('Agreement_detail', pk=Agreement.pk)
    else:
        form = AgreementForm()
    return render(request, 'blog/Agreement_edit.html', {'Agreement': form})

def Agreement_edit(request, pk):
    agr = get_object_or_404(Agreement, pk=pk)
    if request.method == "POST":
        form = AgreementForm(request.POST, instance=agr)
        if form.is_valid():
            agr = form.save(commit=False)
            agr.author = request.user
            agr.published_date = timezone.now()
            agr.save()
            return redirect('Agreement_detail', pk=Agreement.pk)
    else:
        form = AgreementForm(instance=agr)
    return render(request, 'blog/Agreement_edit.html', {'Agreement': form})

def Request_new(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            Request = form.save(commit=False)
            Request.author = request.user
            Request.save()
            return redirect('Request_detail', pk=Request.pk)
    else:
        form = RequestForm()
    return render(request, 'blog/Request_edit.html', {'Request': form})

def Request_edit(request, pk):
    req = get_object_or_404(Request, pk=pk)
    if request.method == "POST":
        form = RequestForm(request.POST, instance=req)
        if form.is_valid():
            req = form.save(commit=False)
            req.author = request.user
            req.save()
            return redirect('Request_detail', pk=Request.pk)
    else:
        form = RequestForm(instance=req)
    return render(request, 'blog/Request_edit.html', {'Request': form})
def search_form(request):
    return render_to_response('Search_Form.html')

def search(request):
    if 'f' in request.GET and request.GET['f']:
        f = request.GET['f']
        requests = Request.objects.filter(id__icontains=f)
        return render_to_response('search_requests.html',
            {'requests': requests, 'query': f})
    else:
        return render_to_response('Search_Form.html', {'error': True})

    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        Agreement = Agreement.objects.filter(id__icontains=q)
        return render_to_response('search_agr.html',
            {'replies': agreement, 'query': q})
    else:
        return render_to_response('Search_Form.html', {'error': True})
