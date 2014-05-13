from embed.handlers import BaseHandler

from django.template.loader import get_template
from django.template import Context


class ScribdHandler(BaseHandler):
    def get_url_from_id(self, content_id):
        return "http://www.scribd.com/embeds/{}".format(content_id)

    def get_embed_code(self, content_id, size):
        template = get_template("embed/scribd.html")
        context = Context({
            'content_id': content_id,
        })
        return template.render(context)

    def get_id_from_url(self, url):
        patterns = [
            'scribd\.com/doc/(\d+)/.*',
            '^(\d+)$',

        ]
        for pattern in patterns:
            result = re.search(pattern, url, re.IGNORECASE)
            if result:
                return result.group(1)
        return ''

    def get_thumbnail_url(self, content_id):
        return None
