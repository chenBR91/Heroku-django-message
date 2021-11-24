from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, permissions
from .models import Message
from .srializers import MessageSerializers
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class MessageViews(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializers
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


# view all messages
def message_views(request):
    data = list(Message.objects.values())
    return JsonResponse(data, safe=False)


# view all message for username or show only read messages
def message_views_specific_user(request, username):
    # convert name to id
    name = User.objects.get(username=username)
    name_id = name.id

    message = Message.objects.filter(sender=name_id)
    try:
        read = request.GET.get('read')
        is_read = eval(read.title())  # convert str to boolean
        unread_message = Message.objects.filter(sender=name_id, read=is_read)
        print(unread_message)
        unread_usr = list(unread_message.values())
        return JsonResponse(unread_usr, safe=False)

    except Exception as e:
        print(e)

    usr = list(message.values())
    return JsonResponse(usr, safe=False)


# view one message
def read_message(request):
    message_id = request.GET.get('message_id')
    get_message = Message.objects.filter(pk=message_id)
    message_content = list(get_message.values())
    return JsonResponse(message_content, safe=False)


# delete one message
@csrf_exempt
def delete_message(request):
    message_id = request.GET.get('message_id')
    get_user = Message.objects.filter(pk=message_id)
    print('delete')
    get_user.delete()
    return JsonResponse({'status': '200'})


# view all message only logged in users (is active)
def logged_message(request):
    user_logged = []
    messages = Message.objects.all()
    for message in messages:
        if message.sender.is_active:
            user_logged.append(message)

    create_json = [{
                    'id': element.id,
                    'sender': element.sender.username,
                    'receiver': element.receiver,
                    'message': element.message,
                    'subject': element.subject,
                    'read': element.read
                    } for element in user_logged]

    return JsonResponse(create_json, safe=False)

