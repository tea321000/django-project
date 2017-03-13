# coding=utf8
from __future__ import unicode_literals
from django.db import models

class Musician(models.Model):
    no=models.IntegerField(primary_key=True)
    name=models.CharField('原名',max_length=40)
    stagename=models.CharField('艺名',max_length=40,null=True,blank=True)
    sex=models.CharField('性别',choices=(('M', '男'), ('F', '女')),max_length=1)
    birthday=models.DateTimeField('出生日期')

class RecordCompany(models.Model):
    no=models.IntegerField(primary_key=True)
    company=models.CharField(max_length=40)

class Album(models.Model):
    no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=40)
    company=models.ForeignKey(RecordCompany,related_name='RecordCompany_company')
    date=models.DateTimeField()

class Music(models.Model):
    no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=40)
    lyricist=models.ForeignKey(Musician,related_name='Musician_lyricist')
    composer=models.ForeignKey(Musician,related_name='Musician_composer')
    singer=models.ForeignKey(Musician,related_name='Musician_singer')
    album=models.ForeignKey(Musician,related_name='Album_album')
    duration=models.DurationField()

class User(models.Model):
    no=models.IntegerField(primary_key=True)
    user=models.CharField(max_length=8)
    passwd=models.CharField(max_length=8)

class PersonalRecord(models.Model):
    no=models.IntegerField(primary_key=True)
    user=models.ForeignKey(User,related_name='User_user')
    song=models.ForeignKey(Music,related_name='Music_song')
    plays=models.IntegerField()
    like=models.IntegerField()
    dislike=models.IntegerField()
