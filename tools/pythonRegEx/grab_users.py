# Matches "@" ,"." and ".se:" to replace desired string with the r'' option
# Saves the results in a new temp .txt file

import re

with open ('testuser.txt', 'r' ) as f:
    content = f.read()
    content_new = re.sub('@|\.se:|\.', r'\n', content, flags = re.M)

f = open("tmpuser.txt", "w")
print(content_new)
f.write(content_new)
f.close()
