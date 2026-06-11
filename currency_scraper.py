import requests

print("🌐 جاري الاتصال بالإنترنت لقنص البيانات الحالية...")

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    egyptian_rate = data["rates"]["EGP"]
    print("\n✅ تم قنص البيانات بنجاح باهر!")
    print(f"💵 سعر الدولار الرسمي المقنوص ديلوقتي يساوي: {egyptian_rate} جنيه مصري")
else:
    print("❌ فشل قناص البيانات في الوصول للموقع.")
