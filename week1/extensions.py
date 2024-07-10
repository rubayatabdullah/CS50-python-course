
fileName = input('File name: ')

fileEx = fileName[-3:]

if fileEx == 'gif':
    print('image/gif')
elif fileEx == 'jpg':
    print('image/jpg')
elif fileEx == 'peg':
    print('image/jpeg')
elif fileEx == 'png':
    print('image/png')
elif fileEx == 'pdf':
    print('application/pdf')
elif fileEx == 'txt':
    print('text/plain')
elif fileEx == 'zip':
    print('application/zip')
else:
    print('application/octet-stream')
