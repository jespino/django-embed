from embed.handlers import BaseHandler

from django.template.loader import get_template
from django.template import Context


class YouTubeHandler(BaseHandler):
    def get_url_from_id(self, content_id):
        return "http://youtube.com/embed/{}".format(content_id)

    def get_embed_code(self, content_id, size):
        template = get_template("embed/youtube.html")
        context = Context({
            'content_id': content_id,
        })
        return template.render(context)

    def get_id_from_url(self, url):
        patterns = [
            'youtube\.com/watch\?v=([\w\-]+).*',
            'youtube\.com/embed/([\w\-]+)',
            'youtube\.com/v/([\w\-]+)',
            'youtube\.com/\?v=([\w\-]+)',
            'youtu\.be/([\w\-]+)',
            'gdata\.youtube\.com/feeds/api/videos/([\w\-]+)',
            '^([\w\-]+)$',
        ]
        for pattern in patterns:
            result = re.search(pattern, url, re.IGNORECASE)
            if result:
                return result.group(1)
        return ''

    def get_thumbnail_url(self, content_id):
        return "//img.youtube.com/vi/{}/1.jpg".format(content_id)
