from __future__ import unicode_literals, division, absolute_import
import logging

from lxml.html import parse
import urllib2


from flexget import plugin
from flexget.utils import requests
from flexget.event import event

log = logging.getLogger("subdivx")


class UrlRewriteSubDivX(object):
    """SubDivX urlrewriter."""

    def url_rewritable(self, feed, entry):
        return entry['url'].startswith('http://www.subdivx.com/') and not 'subdivx.com/sub' in  entry['url']
        
    def url_rewrite(self, feed, entry):
        doc = parse(entry['url']).getroot()
        print "URL"
        print entry['url']
        for link in doc.find_class('link1'):
            if ( 'bajar.php'  in  link.get('href') ):
                print link.get('href')
                linksubdivx = link.get('href')
        u = urllib2.urlopen(linksubdivx)
        entry['url'] = u.geturl()

@event('plugin.register')
def register_plugin():
        plugin.register(UrlRewriteSubDivX, 'subdivx', groups=['urlrewriter'], api_ver=2)
