# requires dropbox python sdk (pip install dropbox); BeautifulSoup; urllib2
import bs4, urllib2, dropbox
# sign in with Dropbox and delete everything in your directory
# you'll need to setup an app and generate an access token in your Dropbox interface, and paste the token here
client=dropbox.client.DropboxClient(TOKEN_FILE_HERE)
oldfile=client.metadata('/WWD')['contents'][0]['path']
delo=client.file_delete(oldfile)
# pull the latest PDF from WWD.com
response=urllib2.urlopen('http://www.wwd.com')
data=response.read()
soup=bs4.BeautifulSoup(data)
next=soup.find('a',class_='stat-tntoday-download').get('href')
response2=urllib2.urlopen(next)
data2=response2.read()
soup2=bs4.BeautifulSoup(data2)
next=soup2.find('a',class_='pdf').get('href')
response3=urllib2.urlopen(next)
# store it in Dropbox
upload=client.put_file('/WWD/'+next.split('/')[-1],response3.read())
response3.close()
# IfTTT will then push to Kindle; cron this to run every morning