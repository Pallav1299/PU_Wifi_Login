# PanjabUniversity_Wifi_Login

Logging in to PU wifi on laptop using the conventional Panjab University wifi login page, is so boring. I have been using this simple method for quite a while now. It saves time and effort.

I found a very useful python script available online on GeeksForGeeks(https://www.geeksforgeeks.org/facebook-login-using-python/). It is being used for logging into facebook.
With a little tinkering I changed this script to login into Panjab University wifi, using my wifi login-ID and password.
This script uses some handy third party open-source packages like "Selenium".

Selenium automates and controls browsers and it’s activity. We can code in our way to control browser tasks with the help of selenium. Primarily, it is for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can be automated as well. As you learn more it’s so much fun to see things happening automatically and saving time in doing useless tasks again and again.

We use selenium here to open the site of our requirement (in this case Facebook) and there we inspect element across email box, password box and login button to find id of them.

-> Using find_element_by_id() function provided by selenium module, we can find the required element (username box, password box, login
button.
-> Using send_keys() function, provided by selenium module, we will send the data into the box.

# SETTING UP:-
 # Download the necessary third party modules/packages:
  # Selenium Module:
         Using pip:
          pip install -U selenium
         Using conda:
          conda install selenium
          
    Additional Requirement : geckodriver for firefox (https://github.com/mozilla/geckodriver/releases/tag/v0.24.0) 
                             chromedriver for chrome (http://chromedriver.chromium.org/downloads)
  # Note: download the geckodriver/chromedriver according to your OS(linux32/linux64/windows32/windows64/macos)

# UNDERSTANDING THE SCRIPT:-
  
 # 1. Importing necessary modules
  
    Selenium : to automate browser
    Time : to pause running of script for some seconds as browsers try to detect automation stuff if we input too fast

 # 2. Providing the username and password:
    a) Provide your username and password in the script.
    b) Provide it using input() function of python.
   # *I'ld prefer option (a) for faster login.*
   
 # 3. Opening browser and required website
     webdriver.Chrome()/webdriver.Firefox() will open new window of chrome/firefox, respectively. We will save it’s object in variable 
     named "driver".
     Now using "get" function we will open up Panjab University Wifi login website(https://securelogin.pu.ac.in/cgi-bin/login?cmd=login&mac=a0:af:bd:ab:52:34&ip=172.16.178.36&essid=PU%40CAMPUS&apname=UIET_BLK1_1F_L1&apgroup=PU-AP-UIET&url=http%3A%2F%2Fbit%2Edo%2FWifion)
     
 # 4. Finding element for sending data and Sending input
    Use inspect element tool on the element of browser of which you want to find id. In this case we will inspect username box, password
    box, login button to find their id. And then use this id combining with selenium function find_element_by_id() and
    find_element_by_name(), to find it across webpage and save it in variables for later use. Then by using send_keys() we will send
    data across the elements found previously.
    
 # 5. Closing the browser
    After all of the above steps we have to quit the session and will be achieved by using driver.quit().
    Note: Here driver is the name of variable you chose for webdriver.Chrome()/webdriver.Firefox().

# For running the script through Terminal/Command prompt:
  # For Windows:-
   Create a new file, wherever you find it convenient. Copy the content of "windows_bat_file" into it and save it with a ".bat"
   extension.
  # Provide correct exact path to the python script in this bat file.
   Copy this .bat file wherever you find it convenient.(I keep it on the desktop).
   
  # For Linux/macOS:-
   For running the python script through terminal, we need to create a bash script which takes the path to the python script and the
   location to the python interpreter.
   Copy this bash script wherever you find it convenient.(I keep it in the Home directory).
  # Please make sure to provide the right path to the python script in the bash script. 
   
   
   
   
