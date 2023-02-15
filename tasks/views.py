from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
# Create your views here.

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

def index(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []
    return render(request, 'index.html', {
        'tasks': request.session['tasks']
    })

def add(request):
    #Server side validation
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks'] += [task]
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'add.html', {
                'form': form
            })
    return render(request, 'add.html', {
                'form': NewTaskForm()
            })
        