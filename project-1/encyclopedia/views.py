from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

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
