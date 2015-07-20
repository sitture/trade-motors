from django.shortcuts import render, render_to_response, RequestContext
# import the custom context processor
from vehicles.context_processor import global_context_processor

from vehicles.models import Vehicle, VehicleMake, Category
from django.core.paginator import Paginator


def home_page(request):
    return render_to_response("home_page.html", locals(),
        context_instance=RequestContext(request, processors=[global_context_processor]))


def category_page(request, slug):
    
    # check if make slug parameter is passed into the url
    vehicle_make_slug = request.GET.get('make', None)
    # get category by slug
    category = Category.objects.get_category_by_slug(slug)
    # get all the vehicles by the category and make (if provided)
    vehicles_list = None
    if vehicle_make_slug is not None:
        # get make by slug
        make = VehicleMake.objects.get_make_by_slug(vehicle_make_slug)
        vehicles_list = Vehicle.objects.get_vehicles_by_category_and_make(
            category, make)
    else:
        vehicles_list = Vehicle.objects.get_vehicles_by_category(category)
    
    # paginate vehicle list for 10 items per page
    paginator = Paginator(vehicles_list, 10)
    
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1
    
    try:
        vehicles = paginator.page(page)
    except (InvalidPage, EmptyPage):
        vehicles = paginator.page(paginator.num_pages)
        
    return render_to_response("home_page.html", locals(),
        context_instance=RequestContext(request, processors=[global_context_processor]))


def get_makes_in_category(category):

    makes_in_category = []
    # get all the vehicle objects by category
    vehicles_in_category = Vehicle.objects.get_vehicles_by_category(category=category)
    for vehicle in vehicles_in_category:
        makes_in_category.append(vehicle.make)

    # remove duplicate makes from the list
    makes_in_category = list(set(makes_in_category))
    makes_in_category = sorted(makes_in_category, key=lambda x:x.v_make)

    return makes_in_category