import os, sys, datetime, time, html

where_am_i = os.getcwd()

print(where_am_i)
print(sys.platform)
print(sys.version)
# print(os.environ)
print(os.getenv('HOME'))
print(datetime.date.today().day)
print(time.strftime("%A %p"))
htmlx = "This is a  html fragment contains a <script>script</script> tag."
htmly = "I &hearts; Python's &lt;standard library&gt;."
print(html.escape(htmlx))
print(html.unescape(htmly))