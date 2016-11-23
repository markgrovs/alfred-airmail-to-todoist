""" Todoist to Airmail


"""
#!/usr/bin/python
# encoding: utf8

import sys

from workflow import Workflow

LOG = None

API_KEY = 'a01aa1a0314d222ae901741cbed2510425913f98'
EMAIL_LABELID = '[151545]'
INBOX_ID = 131035310


def create_task(content):
    """

    """
    todo = todoist.TodoistAPI(API_KEY)
    task = todo.items.add(content, INBOX_ID, labels=EMAIL_LABELID)
    # print task

    airmail = SBApplication.applicationWithBundleIdentifier_("it.bloop.airmail2")

    # Format note text from message subject
    task_note_text = airmail.selectedMessageUrl() + " (" + airmail.selectedMessage().subject() + ")"
    # print airmail.selectedMessage().subject()
    todo.notes.add(task['id'], task_note_text)

    todo.commit()


def main(wf):
    import todoist
    
    if len(wf.args):
        query = wf.args[0]
        print query
    else:
        query = None
        print query


    create_task(query)



if __name__ == u"__main__":
    wf = Workflow(libraries=['./lib'])
    LOG = wf.logger
    sys.exit(wf.run(main))
