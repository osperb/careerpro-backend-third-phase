from django.db import models
from account.models import Account
from django.utils.translation import gettext as _





class Chat(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=128)
    is_group =  models.BooleanField(default=False)

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return str(self.name)

    
class ChatMember(models.Model):
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE,related_name='member'
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.account)


class Message(models.Model):
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE, related_name="messages"
    )
    sender = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="sender"
    )
    # reciever = models.ForeignKey(
    #     Account, on_delete=models.CASCADE, related_name="reciever"
    # )
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.chat.name)

    class Meta:
        db_table = 'message'
        verbose_name = ('Message')
        verbose_name_plural = _('Messages')
        ordering = ('-timestamp',)


# class Message(models.Model):
#     sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sender')
#     receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='receiver')
#     message = models.CharField(max_length=1200)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     is_read = models.BooleanField(default=False)

#     class Meta:
#         db_table = 'message'
#         verbose_name = ('Message')
#         verbose_name_plural = _('Messages')
#         ordering = ('-timestamp',)


#     def __str__(self):
#         return str(self.sender.full_name)
        
