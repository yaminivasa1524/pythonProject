from django.core.mail import send_mail,BadHeaderError
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
import logging
from django.core.mail import send_mail, BadHeaderError

def home(request):
    return render(request,'home1.html')
def help(request):
    return HttpResponse("<h5>Hiii</h5>")
# Create your views here.


#def contact_view(request):
#    if request.method == 'POST':
#       name = request.POST.get('name')
#        email = request.POST.get('email')
#        subject = request.POST.get('subject')
#        message = request.POST.get('message')

        # Process form data (e.g., send an email or save to database)
#        send_mail(
#            subject,
#            message,
#            email,
#            ['yaminivasa1524@gmail.com'],  # Replace with your email
#        )
#       return JsonResponse({'message': 'Your message has been sent successfully!'})

#   return render(request, 'home1.html')


#def contact_view(request):
 #   name = request.POST['name']
  #  email = request.POST['email']
    #from_email = settings.EMAIL_HOST_USER
   # to_email = [email]
    #msg = 'Hi ' + name + ',\n' + '''Thank you for Contacting us. We will get back to you soon!'''
    #send_mail('Thanks for Contacting', msg, from_email, to_email, fail_silently=False)
    #return JsonResponse({'message': 'Your message has been sent successfully!'})



logger = logging.getLogger(__name__)


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Create the full message with user's details
        full_message = f"""
        Name: {name}
        Email: {email}
        Subject: {subject}

        Message:
        {message}
        """

        try:
            # Send email to site admin with sender details
            send_mail(
                subject=f"Contact Form Submission: {subject}",
                message=full_message,
                from_email='yaminivasa1524@gmail.com',  # Replace with your email
                recipient_list=['yaminivasa1524@gmail.com'],  # Replace with your email
                fail_silently=False,
            )

            # Send confirmation email to the sender
            confirmation_message = f"Dear {name},\n\nThank you for contacting us. We have received your message and will get back to you shortly.\n\nBest regards,\nYour Team"
            send_mail(
                subject='Thank you for contacting us',
                message=confirmation_message,
                from_email='yaminivasa1524@gmail.com',  # Replace with your email
                recipient_list=[email],  # Sender's email
                fail_silently=False,
            )

            return JsonResponse({'message': 'Your message has been sent successfully!'})
        except BadHeaderError:
            return JsonResponse({'message': 'Invalid header found.'}, status=400)
        except SMTPException as e:
            logger.error(f"Error sending email: {e}")
            return JsonResponse({'message': 'There was an error sending your email. Please try again later.'},
                                status=500)

    return render(request, 'contact.html')