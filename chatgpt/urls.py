import os
import time
from django.contrib import admin
from django.urls import path
from django.http import StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def streamChat(request):
    def event_stream():
        for chunk in range(10):
            time.sleep(0.2)
            yield f"data: {chunk}\n"
    response = StreamingHttpResponse(
        streaming_content=event_stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response


urlpatterns = [
    path('admin/', admin.site.urls),
    path('completions', streamChat),
]
