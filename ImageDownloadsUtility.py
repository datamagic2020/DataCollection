

import urllib.request
import pandas as pd

# load all URLs excel file
#replace image urls excel file name with your file name
data = pd.read_excel(r'image_urls.xlsx')


# check size of data
print(data.shape)

# get all URLs from loaded data
# 'image' is the name of column which contains my url link in excel file.
urls = data['image']

#set counter for unique filenames
count = 1
#skip these images
substring = 'photo_unavailable500';

#security check issue fix
opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36')

#iterate over each url
for url in urls:  
    # only process available images     
    if str(url).find(substring) == -1:
        # download image from url
        # dataset is folder where my images will be stored you can provide your own folder name. Create folder before using it here.        
        filename, headers = opener.retrieve(url, "./dataset/"+str(count)+".jpg")    
        count = count + 1    
        print(url," Downloaded...")   
    
    import urllib.request
   
print("Download Finished...")

