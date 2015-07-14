# Context processors
from settings.models import Social
from vehicles.models import Category

# to allow these variables to available in all views.


def global_context_processor(request):
    # get all the social service providers
    social_providers = list(Social.objects.all())
    # get all of the categories
    category_objects = Category.objects
    # filter categories without parents
    categories = list(category_objects.filter(category_parent=None))
    # categories with parent categories
    sub_categories = list(category_objects.exclude(category_parent=None))

    all_categories = get_all_categories(categories, sub_categories)

    return locals()


def get_all_categories(categories, sub_categories):

    formatted_categories = []

    for category in categories:
        tmp = sub_temp = []
        for sub_category in sub_categories:
            if category == sub_category.category_parent:
                sub_temp.append(sub_category)
        tmp = [category, sub_temp]
        formatted_categories.append(tmp)

    return formatted_categories
