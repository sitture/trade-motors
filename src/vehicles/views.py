from django.shortcuts import render, render_to_response, RequestContext

def home_page(request):
    return render_to_response("home_page.html",
                              locals(),
                              context_instance=RequestContext(request))
