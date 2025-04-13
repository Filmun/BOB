import time
from click import prompt
import google.generativeai as genai
import os
import textwrap
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



api_key = "AIzaSyB9zdQenlftAMQd8TJMMLMT2IbD5cXGDTc"
genai.configure(api_key=api_key)

bookies = [		"https://www.merkurxtip.cz/sazeni/online/fotbal/S",
            "https://bet-x.cz/cs/sports-betting/offer/fotbal/ceska-republika/ceska-1-liga?hours=72000",
"https://bet-x.cz/cs/sports-betting/offer/fotbal/ceska-republika/cfl?hours=72000",
"https://bet-x.cz/cs/sports-betting/offer/fotbal/mezinarodni-klubove/liga-mistru?hours=72000",
"https://bet-x.cz/cs/sports-betting/offer/fotbal/mezinarodni-klubove/evropska-liga?hours=72000",
"https://bet-x.cz/cs/sports-betting/offer/fotbal/mezinarodni-klubove/uefa-konferencni-liga?hours=72000",
"https://bet-x.cz/cs/sports-betting/offer/fotbal/mezinarodni-klubove/copa-libertadores?hours=72000",
"https://bet-x.cz/cs/sports-betting/offer/fotbal/mezinarodni-klubove/copa-sudamericana?hours=72000",
"https://bet-x.cz/cs/sports-betting/offer/fotbal/anglie/premier-league?hours=72000",
"https://bet-x.cz/cs/sports-betting/offer/fotbal/anglie/championship?hours=72000",
                   "https://bet-x.cz/cs/sports-betting/offer/fotbal/anglie/premier-league?hours=72000",
                   "https://bet-x.cz/cs/sports-betting/offer/fotbal/anglie/championship?hours=72000",
                   "https://bet-x.cz/cs/sports-betting/offer/fotbal/anglie/league-one?hours=72000",
                   "https://bet-x.cz/cs/sports-betting/offer/fotbal/anglie/league-two?hours=72000",
                   "https://bet-x.cz/cs/sports-betting/offer/fotbal/anglie/narodni-liga?hours=72000"
            "https://www.betano.cz/sport/fotbal/cesko/1-liga/16952/",
            "https://www.betano.cz/sport/fotbal/cesko/pohar-facr/17427/",
            "https://www.betano.cz/sport/fotbal/cesko/2-liga/17460/",
            "https://www.betano.cz/sport/fotbal/cesko/3-liga/17678/",
            "https://www.betano.cz/sport/fotbal/cesko/4-liga/184995/",
            "https://www.betano.cz/sport/fotbal/cesko/krajsky-prebor/184198/",
            "https://www.betano.cz/sport/fotbal/souteze/liga-mistru/188566/",
            "https://www.betano.cz/sport/fotbal/souteze/evropska-liga/188567/",
            "https://www.betano.cz/sport/fotbal/souteze/konferencni-liga/189602/",
                   "https://www.betano.cz/sport/fotbal/anglie/premier-league/1/",
                   "https://www.betano.cz/sport/fotbal/anglie/championship/2/",
                   "https://www.betano.cz/sport/fotbal/anglie/league-one/527/",
                   "https://www.betano.cz/sport/fotbal/anglie/league-two/4/",
                   "https://www.betano.cz/sport/fotbal/anglie/national-league/1697/"
           "https://www.ifortuna.cz/sazeni/fotbal/liga-mistru",
"https://www.ifortuna.cz/sazeni/fotbal/evropska-liga",
"https://www.ifortuna.cz/sazeni/fotbal/konferencni-liga",
"https://www.ifortuna.cz/sazeni/fotbal/1-cesko",
"https://www.ifortuna.cz/sazeni/fotbal/cesko-pohar",
"https://www.ifortuna.cz/sazeni/fotbal/3-cesko-cfl",
"https://www.ifortuna.cz/sazeni/fotbal/1-anglie",
"https://www.ifortuna.cz/sazeni/fotbal/anglie-fa-cup",
"https://www.ifortuna.cz/sazeni/fotbal/1-francie",
                   "https://www.ifortuna.cz/sazeni/fotbal/liga-mistru",

            "https://www.sazka.cz/kurzove-sazky/sport/11/fotbal/matches"
        ]

