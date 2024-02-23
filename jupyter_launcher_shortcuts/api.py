from tornado import web
import mimetypes
from jupyter_server.base.handlers import JupyterHandler as handler
from jupyter_server.utils import url_path_join as ujoin

class ShortcutsHandler(handler):
    def initialize(self, shortcuts):
        self.shortcuts = shortcuts

    @web.authenticated
    async def get(self):
        data = []
        for ls in self.shortcuts:
            item = {
                'name': ls.name,
                'title': ls.title,
                'target': ls.target.format(base_url=self.base_url),
            }
            if ls.icon_path:
                item["icon_url"] = ujoin(self.base_url, 'launcher-shortcuts', 'icon', ls.name)
            data.append(item)

        self.write({'shortcuts': data})


# FIXME: Should be a StaticFileHandler subclass
class IconHandler(handler):
    """
    Serve launcher icons
    """
    def initialize(self, icons):
        """
        icons is a dict of titles to paths
        """
        self.icons = icons

    async def get(self, name):
        if name not in self.icons:
            raise web.HTTPError(404)
        path = self.icons[name]

        # Guess mimetype appropriately
        # Stolen from https://github.com/tornadoweb/tornado/blob/b399a9d19c45951e4561e6e580d7e8cf396ef9ff/tornado/web.py#L2881
        mime_type, encoding = mimetypes.guess_type(path)
        if encoding == "gzip":
            content_type = "application/gzip"
        # As of 2015-07-21 there is no bzip2 encoding defined at
        # http://www.iana.org/assignments/media-types/media-types.xhtml
        # So for that (and any other encoding), use octet-stream.
        elif encoding is not None:
            content_type = "application/octet-stream"
        elif mime_type is not None:
            content_type = mime_type
        # if mime_type not detected, use application/octet-stream
        else:
            content_type = "application/octet-stream"

        with open(self.icons[name], "rb") as f:
            self.write(f.read())
        self.set_header('Content-Type', content_type)