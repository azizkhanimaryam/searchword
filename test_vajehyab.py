import requests

querySearch = "آب"  # جایگزین با کلمه مورد نظر
response = requests.get("https://api.codebazan.ir/vajehyab/?text=" + querySearch)

print(response.status_code)  # بررسی وضعیت
print(response.text)          # بررسی محتوای پاسخ

if response.status_code == 200:
    try:
        result = response.json()  # تبدیل به JSON
        print(result)  # نمایش نتیجه
    except ValueError:
        print("خطا در تبدیل به JSON")
else:
    print(f"خطا در درخواست: {response.status_code}")


