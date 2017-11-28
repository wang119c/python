# -*- coding:utf-8 -*-
import requests
import datetime
import time
import json
import sys

reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    existed_codes = {}
    fetch_trains_static_info(existed_codes)
    deal_and_store(existed_codes)
