from datetime import datetime

from mongoengine import Document, StringField, DateTimeField


class User(Document):
    meta = {'collection': 'users'}

    email = StringField()
    password = StringField()

    created_at = DateTimeField()
    updated_at = DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.utcnow()
        else:
            self.updated_at = datetime.utcnow()
        return super(User, self).save(*args, **kwargs)

    def update(self, **kwargs):
        if not self.created_at:
            self.created_at = datetime.utcnow()
        else:
            self.updated_at = datetime.utcnow()
        return super(User, self).update(**kwargs)
