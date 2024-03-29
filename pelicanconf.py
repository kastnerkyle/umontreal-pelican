#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Kyle Kastner'

SITENAME = u'Student Information'
SITEURL = ''  # change in publishconf.py

# Times and dates
DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'US/Eastern'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
MENUITEMS = [('Home', '/index.html'),
             ('Archives', '/archives.html')]

NEWEST_FIRST_ARCHIVES = False

# Blogroll
#LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
#          ('Python.org', 'http://python.org'),
#          ('Jinja2', 'http://jinja.pocoo.org'),
#          ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

# STATIC_OUT_DIR requires pelican 3.3
#STATIC_OUT_DIR = ''
STATIC_PATHS = ['images', 'figures', 'downloads']
FILES_TO_COPY = [('favicon.png', 'favicon.png')]
CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plugins
#  Theme requires http://github.com/duilio/pelican-octopress-theme/
#  Plugins require http://github.com/getpelican/pelican-plugins/
#Remember to add extra header stuff...
THEME = '../pelican-themes/bootstrap'
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal']


# The theme file should be updated so that the base header contains the line:
#
#  {% if EXTRA_HEADER %}
#    {{ EXTRA_HEADER }}
#  {% endif %}
#
# This header file is automatically generated by the notebook plugin
EXTRA_HEADER = open('_nb_header_mod.html').read().decode('utf-8')

LINKS = [('MyMainBlog', 'http://kastnerkyle.github.io'),
         ('MyOtherNotes', 'http://kkjkok.blogspot.com'),
         ('PushButtonRobotics', 'http://pushbuttonrobotics.weebly.com/'),
         ('FastML', 'http://www.fastml.com/'),
         ('PythonicPerambulations', 'http://jakevdp.github.io'),
         ('SnippyHollow', 'http://snippyhollow.github.io'),
         ('AndrejKarpathy', 'http://karpathy.github.io'),
         ('MLWave', 'http://mlwave.com/'),
         ('StronglyConvex', 'http://stronglyconvex.com/'),
         ('SmellTheData', 'http://blog.smellthedata.com/')]

# Sharing
SOCIAL = [('github', 'http://github.com/kastnerkyle'),
          ('kaggle', 'http://www.kaggle.com/users/107564/kyle-kastner'),
          ('twitter', 'http://twitter.com/kastnerkyle'),
          ('google+', 'http://plus.google.com/+KyleKastner'),
          ('linkedin', 'http://www.linkedin.com/pub/kyle-kastner/24/605/4a1')]

#GITHUB_URL = 'http://github.com/kastnerkyle'
#GITHUB_USERNAME = 'kastnerkyle'
#GITHUB_REPO_COUNT = 5
#GITHUB_SKIP_FORK = True
#GITHUB_SHOW_USER_LINK = True

#GOOGLE_PLUS_USERNAME = 'kastnerkyle'
#GOOGLE_PLUS_ONE = True
#GOOGLE_PLUS_HIDDEN = False

#TWITTER_USERNAME = 'kastnerkyle'
#TWITTER_TWEET_BUTTON = True
#TWITTER_LATEST_TWEETS = True
#TWITTER_FOLLOW_BUTTON = True
#TWITTER_TWEET_COUNT = 3
#TWITTER_SHOW_REPLIES = 'false'
#TWITTER_SHOW_FOLLOWER_COUNT = 'true'

#FACEBOOK_LIKE = False

# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'

# Search
SEARCH_BOX = False
