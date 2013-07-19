#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Copyright (c) 2010 Gerson Minichiello
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.

import urllib2
import pyRdfa
import html5lib
from xml.dom import minidom
from html5lib import treebuilders
from cStringIO import StringIO

OPENGRAPH_NAMESPACES = [
  "http://opengraphprotocol.org/schema",
  "http://opengraphprotocol.org/schema/",
  "http://ogp.me/ns#",
]

class opengraph(object):
   
    def __init__(self, url=None, xml=None):
        if not xml:
            xml = urllib2.urlopen(url).read()

        pyRdfa_options = pyRdfa.Options()

        try:
            dom = minidom.parse(StringIO(xml))
        except:
            parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder('dom'))
            dom = parser.parse(xml, encoding='utf-8')
            pyRdfa_options.host_language = pyRdfa.HTML5_RDFA

        # Workaround the problem that YouTube does not correctly set
        #   the xmlns:og attribute on <html> node; without this,
        #   pyRdfa does not find any OpenGraph tags

        for n in dom.childNodes:
            if n.nodeType == dom.ELEMENT_NODE and n.tagName == 'html':
                if not n.hasAttribute('xmlns:og'):
                    n.setAttributeNS('', 'xmlns:og', OPENGRAPH_NAMESPACES[0])

        self.metadata = {}

        for s, p, o in pyRdfa.parseRDFa(dom, url, options=pyRdfa_options):
            if s.encode('utf-8') != url:
                continue
            k = p.encode('utf-8')
            for ns in OPENGRAPH_NAMESPACES:
                if k.startswith(ns):
                    self.metadata.setdefault(k.replace(ns, ''), o.encode('utf-8'))

    def get_properties(self, data):
        content = {}
        for k, v in data.iteritems():
            for ns in OPENGRAPH_NAMESPACES:
                if k.startswith(ns) and len(v)>0:
                    content[k.replace(ns, '')] = v[0]
        return content
    
    def __str__(self):
        return self.metadata['title']

if __name__ == '__main__':
    # Usage
    og = opengraph('http://www.zappos.com/timberland-pro-titan-safety-toe-oxford')
    print og.metadata
