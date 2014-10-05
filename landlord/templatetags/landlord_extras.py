from django.contrib.humanize.templatetags import humanize
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.template import defaultfilters, Library

from .. import models

register = template.Library()