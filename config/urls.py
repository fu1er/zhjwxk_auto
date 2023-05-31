# get validation image
IMAGE_URL = 'https://zhjwxk.cic.tsinghua.edu.cn/login-jcaptcah.jpg?captchaflag=login1'
# login page
LOGIN_URL = 'https://zhjwxk.cic.tsinghua.edu.cn/xklogin.do' 
# get JSESSIONID and serverid
COOKIE_URL = 'http://zhjwxk.cic.tsinghua.edu.cn/xsxk_index.jsp'
# post form
POST_URL = 'https://zhjwxk.cic.tsinghua.edu.cn:443/j_acegi_formlogin_xsxk.do'
# when successfully login, request this url and get http response 302, jump to the next url
ACCESS_URL = 'http://zhjwxk.cic.tsinghua.edu.cn/zhjw.do?m=xsxk_index'
# main page, need correct JSESSIONID, serverid
MAIN_URL = 'http://zhjwxk.cic.tsinghua.edu.cn/xkBks.vxkBksXkbBs.do?m=main'