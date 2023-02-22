import re
email_sentence = "Get Rich Quick! Invest in our Stock now!"
pattern = r'ivest|rich|stock|money|quick'
match = re.search(pattern, email_sentence, re.IGNORECASE)

if match:
    print('Spam Email')
else:
    print('Not Spam Email')