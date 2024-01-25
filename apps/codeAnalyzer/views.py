import json
import codecs

from django.shortcuts import render

from Analizator.analyze_bandit import unzip_directory, analyze_code
from Analizator.pentest import attack
from .models import *


# Create your views here.


def index(request):
    return render(request, 'index.html')

def pentest_attack(request):

    if request.method == 'POST':
        url = request.POST.get('url')
        attack(url)

    return render(request, 'entered.html')

def enter(request):
    return render(request, 'entered.html')

def analyzer(request):
    print(request.GET.get('project'))
    print(request.GET.get('error'))
    if request.method == 'POST':
        try:
            archive = Archive.objects.filter(name=request.FILES['source'].name.rsplit('.', 1)[0]).first()

            if archive is None:
                archive = Archive()
                archive.name = request.FILES['source'].name.rsplit('.', 1)[0]
                archive.file = request.FILES['source']
                archive.save()
                archive = Archive.objects.last()
                print("here")
                unzip_directory(archive.file.path)
                analyze_code(archive)
        except Exception as e:
            pass
    if request.GET.get('project') != None:
        archive = request.GET.get('project')

    try:

        first = Problems.objects.filter(project=archive).first()
        problems = Problems.objects.filter(project=archive, level=first.level).all()
    except Exception as e:
        problems = ""
        first = ""

    if request.GET.get('level') != None:
        first_l = Problems.objects.filter(project=archive, level=request.GET.get('level')).first()
        problems = Problems.objects.filter(project=archive, level=request.GET.get('level')).all()
        if first_l != None:
            first = first_l

    if request.GET.get('error') != None:
        first_l = Problems.objects.filter(project=archive, id=request.GET.get('error')).first()
        problems = Problems.objects.filter(project=archive, level=first_l.level).all()
        if first_l != None:
            first = first_l


    try:
        high = Problems.objects.filter(project=archive, level='High').count()
        medium = Problems.objects.filter(project=archive, level='Medium').count()
        info = Problems.objects.filter(project=archive, level='Low').count()
    except Exception as e:
        pass



    try:
        file_path, start, column = first.location.split(':')
        file = codecs.open(file_path, "r", "utf-8")
        data = file.read()
        file.close()
    except Exception as e:
        context = {
            'problems': problems,
            'first': first,
            'data': json.dumps("data"),
            'start': json.dumps("start"),
            'column': json.dumps("column"),
            'high': high,
            'medium': medium,
            'info': info,

        }
        return render(request, 'analyze.html', context)
    context = {
        'problems': problems,
        'first': first,
        'data': json.dumps(data),
        'start': json.dumps(start),
        'column': json.dumps(column),
        'high': high,
        'medium': medium,
        'info': info,
    }

    return render(request, 'analyze.html', context)


def report(request):
    return render(request, 'bandit_report.html')


def pentest(request):
    return render(request, 'pentest.html')