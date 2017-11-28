# Create your views here.
import logging
from django.shortcuts import render
from django.conf import settings
logger = logging.getLogger(__name__)

def global_setting(request):
    return {
        'SITE_NAME':settings.SITE_NAME,
        'SITE_DESC':settings.SITE_DESC,
    }

def index(request):
    try:
        # pass
        file = open('test.txt','r')
    except Exception as e:
        # pass
        logger.error(e)
    logger.error("21312")
    return render(request,'index.htm')