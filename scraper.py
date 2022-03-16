from mysqlx import Column
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests

import time
import os


def download_video_series(video_links):
 
  for count,link in enumerate(video_links):
    
   # iterate through all links in video_links
    # and download them one by one
    #obtain filename by splitting url and getting last string
    file_name = link.split('/')[-1]  
 
    print ("Downloading file:%s"%file_name)
    if count==0:
        file_name="wide.mp4"
    elif count==1:
        file_name="square.mp4"
    elif count==2:
        file_name="vertical.mp4"
    else:
        pass
    #create response object
    r = requests.get(link, stream = True)
 
    #download started
    with open(file_name, 'wb') as f:
      for chunk in r.iter_content(chunk_size = 1024*1024):
        if chunk:
          f.write(chunk)
 
    print ("%s downloaded!\n"%file_name)
 
  print ("All videos downloaded!")
  return

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://invideo.io/workflow/marketing-templates/categories")
time.sleep(12)
driver.find_element_by_class_name('btn-cta').click()

time.sleep(17)

while True:
    videos=driver.find_elements_by_class_name('ng-trigger-myInsertRemoveTrigger')
    actions = ActionChains(driver)
    actions.move_to_element(videos[-1])
    actions.click(videos[-1])
    actions.perform()
    time.sleep(5)
    videos1=driver.find_elements_by_class_name('ng-trigger-myInsertRemoveTrigger')
    if len(videos1) == len(videos):
        break
videos=driver.find_elements_by_class_name('ng-trigger-myInsertRemoveTrigger')
print(len(videos))
for video in videos:
    actions = ActionChains(driver)
    actions.move_to_element(video)
    actions.click(video)
    actions.perform()
    time.sleep(7)
    wide=driver.find_element_by_tag_name('video').get_attribute("src")

    column=driver.find_elements_by_class_name('dimension-column')
    column[1].click()
    time.sleep(8)
    square=driver.find_element_by_tag_name('video').get_attribute("src")
    column[2].click()
    time.sleep(7)
    vertical=driver.find_element_by_tag_name('video').get_attribute("src")

    foler_name=driver.find_element_by_class_name('template-details').text
    print(str(os.getcwd())+'\\'+foler_name)
    try:

        os.mkdir(str(os.getcwd())+'\\'+foler_name)
    except:
        pass
    localpth=str(os.getcwd())
    l=[wide,square,vertical]
    os.chdir(str(os.getcwd())+'\\'+foler_name)
    download_video_series(l)
    os.chdir(localpth)