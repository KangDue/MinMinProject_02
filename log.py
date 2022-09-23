from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(1)
driver.get('https://edu.ssafy.com/comm/login/SecurityLoginForm.do')
driver.find_element(By.ID, 'userId').send_keys('rkdrlgks321@naver.com')
driver.find_element(By.ID, 'userPwd').send_keys('rkdtkvl12#')
driver.find_element(By.CLASS_NAME, 'form-btn').click()
driver.implicitly_wait(1)
# 초기 로그인시만 뜸
# driver.find_element(By.ID, 'checkIn').click()
# driver.find_element(By.CLASS_NAME, 'btn-primary').click()
driver.implicitly_wait(1)

driver.get('https://edu.ssafy.com/edu/lectureroom/survey/surveyList.do')
# driver.find_element(By.CSS_SELECTOR, "wrap > form > div > div.content > div > div.my-quest-area.poll-area > ul > li:nth-child(1) > div > div.mql-etc > a").click()