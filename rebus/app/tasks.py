# -*- coding: utf8 -*-
from __future__ import absolute_import
from celery import shared_task

@shared_task
def cobro():
    print "Combraré"

@shared_task
def compra():
    print "Compraré :D"