from django.contrib.sessions.models import Session
from django.contrib.auth import get_user_model
from .models import Dialog
from django.db.models import Q
import logging
import sys


def get_user_from_session(session_key):

    session = Session.objects.get(session_key=session_key)
    session_data = session.get_decoded()
    uid = session_data.get('_auth_user_id')
    user = get_user_model().objects.filter(id=uid).first()  # get object or none
    return user


def get_dialogs_with_user(user_1, user_2):

    return Dialog.objects.filter(
        Q(owner=user_1, opponent=user_2) | Q(opponent=user_1, owner=user_2))


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s",
                    datefmt='%d.%m.%y %H:%M:%S')
logger = logging.getLogger('private-dialog')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
