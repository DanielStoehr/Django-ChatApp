from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import Chat, Message


# Create your views here.


@login_required(login_url="/login/")
def index(request):
    if request.method == "POST":
        print(request.POST["textmessage"])
        my_chat = Chat.objects.get(id=1)
        Message.objects.create(
            text=request.POST["textmessage"],
            chat=my_chat,
            author=request.user,
            receiver=request.user,
        )

    chat_messages = Message.objects.filter(chat__id=1)
    return render(request, "chat/index.html", {"messages": chat_messages})


def login_view(request):
    redirect = request.GET.get("next")
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get("username"), password=request.POST.get("password")
        )
        if user:
            login(request, user)
            return HttpResponseRedirect(request.POST.get("redirect"))
        else:
            return render(
                request,
                "chat/login.html",
                {"wrong_password": True, "redirect": redirect},
            )
    return render(request, "chat/login.html", {"redirect": redirect})


def register_view(request):
    if request.method == "POST":
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            return render(
                request,
                "chat/register.html",
                {"password_not_match": True},
            )
        username = request.POST.get("username")
        try:
            user = User.objects.create_user(username=username, password=password1)
        except:
            return render(request, "chat/register.html", {"user_exists": True})
        return render(request, "chat/register.html", {"user": user, "success": True})
    # user = authenticate(
    #     username=request.POST.get("username"), password=request.POST.get("password")
    # )
    # if user:
    #     login(request, user)
    #     return HttpResponseRedirect("/login")
    # else:
    #     return render(
    #         request,
    #         "chat/login.html",
    #         {"wrong_password": True},
    #     )
    return render(request, "chat/register.html")
