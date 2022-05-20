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
    """
        It takes a youtube link, uses youtube-dl to get the video's metadata, and returns the metadata in a
        JSON response
        
        :param request: The request object is an HttpRequest object. It contains metadata about the request,
        such as the HTTP method
        :return: A JsonResponse object is being returned.
    """
    if request.method == 'POST':
        ydl_opts = {}
        try:
            # Using the youtube-dl library to get the metadata of the video.
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                meta = ydl.extract_info(
                    request.POST['yt_link'], download=False)
            video_audio_streams = []
           # Getting the metadata of the video.
            for m in meta['formats']:
                file_size = m['filesize']
                if file_size is not None:
                    file_size = f'{round(int(file_size) / 1000000, 2)} mb'

                resolution = 'Audio'
                if m['height'] is not None:
                    resolution = f"{m['height']}x{m['width']}"
                video_audio_streams.append({
                    'resolution': resolution,
                    'extension': m['ext'],
                    'file_size': file_size,
                    'video_url': m['url']
                })
            video_audio_streams = video_audio_streams[::-1]
          # A dictionary that contains the metadata of the video.
            context = {
                'title': meta.get('title', None),
                'streams': video_audio_streams,
                'description': meta.get('description'),
                'likes': f'{int(meta.get("like_count", 0)):,}',
                'dislikes': f'{int(meta.get("dislike_count", 0)):,}',
                'thumb': meta.get('thumbnails')[3]['url'],
                'duration': round(int(meta.get('duration', 1)) / 60, 2),
                'views': f'{int(meta.get("view_count")):,}'
            }
            return JsonResponse({"success": 'Successfully get youtube data', "video_data": context}, status=200)
        except Exception as error:
            return JsonResponse({"error": error.args[0]}, status=400)

    return render(request, 'index.html')


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
                subject=request.POST['subject'],
                message=request.POST['message'],
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[request.POST['email'],]
            )
            return JsonResponse({"success":'Success! Your message has been sent to us.'}, status=200)
        except SMTPException as e:
            return JsonResponse({"error": f'There was an error sending an email{e}'}, status=400)
    return render(request, 'contact.html')



def error_404_view(request, exception):
    return render(request, '404.html')