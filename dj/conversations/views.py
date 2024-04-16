from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from khejas.models import Khejas

from .forms import ConversationsMessageForm
from .models import Conversations

@login_required
def new_conversations(request, khejas_pk):
    khejas = get_object_or_404(khejas, pk=khejas_pk)

    if khejas.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversations.objects.filter(khejas=khejas).filter(members__in=[request.user.id])

    if conversations:
        return redirect('conversations:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationsMessageForm(request.POST)

        if form.is_valid():
            conversations = Conversations.objects.create(khejas=khejas)
            conversations.members.add(request.user)
            conversations.members.add(khejas.created_by)
            conversations.save()

            conversations_message = form.save(commit=False)
            conversations_message.conversations = conversations
            conversations_message.created_by = request.user
            conversations_message.save()

            return redirect('khejas:detail', pk=khejas_pk)
    else:
        form = ConversationsMessageForm()
    
    return render(request, 'conversations/new.html', {
        'form': form
    })

@login_required
def inbox(request):
    conversations = Conversations.objects.filter(members__in=[request.user.id])

    return render(request, 'conversations/inbox.html', {
        'conversations': conversations
    })

@login_required
def detail(request, pk):
    conversations = Conversations.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversationsMessageForm(request.POST)

        if form.is_valid():
            conversations_message = form.save(commit=False)
            conversations_message.conversations = conversations
            conversations_message.created_by = request.user
            conversations_message.save()

            conversations.save()

            return redirect('conversations:detail', pk=pk)
    else:
        form = ConversationsMessageForm()

    return render(request, 'conversations/detail.html', {
        'conversations': conversations,
        'form': form
    })