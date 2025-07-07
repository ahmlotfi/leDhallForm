from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to ChromeDriver
path = r"C:\Program Files (x86)\chromedriver.exe"

# Initialize WebDriver
service = Service(path)
driver = webdriver.Chrome(service=service)

try:
    # Open the form
    driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=D59Rsb8tIU6_NKaGzpdYioIz-RoWPs5FoBoJAop9UFdUNEcxNlJETVI2U0I4VksxWDRWWjZPVUlFOC4u")

    # Wait for the form to load
    wait = WebDriverWait(driver, 10)

    # Loop through 28 days in March
    for day in range(1, 30):  # From March 1 to March 28
        # Fill out personal details
        first = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[1]/div[2]/div/span/textarea")))
        first.send_keys("Yassin")

        last = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[2]/div[2]/div/span/textarea")))
        last.send_keys("Badawy")

        id_field = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[3]/div[2]/div/span/textarea")))
        id_field.send_keys("202314661")

        number = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[4]/div[2]/div/span/textarea")))
        number.send_keys("1(709)631-7299")

        email = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[5]/div[2]/div/span/textarea")))
        email.send_keys("yamsabadawy@mun.ca")

        # Agree to terms
        agree = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[6]/div[2]/div/div/div/div/label/span[1]/input")))
        agree.click()

        # Dynamically input the date (March 1 to March 28)
        date = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[7]/div[2]/div/div/div/div/div/input")))
        date.send_keys(f"3/{day}/2025")

        # Order Details
        order = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[8]/div[2]/div/div/div[2]/div/label/span[1]/input")))
        order.click()

        lunch = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[9]/div[2]/div/div/div[2]/div/label/span[1]/input")))
        lunch.click()

        # Sandwich Ingredients
        bread = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[10]/div[2]/div/div/div[7]/div/label/span[1]/input")))
        bread.click()

        protein = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[11]/div[2]/div/div/div[2]/div/label/span[1]/input")))
        protein.click()

        cheese = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[12]/div[2]/div/div/div[2]/div/label/span[1]/input")))
        cheese.click()

        lettuce = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[13]/div[2]/div/div/div[1]/div/label/span[1]/input")))
        lettuce.click()

        # tomatoes = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[13]/div[2]/div/div/div[2]/div/label/span[1]/input")))
        # tomatoes.click()
        #
        # cucumbers = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[13]/div[2]/div/div/div[3]/div/label/span[1]/input")))
        # cucumbers.click()
        olives = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[13]/div[2]/div/div/div[7]/div/label/span[1]/input")))
        olives.click()

        mayo = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[14]/div[2]/div/div/div[3]/div/label/span[1]/input")))
        mayo.click()

        bbq = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[14]/div[2]/div/div/div[4]/div/label/span[1]/input")))
        bbq.click()

        # Salad Selection
        salad = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[15]/div[2]/div/div/div[6]/div/label/span[1]/input")))
        salad.click()

        ceasar = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[16]/div[2]/div/div/div[2]/div/label/span[1]/input")))
        ceasar.click()

        # Dessert and Drinks
        orange = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[17]/div[2]/div/div/div[3]/div/label/span[1]/input")))
        orange.click()

        cookie = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[18]/div[2]/div/div/div[1]/div/label/span[1]/input")))
        cookie.click()

        cola = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[19]/div[2]/div/div/div[4]/div/label/span[1]/input")))
        cola.click()

        # Add extra notes
        extra = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[2]/div[20]/div[2]/div/span/textarea")))
        extra.send_keys("Please add extra chips and cola thanks.")

        # Submit the form
        submit = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/div[2]/div[4]/div/button")))
        submit.click()

        # Wait for the "Submit Another Response" button and click it
        another_form = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]/div[4]/span")))
        another_form.click()

finally:
    # Close the driver
    driver.quit()
