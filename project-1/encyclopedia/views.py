from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewWikiForm(forms.Form):
  title = forms.CharField(label="Title")
  content = forms.CharField(widget=forms.Textarea)

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, entry):
    if util.get_entry(entry):
        return render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry(entry),
            "title": entry.capitalize()
        })
    else:
        return render(request, "encyclopedia/no-entry.html")

def search(request):
    if request.method == "POST":
        query = request.POST["q"]
        if util.get_entry(query):
            return HttpResponseRedirect(reverse("encyclopedia:entry", args=(query,)))
        
        entries = util.list_entries()
        filtered_entries = []
        for entry in entries:
            if query.upper() in entry.upper():
                filtered_entries.append(entry)
        
        return render(request, "encyclopedia/search.html", {
            "entries": filtered_entries
        })
        
    return render(request, "encyclopedia/search.html", {
        "entries": False
    })


def new(request):
    if request.method == "POST":
        form = NewWikiForm(request.POST)
        if form.is_valid():
            entry_title = form.cleaned_data["title"]
            entry_content = form.cleaned_data["content"]
            util.save_entry(entry_title, entry_content)
            return HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            return render(request, 'encyclopedia/new.html', {
                "form": form
            })
      
    return render(request, "encyclopedia/new.html", {
    "form": NewWikiForm
  })