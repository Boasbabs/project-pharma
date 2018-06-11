from django.shortcuts import render


def results(request):
    return render(request, "frontend/search_result_page.html", context={})