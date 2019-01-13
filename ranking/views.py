from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Pupper
from .utils import check_task_finished, setup_database

# Create your views here.

class LeaderboardView(generic.ListView):
    template_name = 'leaderboard.html'
    context_object_name = 'top_scoring_puppers_list'

    def get_queryset(self):
        return Pupper.objects.order_by('-score')[:5]

def authenticate_callback(request):
    return HttpResponse("authenticate")

def test(request):
    return HttpResponse(len(Pupper.objects.all()))