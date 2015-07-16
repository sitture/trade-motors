from django.shortcuts import render, render_to_response, RequestContext
# import the custom context processor
from vehicles.context_processor import global_context_processor

from vehicles.models import Vehicle, Category


def home_page(request):
    return render_to_response("home_page.html", locals(),
                              context_instance=RequestContext(
        						request, processors=[global_context_processor]))


def get_makes_in_category(category):

    makes_in_category = []
    # get all the vehicle objects by category
    vehicles_in_category = Vehicle.objects.filter(category=category)
    for vehicle in vehicles_in_category:
        makes_in_category.append(vehicle.make)

    # remove duplicate makes from the list
    makes_in_category = list(set(makes_in_category))

    return sorted(makes_in_category)
