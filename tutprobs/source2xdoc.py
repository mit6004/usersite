import os.path,sys

pnum = 0
ppnum = 0

source = open(sys.argv[1])
xdoc = open(sys.argv[1].split('.')[0]+'.xdoc','w')

xdoc.write("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<q:questions xmlns="http://www.w3.org/1999/xhtml"
             xmlns:q="py:tutprobs">
""")

question = False
subquestion = False
answer = False
for line in source:
    if line.startswith('{question}'):
        if answer:
            xdoc.write('</q:answer>\n')
            answer = False
        if subquestion:
            xdoc.write('</q:subquestion>\n')
            subquestion = False
        if question:
            xdoc.write('</q:question>\n')
            question = False
        xdoc.write('<q:question>\n')
        question = True
    elif line.startswith('{subquestion}'):
        if answer:
            xdoc.write('</q:answer>\n')
            answer = False
        if subquestion:
            xdoc.write('</q:subquestion>\n')
            subquestion = False
        xdoc.write('<q:subquestion>\n')
        subquestion = True
    elif line.startswith('{answer}'):
        xdoc.write('<q:answer>\n')
        answer = True
    else:
        line = line.replace('<p>','<p/>')
        line = line.replace('<br>','<br/>')
        line = line.replace('.gif">','.gif"/>')
        line = line.replace('in section">','in section"/>')
        line = line.replace('&','&amp;')
        xdoc.write(line)

if answer: xdoc.write('</q:answer>\n')
if subquestion: xdoc.write('</q:subquestion>\n')
if question: xdoc.write('</q:question>\n')
xdoc.write('</q:questions>\n');

source.close()
xdoc.close()

    
