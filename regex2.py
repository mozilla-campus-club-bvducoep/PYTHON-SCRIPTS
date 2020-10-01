Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> fonReg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> fonReg
re.compile('\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d')
>>> #findall() does not returns Match but returns all the charaters matching the given pattern
>>> resume = '''
sdwr3rf w 123-444-5656 qiodswhduwncjnc jcebfiuebfhe  ebfuiebfiej ciudf
efjihifnfndf
foefjoiefnefe
feiofewnfoiewmfe
fewjoifnewiofew

123-555-9234
aojdiwj
'''
>>> fonReg.search(resume)
<re.Match object; span=(11, 23), match='123-444-5656'>
>>> fonReg.findall(resume)
['123-444-5656', '123-555-9234']
>>> 
>>> 
>>> 
>>> #in findall() method if the pattern has some groups in it then it will return list of tuples
>>> fonReg = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
>>> fonReg.findall(resume)
[('123-444-5656', '123', '444-5656'), ('123-555-9234', '123', '555-9234')]
>>> 
>>> 
>>> 
>>> 
>>> #Character Class
>>> 
>>> 
