import time
while True:
 print("****** How to👇 ******")
 print("")
 print("Format of putting date of birth is: ")
 print(" Day / month / year ")
 print(" For eg:\n 12 \n feb \n 1999")
 print("")
 print("")
#day
 x=0
 y=0
 z=0
 time.sleep(2)
 inp=int(input("Enter the day : "))
 if inp<=33:
  x= inp
 else:
   print("check your day!!")
 

#month
 print("")
 
 
 month=input("Enter month: ")
 month=month.lower()
 if month=="jan" or month=="january":
  y= 1
 elif month=="feb" or month=="february":
  y= 4
 elif month=="mar" or month=="march":
  y= 4
 elif month=="apr" or month=="april":
  y= 0
 elif month=="may":
  y= 2
 elif month=="june" or month=="jun":
  y= 5
 elif month=="july":
  y= 0
 elif month=="aug" or month=="august":
  y= 3
 elif month=="sep" or month=="september":
  y= 6
 elif month=="oct" or month=="october":
  y= 1
 elif month=="nov" or month=="november":
  y= 4
 elif month=="dec" or month=="december":
  y= 6
 else:
  print("Check the spelling!!:\n You can write both shortcut or full name of month\n For eg: jan or january 😊 ")
  
#year
 print("")
 
 time.sleep(1)
 year=input("Enter your birth year: ")
 if year=="1901" or year=="1907" or year=="1912" or year=="1918" or year=="1929" or year=="1935" or year=="1940" or year=="1946" or year=="1957" or year=="1963" or year=="1968" or year=="1974" or year=="1985" or year=="1991" or year=="1996" or year=="2002" or year=="2013" :
  z= 1
 elif year=="1902" or year=="1913" or year=="1919" or year=="1924" or year=="1930" or year=="1941" or year=="1947" or year=="1952" or year=="1958" or year=="1969" or year=="1975" or year=="1980" or year=="1986" or year=="1997" or year=="2003" or year=="2008" or year=="2014" :
  z= 2
 elif year=="1903" or year=="1908" or year=="1914" or year=="1925" or year=="1931" or year=="1936" or year=="1942" or year=="1953" or year=="1959" or year=="1964" or year=="1970" or year=="1981" or year=="1987" or year=="1992" or year=="1998" or year=="2009" or year=="2015" :
  z= 3
 elif year=="1909" or year=="1915" or year=="1920" or year=="1926" or year=="1937" or year=="1943" or year=="1948" or year=="1954" or year=="1965" or year=="1971" or year=="1976" or year=="1982" or year=="1993" or year=="1999" or year=="2004" or year=="2010":
  z= 4
 elif year=="1904" or year=="1910" or year=="1921" or year=="1927" or year=="1932" or year=="1938" or year=="1949" or year=="1955" or year=="1960" or year=="1966" or year=="1972" or year=="1977" or year=="1983" or year=="1988" or year=="1994" or year=="2005" or year=="2011" :
  z= 5
 elif year=="1905" or year=="1911" or year=="1916" or year=="1922" or year=="1933" or year=="1939" or year=="1944" or year=="1950" or year=="1961" or year=="1967" or year=="1978" or year=="1989" or year=="1995" or year=="2000" or year=="2006" :
  z= 6
 elif year=="1906" or year=="1917" or year=="1923" or year=="1928" or year=="1934" or year=="1945" or year=="1951" or year=="1956" or year=="1962" or year=="1973" or year=="1979" or year=="1984" or year=="1990" or year=="2001" or year=="2007" or year=="2012":
  z= 0
 
 a =(x+y+z)%7
 print("")
 print("")

 if a==1:
   print("You born on sunday")
 elif a==2:
  print("You born on Monday")
 elif a==3:
  print("You born on Tuesday")
 elif a==4:
  print("You born on Wednesday")
 elif a==5:
  print("You born on Thursday")
 elif a==6:
  print("You born on Friday")
 elif a==0:
  print("You born on Saturday")
 
 time.sleep(5)