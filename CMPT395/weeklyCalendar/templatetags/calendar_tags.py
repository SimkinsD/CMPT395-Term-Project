from django import template

register = template.Library()

@register.simple_tag
def format_time(time):
  return time.__format__("%H:%M")

@register.simple_tag
def format_date(date):
  return date.__format__("%Y-%m-%d")

@register.simple_tag
def comp(str1, str2):
  if str1 == str2:
    return "true"
  else:
    return "false"

@register.simple_tag
def user_match(volunteer, view):
  if volunteer.family.user == view.request.user:
    return True
  else:
    return False