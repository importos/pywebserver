#-------------------------------------------------------------------------------
# Name:        simple fast cgi
# Purpose:
#
# Author:      m.j_banitaba
#
# Created:     12/07/2016
# Copyright:   (c) User 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import cgi
import cgitb; cgitb.enable()
import os
__SERVER__=os.environ
__PATH__=__SERVER__['PATH_INFO']
__DOC_ROOT__=__SERVER__['DOCUMENT_ROOT']


def load_doc():
    pp=os.path.abspath(__DOC_ROOT__+__PATH__+"index.html")
    if os.path.exists(pp):
        hf=open(pp,'rb')
        data=hf.read()
        hf.close()
        return data
    return pp + str()
message=load_doc()

print "Content-type: text/html"
print "Content-Length:", str(len(message))
print

print message
