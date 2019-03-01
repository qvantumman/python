import pyperclip

text = pyperclip.paste()

stroca=text.split('\n')
for i in range(len(stroca)):
    stroca[i] = '* ' +stroca[i]
text='\n'.join(stroca)
pyperclip.copy(text)
