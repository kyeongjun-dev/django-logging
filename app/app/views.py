from django.shortcuts import render
import logging
from django.http import HttpResponse
# Create your views here.
def index(request):
    text = """you can create log in urls(example)
    localhost:8000/logging/debug
    localhost:8000/logging/info
    localhost:8000/logging/error
    """
    return HttpResponse(text)

def debug(request):
    logger = logging.getLogger('django')
    logger.debug("DEBUG msg...")
    return HttpResponse("debug log added to /var/log/debug.log")

def info(request):
    logger = logging.getLogger('django')
    logger.info("INFO msg...")
    return HttpResponse("info log added to /var/log/info.log")

def error(request):
    logger = logging.getLogger('django')
    logger.error("ERROR msg...")
    return HttpResponse("error log added to /var/log/error.log")