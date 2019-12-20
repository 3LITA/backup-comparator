import json
import os

import app.script

ADDED_USER = {'id': '6e7b768e-07e2-4810-8459-485f84f8f204', 'userType': 'Member'}
CHANGED_ATTRIBUTE = {
            'id': '6e7b768e-07e2-4810-8459-485f84f8f204',
            'attribute': 'mail',
            'oldValue': 'Adamse@M365x214355.onmicrosoft.com',
            'newValue': 'Adams@M365x214355.onmicrosoft.com',
        }


def test_added_user():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/testing_files/src_added.json') as file:
        source = json.load(file)
    with open(os.path.dirname(os.path.abspath(__file__)) + '/testing_files/tgt_added.json') as file:
        target = json.load(file)
    assert app.script.compare_content(source['value'], target['value']) == {
        'Deleted': [],
        'Added': [ADDED_USER],
        'ChangedAttribute': [],
    }


def test_deleted_user():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/testing_files/src_added.json') as file:
        target = json.load(file)
    with open(os.path.dirname(os.path.abspath(__file__)) + '/testing_files/tgt_added.json') as file:
        source = json.load(file)
    assert app.script.compare_content(source['value'], target['value']) == {
        'Deleted': [ADDED_USER],
        'Added': [],
        'ChangedAttribute': [],
    }


def test_changed_attribute():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/testing_files/src_changed.json') as file:
        source = json.load(file)
    with open(os.path.dirname(os.path.abspath(__file__)) + '/testing_files/tgt_changed.json') as file:
        target = json.load(file)
    assert app.script.compare_content(source['value'], target['value']) == {
        'Deleted': [],
        'Added': [],
        'ChangedAttribute': [CHANGED_ATTRIBUTE],
    }
