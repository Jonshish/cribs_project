from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import roomContact

def roomcontact(request):
    if request.method == "POST":
        room_id = request.POST['room_id']
        room = request.POST['room']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = roomContact.objects.all().filter(room_id=room_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this room')
                return redirect('/rooms/'+room_id)

        roomcontact = roomContact(room=room, room_id=room_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        roomcontact.save()

        send_mail('Room Inquiry', 'There has been an inquiry for ' + room + '. Sign into the admin panel for more info', 'jonwebsitetest1993@gmail.com', [realtor_email,], fail_silently=False)

        messages.success(request, 'Your request has been submitted, an agent will get back to you soon')
        return redirect('/rooms/'+room_id)

