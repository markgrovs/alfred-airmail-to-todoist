""" Todoist to Airmail


"""
#!/usr/bin/python
# encoding: utf8

import sys
import os
import todoist
from Foundation import *
from ScriptingBridge import *

from workflow import Workflow3

LOG = None

API_KEY = None
EMAIL_LABELID = '[151545]'
INBOX_ID = None


def create_task(content):
    """

    """
    todo = todoist.TodoistAPI(API_KEY)

    # task = todo.items.add(content, INBOX_ID, labels=EMAIL_LABELID)
    task = todo.items.add(content, 1)
    # print task

    airmail = SBApplication.applicationWithBundleIdentifier_("it.bloop.airmail2")

    # Format note text from message subject
    task_note_text = airmail.selectedMessageUrl() + " (" + airmail.selectedMessage().subject() + ")"
    # print airmail.selectedMessage().subject()
    todo.notes.add(task['id'], task_note_text)

    todo.commit()


def main(wf):
    """

    """
    if len(wf.args):
        query = wf.args[0]
        print query
    else:
        query = None
        print query

    create_task(query)



if __name__ == u"__main__":
    wf = Workflow3(libraries=[os.path.join(os.path.dirname(__file__), 'lib')])
    LOG = wf.logger
    
    API_KEY = os.environ['API_KEY']
    INBOX_ID = os.environ['INBOX_ID']
    LOG.debug(INBOX_ID)
    sys.exit(wf.run(main))
