from django.shortcuts import render

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

def search(request, results):
    return render(request, "encyclopedia/search.html")
