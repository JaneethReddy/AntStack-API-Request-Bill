Pre Requisites:

  -Python
  
  -Postman ([Download From Here](https://www.postman.com/downloads/))
  - Virtualenv package installed
Steps to Run app:
  - Use any Editor that contains a terminal to work with(I will be using Git Bash to explain the following steps)
  - Clone my git repository
  - Move to my repository folder
  - In terminal type virtualenv env
  - Source the virtual environment using `source env/Scripts/activate`
  - Install required packages using `pip3 install -r requirements.txt`
  - Run app using `flask run`
  - Open Postman app to post json api requests to our app
  - Give required details in the postman tab as shown in the reference image by me
  - Info given:
    - Under =='Enter request URL'== give flask localhost ip
    - Select =='Post'== method
    - Under =='Body'== select *raw* & *json* as text
    - Then click on **Send**
    - You can see the required Bill Reciept under 'Response' tab
  
