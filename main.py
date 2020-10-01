import requests
import bs4 

url=input("Enter your url: ")
response = requests.get(url)
#Below given is an extra testing section.
#print(type(response))
#print(response.text)
filename="temp.html"
bs = bs4.BeautifulSoup(response.text,"html.parser")

formatted_text = bs.prettify()
print(formatted_text)

with open(filename,"w+") as f:
    f.write(formatted_text)

list_div = bs.find_all('div')    
print(list_div)
no_of_div = len(list_div)

list_as = bs.find_all('a')
no_of_as = len(list_as)

print("Number of content :",list_div)
print("Number of as :", no_of_as)
