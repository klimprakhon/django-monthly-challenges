from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges_list = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 mins every day!",
    "march": "Learn Django at least 20 mins every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 mins every day!",
    "june": "Learn Django at least 20 mins every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 mins every day!",
    "september": "Learn Django at least 20 mins every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 mins every day!",
    "december": None,
}

# Create your views here.


def index(request):
    # list_items = ""
    months = list(monthly_challenges_list.keys())

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href={month_path}>{capitalized_month}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"

    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_list.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_list[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month.capitalize()
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)
        raise Http404()