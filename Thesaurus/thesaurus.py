# This is command-line text-based English thesaurus
# First Application from The Python mega Course

import json
import sys
from pprint import pprint

class Thesaurus:
	def __init__(self, data):
		self._data = data

	def translate(self, keyword):
		if not isinstance(keyword, str):
			raise ValueError("Keyword must be a word")
		# self.keyword = keyword
		if not keyword in self._data:
			raise KeyError(f"Can't find {keyword}")

		return self._data[keyword]


with open("data.json", "r")as datafile:
	data = json.load(datafile)

thesaurus = Thesaurus(data)

for word in sys.argv[1:]:
	print(f"\n{word}: ")
	try:
	    results = thesaurus.translate(word)
	    pprint(results)
	except:
		pass
