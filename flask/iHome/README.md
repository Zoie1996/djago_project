第一天：

用户模块：

	1. 注册(演示)
		用户名，密码，重复密码
		POST  /use/register/
		# 1. 验证数据完整性
		# 2. 验证手机号码的正确性
		# 3. 验证密码
		# 4. 保存用户数据
	
	2. 登录(演示)
		用户名，密码，校验密码
		POST /user/login/
			mobile
			password
	
		# 1.验证数据完整
		# 2.验证手机正确性
		# 3.验证用户
		# 4.校验密码
		# 5.验证用户成功
	
	3. 装饰器(作业)
		验证登录与否
	
	4. 上传头像(演示)
		图片上传，图片展示，修改用户名
	
	5. 注销(作业)
		删除session中的值

项目搭建：

	1. 环境virtualenv
		virtualenv --no-site-packages ajenv
	2. 激活环境
		windows:
			cd ajenv/Script
			activate / deativate
		linux,mac
			source ajenv/Script/bin/activate
	3. 并安装flask
		1）pip3 install flask
	
		2)创建需要安装环境的txt文件
		  requeirement.txt中加入flask
	
		  pip install -r requirement.txt
	4. 一个最小的web
	
		from flask import Flask
	
		app = Flask(__name__)
	
		@app.route('/')
		def hello():
			return 'hello world'
	
		if __name__ == '__main__':
			app.run()
	
	5. MVC思路拆分项目
	
	6. pycharm配置
		setting中python解释器指定
	
		debug模式的配置文件配置，启动方式修改
		python xxx.py runserver -p -h -d









