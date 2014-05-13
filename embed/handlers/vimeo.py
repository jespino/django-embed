from embed.handlers import BaseHandler

from django.template.loader import get_template
from django.template import Context


class VimeoHandler(BaseHandler):
    def get_url_from_id(self, content_id):
        return "https://player.vimeo.com/video/{}".format(content_id)

    def get_embed_code(self, content_id, size):
        template = get_template("embed/vimeo.html")
        context = Context({
            'content_id': content_id,
        })
        return template.render(context)

    def get_id_from_url(self, url):
        patterns = [
            'vimeo\.com/(\d+)',
            'vimeo\.com/video/(\d+)',
            'vimeo\.com/groups/.+/videos/(\d+)',
            'vimeo\.com/channels/.+#(\d+)',
            '^(\d+)$',
        ]
        for pattern in patterns:
            result = re.search(pattern, url, re.IGNORECASE)
            if result:
                return result.group(1)
        return ''

    def get_thumbnail_url(self, content_id):
        try:
            response = requests.get("https://vimeo.com/api/v2/video/%s.json" % unicode(content_id))
            data = json.loads(response.content)
            url = data[0].get('thumbnail_small', '')
            return url
        except Exception:
            return ""
