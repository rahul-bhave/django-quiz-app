from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from faunadb import query as q
import pytz
from faunadb.objects import Ref
from faunadb.client import FaunaClient
import hashlib
import datetime

client = FaunaClient(secret="SECRET_KEY")
indexes = client.query(q.paginate(q.indexes()))