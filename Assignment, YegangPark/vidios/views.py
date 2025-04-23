from django.shortcuts import render
from .models import Lecture, Topic
from datetime import date
from dateutil.relativedelta import relativedelta
from django.db.models import Q


def index(request):
    lectures = Lecture.objects.all()
    return render(request, "vidios/index.html", {
        "lectures": lectures,
    })



def lecture_search(request):
    # 1) User request parsing
    lecturer_input = request.GET.get("lecturer", "").strip()      
    title_input    = request.GET.get("title", "").strip()         
    date_range     = request.GET.get("date_range")                
    topics_selected= request.GET.getlist("topics")                

    # 2) Combining conditions by Q object 
    q = Q()
    if lecturer_input:
        # lecturer name
        q &= Q(lecturers__name__icontains=lecturer_input)
    if title_input:
        # lecture title
        q &= Q(lecture_title__icontains=title_input)
    if date_range:
        try:
            months = int(date_range)
            cutoff = date.today() - relativedelta(months=months)
            # lectures after the cutoff
            q &= Q(lecture_date__gte=cutoff)
        except ValueError:
            pass
    if topics_selected:
        # does have at least one selected topics
        q &= Q(lecture_topics__name__in=topics_selected)

    # 3) actual query 
    lectures = Lecture.objects.filter(q).distinct()

    # 4) passes all topics of the model
    all_topics = Topic.objects.all()

    months = list(range(1, 13))

    return render(request, "vidios/query.html", {
        "lectures": lectures,
        "all_topics": all_topics,
        "months": months,
        "filter": {
            "lecturer":    lecturer_input,
            "title":       title_input,
            "date_range":  date_range,
            "topics":      topics_selected,
        }
    })