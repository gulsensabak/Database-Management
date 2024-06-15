from django.shortcuts import render, redirect
from django.http import HttpResponse
from tutorial_app.users.login import *
from tutorial_app.users.forms import *
from tutorial_app.users.shows import *


# Create your views here.
def index(request):
    index_text="view.index func is called"
    context={'index_text': index_text}
    return render(request, 'renders/index.html', context)

def printNumber(request, number):
    numbers=[i for i in range(number,number+5)]
    arr=[]
    for i in range(len(numbers)):
        arr.append({"index": i, "number": numbers[i]})
    return render(request, 'renders/numbers.html', {'arr': arr})
    


def listShowsManager(request, num):
    if ('username' in request.session):
        username=request.session['username']
    else:
        return redirect('../login/')
    shows=[]
    if (num==0):
        return render(request, 'tutorial_app/create_user.html') 

    elif (num==1):
        shows=returnStadimName()
    
        return render(request, 'tutorial_app/change_std_name.html',{"std_name": shows}) 
    
def listShowsJury(request, num):
    if ('username' in request.session):
        username=request.session['username']
    else:
        return redirect('../login/')
    if (num==0):
        arr=returnRatings(username)
        return render(request, 'tutorial_app/jury_view_rate.html', {"arr": arr}) 

    elif (num==1):
        context=return_unrated_sessions(username)
    
        return render(request, 'tutorial_app/jury_rate.html',{"unrated_sessions": context}) 
    
def listShowsCoach(request, num):
    if ('username' in request.session):
        username=request.session['username']
    else:
        return redirect('../login/')

    if (num==0):
        shows=returns_sessions(username)
        request.session['username']=username

        return render(request, 'tutorial_app/coach_delete.html',{"sessions": shows}) 

    elif (num==1):
        context= return_team_id(username)[0]["team_id"]
        context2=returns_sessions(username)
        return render(request, 'tutorial_app/coach_add.html',{"adding_failed": False, "team_id": context, "session_names": context2}) 

    elif (num==2):

        context=coach_return_available_session(username)
        context2=coach_return_player_names(username)
    
        return render(request, 'tutorial_app/coach_create_squad.html',{"adding_failed": False, "player_names": context2, "session_names": context}) 

    elif (num==3):
        context=return_std_name_and_counties()
    
        return render(request, 'tutorial_app/coach_view.html',{"arr1": context}) 
    
def coach_delete(request):
    if ('username' in request.session):
        username=request.session['username']
    else:
        return redirect('../login/')
    session_id=request.POST.get("session_id")
    delete_session(session_id)
    context=returns_sessions(username)
    request.session['username']=username
    return render(request, 'tutorial_app/coach_delete.html',{"sessions": context}) 

# !!!!!!!!!!!!!!!!!!
def coach_add(request):
    if ('username' in request.session):
        username=request.session['username']
    else:
        return redirect('../login/')
    session_ID=request.POST.get("session_id")
    team_id=request.POST.get("team_id")
    stadium_ID=request.POST.get("stadium_ID")
    time_slot=request.POST.get("time_slot")
    date=request.POST.get("date")
    assigned_jury_username=request.POST.get("assigned_jury_username")
    played_player_username_list=request.POST.get("played_player_username_list")


    addable=add_session(username,session_ID, team_id, stadium_ID, time_slot, date, assigned_jury_username, played_player_username_list)
    if addable[0]:
        context=returns_sessions(username)
        request.session['username']=username
        return render(request, 'tutorial_app/coach_add.html',{"adding_failed": False ,"team_id": team_id, "session_names": context, "arr1":addable[1] }) 
    else:
        context=returns_sessions(username)
        return render(request, 'tutorial_app/coach_add.html',{"adding_failed": True ,"team_id": team_id, "session_names": context, "arr1":addable[1] }) 


