#!bin/python
import datetime

def pyglatin(original):
	pyg = 'ay'
  	word = original.lower()
	first = word[0]
	rword = ''
        index = len(word)
        while index > 0:
        	rword += word[index-1]
        	index = index - 1
	word = rword
  	new_word = word + first + pyg
	#new_word = new_word[1:len(new_word)]
	return new_word


original = raw_input('Enter a word:')
print "You have entered" + original

"""
conditional check for doing the pyglatin transformation
"""
if len(original) > 0 and original.isalpha():
  new_word = pyglatin(original)
  print "Customized pyglatin is " + new_word + " at time : " + str(datetime.datetime.now())
else:
  print 'empty'