def get_page_text(url, all_text = ""):

    try:
        # Set up Chrome options (optional, but good practice)
        chrome_options = Options()
        # Uncomment the line below if you want to run in headless mode (no browser window)
        # chrome_options.add_argument("--headless")

        # Initialize the Chrome webdriver
        driver = webdriver.Chrome(options=chrome_options)


        # Navigate to the URL
        driver.get(url)
        print(f"Successfully accessed URL: {url}")

        if "sazka" in url:
            time.sleep(3)

        if "merkur" in url:


            alert = WebDriverWait(driver, 3).until(EC.alert_is_present())  # Wait for alert to appear (max 3 seconds)
            if alert:
                alert_text = alert.text
                print(f"Alert Text: {alert_text}")

                # **Choose one of the following actions:**

                # a) Accept (Click "OK") - Most common for alerts
                alert.accept()
                print("Alert accepted (OK clicked).")

            consent_cookie = {
                "name": "CookieConsent",
                "value": "{stamp:%27nHTqzpLg9dQidQkoGU3FSEN5bIsDPaQr448oPLKJROzL4q2Z94u2rA==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:2%2Cutc:1742928529266%2Cregion:%27cz%27}",  # Or "accepted", "true", etc.
                "domain": "www.merkurxtip.cz",  # e.g., "www.example.com" or ".example.com"
                "path": "/"
            }

            driver.add_cookie(consent_cookie)

            driver.refresh()

            # Wait for the page to load (important for dynamic content)
            time.sleep(10)  # Adjust sleep time if needed

            # Find the main body element (or a more specific container if needed)



            driver.switch_to.frame(0)


        time.sleep(4)

        body_element = driver.find_element(By.TAG_NAME, 'body')


        # Get all text content from the body element and its descendants

        all_text = body_element.text

        print(all_text)


        #print("Extracted text content:")
        #print("-" * 50)
        #print(all_text)
        #print("-" * 50)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the webdriver, even if an error occurred
        if 'driver' in locals() and driver:
            driver.quit()
            print("WebDriver closed.")

    return all_text

def generate_text(prompt, model_name="gemini-2.0-flash"):
    """Generates text from a prompt."""
    model = genai.GenerativeModel(model_name)
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error: {e}") # Print the error for debugging
        return None

def wrap_text(text, width=80):
    """Wraps text for readability."""
    return textwrap.fill(text, width=width)


