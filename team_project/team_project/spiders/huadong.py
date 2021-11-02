from selenium import webdriver
from selenium.webdriver import ActionChains
import time
bro=webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
bro.implicitly_wait(10)

#切换frame（很少）
bro.switch_to.frame('iframeResult')
div=bro.find_element_by_xpath('//*[@id="draggable"]')

# 1 生成一个动作练对象
action=ActionChains(bro)
# 2 点击并夯住某个控件
action.click_and_hold(div)
# 3 移动（三种方式）
# action.move_by_offset() # 通过坐标（x,y）
# action.move_to_element() # 到另一个标签
# action.move_to_element_with_offset() # 到另一个标签，再偏移一部分


for i in range(5):
    action.move_by_offset(10,10)

# 4 真正的移动
action.perform()

# 5 释放控件（松开鼠标）
action.release()

async def login():
    for res in setting.user:
        try:
            username = res[0]
            password = res[1]
            # headless参数设为False，则变成有头模式
            browser = await launch(
                {'headless': False}
            )
            # 打开一个页面
            page = await browser.newPage()
            await page.setViewport(viewport={'width': 1280, 'height': 800})

            res = await page.goto('https://captcha1.scrape.center/', options={'timeout': 10000})             #修改网站
            await page.type('#fm-login-id', username)                                                        #修改用户名对象
            await page.type('#fm-login-password', password)                                                  #修改密码对象
            await page.waitFor(1000)  # 等待时间

            slider = await page.querySelector('#geetest_slider_button')  # 是否有滑块                                     #修改滑块名
            if slider:
                try:
                    print('有滑块')
                    await page.hover('#geetest_slider_button')  # 不同场景的验证码模块能名字不同。                        #修改滑块名
                    await page.mouse.down()
                    await page.mouse.move(2000, 0, {'delay': random.randint(1000, 2000)})
                    await page.mouse.up()
                except Exception as e:
                    print(e)
                    input('验证失败，人工登录：')
            else:
                print('没有滑块')
            await page.click("#app > div:nth-child > div > div > div > div > div > form > div:nth-child > div > button")  # 点击登录
            input('进入登录成功页面后，按回车：')                                                            #上面修改点击登录对象
            return page
        except Exception as e:
            continue
