#!/usr/bin/env python
"""
markdown-plugin.py -- A Python Markdown v2.x plugin for PyBlosxom.

This plugin requires Python Markdown v2.x, which you can download from:

	http://www.freewisdom.org/projects/python-markdown/

Extract the 'markdown' directory from the Python Markdown tarball (the
directory containing __init__.py, not the Markdown-2.x.y directory)  into your
pyblosxom plugins dir alongside this plugin. Your plugins dir should look like
this:

	plugins/ <-- your pyblosxom plugins dir
		markdown-plugin.py <-- this file
		markdown/ <-- the Python Markdown module
		... <-- (any other pyblosxom plugins)

Now any posts with filenames ending in one of the FILENAME_EXTENSIONS defined
below will be passed through python-markdown.

Copyright (C) Benjamin Mako Hill, 2005
Updated for Python Markdown 2 by seanh 2009

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or (at
your option) any later versi

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
USA.

"""
PREFORMATTER_ID = 'markdown'
FILENAME_EXTENSIONS = ('txt','text','mkdn','markdown','md','mdown','markdn','mkd')
_version__ = '0.3'
__author__ = 'Benjamin Mako Hill <mako@atdot.cc>'
__author__ = 'seanh <snhmnd@gmail.com>'

import codecs
import markdown
from Pyblosxom import tools

md = markdown.Markdown(
	#safe_mode=True,
	output_format='html4',
	extensions=[ #'codehilite', # Requires python-pygments
				'extra',
				 #'html_tidy', # Requires libtidy and uTidylib
				 #'imagelinks', # Broken?
				 #'meta',
				 #'rss',
				 #'toc',
				 #'wikilinks'
			   ]
)

def cb_entryparser(args):
	for FILENAME_EXTENSION in FILENAME_EXTENSIONS:
		args[FILENAME_EXTENSION] = readfile
	return args

def cb_preformat(args):
	if args['parser'] == PREFORMATTER_ID:
		return parse(''.join(args['story']))

def parse(story):
	# Convert the ASCII text to HTML with python-markdown.
	html = md.convert(story)
	# Reset python-markdown ready for next time.
	md.reset()
	return html

def readfile(filename, request):
	entryData = {}
	lines = codecs.open(filename, mode="r", encoding="utf8").readlines()
	title = lines.pop(0).strip()
	while lines and lines[0].startswith("#"):
		meta = lines.pop(0)
		meta = meta[1:].strip()
		meta = meta.split(" ", 1)
		entryData[meta[0].strip()] = meta[1].strip()
	entryData['title'] = title
	entryData['body'] = parse(''.join(lines))
	# Call the postformat callbacks
	tools.run_callback('postformat',
			{'request': request,
			 'entry_data': entryData})
	return entryData
