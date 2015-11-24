# requires dropbox python sdk (pip install dropbox); BeautifulSoup; urllib2
import bs4, urllib2, dropbox
from datetime import date
# sign in with Dropbox and delete everything in your directory
# you'll need to setup an app and generate an access token in your Dropbox interface, and paste the token here
client=dropbox.client.DropboxClient(TOKEN_FILE_HERE)
oldfile=client.metadata('/WWD')['contents'][0]['path']
delo=client.file_delete(oldfile)
# pull the latest PDF from WWD.com
opener = urllib2.build_opener(
    urllib2.HTTPRedirectHandler(),
    urllib2.HTTPHandler(debuglevel=0),
    urllib2.HTTPSHandler(debuglevel=0)
)
opener.addheaders = [
    ('User-agent', ('Mozilla/4.0 (compatible; MSIE 6.0; '
                   'Windows NT 5.2; .NET CLR 1.1.4322)'))
]
html = opener.open("http://www.wwd.com")
soup = bs4.BeautifulSoup(html)
link = soup.find(class_="pub-pdf")['href']
html = opener.open(link)
soup = bs4.BeautifulSoup(html)
z = soup.find(class_="pdf")['href']
response=urllib2.urlopen(z)
# store it in Dropbox
upload=client.put_file('/WWD/'+z.split('/')[-1],response.read())
response.close()
# IfTTT will then push to Kindle; cron this to run every Wednesday morning
