from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    messages_qs = Message.objects.filter(recipient=request.user)
    return render(request, "messaging/inbox.html", {"messages_list": messages_qs})

@login_required
def sent_messages(request):
    messages_qs = Message.objects.filter(sender=request.user)
    return render(request, "messaging/sent.html", {"messages_list": messages_qs})

@login_required
def message_detail(request, pk):
    message_obj = get_object_or_404(Message, pk=pk)
    if message_obj.recipient == request.user and not message_obj.is_read:
        message_obj.is_read = True
        message_obj.save()
    return render(request, "messaging/message_detail.html", {"message_obj": message_obj})

@login_required
def send_message(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            messages.success(request, "Mensaje enviado.")
            return redirect("inbox")
    else:
        form = MessageForm()
    return render(request, "messaging/message_form.html", {"form": form})
