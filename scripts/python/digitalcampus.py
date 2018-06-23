import requests
url = 'http://digitalcampus.in/'
values = {'uname': '806', 
          'password': '10acious', 
          'school_id': 'MER-MP1718'}

with requests.Session() as s:
    p = s.post(url, data = values)
    print p.text


url1 = 'http://digitalcampus.in/meridian/inbox_msg_details.jsp?pre_id=2140&fromempid=200058&mstatus=C-123401&mdate=18-10-2017&msubj=math%20home%20work'

# url1 = 'http://digitalcampus.in/meridian/Inbox.jsp'

with requests.Session() as s1:
    p1 = s1.post(url1, data = values)
    print p1.text

