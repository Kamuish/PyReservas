
def login(driver,email, password):
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("password")

    username.send_keys(email)
    password.send_keys(password)

    driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/div/div[2]/form/fieldset/input[1]').click()