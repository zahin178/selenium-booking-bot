# selenium-booking-bot
This repo consists python-selenium based web crawler to crawl the Booking.com website. The user has to input some basic info like destination, check-in and check-out dates etc and the output will be an excel file with all the available hotel names with their rating, review number and distance from the location.

# How to use

- Find the version of your chrome browser by typing chrome://version/ in the url
- After identifying the browser version go to the following link and download the chromedriver zip file which has the same version as your browser
https://chromedriver.storage.googleapis.com/index.html
- Now create a folder named "SeleniumDrivers" like the following path
C:/Program Files/SeleniumDrivers
- Extarct the zip file into the C:/Program Files/SeleniumDrivers folder
- clone the repo
- go to the selenium-booking-bot folder
- create a virtual environment | python -m venv venv
- activate the virtual environment | venv\Scripts\activate
- install all the packages using the requirements.txt file | pip install requirements.txt
- create a folder named "outputs"
- run the following command

  `python run.py -c "<currecny>" -d "<destination>" -ci "<check-in date>" -co "<check-out date>" -an <numbe of adults> -cn <number of children> -ca "<age of child 1> <age of child 2>..." -rn  <room number>`

  Here is a sample command

  `python run.py -c "BDT" -d "coxs bazar" -ci "29112022" -co "12122022" -an 5 -cn 2 -ca "13 12" -rn 3`
  
# Outputs
  
In the outputs folder the excel file will be created with the destination name.

<img src="https://github.com/pythonboy178/selenium-booking-bot/blob/master/images/image_1.JPG">

Each file conatian hotel names, their scores in the website, the number of reviews given to them and their corresponding distannce

 <img src="https://github.com/pythonboy178/selenium-booking-bot/blob/master/images/image_2.JPG" width=800>
 
# Warning

You may get the following line as the output when you run the command

`Could not find the desired element, Please run again!`

If you get the above message in the command prompt please run the command again. It may take 3-4 times to load teh webpage correctly.

