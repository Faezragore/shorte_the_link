project objective:
=====================
    Shortening a long link to a short one and getting the number of clicks on a short link.

    For the reduction we use website bit.ly.
    
    If the link is already shortened with the help of the service,we will get statistics of clicks on the link.

### Installation and setup:

    To work with bit.ly needs the token.

    The token looks like the following string: 17c09e20ad155405123ac1977542fecf00231da7

### How to get token.

    1)Register for https://bit.ly via e-mail.
 
    2)Link to generate token: https://dev.bitly.com/get_started.html
 
   **Creating a shortened link: **
   
     Address: https://api-ssl.bitly.com/v4/bitlinks method POST send request.
     Request body: long_url (required)- the long link you want to shorten.
 
     For authorization using OAuth 2, you need to add to the HTTP request header
 
   **Authorization: Bearer Wastaken.**
 
 Example: 
     creating_a_shortened_link function in main.py
 
     At the entrance we submit a token and a link.
 
     The output is a short link.
 
Example of work:

![screenshot of sample](https://wampi.ru/image/6W9Ttk4)


Python3 should be already installed. 
Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```

* To run:  In command line:   ``` python main.py 'link' ```

The code is written for educational purposes on online-course for web-developers https://dvmn.org.
