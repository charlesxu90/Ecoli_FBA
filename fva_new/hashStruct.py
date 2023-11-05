# This defines a function allowing creating a
# data struct similar to Perl Hash
##################################
#Author: xiaopeng xu
#Email: charlesxu90@gmail.com
##################################
# Define classes

class AutoVivification(dict):
    '''Implementation of perl's autovivification feature.'''
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value
