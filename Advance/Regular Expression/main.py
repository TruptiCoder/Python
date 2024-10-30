import re

pattern = r"[A-Z]+yclone"
text = '''Wikipedia[c] is a free content online encyclopedia written and maintained by a community of volunteers, known Cyclone, Dyclone as Wikipedians, through open collaboration and the wiki software MediaWiki. Wikipedia is the largest and most-read reference work in history,[3][4] and is consistently ranked among the ten most visited websites; as of August 2024, it was ranked fourth by Semrush,[5] and seventh by Similarweb.[6] Founded by Jimmy Wales and Larry Sanger on January 15, 2001, Wikipedia has been hosted since 2003 by the Wikimedia Foundation, an American nonprofit organization funded mainly by donations from readers.[7]
'''
# match = re.search(pattern, text)
# print(match)

match = re.finditer(pattern, text)
for m in match:
    print(text[m.span()[0]:m.span()[1]])

# metacharacters in regular expression
# [] represents a chracter class 
# ^ matches the beginning
# $ matches the end
# . matches any character except newline
# ? matches zero or one occurrence.
# | means OR {matches with any of the characters seperated by it.}
# * Any number of occurrences (including 0 occurrences)
# + one ore more occurrences
# {} Indicate number of occurrences of a preceding RE to match
# () Enclose a group of REs