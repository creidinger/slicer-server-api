'''
    Test
'''
import os
import logging
import django

logging.basicConfig(filename='slicer.log', level=logging.DEBUG)

logging.info( "slicer starting" )
print(django.get_version())

# var = input("slicer input ")
# print (var)

# env = os.environ
# contents = os.listdir('.')

# print(env)
# for e in env:
#     print(e)
#     pass

# print("")

# print(contents)
# for i in contents:
#     print(i)
#     pass


# os.mkdir('test')
# os.rmdir('test')
