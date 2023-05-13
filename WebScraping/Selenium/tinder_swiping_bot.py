from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
chrome_driver_path = "/Users/sangeethkumarpg/Desktop/Development/Python/chromedriver"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
service = ChromeService(executable_path=chrome_driver_path)
driver = webdriver.Chrome(options=options, service=service)



url="https://tinder.com/app/recs"
driver.get(url)
main_page = driver.current_window_handle
try:
    time.sleep(5)
    try:
        login_button = driver.find_element(By.CSS_SELECTOR,'#c24809439 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > header > div > div.D\(f\).Ai\(c\).Fxs\(0\) > div:nth-child(2) > a > div.w1u9t036 > div.l17p5q9z')
        login_button.click()
        time.sleep(1)
    except exceptions.NoSuchElementException:
        pass
    try:
        main_container_div = driver.find_element(By.CSS_SELECTOR,'#c-1703571637 > main > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div:nth-child(3)')
        login_in_with_fb = main_container_div.find_element(By.CSS_SELECTOR,'span > div:nth-child(2) > button')
        if login_in_with_fb.get_attribute('aria-label') == "Login with Facebook":
            login_in_with_fb.click()
        else:
            more_options = driver.find_element(By.CSS_SELECTOR,'#c-1703571637 > main > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div:nth-child(3) > span > button')
            time.sleep(1)
            more_options.click()
            time.sleep(2)
            login_with_facebook = driver.find_element(By.CSS_SELECTOR,'#c-1703571637 > main > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div:nth-child(3) > span > div:nth-child(2) > button > div.w1u9t036 > div.l17p5q9z > div > div')
            time.sleep(1)
            login_with_facebook.click()
    except exceptions.NoSuchElementException:
        print("here")
        more_options = driver.find_element(By.CSS_SELECTOR,'#c-1703571637 > main > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div:nth-child(3) > span > button')
        time.sleep(1)
        more_options.click()
        time.sleep(2)
        login_with_facebook = driver.find_element(By.CSS_SELECTOR,'#c-1703571637 > main > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div > div:nth-child(3) > span > div:nth-child(2) > button > div.w1u9t036 > div.l17p5q9z > div > div')
        time.sleep(1)
        login_with_facebook.click()
    time.sleep(1)
    for handle in driver.window_handles:
        login_page = handle
    time.sleep(1)
    driver.switch_to.window(login_page)
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("#YourEmail")
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="pass"]').send_keys("YourPassWord")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,'#loginbutton').click()
    
    driver.switch_to.window(main_page)

    wait = WebDriverWait(driver,40)
    time.sleep(20)
    frame = driver.find_element(By.CSS_SELECTOR,'#c-1703571637 > main > div > div > div > div.CenterAlign.Pb\(24px\).Px\(24px\).Py\(12px\).D\(f\).Fxd\(rr\).Ai\(st\)')
    frame.find_element(By.CSS_SELECTOR,'button').click()
    time.sleep(10)
    new_frame = driver.find_element(By.CSS_SELECTOR,'#c-1703571637 > main > div > div > div > div.CenterAlign.Pb\(24px\).Px\(24px\).Py\(12px\).D\(f\).Fxd\(rr\).Ai\(st\)')
    new_frame.find_element(By.CLASS_NAME,'l17p5q9z')
    time.sleep(3)
    new_frame.find_element(By.CSS_SELECTOR,'button').click()
    counter = 1
    while counter <= 50:
        time.sleep(5)
        # driver.switch_to.default_content()
        # slider = driver.find_element(By.CSS_SELECTOR,'#c24809439 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Tcha\(n\).Bdbw\(--recs-gamepad-height\).Bdbc\(t\).Bdbs\(s\).Bgc\(\#000\).Wc\(\$transform\).Prs\(1000px\).Bfv\(h\).Ov\(h\).W\(100\%\).StretchedBox.Bdrs\(8px\) > div.Pos\(a\).D\(f\).Jc\(sb\).C\(\$c-ds-text-primary-overlay\).Ta\(start\).W\(100\%\).Ai\(fe\).B\(0\).P\(8px\)--xs.P\(16px\).P\(20px\)--l.Cur\(p\).focus-button-style')

        image = driver.find_element(By.CSS_SELECTOR,'#c24809439 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Tcha\(n\).Bdbw\(--recs-gamepad-height\).Bdbc\(t\).Bdbs\(s\).Bgc\(\#000\).Wc\(\$transform\).Prs\(1000px\).Bfv\(h\).Ov\(h\).W\(100\%\).StretchedBox.Bdrs\(8px\) > div.Expand.D\(f\).Pos\(r\).tappable-view.Cur\(p\) > div.Expand.Pos\(a\).D\(f\).Ov\(h\).Us\(n\).keen-slider > span:nth-child(1) > div')
        # print(image.get_attribute('role'))
        action = ActionChains(driver)
        # action.click_and_hold(slider).move_by_offset(220,40).release().perform()
        action.click_and_hold(image).move_by_offset(220,40).release().perform()
        counter+=1
#c24809439 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Tcha\(n\).Bdbw\(--recs-gamepad-height\).Bdbc\(t\).Bdbs\(s\).Bgc\(\#000\).Wc\(\$transform\).Prs\(1000px\).Bfv\(h\).Ov\(h\).W\(100\%\).StretchedBox.Bdrs\(8px\) > div.Expand.D\(f\).Pos\(r\).tappable-view > div > span > div
    #click on the slider and slide to resolve the error
except exceptions.NoSuchElementException as e:
    print(counter)
    print(e)

