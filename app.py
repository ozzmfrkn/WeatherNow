from flask import Flask, render_template, request
import requests
import config
from datetime import datetime

app = Flask(__name__)

def datetimeformat(value):
    try:
        dt = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        return dt.strftime('%d %b %Y, %H:%M')
    except:
        return value

app.jinja_env.filters['datetimeformat'] = datetimeformat

@app.route('/')
def ana_sayfa():
    return render_template('index.html')

@app.route('/hava-durumu', methods=['POST'])
def hava_durumu():
    sehir = request.form['sehir']
    api_key = config.API_KEY
    url_guncel = f"http://api.openweathermap.org/data/2.5/weather?q={sehir}&appid={api_key}&units=metric&lang=tr"
    url_tahmin = f"http://api.openweathermap.org/data/2.5/forecast?q={sehir}&appid={api_key}&units=metric&lang=tr"
    try:
        response_guncel = requests.get(url_guncel)
        veri_guncel = response_guncel.json()
        response_tahmin = requests.get(url_tahmin)
        veri_tahmin = response_tahmin.json()
        if response_guncel.status_code == 200 and response_tahmin.status_code == 200:
            hava_veri = {
                'sehir': sehir,
                'sicaklik': veri_guncel['main']['temp'],
                'hissedilen': veri_guncel['main']['feels_like'],
                'nem': veri_guncel['main']['humidity'],
                'ruzgar': veri_guncel['wind']['speed'],
                'durum': veri_guncel['weather'][0]['description'],
                'ikon': veri_guncel['weather'][0]['icon']
            }
            tahminler = []
            for forecast in veri_tahmin['list'][:24:8]:
                tahminler.append({
                    'tarih': forecast['dt_txt'],
                    'sicaklik': forecast['main']['temp'],
                    'durum': forecast['weather'][0]['description'],
                    'ikon': forecast['weather'][0]['icon']
                })
            return render_template('index.html', veri=hava_veri, tahminler=tahminler)
        else:
            return render_template('index.html', hata="Şehir bulunamadı!")
    except:
        return render_template('index.html', hata="Bağlantı hatası!")

if __name__ == '__main__':
    app.run(debug=True)