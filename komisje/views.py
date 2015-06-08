from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from komisje.models import *
from django.utils import timezone
from django.contrib.auth import authenticate, login
from datetime import datetime, date, time

def home(request):
    woj_list = Wojewodztwo.objects.all().order_by('name')
    context = {'woj_list': woj_list}
    return render(request, 'index.html', context)

def woj(request, woj_id):
    woj = get_object_or_404(Wojewodztwo, pk=woj_id)
    pow_list = Powiat.objects.all().filter(woj=woj)
    return render(request, 'woj.html', {'woj': woj, 'pow_list': pow_list})

def powiat(request, pow_id):
    powiat = get_object_or_404(Powiat, pk=pow_id)
    woj = powiat.woj
    gm_list = Gmina.objects.all().filter(powiat=powiat)
    context = {'powiat': powiat, 'gm_list': gm_list,'woj': woj}
    return render(request, 'powiat.html', context)

def gmina(request, gm_id):
    gm = get_object_or_404(Gmina, pk=gm_id)
    okr_list = Okreg.objects.all().filter(gmina=gm)
    powiat = gm.powiat
    woj = powiat.woj
    context = {'gm': gm, 'okr_list': okr_list, 'powiat': powiat,'woj': woj}
    return render(request, 'gmina.html', context)
    
def okreg(request, okr_id):
    d = date.today()
    t = datetime.now().time()
    okr = get_object_or_404(Okreg, pk=okr_id)
    gm = okr.gmina
    powiat = gm.powiat
    woj = powiat.woj
    context = {'gm': gm, 'okr': okr, 'powiat': powiat,'woj': woj, 't':t, 'd':str(d)}
    return render(request, 'okreg.html', context)

def error(request, gm_id):
    gm = get_object_or_404(Gmina, pk=gm_id)
    okr_list = Okreg.objects.all().filter(gmina=gm)
    powiat = gm.powiat
    woj = powiat.woj
    context = {'gm': gm, 'okr_list': okr_list, 'powiat': powiat,'woj': woj}
    return render(request, 'error.html', context)

def input_error(request, gm_id):
    gm = get_object_or_404(Gmina, pk=gm_id)
    okr_list = Okreg.objects.all().filter(gmina=gm)
    powiat = gm.powiat
    woj = powiat.woj
    context = {'gm': gm, 'okr_list': okr_list, 'powiat': powiat,'woj': woj}
    return render(request, 'input_error.html', context)

def zapisz(request, okr_id):
    okr = get_object_or_404(Okreg, pk=okr_id)
    try:
        okr.karty = request.POST['karty']
        okr.wyborcy = request.POST['wyborcy']
        d = datetime.strptime(request.POST['d'], "%Y-%m-%d").date()
        t = datetime.strptime(request.POST['t'], "%H:%M:%S").time()
        dd = datetime.combine(d, t)
        if (int(okr.karty) < 0) or (int(okr.wyborcy) < 0):
            return input_error(request, okr.gmina.id)
        okr.resave(dd)
    except(ValidationError):
        return error(request, okr.gmina.id)
    return gmina(request, okr.gmina.id)
