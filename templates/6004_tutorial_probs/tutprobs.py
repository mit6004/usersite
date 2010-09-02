#!/usr/bin/env python
import pre as re
import sys

def process_answer(match):
    global question,subquestion,args
    num = "%d%c" % (question,chr(ord('@')+subquestion))
    if args.has_key('noanswers'): return ''
    if args.has_key('answers'):
        display = 'display:block'
        spacer = '<p/>'
        prefix = ''
    else:
        display = 'display:none'
        spacer = ''
        prefix = """<div id="control%s" class="control" style="padding-top: 8px; padding-bottom: 8px">
        <a href="#" onClick="toggle('%s'); return false">
          <img name="ctl%s" class="hideshow" src="show.gif" border="0"/>
        </a></div> """ % (num,num,num)
    return prefix+'<div id="answer%s" class="answer" style="%s"><font color="blue">%s%s</font><div>' % (num,display,spacer,match.group(1))

def process_subquestion(match):
    global question,subquestion
    subquestion += 1
    num = "%d%c" % (question,chr(ord('@')+subquestion))
    prefix = """
    <div id="question%s" class="question">
    <ol type="A" start="%d"><li>
    """ % (num,subquestion)
    suffix = '</li></ol></div>'
    return prefix + re.sub(r'(?s)<q:answer>(.*?)</q:answer>',process_answer,match.group(1)) + suffix

def process_question(match):
    global question,subquestion
    question += 1
    subquestion = 0
    prefix = """
    <div id="question%d" class="question">
    <p/><hr/><p/><u>Problem %d.</u>
    """ % (question,question)
    suffix = '</div>'
    return prefix + re.sub(r'(?s)<q:subquestion>(.*?)</q:subquestion>',process_subquestion,match.group(1)) + suffix

def process_questions(match):
    global question,args
    question = 0

    if not args.has_key('answers') and not args.has_key('noanswers'):
        head = '<head><script language="JavaScript1.2" src="tutprobs.js"></script></head>'
	noscript = """
	<noscript><table width=100%% border="1" cellpadding="8" bgcolor="yellow"><tr><td>
        You need to have Javascript enabled to view this page
        properly.  If your browser does not support Javascript
        or you have chosen not to enable it, please return to
        the previous page and use the appropriate link to view
        non-script versions of this tutorial page.
        </td></tr></table></noscript>"""
        buttons = """
        <a href="\#" onClick="showall(); return false"><img border="0" src="showall.gif"/></a>
        &nbsp;
        <a href="\#" onClick="hideall(); return false"><img border="0" src="hideall.gif"/></a>
        <p/><img src="star.gif" alt="Discussed in section"/>
        indicates problems that have been selected for discussion
        in section, time permitting.
        """
    else:
        head = ''
	noscript = ''
        buttons = ''
    return ('<html>'+head+'<body style="margin-top:5px">'+noscript+
           '<h3>'+match.group(1)+'</h3>'+buttons+
           re.sub(r'(?s)<q:question>(.*?)</q:question>',process_question,match.group(2))+
           '</body></html>')

def process_file(contents,answers=0,noanswers=0):
    global args
    args = {}
    if answers: args['answers'] = 1
    if noanswers: args['noanswers'] = 1
    return re.sub(r'(?s)<q:questions.*?title.*?=.*?"(.*?)".*?>(.*)</q:questions>',process_questions,contents)

if __name__ == '__main__':
    file = sys.argv[1]

    try:
        f = open(file+".xdoc")
        contents = f.read()
        f.close()
    except Exception,e:
        print 'Oops!  Error while reading ',file,': ',e
        sys.exit()

    try:
	f = open(file+".html","w")
	f.write(process_file(contents))
	f.close()

	f = open(file+"_answers.html","w")
	f.write(process_file(contents,answers=1))
	f.close()

	f = open(file+"_noanswers.html","w")
	f.write(process_file(contents,noanswers=1))
	f.close()
    except Exception,e:
        print 'Oops!  Error while processing ',file,': ',e
        print 'question',question,'subquestion',subquestion
        sys.exit()
