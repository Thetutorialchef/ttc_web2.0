"""
from django.shortcuts import render
from .models import ToDoList

# Create your views here.

    def index(response, id):
        ls = ToDoList.objects.get(id=id)
        return render(response,"main/list.html",{"ls":ls})

    def home(response):
        return render(response, "main/home.html", {})
        """
# views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)

    if ls in response.user.todolist.all():

        if response.method == "POST":
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False

                    item.save()

            elif response.POST.get("newItem"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")

        return render(response, "main/list.html", {"ls": ls})

    return render(response, "main/home.html", {})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)  # adds the to do list to the current logged in user

            return HttpResponseRedirect("/%i" % t.id)

    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})


def view(response):
    return render(response, "main/view.html", {})


def about(response):
    return render(response, "main/about.html", {})


def tutorials(response):
    return render(response, "main/tutorials.html", {})


def sitemap(response):
    return render(response, "main/sitemap.html", {})


def contribute(response):
    return render(response, "main/contribute.html", {})


def policy(response):
    return render(response, "main/policy.html", {})


def contact(response):
    return render(response, "main/contact.html", {})


def disclaimer(response):
    return render(response, "main/disclaimer.html", {})

