#-- I USE PYTHON 2.7#
#---AUTHOR-MR-LI#
#coding:utf-8#
from bs4 import BeautifulSoup
from urllib2 import HTTPError
from urllib2 import urlopen
from urllib2 import URLError
def get_url(url):
    try:
        html=urlopen(url)
    except Exception as e:
        print "this is urlerror or HTTPError!!\n"
    try:
        Bobj=BeautifulSoup(html,'html.parser')
        title=Bobj.h1.p
        """
        last is not exists return title=None
        last but one is not exist return error...
        """
    except AttributeError as e:
        print "we find attribute error\n"
    else:
        if title==None:
            print "the title you supply is not useful"
        else:
            return title
target_url="http://"+raw_input("please input the target url you want to get imformation :  ")
print "please wait we are loading..............\n"
title=get_url(target_url)
if title==None:
    exit(1)
print "\n"+"     "+title.get_text().encode('gb18030')
