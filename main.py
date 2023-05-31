from kernel import engine
from user.user import *

if __name__=="__main__":
    kernel = engine.Engine(USERNAME, PASSWORD)
    kernel.login()
    kernel.set_browser_cookie()
    kernel.access_mainpage()
    # while 1:
    #     pass