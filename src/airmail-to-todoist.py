""" Todoist to Airmail


"""
#!/usr/bin/python
# encoding: utf8

import sys
import os
from workflow import Workflow3
from Foundation import *
from ScriptingBridge import *

LOG = None
API_KEY = None

def create_task(content):
    """

    """
    todo = todoist.TodoistAPI(API_KEY)

    if not wf.settings.get('inbox_id', None):
        todo.sync()
        inbox = [p for p in todo.state['projects'] if p['name'] == 'Inbox'][0]
        wf.settings['inbox_id'] = inbox['id']

    task = todo.items.add(content, wf.settings['inbox_id'])
    # print task

    # airmail = SBApplication.applicationWithBundleIdentifier_("it.bloop.airmail2")
    # 
    airmail = SBApplication.applicationWithBundleIdentifier_("it.bloop.airmail.beta11")

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
        LOG.debug(query)
    else:
        query = None
        LOG.debug(query)

    create_task(query)

if __name__ == u"__main__":
    wf = Workflow3(libraries=['./lib'])
    import todoist
    LOG = wf.logger
    API_KEY = os.environ['API_KEY']

    sys.exit(wf.run(main))
