try:
    ## import numpy
    import pyperclip
except ImportError:
    print('Library import not successful, check install')
else:
    print('Library sucessfully imported')
finally:
    print('Excuting Finally - Import code has run')
