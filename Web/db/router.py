class OracleRouter:

    non_boad_attribute_tables = {'admin', 'auth', 'contenttypes', 'django_q', 'sessions', 'messages', 'staticfiles', 'user', 'homepage'}
    def db_for_read(self, model, **hints):
        #print(model._meta.app_label)
        if model._meta.app_label in self.non_boad_attribute_tables:
            return 'sqlite'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.non_boad_attribute_tables:
            return 'sqlite'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.non_boad_attribute_tables or obj2._meta.app_label in self.non_boad_attribute_tables:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.non_boad_attribute_tables:
            return db=='sqlite'
        return None



class MySqlRouter:

    non_boad_attribute_tables = {'electronicos'}
    def db_for_read(self, model, **hints):
        #print(model._meta.app_label)
        if model._meta.app_label in self.non_boad_attribute_tables:
            return 'mysql'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.non_boad_attribute_tables:
            return 'mysql'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.non_boad_attribute_tables or obj2._meta.app_label in self.non_boad_attribute_tables:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.non_boad_attribute_tables:
            return db=='mysql'
        return None