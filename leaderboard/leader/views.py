from django.shortcuts import render , HttpResponse
from django.utils import timezone
from django.db.models import Sum

from .models import StudyRecord

# Create your views here.
def home (request):
    return HttpResponse( "hello world") 
def leaderboard(request):
    # Get today's and this week's data
    day_data = (
    StudyRecord.objects.filter(date__date=timezone.now().date())
    .values('user__username')
    .annotate(total_hours=Sum('hours_studied'))
    .order_by('-total_hours')
)
    week_data = (
    StudyRecord.objects.filter(date__week=timezone.now().isocalendar()[1])
    .values('user__username')
    .annotate(total_hours=Sum('hours_studied'))
    .order_by('-total_hours')
)

    return render(request, 'leaderboard.html', {'day_data': day_data, 'week_data': week_data})