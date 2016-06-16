import re

pattern = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', re.M)

# match = pattern.match('\naWWWaWWW')
# print match.group(1)

# with open('data2', 'r') as f:
#     for idx, line in enumerate(f):
#         matchs = pattern.finditer(line)
#         for match in matchs:
#             if match:
#                 print '%s - %s' % (idx, match.group(1))

with open('data2', 'r') as f:
    matchs = pattern.finditer(f.read())
    for idx, match in enumerate(matchs):
        print '%s - %s' % (idx, match.group(1))


# delete times
# >>> import re
# >>> p = re.compile(ur"([a-zA-Z])(\1+)")
# >>> s = "abbbcccbba"
# >>> p.sub(ur"\1",s)
# 'abcba'
# >>> 

# >>> import re
# >>> p = re.compile(ur"([a-zA-Z])(\1*)")
# >>> s = "abbbcccbba"
# >>> p.sub(lambda m: m.group(1)+str(1+len(m.group(2))), s)
# 'a1b3c3b2a1'