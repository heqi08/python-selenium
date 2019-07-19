# python-selenium


--------
Page Object Model automation test selenium
--------


------
Setup 
------

The setup has 4 parts:

1. Prerequisites 
2. Setup for GUI/Selenium automation
3. How to run test cases
4. Code


__1. Prerequisites__

a) Install Python 3.x

b) Add Python 3.x and chromedriver and geckodriver to your PATH environment variable

c) If you do not have it, get pip (NOTE: Most recent Python distributions come with pip)

d) Input command in terminal : pip install pipenv 
####Note: Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.
   > [pipenv homepage](https://github.com/pypa/pipenv)

e) git clone this project, and go to root, run command pipenv install, all the dependencies will install automatically. 


__2. Setup for GUI/Selenium automation__
 

a) Get setup with your browser driver. If you don't know how to, please try:

   > [For Chrome](https://sites.google.com/a/chromium.org/chromedriver/getting-started)

   > [For Firefox]( https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver)
   	
#Note: Check Firefox and chrome version & Selenium version compatibility before downloading geckodriver.

__3. How to run test cases__

a) Environment url setting are in config.ini
path as /Config/config.ini

b) entrance.py is the main for unittest, you can run different test cases via command line.


__4. Code__

a) /framework/base_page.py it's the base class, and include public method.

b) /pageobject folder include each page class.

c) /testsuites folder include test cases corresponding pageobject.

d) /logs folder include log function and logs saved.

e) /report folder include test report saved here.

f) Pipfile and Pipfile.lock are pipenv file include dependencies information.