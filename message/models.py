from django.db import models

# Create your models here.


class UserMessage(models.Model):
    userName = models.CharField(max_length=50)

    def __str__(self):
        return self.userName


'''
def get_name(pid):
    usr_obj = UserMessage.objects.all()
    for name in usr_obj:
        if pid == name.id:
            return str(name)
'''


class Message(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    # sender = models.ForeignKey(UserMessage, on_delete=models.CASCADE)
    # receiver = models.ForeignKey(UserMessage, related_name='receiver_message_set', on_delete=models.CASCADE)
    message = models.TextField(max_length=1000)
    subject = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        # print(self.sender.userName)
        # print(self.sender.id)
        return self.sender
