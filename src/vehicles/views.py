from django.shortcuts import render, render_to_response, RequestContext

from vehicles.models import Vehicle, Category

def home_page(request):
    
    # get all of the categories
    category_objects = Category.objects
    # filter categories without parents
    categories = list(category_objects.filter(category_parent=None))
    # categories with parent categories
    sub_categories = list(category_objects.exclude(category_parent=None))
    
    return render_to_response("home_page.html",
                              locals(), # gives access to local variables
                              context_instance=RequestContext(request))
