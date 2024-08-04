from selenium import webdriver

def login(username, password):
    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    # Open the login page
    driver.get('https://academico.ifes.edu.br/qacademico/index.asp?t=1001')

    # Find the login form elements
    username_input = driver.find_element_by_name('LOGIN')
    password_input = driver.find_element_by_name('SENHA')

    # Fill in the login credentials
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Submit the form
    password_input.submit()

    # Check if login was successful by verifying the page title or URL
    if "https://academico.ifes.edu.br/qacademico/index.asp?t=2000" in driver.page_source:
        print("foi")
    else:
        print("Login falhou!")

    # Close the browser
    driver.quit()

# Usage
username = "matricula"
password = "senha"
login(username, password)
