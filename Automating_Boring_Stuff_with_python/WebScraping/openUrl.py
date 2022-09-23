import webbrowser

print('You can try:')
print('https://www.google.com/')
print('')

link = input('Enter complete link(including https://) :')
webbrowser.open(link)       # will open link in you default browser