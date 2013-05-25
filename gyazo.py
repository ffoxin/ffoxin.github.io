#!/usr/bin/python
import cgi

print 'Content-Type: text/html'
print ''

key = 'img'
arguments = cgi.FieldStorage()
if key in arguments.keys():
	print '<html>'
	print '<body>'
	print '<image src="{0}" />'.format(arguments[key].value)
	print '</body>'
	print '</html>'
