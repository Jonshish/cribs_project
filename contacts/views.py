  
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    """ Sends apartment inquiry to admin dashboard """
    if request.method == 'POST':
        rental_id = request.POST['rental_id']
        rental = request.POST['rental']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

    #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(rental_id=rental_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this apartment')
                return redirect('/rentals/'+rental_id)

    contact = Contact(rental=rental, rental_id=rental_id, name=name, email=email, phone=phone, message=message, user_id=user_id, )

    contact.save()

    # Send email
    # send_mail('Apartment Inquiry', 'There has been an inquiry for ' + rental + '. Sign into the admin panel for more info', 'jonwebsitetest1993@gmail.com', [realtor_email,], fail_silently=False)

    messages.success(request, 'Your request has been submitted, an agent will get back to you soon')
    return redirect('/rentals/'+rental_id)