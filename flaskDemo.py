#coding=utf8
import sys;'qgb.U' in sys.modules or sys.path.append('G:/QGB/babun/cygwin/lib/python2.7/');from qgb import *;py=U.py
sys.path.pop()

from flask import Flask,request,make_response,json
app = Flask(__name__)
app.static_folder='..'

from bilibili_comment import spider

giav=0

@app.route('/<f>', methods=['GET'] )
def staticFile(f):
	'''app.static_folder default is "pwd/static
	'''
	# U.log(request)
	# U.ipyEmbed()()
	return app.send_static_file(f)

@app.route('/', methods=['POST','GET'] )
def index():
	'''  在谷歌搜索页面控制台无法发送请求？？？？？？ 一直为 Pending   yandex浏览器
	'''
	global giav
	U.log(request)
	U.log(request.get_data())
	
	html='''
<title>Bilibili弹幕抓取</title>
<img height="199" width="444" src="/logo.png">
<form action="/" method="post">
	<input name="a" type="text" size="40" placeholder="请输入 B站视频地址 或者 av号"> 
	<input type="submit"  value="确定">
</form>
<textarea  readonly="readonly">{}</textarea>
'''
	if request.method=='GET':
		return make_response(html.format(  spider(giav)  ))
	else:
		a=request.form['a']
		a=a.lower()
		i=a.find('av')
		if i>-1:
			a=a[i+2:]
			r='0'
			for i in a:
				try:
					int(r+i)
					r+=i
				except:break;		
			giav=int(r)
		else:
			try:giav=int(a)
			except:return '视频地址错误 %s \n giav %s'%(a,giav)
		return make_response(html.format(  spider(giav)  ))
		
# key=r'G:\QGB\software\xxnet\data\gae_proxy\Certkey.pem'
# crt=r'G:\QGB\babun\cygwin\home\qgb\chromExt\tabList\lk.lk.crt'
# ka={'port':443,'host':'0.0.0.0','ssl_context':(crt,key)}
ka={'port':1212,'host':'0.0.0.0'}
if __name__=='__main__':
	app.run(**ka,debug=1)