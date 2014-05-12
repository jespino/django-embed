from embed.handlers import BaseHandler

from django.template.loader import get_template
from django.template import Context


class YouTubeHandler(BaseHandler):
    def get_url_from_id(self, content_id):
        return "http://prezi.com/embed/{}".format(content_id)

    def get_embed_code(self, content_id, size):
        template = get_template("embed/prezi.html")
        context = Context({
            'content_id': content_id,
        })
        return template.render(context)

    def get_id_from_url(self, url):
        patterns = [
            'prezi\.com/([a-zA-Z\d\-]+)/.*',
            '^([a-zA-Z\d\-]+)$',

        ]
        for pattern in patterns:
            result = re.search(pattern, url, re.IGNORECASE)
            if result:
                return result.group(1)
        return ''

    def get_thumbnail_url(self, content_id):
        return None
