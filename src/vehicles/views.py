from django.shortcuts import render, render_to_response, RequestContext
# import the custom context processor
from vehicles.context_processor import global_context_processor

from vehicles.models import Vehicle, Category

def home_page(request):    
    return render_to_response("home_page.html",
                              locals(), # gives access to local variables
                              context_instance=RequestContext(request, processors=[global_context_processor]))
