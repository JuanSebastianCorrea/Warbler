"""User View tests."""

import os
from unittest import TestCase

from models import db, connect_db, Message, User, Likes, Follows