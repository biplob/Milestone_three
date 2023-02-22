import re
text = '<p>This is paragraph.</p><h2>This is first heading.</h2>'
pattern = '<.*?>'
new_text = re.sub(pattern, '', text)
print(new_text)