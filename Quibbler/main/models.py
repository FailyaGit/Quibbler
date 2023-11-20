from django.db import models

# Create your models here.

class News:
    def __init__(self, newshead, newssummary, newstext):
        self.newshead = newshead
        self.newssummary = newssummary
        self.newstext = newstext

    def __str__(self):
        return f'{self.newshead}, {self.newssummary}, {self.newstext} '


class User:
    def __init__(self, usrname, email, telephone, password):
        self.usrname = usrname
        self.email = email
        self.telephone = telephone
        self.password = password

    def __str__(self):
        return f'{self.usrname}, {self.email}, {self.telephone}, {self.password}'

from django.db import models

# Create your models here.
