from django.shortcuts import render
from pf_project.models import pf_project


def index(request):
	projects = pf_project.objects.all()
	context = {
		'projects' : projects
	}
	return render(request, 'pf_index.html', context)

def detail(request, pk):
	project = pf_project.objects.get(pk=pk)
	context = {
		'project' : project
	}
	return render(request, 'pf_detail.html', context)

