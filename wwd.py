# requires dropbox python sdk (pip install dropbox); BeautifulSoup; urllib2
import bs4, urllib2, dropbox
from datetime import date
# sign in with Dropbox and delete everything in your directory
# you'll need to setup an app and generate an access token in your Dropbox interface, and paste the token here
client=dropbox.client.DropboxClient(TOKEN_FILE_HERE)
oldfile=client.metadata('/WWD')['contents'][0]['path']
delo=client.file_delete(oldfile)
# pull the latest PDF from WWD.com
d=date.today()
y=d.strftime('%Y')
m=d.strftime('%m')
da=d.strftime('%d')
z='https://pmcwwd.files.wordpress.com/'+y+'/'+m+'/wwd'+m+da+'web.pdf'
response=urllib2.urlopen(z)
# store it in Dropbox
upload=client.put_file('/WWD/'+z.split('/')[-1],response.read())
response.close()
# IfTTT will then push to Kindle; cron this to run every Weds morning