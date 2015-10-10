
from django.conf import settings
from django.template import loader, RequestContext

from nadmin.sites import site
from nadmin.views import BaseAdminPlugin, CommAdminView


class SetLangNavPlugin(BaseAdminPlugin):

    def block_top_navmenu(self, context, nodes):
        nodes.append(
            loader.render_to_string('nadmin/blocks/comm.top.setlang.html', {
                'redirect_to': self.request.get_full_path(),
            }, context_instance=RequestContext(self.request)))

if settings.LANGUAGES and 'django.middleware.locale.LocaleMiddleware' in settings.MIDDLEWARE_CLASSES:
    site.register_plugin(SetLangNavPlugin, CommAdminView)
    site.register_view(r'^i18n/', lambda site: 'django.conf.urls.i18n', 'i18n')
