from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Service, Queue


# ---------------- HOME PAGE ----------------

@login_required
def home(request):

    services = Service.objects.all()

    return render(request, "home.html", {
        "services": services
    })


# ---------------- REGISTER ----------------

def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        return redirect("login")

    return render(request, "register.html")


# ---------------- LOGIN ----------------

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("home")

    return render(request, "login.html")


# ---------------- LOGOUT ----------------

def user_logout(request):

    logout(request)

    return redirect("login")


# ---------------- JOIN QUEUE ----------------

@login_required
def join_queue(request, service_id):

    service = Service.objects.get(id=service_id)

    last_token = Queue.objects.filter(service=service).count()

    token_number = last_token + 1

    wait_time = token_number * 5

    Queue.objects.create(
        user=request.user,
        service=service,
        token_number=token_number,
        status="Waiting"
    )

    return render(request, "token.html", {

        "token": token_number,
        "wait": wait_time,
        "service": service

    })


# ---------------- MY TOKEN ----------------

@login_required
def my_token(request):

    token = Queue.objects.filter(user=request.user).last()

    if token is None:
        return redirect("home")

    wait_time = token.token_number * 5

    message = "Please wait for your turn"

    if token.token_number <= 3:
        message = "Your turn will be called soon"

    return render(request, "token.html", {

        "token": token.token_number,
        "service": token.service,
        "wait": wait_time,
        "message": message

    })


# ---------------- USER DASHBOARD ----------------

@login_required
def dashboard(request):

    tokens = Queue.objects.filter(user=request.user)

    return render(request, "dashboard.html", {

        "tokens": tokens

    })


# ---------------- ADMIN DASHBOARD ----------------

@staff_member_required
def admin_dashboard(request):

    queues = Queue.objects.all().order_by("token_number")

    return render(request, "admin_dashboard.html", {

        "queues": queues

    })


# ---------------- LIVE DISPLAY BOARD ----------------

def display_board(request):

    queues = Queue.objects.filter(status="Waiting").order_by("token_number")

    now_serving = queues.first()

    next_token = None

    waiting = []

    if now_serving:

        next_list = queues[1:2]

        if next_list:
            next_token = next_list[0]

        waiting = queues[2:7]

    return render(request, "display_board.html", {

        "now_serving": now_serving,
        "next_token": next_token,
        "waiting": waiting

    })


