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

Copyright (C) 2005, 2011 Benjamin Mako Hill
Copyright (c) 2009, 2010, seanh

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

"""
_version__ = '0.3'
__author__ = 'Benjamin Mako Hill <mako@atdot.cc>'
__author__ = 'seanh <snhmnd@gmail.com>'

FILENAME_EXTENSIONS = ('.txt','.text','.mkdn','.markdown','.md','.mdown','.markdn','.mkd','.mdwn')

import markdown
import os

md = markdown.Markdown(output_format='html4',extensions=['extra',])

def cb_story(args):
	entry = args['entry']
	if os.path.splitext(entry['filename'])[1] in FILENAME_EXTENSIONS:
		entry['body'] = md.convert(u''.join(entry['body'].decode("utf-8")))
		md.reset()
	return args
