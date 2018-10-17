from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from .forms import EntryForm
from .models import FormModel2


def index(request):
    form_list = FormModel2.objects.all()
    context = {'form_list': form_list}
    return render(request, 'forms_app/index.html', context)

def about(request):
    return render(request, 'forms_app/about.html')

def addEntry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntryForm()
    return render(request, 'forms_app/entryFormPage.html', {'form':form})

def editEntry(request, pk):
    EntryModel = get_object_or_404(FormModel2, pk=pk)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=EntryModel)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EntryForm()
    return render(request, 'forms_app/entryFormPage.html', {'form': form})

def deleteEntry(request, pk):
    dataEntry = get_object_or_404(FormModel2, pk=pk)
    #if request == "DELETE":
    dataEntry.delete()
    return redirect('index')
