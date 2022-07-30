
class DBRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.model_name == "Position":
            return "gadzmap"
        return "users"

    def db_for_write(self, model, **hints):
        if model._meta.model_name == "Position":
            return "gadzmap"
        return "users"

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'gadzmap':
            return db == 'gadzmap'
        return "users"