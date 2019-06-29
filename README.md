# project objective: 

link shortening service Bitly

  * enter a long link, the output is an abbreviated link

  *  If the link is already shortened with the help of the service,we will get statistics of clicks on the link.

### Installation and setup:

Python3 should be already installed. 
Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```
    To interact with the Bitly service, you need a token

### How to get token.

   * Register for https://bit.ly via e-mail.
 
   * Link to generate token: https://dev.bitly.com/get_started.html
   
   * The token looks like the following string: 17c09e20ad155405123ac1977542fecf00231da7
 
   * In the folder with the downloaded repository, create a file .env (starting point is important).
 
   * Into a file .env register your token ```TOKEN=your token ```
 
 Example: 
     creating_a_shortened_link function in main.py
 
     At the entrance we submit a token and a link.
 
     The output is a short link.
 
Example of work:

![screenshot of sample](https://i7.wampi.ru/2019/06/30/shorte_the_link.gif)


* To run:  In command line:   ``` python main.py 'link' ```

The code is written for educational purposes on online-course for web-developers https://dvmn.org.
