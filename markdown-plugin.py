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
Rewritten by seanh 2009, 2010

"""
_version__ = '0.3'
__author__ = 'Benjamin Mako Hill <mako@atdot.cc>'
__author__ = 'seanh <snhmnd@gmail.com>'

FILENAME_EXTENSIONS = ('.txt','.text','.mkdn','.markdown','.md','.mdown','.markdn','.mkd')

import markdown
import os

md = markdown.Markdown(output_format='html4',extensions=['extra',])

def cb_story(args):
	entry = args['entry']
	if os.path.splitext(entry['filename'])[1] in FILENAME_EXTENSIONS:
		entry['body'] = md.convert(''.join(entry['body']))
		md.reset()
	return args