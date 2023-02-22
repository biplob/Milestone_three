import re
text = "This  example of mulpule     space"
pattern = r'\s+'
new_text = re.sub(pattern, " ", text)
print(new_text)