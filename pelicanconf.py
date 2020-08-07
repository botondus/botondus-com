#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Botond Béres"
SITENAME = "Botondus.com"
SITE_URL = ""

PATH = "content"

TIMEZONE = "Europe/Bucharest"
DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "http://getpelican.com/"),
    ("Python.org", "http://python.org/"),
    ("Jinja2", "http://jinja.pocoo.org/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

DEFAULT_METADATA = {"status": "draft", "authors": "Botond Béres"}

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

TYPOGRIFY = True

# DO NOT automatically generate slugs
# For how to write slugs see https://www.theengineeringprojects.com/2018/07/structure-blog-post-url.html
SLUGIFY_SOURCE = ''

# Configure URLs
#ARTICLE_URL = '{slug}.html'
#ARTICLE_SAVE_AS = '{slug}.html'
#PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# If you do not want one or more of the default pages to be created
# (e.g., you are the only author on your site and thus do not need an Authors page),
# set the corresponding *_SAVE_AS setting to '' to prevent the relevant page
# from being generated.
AUTHOR_SAVE_AS = ''

# When experimenting with different plugins (especially the ones that deal
# with metadata and content) caching may interfere and the changes may
# not be visible. In such cases disable caching with
# LOAD_CONTENT_CACHE = False or use the --ignore-cache command-line switch.
# LOAD_CONTENT_CACHE = False
