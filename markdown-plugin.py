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
