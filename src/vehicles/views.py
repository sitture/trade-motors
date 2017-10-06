from django.shortcuts import render, get_object_or_404
# import the custom context processor
from vehicles.context_processor import global_context_processor

from vehicles.models import Vehicle, VehicleMake, Category
from settings.models import SliderImage
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from dynamic_preferences.registries import global_preferences_registry


def home_page(request):
    # instanciate a manager for global preferences
    global_preferences = global_preferences_registry.manager()
    MAX_VEHICLES_TO_SHOW = global_preferences['homepage__number_of_vehicles']
    MAX_CATEGORIES_TO_SHOW = 4

    # get list of slider objects
    sliders = SliderImage.objects.all()

    # get categories to show on homepage
    top_categories = Category.objects.get_home_page_categories()
    if top_categories:
        top_categories = top_categories[:MAX_CATEGORIES_TO_SHOW]

    # get recently added vehicles
    top_vehicles = Vehicle.objects.all().order_by(
        '-timestamp').prefetch_related('images')
    if top_vehicles:
        top_vehicles = top_vehicles[:MAX_VEHICLES_TO_SHOW]
    context = global_context_processor(locals())

    return render(request, "home_page.html", context)


def exports_page(request):
    context = global_context_processor(locals())
    return render(request, "exports_page.html", context)


def how_to_buy(request):
    context = global_context_processor(locals())
    return render(request, "how_to_buy.html", context)


def category_page(request, slug):
    # check if make slug parameter is passed into the url
    vehicle_make_slug = request.GET.get('make', None)
    # get category by slug
    category = Category.objects.get_category_by_slug(slug)
    # get all the vehicles by the category and make (if provided)
    if vehicle_make_slug:
        # get make by slug
        make = VehicleMake.objects.get_make_by_slug(vehicle_make_slug)
        if category:
            vehicles_list = Vehicle.objects.get_vehicles_by_category_and_make(
                category, make
            ).prefetch_related('images')
        else:
            vehicles_list = Vehicle.objects.get_vehicles_by_make(
                make
            ).prefetch_related('images')
    else:
        # if category is not found then get all of the vehicles
        if category:
            vehicles_list = Vehicle.objects.get_vehicles_by_category(
                category
            ).prefetch_related('images')
        else:
            vehicles_list = Vehicle.objects.all().prefetch_related('images')

    # paginate vehicle list for 10 items per page
    paginator = Paginator(vehicles_list, 16)

    try:
        page = int(request.GET.get("page", '1'))
    except ValueError:
        page = 1

    try:
        vehicles = paginator.page(page)
    except (InvalidPage, EmptyPage):
        vehicles = paginator.page(paginator.num_pages)

    makes = get_makes_in_category(category)
    context = global_context_processor(locals())

    return render(request, "categories_page.html", context)


def vehicle_detail_page(request, category_slug, vehicle_id, vehicle_slug):
    # get vehicle details by vehicle_id
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    related_vehicles = Vehicle.objects.get_vehicles_by_category(
        vehicle.category)

    return render(request, "detail_page.html", global_context_processor(locals()))


def get_makes_in_category(category):
    makes_in_category = []
    # get all the vehicle objects by category
    vehicles_in_category = Vehicle.objects.get_vehicles_by_category(
        category=category)
    for vehicle in vehicles_in_category:
        makes_in_category.append(vehicle.make)

    # remove duplicate makes from the list
    makes_in_category = list(set(makes_in_category))
    makes_in_category = sorted(makes_in_category, key=lambda x: x.v_make)

    return makes_in_category
