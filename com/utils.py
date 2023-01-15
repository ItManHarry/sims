from flask import request, redirect, url_for, current_app
from urllib.parse import urlparse, urljoin
from com.plugins import db
import time, datetime, os, uuid, random, PIL
from PIL import Image

def get_time_today():
    '''
    获取当前时间
    :return:
    '''
    return time.strftime('%Y-%m-%d')
def is_safe_url(target):
    '''
    判断地址是否安全
    :param target:
    :return:
    '''
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http','https') and ref_url.netloc == test_url.netloc
def redirect_back(default='main.index', **kwargs):
    '''
    通用返回方法(默认返回博客首页)
    :param default:
    :param kwargs:
    :return:
    '''
    target = request.args.get('next')
    if target and is_safe_url(target):
        return redirect(target)
    return redirect(url_for(default, **kwargs))
def random_filename(filename):
    '''
    重命名文件
    :param filename:
    :return:
    '''
    ext = os.path.splitext(filename)[1]
    new_file_name = uuid.uuid4().hex + ext
    return new_file_name