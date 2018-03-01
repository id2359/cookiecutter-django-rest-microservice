# {{cookiecutter.project_name}}
{{cookiecutter.project_short_description}}

# 部署前须知
1. 项目部署时会启动三个容器：
    1. django后端服务
    2. celery beat
    3. celery worker
2. 目前使用docker-compose进行容器编排
3. 请参照example.env文件在项目根目录生成.env文件，将其中的各环境变量做相应修改
4. 一切准备就绪好之后运行
	```bash
	docker-compose build && docker-compose up -d
	```
5. 容器基础镜像继承自alpine:3.6， python版本3.6

# 开发须知
1. 参照config/settings/local.py.example文件生成config/settings/local.py文件，根据本地环境对其中各项字段修改
2. 安装项目依赖: ``` pip install -r requirements/local.txt```(需要python3.6以上)
3. 数据库迁移```python manage.py makemigrations && python manage.py migrate```
4. 根据项目别，运行必要的初始化脚本 ```python manage.py initialize```，具体执行任务参照```api/managements/commands/initialize.py```

