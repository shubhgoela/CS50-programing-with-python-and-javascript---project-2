from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import util
from re import search
import markdown2 as markdown
from django import forms
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def index2(request, title="error"):
    if(util.get_entry(title)):
        f = util.get_entry(title)
        return HttpResponse(render(request, "encyclopedia/displaywiki.html", {
            "title": title,
            "data":markdown.markdown(f)
        }))
    else:
        return render(request,"encyclopedia/error.html")


def search(request):
    if request.method == "POST":
        if util.get_entry(request.POST['q']):
            return HttpResponseRedirect("/wiki/"+request.POST['q'])
        else:
            list2 = []
            for i in util.list_entries():
                if request.POST['q'].lower() in i.lower():
                    list2.append(i)
            print(list2)
            if len(list2) == 0:
                return render(request,"encyclopedia/search.html",{
                    "false":True,
                    "entries":list2
            })
            else:
                return render(request,"encyclopedia/search.html",{
                    "false":False,
                    "entries":list2
            })


def CNP(request):
    if request.method == "POST":
        print(request.POST)
        flag = 0
        for i in util.list_entries():
            if request.POST['title'].lower().strip() == i.lower():
                flag = 1
                return render(request, "encyclopedia/EntryPage.html",{
                "newpage":True,
                "error":True,
                "title":request.POST['title'],
                "value":request.POST['text']
                })
        if flag == 0:
            util.save_entry(request.POST['title'],request.POST['text'])
        return HttpResponseRedirect("/")
    return render(request, "encyclopedia/EntryPage.html",{
        "newpage":True,
        "title":"",
        "value":""
    })


def editEntry(request, title):
    if request.method == "POST":
        print(request.POST)
        print(request.POST['title'])
        util.save_entry(request.POST['title'],request.POST['text']) 
        print(f"name of new file created {request.POST['title']}.md")
        return HttpResponseRedirect("/")    
    f = util.get_entry(title)  
    return render(request,"encyclopedia/EntryPage.html",{
        "newpage":False,
        "title":title,
        "value":f
    })

def rand(request):
    print(random.choice(util.list_entries()))
    return HttpResponseRedirect("/wiki/"+random.choice(util.list_entries()))


def err(request, title):
    return render(request,"encyclopedia/error.html")