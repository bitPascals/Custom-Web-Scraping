import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

options = ChromeOptions()
options.add_argument("--start-m aximized")

# Keeping browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Setting up Chrome driver
driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.allrecipes.com/")

trending_recipes = driver.find_elements(By.CSS_SELECTOR,
                                        value='.comp.three-post__inner.card-list.mntl-document-'
                                              'card-list.mntl-card-list.mntl-block .card__title-text ')
trending_rating = driver.find_elements(By.CSS_SELECTOR, value='.comp.three-post__inner.card-list.mntl-'
                                                              'document-card-list.mntl-card-list.mntl-block '
                                                              '.recipe-card-meta__rating-count-number ')
print("America's #1 Trusted & Trending Recipes")
trends = []
for n in range(len(trending_recipes)):
    trends_ = {
        "Recipe": trending_recipes[n].text,
        "Rating": trending_rating[n].text
    }
    trends.append(trends_)
# print(trends)

# Convert dictionary to dataframe then convert and save in a csv file.
df = pd.DataFrame(trends)
df.to_csv("recipe_data.csv")

driver.quit()
