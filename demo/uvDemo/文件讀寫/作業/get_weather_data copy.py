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


# 3. 準備寫入資料
# 🌟 先在 Excel 第一排寫上「標題」，這樣比較清楚
sheet.append(["標籤名稱", "氣象內容"])

# 變成樹根
root = ET.XML(weather_data.text)
for node in root.iter():
    text = node.text.strip() if node.text else ""
    print(node.tag)
    if text:
        sheet.append(text.split(" "))


# 存檔
wb.save("桃園氣象數據.xlsx")
wb.close()
print("✅ 檔案已經成功存檔囉！")

#執行xlsx
import os
os.startfile("桃園氣象數據.xlsx")