def coach_add_squad(request):
    if ('username' in request.session):
        username=request.session['username']
    else:
        return redirect('../login/')
    players=[]
    adding_failed=False
    player1=request.POST.get("player1")
    players.append(player1)
    player2=request.POST.get("player2")
    if player2 not in players:
        players.append(player2)
    else:
        adding_failed=True
    player3=request.POST.get("player3")
    if player3 not in players:
        players.append(player3)
    else:
        adding_failed=True
    player4=request.POST.get("player4")

    if player4 not in players:
        players.append(player4)
    else:
        adding_failed=True
    player5=request.POST.get("player5")
    if player5 not in players:
        players.append(player5)    
    else:
        adding_failed=True
    player6=request.POST.get("player6")
    if player6 not in players:
        players.append(player6)
    else:
        adding_failed=True
    session_name=request.POST.get("session_name")
    coach_add_new_squad_quer(players,session_name)

    context=coach_return_available_session(username)
    context2=coach_return_player_names(username)

    return render(request, 'tutorial_app/coach_create_squad.html',{"adding_failed": adding_failed,"player_names": context2, "session_names": context}) 

    
# !!!!!!!!!!!!!!!!!! 
def createUser(request, num):
    if (num==0):
        return render(request, 'tutorial_app/create_user_player.html') 
    elif (num==1):
        return render(request, 'tutorial_app/create_user_coach.html') 
    elif (num==2):
        return render(request, 'tutorial_app/create_user_jury.html') 
    
def createPlayer(request):
    username=request.POST.get("username")
    date_of_birth=request.POST.get("date_of_birth")
    height =request.POST.get("height")
    weight=request.POST.get("weight")
    password=request.POST.get("password")
    cannot_create=create_player(username, date_of_birth, height, weight, password)
    return render(request, 'tutorial_app/create_user.html',{"cannot_create":cannot_create})  


def createJury(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    nationality=request.POST.get("nationality")
    cannot_create=create_jury(username, nationality, password)
    return render(request, 'tutorial_app/create_user.html', {"cannot_create":cannot_create}) 


def createCoach(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    nationality=request.POST.get("nationality")
    cannot_create=create_coach(username, nationality, password)
    return render(request, 'tutorial_app/create_user.html',{"cannot_create":cannot_create} ) 


def changeStdName(request):
    old_name= request.POST.get("old_name")
    new_name=request.POST.get("new_name")
    changeStadium(old_name,new_name)
    shows=returnStadimName()
    return render(request, 'tutorial_app/change_std_name.html',{"std_name": shows}) 

def loginIndex(request):
    context={"login_fail": False, "login_form":LoginForm}
    return render(request, 'tutorial_app/login.html', context)

def login(request):
    username= request.POST.get("username")
    password=request.POST.get("password")
    loginCheck=checkCredetials(username,password)

    if loginCheck==1:
        request.session['username']=username
        return redirect('../../home_manager/')
    elif loginCheck==2:
        request.session['username']=username
        return redirect('../../home_jury/')
    elif loginCheck==3:
        request.session['username']=username
        return redirect('../../home_player/')
    elif loginCheck==4:
        request.session['username']=username
        return redirect('../../home_coach/')
    context={"login_fail": True, "login_form":LoginForm}
    return render(request, 'tutorial_app/login.html', context)

def home(request):
    name=request.session['name']
    context={"name": name}
    return render(request, 'tutorial_app/home.html', context)

def home_manager(request):
    username=request.session['username']
    context={"username": username}
    return render(request, 'tutorial_app/home_manager.html', context)

def home_jury(request):
    username=request.session['username']
    context={"username": username}
    return render(request, 'tutorial_app/home_jury.html', context)

def home_coach(request):
    username=request.session['username']
    context={"username": username}
    return render(request, 'tutorial_app/home_coach.html', context)

def home_player(request):
    username=request.session['username']
    arr1=return_player_home1(username)
    arr2=return_player_home2(username)

    context={"arr1": arr1, "arr2": arr2}
    return render(request, 'tutorial_app/home_player.html', context)

def view_rate(request):
    username=request.session['username']
    context=returnRatings(username)
    return render(request, 'tutorial_app/jury_view_rate.html', {"arr": context})

def rate(request):
    username=request.session['username']
    context=return_unrated_sessions(username)
    return render(request, 'tutorial_app/jury_rate.html', {"unrated_sessions": context})

def add_rated_session(request):
    username=request.session['username']
    Match_Session_ID=request.POST.get("Match_Session_ID")
    rate=request.POST.get("rate")

    rate_sessions(username ,Match_Session_ID ,rate)
    context=return_unrated_sessions(username)
    
    return render(request, 'tutorial_app/jury_rate.html',{"unrated_sessions": context}) 
