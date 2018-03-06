#!/bin/python

print "Please enter your initials:",
Init = raw_input()

print "Please enter your today's date as yyyymmdd:",
Date = raw_input()

print "Please enter the reference as follows: Author(s); Year; Journal; Volume#; Issue",
REFERENCE = raw_input()

print "Please enter the reference title:",
Title = raw_input()

print "Write three to five key background points for this paper."
Background = raw_input()

print "Please enter your research question for this experiment:",
Question = raw_input()

print "Summarize the methods used in the paper"
Procedures = raw_input()

print "Write out key findings for this paper. Keep it to one sentence per figure/table"
Findings = raw_input()

print "Do the findings support or reject the original research question? Summarize in one sentence."
Conclusion = raw_input()

print "Please re-enter your initials:",
ReInit = raw_input()

print "Please re-enter your today's date:",
ReDate = raw_input()

FullRef = [REFERENCE, Title]
Summary = 
\t* str(Background)
\t* str(Question)
\t* str(Procedures)
\t* str(Findings)
\t* str(Conclusion)


print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print [Init, Date]
print FullRef
print ""
print Summary
print ""
print [ReInit, ReDate]