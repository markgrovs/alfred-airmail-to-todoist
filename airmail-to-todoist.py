import sys
import todoist
from workflow import Workflow, ICON_WEB, web
from Foundation import *
from ScriptingBridge import * 

API_KEY = 'a01aa1a0314d222ae901741cbed2510425913f98'
EMAIL_LABELID = '[151545]'
INBOX_ID = 131035310


def create_task(content):
	todo = todoist.TodoistAPI(API_KEY)
	task = todo.items.add(content, INBOX_ID, labels=EMAIL_LABELID)
	# print task

	airmail = SBApplication.applicationWithBundleIdentifier_("it.bloop.airmail2")
	# airmail = SBApplication.applicationWithBundleIdentifier_("it.bloop.airmail.beta11")
	

	task_note_text = airmail.selectedMessageUrl() + " (" + airmail.selectedMessage().subject() + ")" 
	# print airmail.selectedMessage().subject()
	todo.notes.add(task['id'], task_note_text)

	todo.commit()


def main(wf):

	if len(wf.args):
		query = wf.args[0]
		print query
	else:
		query = None
		print query


	create_task(query)



if __name__ == u"__main__":
	wf = Workflow()
	wf
	
	sys.exit(wf.run(main))
