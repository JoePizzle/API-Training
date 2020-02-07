#!/user/bin/python3

#global of our API ROOT of the website.  Use Google extension JSON Viewer on the webites api list.
BASEURL = "https://anapioficeandfire.com/api/"

# Python -m pip install requests
import requests #used to fetch api data from a web address

def main():
#send an HTTPS GET and the save the response
# apiLookUp Lookup API lets your client applications send requests to the Safe Browsing servers to check if URLs are included on any of the Safe Browsing lists
	apiLookUp = requests.get(f"{BASEURL}books") #fetching the books dictionary with {} page of the aforementioned url
	# recast apilookup as a pythonic lists and dictionarties created by convertin
	# attached JSON from the api website
	# loads JSON-encoded data from the server using a GET HTTP request
	apiLookUp = apiLookUp.json()

	#loop accross our data
	#the following catagories are listed on the api book page. 
	for book in apiLookUp:
		#print(book["name"])
		#print(book["numberOfPages"])
		#print(book["authors"])
		#print(book["released"])
		# to remove brakets in the python output, add a [0] thread. 0 calls the first word
		print(f'{book.get("name")} by {book.get("authors")[0]} has {book.get("numberOfPages")} pages and was released on {book.get("released").split("T")[0]}')

if __name__ == "__main__":
	main()

