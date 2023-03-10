import re
from googletrans import Translator, constants

translator = Translator()
count1=0
f = open(r"C:\Users\andre\Downloads\class\collections.htm","rt",encoding="utf8") #mentioning the file directory which i want to translate
string=f.read()
special=[";",">","<",]  
links=re.findall('>(.*?)<',string)
for link in links:
    if (link.count("@")==0) and len(link)>2 and link.count(">")==0 and link.count("<")==0: #to avoid translating the html tags
        try:  #sometime because of the large statement, got error from the google translator end as a timeout. to avoid this i have written inside try block.
            translation = translator.translate(link, dest="hi")
            string=string.replace(link,translation.text) #after translating, i am replacing the string on the same file
            #print(translation.text)
            f.close()
            f = open(r"C:\Users\andre\Downloads\class\collections.htm","wt",encoding="utf8")
            f.write(string)
            f.close()
        except:
            string=string.replace(link,link)
            f.close()
            f = open(r"C:\Users\andre\Downloads\class\collections.htm","wt",encoding="utf8")
            f.write(string)
            f.close()
            