import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=698, y=407)
pyautogui.write("gabrielp@hotmail.com")
pyautogui.press("tab")
pyautogui.write("test1234")
pyautogui.press("tab")
pyautogui.press("enter")

products = pd.read_csv("produtos.csv")
print(products)

time.sleep(3)

for line in products.index:
    pyautogui.click(x=697, y=292)
    
    #product code
    product_code = products.loc[line, "codigo"]
    pyautogui.write(str(product_code))
    pyautogui.press("tab")
    
    #company
    company = products.loc[line, "marca"]
    pyautogui.write(str(company))
    pyautogui.press("tab")
        
    #product type
    product_type = products.loc[line, "tipo"]
    pyautogui.write(str(product_type))
    pyautogui.press("tab")
    
    #category
    category = products.loc[line, "categoria"]
    pyautogui.write(str(category))
    pyautogui.press("tab")

    #unit_price
    unit_price = products.loc[line, "preo_unitario"]
    pyautogui.write(str(unit_price))
    pyautogui.press("tab")
    
    #unit_cost
    unit_cost = products.loc[line, "custo"]
    pyautogui.write(str(unit_cost))
    pyautogui.press("tab")
    
    #obs
    obs = str(products.loc[line, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)