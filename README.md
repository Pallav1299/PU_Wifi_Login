# PanjabUniversity_Wifi_Login
Logging in to PU wifi on laptop using the conventional Panjab University wifi login page, is so boring. I have been using this simple method for quite a while now. It saves time and effort.

I found a very useful python script available online on GeeksForGeeks. It is being used for logging into facebook.
With a little tinkering I changed this script to login into Panjab University wifi, using my wifi login-ID and password.
This script uses some handy third party open-source packages like "Selenium".

Selenium automates and controls browsers and it’s activity. We can code in our way to control browser tasks with the help of selenium. Primarily, it is for automating web applications for testing purposes, but is certainly not limited to just that. Boring web-based administration tasks can be automated as well. As you learn more it’s so much fun to see things happening automatically and saving time in doing useless tasks again and again.

We use selenium here to open the site of our requirement (in this case Facebook) and there we inspect element across email box, password box and login button to find id of them.

-> Using find_element_by_id() function provided by selenium module, we can find the required element (username box, password box, login
button.
-> Using send_keys() function, provided by selenium module, we will send the data into the box.


# Settings for windows:
