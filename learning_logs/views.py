from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm

# Create your views here.


def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.xhtml')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.xhtml', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)  # This is called query
    entries = topic.entry_set.order_by(
        "-date_added")  # Use shell to test first
    context = {"topic": topic, 'entries': entries}
    return render(request, 'learning_logs/topic.xhtml', context)


def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form.
    # 这个地方务必放在if block外面，否则不对劲
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.xhtml', context)


def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        # NO data submitted ; create a blank form.
        form = EntryForm()
    else:
        # Post data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.xhtml', context)
