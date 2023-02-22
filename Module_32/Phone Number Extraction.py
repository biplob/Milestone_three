import  re
text = "Please call us at +1 (555) 123-4567 for more information."
pattern = "\+\d{1,2} \(\d{3}\) [0-9]{3}-[0-9]{4}"
phone = re.search(pattern, text)
print(phone.group())