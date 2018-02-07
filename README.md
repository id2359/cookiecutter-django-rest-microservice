# cookiecutter-django-rest-microservice
cookiecutter-django-rest-microservice

TODO: 使用django-channels 替代celery执行异步任务，并提供websocket支持，
对于定时任务:
    1. 编写任务脚本，app/management/commands 内加入自定义命令
    2. Docerfile中直接写入crontab执行相应脚本
