from django import template
import techblog.settings as blogsettings

register = template.Library()

"""
    Returns data from social networks defined in settings.py

    To load in the template:
    {% load social %}
    ...
    <a href="{% facebook_url %}">Link to Facebook</a>
"""

@register.simple_tag
def facebook_id():
    return blogsettings.FACEBOOK_ID

@register.simple_tag
def facebook_url():
    return blogsettings.FACEBOOK_URL

@register.simple_tag
def twitter_url():
    return blogsettings.TWITTER_URL

@register.simple_tag
def twitter_handle():
    return blogsettings.TWITTER_HANDLE

@register.simple_tag
def linkedin_url():
    return blogsettings.LINKEDIN_URL

@register.simple_tag
def google_plus_url():
    return blogsettings.GOOGLE_PLUS_URL

@register.simple_tag
def pinterest_url():
    return blogsettings.PINTEREST_URL

@register.simple_tag
def instagram_url():
    return blogsettings.INSTAGRAM_URL

@register.simple_tag
def rss_url():
    return blogsettings.RSS_URL