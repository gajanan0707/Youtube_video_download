from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import youtube_dl
from django.core.mail import send_mail
from django.conf import settings
from smtplib import SMTPException


# Create your views here.
@csrf_exempt
def home(request):
    return render(request, "index.html")


@csrf_exempt
def contact_us(request):
    """
    It renders the contact.html template

    :param request: The request object is an HttpRequest object. It contains metadata about the request,
    such as the HTTP method, the URL, the headers, and the body
    :return: The contact.html page is being returned.
    """
    if request.POST:
        try:
            send_mail(
                subject=request.POST["subject"],
                message=request.POST["message"],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[
                    request.POST["email"],
                ],
            )
            return JsonResponse(
                {"success": "Success! Your message has been sent to us."}, status=200
            )
        except SMTPException as e:
            return JsonResponse(
                {"error": f"There was an error sending an email{e}"}, status=400
            )
    return render(request, "contact.html")


def error_404_view(request, exception):
    return render(request, "404.html")
