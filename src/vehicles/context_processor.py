# Context processors
from settings.models import Social
from vehicles.models import Category

# to allow these variables to available in all views.


def global_context_processor(request):
    # get all the social service providers
    social_providers = list(Social.objects.all())
    # get all parent categories with sub categories
    all_categories = Category.objects.get_categories_with_sub_categories()

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
