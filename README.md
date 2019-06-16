:bomb:
**project objective:**
Shortening a long link to a short one and getting the number of clicks on a short link.

For the reduction we use website bit.ly

**Installation and setup:**
To work with bit.y needs the token.
The token looks like the following string: 17c09e20ad155405123ac1977542fecf00231da7
How to get token.
 1)Register for https://bit.ly via e-mail.
 2)Link to generate token :https://dev.bitly.com/get_started.html
Creating a shortened link:
 Address: https://api-ssl.bitly.com/v4/bitlinks method POST send request.
 Request body: long_url (required)- the long link you want to shorten.
 For authorization using OAuth 2, you need to add to the HTTP request header Authorization: Bearer Wastaken.
 
 Example: creating_a_shortened_link function in main.py
 At the entrance we submit a token and a link.
 The output is a short link.
 
 Response example:

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

pip install -r requirements.txt

The code is written for educational purposes on online-course for web-developers dvmn.org.

***********************************************

**Цель проекта:**
Сокращение длинной ссылки до короткой и получение количества переходов по короткой ссылке.

Для сокращение используем сайт bit.ly

**Установка и настройка**
Для работы с bit.y нужен токен.
Токен выглядит как строка наподобие следующей: 17c09e20ad155405123ac1977542fecf00231da7
Как получить токен.
  1)Регистрируйтесь на https://bit.ly через e-mail.
  2)Ссылка для генерации токена :https://dev.bitly.com/get_started.html
Создание укороченной ссылки:
  На адрес: https://api-ssl.bitly.com/v4/bitlinks методом POST отправляем запрос.
  Тело запроса: long_url (обязательный)- длинная ссылка, которую вы хотите сократить.
  Для авторизации с помощью OAuth 2 нужно добавить к запросу HTTP-заголовок Authorization: Bearer ВашТокен.
  
  Пример: функция creating_a_shortened_link в main.py
    На вход мы подаём токен и ссылку.
    На выходе получаем короткую ссылку.
  
  Пример ответа:
    
  

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

  pip install -r requirements.txt
  
Для запуска:
  В командной строке:python main.py 'link'

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
