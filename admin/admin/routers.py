from django.conf import settings

_config = getattr(settings, 'APP_DATABASES', {})


class AppRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    def db_for_read(self, model, **hints):
        """Attempts to read auth models go to auth_db."""
        if settings.DEBUG is True:
            return None
        return _config.get(model._meta.app_label)

    def db_for_write(self, model, **hints):
        """Attempts to write auth models go to auth_db."""
        if settings.DEBUG is True:
            return None
        return _config.get(model._meta.app_label)

    def allow_relation(self, obj1, obj2, **hints):
        """ Allow relations if a model in the auth app is involved."""
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """Make sure the auth app only appears in the 'auth_db' database."""
        if settings.DEBUG is True:
            return None

        if app_label in _config:
            return db == _config.get(app_label)
        return None
