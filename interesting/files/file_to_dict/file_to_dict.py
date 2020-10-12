######################################
#  Snoopjedi suggestion, so valuable
######################################

#  12:08 [snoopjedi@denton ~]
#  $ cat test.py && echo
#  from io import StringIO
#
#  doc = StringIO("""
#  Tim 350
#  Jane 200
#  Alex 400
#  """.strip())
#
#  def parse_line(line):
#      fields = line.split()
#      if len(fields) != 2:
#          raise ValueError("wrong number of fields")
#      else:
#          return fields
#
#  d = dict([parse_line(line) for line in doc.readlines()])
#  print(d)
#
#  12:08 [snoopjedi@denton ~]
#  $ python3 test.py
#  {'Tim': '350', 'Jane': '200', 'Alex': '400'}


rating_file = open("rating.txt", "r")

rating_dict = dict(line.split() for line in rating_file.readlines())

print(rating_dict)
