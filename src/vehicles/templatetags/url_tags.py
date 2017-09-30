from django import template
register = template.Library()


@register.simple_tag
def add_to_query_string(request, **kwargs):
    """
    Lets you append a query string to url.

    If the querystring argument is already present it will be replaced
    otherwise it will be appended to the current querystring.

    template uses
    <a href="{% add_to_query_string request a=5 b=6 %}">
    <a href="{% url 'view_name' %}{% add_to_query_string request a=5 b=6 %}">

    """
    updated = request.GET.copy()
    for k, v in kwargs.iteritems():
        updated[k] = v

    return '?' + updated.urlencode()
