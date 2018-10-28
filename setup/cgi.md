 # setting up CGI on AWS 
 
`sudo a2enmod cgi`  
`sudo systemctl restart apache2`  
`sudo vi /usr/lib/cgi-bin/test_script`  

 ```
 -----------Copy and Paste the Script to this file---------
                  #!/usr/bin/env python
                  print "Content-type: text/html\n\n"
                  print "Hello"
------------End File--------------------------------------
 ```

`sudo chmod 705 /usr/lib/cgi-bin/test_script`  
  
Test that script works by curling content    
`curl http://localhost/cgi-bin/test_script`  

or by going to your webbrowser and navigaing to  
`yoururl/cgi-bin/test_script`  

Change permissions so that the project group users can edit files in the cgi-bin directory  
`cd /usr/lib/`  
`sudo chgrp -R djmm cgi-bin`    
`sudo chmod -R g+w cgi-bin/`  
