# TgInfoSender

Чтобы воспользоваться скриптом вам понадобиться:

[[1]]
IP_ID и IP_HASH. Для их получения нужно:
1) Зайти на https://my.telegram.org/
2) Ввести ваш номер телефона -> next. На этот номер будет отправлено сообщение в Телеграм, который нам понадобится в следующем пункте.
3) После этого у Вас появится поле Confirmation code. В это поле Вам необходимо вставить код, который Вы получите в приложении Telegram На телефоне или компьютере и нажать на кнопку Sign In.
4) Далее нажимем на ссылку "API development tools"
5) Вам предложат создать новое приложение.
Заполняем поля по примеру:
App title: Любое название на английском языке
Shortname: Любая строчка на английском языке без пробелов! Длина от 5 до 32 символа
Url: Ссылка на любой сайт, который не является популярным
Platform: Desktop
Description: Придумайте любое описание
Нажимаем "Create application"
6) Если всё прошло хорошо, вы увидите страницу, на которой под заголовком App configuration находится IP_ID и IP_HASH

[[2]] 
Список пользователей, которым вы будете посылать сообщение. 
Cоздаете самый обычный список. Чтобы сообщение отправилось нужно заполнять список так:  
users = ['88005553535', '88001233232'....]                     
ИЛИ     
users = ['@Test_user1', 'TestUser2'....]   
ИЛИ   
users = ['Иван Иванов', 'Мария Сергеевна'....] !!! Но для этого человек должен быть в вашем списке контактов

--ПРИМЕР РАБОТЫ---
![image](https://user-images.githubusercontent.com/84981999/199223337-8795dbbb-620b-4b77-9fd9-681ce01c8a7d.png)
