# Context processors
from settings.models import Social, ContactDetail
from vehicles.models import Category
from dynamic_preferences import global_preferences_registry


def global_context_processor(request):
    # instanciate a manager for global preferences
    global_preferences = global_preferences_registry.manager()
    default_email = global_preferences.get('general__default_email', None)
    live_chat = global_preferences.get('general__live_chat', False)
    # get all the social service providers
    social_providers = list(Social.objects.all())
    # get all parent categories with sub categories
    all_categories = Category.objects.get_categories_with_sub_categories()
    # get latest contact details
    contact_details = ContactDetail.objects.get_latest_contact_details()

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
