from __future__ import unicode_literals

import os.path

from logging import info
from codecs import open

from pelican import signals

LUA_TOP = """
mapping = {
"""

LUA_BOTTOM = """
};
"""


class RandomArticleGenerator(object):
    """
        The structure is derived from sitemap plugin
    """

    def __init__(self, context, settings, path, theme, output_path, *null):

        self.output_path = output_path
        self.context = context
        self.siteurl = settings.get('SITEURL')
        self.sitemap = settings.get('SITE_MAP')

    def write_map(self, article, fd):
        if getattr(article, 'status', 'published') != 'published':
            return

        page_path = os.path.join(self.output_path, article.url)
        if not os.path.exists(page_path):
            return

        fd.write("%s=\"%s\",\n" % (article.slug, article.url))


    def generate_output(self, writer):
        path = os.path.join(self.output_path, self.sitemap)
        articles = self.context['articles']
        info('writing {0}'.format(path))

        if len(articles) == 0:
            return

        with open(path, 'w', encoding='utf-8') as fd:
            fd.write(LUA_TOP)

            for art in articles:
                self.write_map(art, fd)

            fd.write(LUA_BOTTOM)

def get_generators(generators):
    return RandomArticleGenerator


def register():
    signals.get_generators.connect(get_generators)