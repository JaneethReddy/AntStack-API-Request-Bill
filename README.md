<h3>Pre Requisites: <br>

  -Python3 <br>
  - Virtualenv package installed <br>
  
  -Postman ([Download From Here](https://www.postman.com/downloads/))  <br>
  
 
 Steps to Run app: <br>
  - Use any Editor that contains a terminal to work with(I will be using Git Bash to explain the following steps) <br>
  - Clone my git repository (`git clone https://github.com/JaneethReddy/AntStack-API-Request-Bill.git`) <br>
  - Move to my repository folder <br>
  - In terminal type `virtualenv env` <br>
  - Source the virtual environment using `source env/Scripts/activate` <br>
  - Install required packages using `pip3 install -r requirements.txt` <br>
  - Run app using `flask run` <br>
  - Open Postman app to post json api requests to our app <br>
  - Give required details in the postman tab as shown in the reference screenshot image by me <br> </h3> 
  
  ![Reference Screenshot](https://github.com/JaneethReddy/AntStack-API-Request-Bill/blob/2afbc32515613be47d71b50500c27dc9ad3415eb/Screenshot%20(186).png)  <br>
  
  
  >- Info given: <br>
  >
    - Under 'Enter request URL' give flask localhost ip <br>
    
    - Select 'Post' method <br>
    
    - Under 'Body' select -raw & then -json as text <br>
    
    - Then click on 'Send' <br>
    
    - You can see the required Bill Reciept under 'Response' tab <br>
  
