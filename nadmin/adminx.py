import nadmin
from models import UserSettings
from nadmin.layout import *


class UserSettingsAdmin(object):
    model_icon = 'fa fa-cog'
    hidden_menu = True
nadmin.site.register(UserSettings, UserSettingsAdmin)