if __name__ == "__main__":


    '''page_text = get_page_text("https://bet-x.cz/cs/sports-betting/offer/fotbal/mezinarodni-klubove/liga-mistru?hours=72000")
    print(page_text)

    task1 = f"V odpovědi napiš POUZE '[název sázkové kanceláře, název týmu 1, název týmu 2, kurz na výhru týmu 1, kurz na remízu, kurz na výhru týmu 2]' pro všechny zápasy."
    prompt1 = f"{task1}\nSázková kancelář: {link}\nToto je výchozí text: \n{page_text}"

    answer = generate_text(prompt1)
    print(answer)'''

    #page_text = get_page_text("https://bet-x.cz/cs/sports-betting/offer/fotbal/ceska-republika/cfl?hours=72000")
    #task1 = f"V odpovědi napiš POUZE '[název sázkové kanceláře, název týmu 1, název týmu 2, kurz na výhru týmu 1, kurz na remízu, kurz na výhru týmu 2]' pro všechny zápasy. Ignoruj live zápasy."
    #prompt1 = f"{task1}\nSázková kancelář: \nToto je výchozí text: \n{page_text}"

    #answer = generate_text(prompt1)
    #print(answer)






    for link in bookies:
        page_text = get_page_text(link)
        task1 = f"V odpovědi napiš POUZE '[název sázkové kanceláře, název týmu 1, název týmu 2, kurz na výhru týmu 1, kurz na remízu, kurz na výhru týmu 2]' pro všechny zápasy. Ignoruj live zápasy."
        prompt1 = f"{task1}\nSázková kancelář: {link}\nToto je výchozí text: \n{page_text}"


        answer = generate_text(prompt1)
        print(answer)

        filepath = r"C:\Users\filip\PycharmProjects\arbitrage\drive.txt"
        with open(filepath, 'a', encoding='utf-8') as file:
            file.write(f"\n{wrap_text(answer)}")

    with open(filepath, 'r', encoding='utf-8') as file:  # Mode 'r' for reading
        kurzy = file.read()



    task2 = f"""Dostaneš text obsahující seznam fotbalových zápasů ve formátu [sázková kancelář, tým 1, tým 2, kurz na tým 1, kurz na remízu, kurz na tým 2]. Chci aby jsi k sobě seřadil ty stejné zápasy od jiných sázkových kanceláří. Budeš muset dát pozor na trošku odlišná jména týmu. Zapiš to jako vícerozměrný python seznam, kde jeden rozměr bude jeden specifický zápas od různých sázkovek. Ignoruj zápasy kde jakýkoliv kurz neni číslo, například "N/A" nebo "neuvedeno". Potřebuji aby text byl použitelný s python metodou eval. Nechci python program chci abys to udělal ty."""


    prompt2 = f"{task2}\nToto je výchozí text: \n{kurzy}"

    filepath1 = r"C:\Users\filip\PycharmProjects\arbitrage\drive_serazene.txt"

    with open(filepath1, 'a', encoding='utf-8') as file:
        file.write(f"\n{generate_text(prompt2)}")

    with open(filepath1, 'r', encoding='utf-8') as file:  # Mode 'r' for reading
        kurzy = file.read()

    if "```" in kurzy:
        kurzy = kurzy.replace("```", "")

    if "python" in kurzy:
        kurzy = kurzy.replace("python", "")

    if "json" in kurzy:
        kurzy = kurzy.replace("json", "")

    kurzy_seznam = eval(kurzy)

    kurzy_best_mezi = ['tým 1', 'tým 2', 'saz_1', '0', 'saz_2', '0', 'saz_3', '0']

    for i in kurzy_seznam:

        kurzy_best_mezi = ['tým 1', 'tým 2', 'saz_1', '0', 'saz_2', '0', 'saz_3', '0']

        for b in i:

            kurzy_best_mezi[0] = b[1]
            kurzy_best_mezi[1] = b[2]

            b[3] = str(b[3])
            b[4] = str(b[4])
            b[5] = str(b[5])

            if "," in b[3]:
                b[3] = b[3].replace(",", ".")
            if "," in b[4]:
                b[4] = b[4].replace(",", ".")
            if "," in b[5]:
                b[5] = b[5].replace(",", ".")

            try:
                if float(b[3]) > float(kurzy_best_mezi[3]):
                    kurzy_best_mezi[3] = b[3]
                    kurzy_best_mezi[2] = b[0]
            except:

                break
            try:
                if float(b[4]) > float(kurzy_best_mezi[5]):
                    kurzy_best_mezi[5] = b[4]
                    kurzy_best_mezi[4] = b[0]
            except:

                break
            try:
                if float(b[5]) > float(kurzy_best_mezi[7]):
                    kurzy_best_mezi[7] = b[5]
                    kurzy_best_mezi[6] = b[0]
            except:

                break

        bob = (1 / float(kurzy_best_mezi[3])) + (1 / float(kurzy_best_mezi[5])) + (1 / float(kurzy_best_mezi[7]))
        print(bob)
        if bob < 1:
            print("PINDOUUUUUUUUUUR!!!!!!!")
            print(kurzy_best_mezi)
            print(bob)

