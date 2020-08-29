import datetime

import peewee
from playhouse.sqlite_ext import JSONField

db = peewee.SqliteDatabase('spotlike.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    id = peewee.CharField(primary_key=True)
    name = peewee.CharField()
    email = peewee.CharField(unique=True)
    picture = peewee.CharField()
    token = JSONField()
    join_date = peewee.DateTimeField(default=datetime.datetime.utcnow)


class Artist(BaseModel):
    id = peewee.CharField(primary_key=True)
    name = peewee.CharField()


class Track(BaseModel):
    id = peewee.CharField(primary_key=True)
    title = peewee.CharField()
    duration = peewee.IntegerField()


class TrackArtist(BaseModel):
    # a many to many relation table
    track = peewee.ForeignKeyField(Track)
    artist = peewee.ForeignKeyField(Artist)


class Play(BaseModel):
    user = peewee.ForeignKeyField(User, backref='played')
    track = peewee.ForeignKeyField(Track)
    played_at = peewee.DateTimeField()


class Liked(BaseModel):
    # a many to many relation table
    user = peewee.ForeignKeyField(User),
    track = peewee.ForeignKeyField(Track)


def initdb():
    db.connect(reuse_if_open=True)
    db.create_tables((User,
                      Artist, Track, TrackArtist,
                      Play
                      ))


if __name__ == '__main__':
    initdb()
