# -*- coding:utf-8 -*-
# @Time : 2021/2/27 2:22 下午
# @Author : huichuan LI
# @File : Student.py
# @Software: PyCharm


class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def __repr__(self):
        return "Student(name:{0},score:{1})".format(self.name, self.score)


