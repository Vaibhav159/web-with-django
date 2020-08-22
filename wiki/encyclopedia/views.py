from markdown2 import Markdown
from django.shortcuts import redirect, render
from . import util
from .forms import NewEntryForm
from django import forms

from random import choice


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def showPage(request, name):
    markdown = Markdown()
    content = util.get_entry(name)
    if content:
        return render(request, "encyclopedia/content.html", {
            "content": markdown.convert(content),
            "Entry": name

        })
    else:
        return render(request, "encyclopedia/entry-not-found.html", {
            "Entry": name
        })


def randomPage(request):
    pages = util.list_entries()
    return redirect("showPage", name=choice(pages))


def searchTopic(request):
    topic = request.GET['q']
    allTopics = util.list_entries()
    if topic in allTopics:
        return redirect("showPage", name=topic)
    else:
        matches = []

        for page in allTopics:
            if topic in page:
                matches.append(page)

        return render(request, "encyclopedia/search.html", {
            "matches": matches,
            "topic": topic
        })


def newPage(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            if (form.cleaned_data['edit'] is True) or (util.get_entry(title) == "None"):
                util.save_entry(title, content)
                return redirect("showPage", name=title)
            else:
                print("gello")
                return render(request, "encyclopedia/new-entry.html", {
                    "form": form,
                    "title": title,
                    "entryExist": True
                })
        else:
            print("pello")
            return render(request, "encyclopedia/new-entry.html", {
                "form": form,
                "entryExist": False,
            })

    else:
        return render(request, "encyclopedia/new-entry.html", {
            "form": NewEntryForm(),
            "entryExist": False
        })


def editPage(request, name):
    entry = util.get_entry(name)
    if entry:
        form = NewEntryForm()
        form.fields["title"].initial = name
        form.fields["title"].widget = forms.HiddenInput()
        form.fields["content"].initial = entry
        form.fields["edit"].initial = True
        return render(request, "encyclopedia/new-entry.html", {
            "form": form,
            "edit": form.fields["edit"].initial,
            "title": form.fields["title"].initial
        })
    else:
        return render(request, "encyclopedia/entry-not-found.html", {
            "Entry": name
        })
