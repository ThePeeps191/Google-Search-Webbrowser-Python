def search(keyword):
	k = str(keyword).replace(" ", "+")
	return "https://google.com/search?q="+k
  
import webbrowser

webbrowser.open(search("the peeps191"))
