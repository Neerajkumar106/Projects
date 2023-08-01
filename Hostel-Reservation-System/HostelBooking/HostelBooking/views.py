from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
# from .forms import userForm
from Tables.models import FLOOR, ROOM, REQ_ROOM

import datetime


def Home(request):
    data = {
        'title': 'Booking Hostel'
    }
    return render(request, "HOME.html", data)


def Booking(request):
    numberof_room = ROOM.objects.filter(room_status=True).count()
    data= {'numberof_room': numberof_room}
    return render(request, 'BOOKING.html',data)


def Floor(request):
    floor = FLOOR.objects.all()
    data = {'floor': floor}
    return render(request, 'FLOOR.html', data)


def Room(request, floor_id):
    numberof_room = ROOM.objects.filter(room_status=True).count()
    room = ROOM.objects.filter(floor_id=floor_id)
    data = {'room': room,'numberof_room': numberof_room}
    return render(request, 'ROOM.html', data)


def Apply(request):
    if request.user.is_authenticated:
        user = request.user 
        if request.method == 'POST':
            room_id = request.POST['room_id']
        room= ROOM.objects.get(room_id=room_id)
        REQ_ROOM(user=user,room=room).save()
        return render(request, 'APPLY.html')
    return render(request, "LOGIN.html")


def changePassword(request):
    return render(request, "changePassword.html")


def Popup(request):
    return render(request, "popup.html")


def Login(request):
    if request.method == 'POST':
        loginusername = request.POST['email']
        loginpassword = request.POST['password']
        user = auth.authenticate(
            username=loginusername, password=loginpassword)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully loged in")
            return redirect('home')
        else:
            messages.warning(request, "Username or password is wrong. Please try again")
            return redirect('login')
    return render(request, 'LOGIN.html')


def Register(request):
    if request.method == "POST":
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already taken. Please try another email.")
            return redirect('register')
        else:
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, username=email, email=email, password=password)
            user.save()
            messages.success(request, "You have Successfully Registered.")
            return redirect('login')
    return render(request, 'REGISTER.html')


def logout(request):
    auth.logout(request)
    messages.success(request, "Successfully loged out")
    return redirect('home')

































def addRoom(request):
    return render(request, "AddRoom.html")


def viewRoom(request):
    return render(request, "view_Room.html")


def removeStudent(request):
    return render(request, "Remove_Student.html")


# def otp(request):
#    try:
#        # Display the OTP verification form
#        otp = random.randint(100000, 999999)
#        account_sid = 'YOUR_ACCOUNT_SID'
#        auth_token = 'YOUR_AUTH_TOKEN'
#
# Create a Twilio client with your account SID and auth token
#        client = Client(account_sid, auth_token)
#
# The mobile number to send the OTP to (format: +1234567890)
#        to_number = '+1234567890'
#
# The message to send (include the OTP)
#        message = f'Your OTP is: {otp}'
#
# Send the message using the Twilio API
#        client.messages.create(to=to_number, from_='YOUR_TWILIO_PHONE_NUMBER', body=message)
#        if request.method == 'POST':
#            submitted_otp = request.POST.get('otp')
#
#        if submitted_otp == otp:
#            # OTP is correct, do something
#            return render(request, 'my_template.html')
#        else:
#            # OTP is incorrect, display an error message
#            return render(request, 'my_template.html')
#    except:
#        else:
#            # Display the OTP verification form
#            return render(request, 'my_template.html')
# return render(request, 'my_template.html', {'otp': otp})
#
# def verify(request):
 #   if request.method == 'POST':
 #       submitted_otp = request.POST.get('otp')
#
 #       if submitted_otp == otp:
 #           # OTP is correct, do something
 #       else:
 #           # OTP is incorrect, display an error message
 #   else:
 #       # Display the OTP verification form
 #       return render(request, 'otp.html')
# def calculator(request):
#    c=''
#    try:
#        if request.method=="POST":
#            n1=eval(request.POST.get('num1'))
#            n2=eval(request.POST.get('num2'))
#            opr=request.POST.get('opr')
#            if opr =="+":
#                c=n1+n2
#            elif opr=="-":
#                c=n1-n2
#            elif opr =="*":
#                c=n1*n2
#            elif opr=="/":
#                c=n1/n2
#    except:
#        c="Invalid opr......."
#    print(c)
#    return render(request,"calculator.html",{'c':c})
