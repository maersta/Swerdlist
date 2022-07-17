# Matches the line text before the password part and replace desired string with the r'' option
# Saves the results in a new temp .txt file

import re
with open ('testpass.txt', 'r' ) as f:
    content = f.read()
    content_new = re.sub('\w+(.+):', r'', content, flags = re.M)

f = open("tmppass.txt", "w")
f.write(content_new)
f.close()
print("Done")
