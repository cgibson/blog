from __future__ import unicode_literals

import os.path

from logging import info
from codecs import open

from pelican import signals
import logging
logger = logging.getLogger(__name__)


def fetch_movie_list(gen, metadata):
    articles = gen.context['articles']
    movies = []

    #for article in articles:
    #    if article.category == "reviews":
    #        movies.append(article)
    gen.context['movies'] = movies


def register():
    try:
        signals.pages_generator_finalized.connect(fetch_movie_list)
    except ImportError:
            logger.warning('movie list failed to load.')