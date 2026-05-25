import xml.etree.ElementTree as ET
import openpyxl
import requests

# 1. 建立一個工作簿
wb = openpyxl.Workbook()
del wb["Sheet"]
wb.create_sheet("桃園氣象數據")
sheet = wb["桃園氣象數據"]

# 2. 獲取氣象數據
url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-76E008DF-3150-4172-A940-46BAB7E8665E&format=XML&locationName=%E6%A1%83%E5%9C%92%E5%B8%82"
weather_data = requests.get(url)

# 變成樹根
xml_data = ET.fromstring(weather_data.text)

# 3. 準備寫入資料
# 🌟 先在 Excel 第一排寫上「標題」，這樣比較清楚
sheet.append(["標籤名稱", "氣象內容"])

# 4. 把樹裡面的資料拿出來
for item in xml_data.iter():
    # 🌟 記得把這行加回來！把前面醜醜的符號切掉，只留最後乾淨的名字
    clean_tag = item.tag.split("}")[-1] 
    
    # 拿走文字，並把多餘的空白清乾淨
    text = item.text.strip() if item.text else ""
    
    # 🌟 只要文字不是空的，我們就一列一列加進 Excel！
    if text:
        print(clean_tag, text)
        # 這裡的魔法：直接用 append 將標籤跟內容包成一個中括號 [ ]，它就會自動幫你寫在 A 欄和 B 欄！
        sheet.append([clean_tag, text]) 

# 存檔
wb.save("桃園氣象數據.xlsx")
wb.close()
print("✅ 檔案已經成功存檔囉！你可以打開 Excel 看看。")