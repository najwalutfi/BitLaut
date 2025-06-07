from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def beranda():
    return render_template('index.html')

@app.route('/prediksi', methods=['GET', 'POST'])
def prediksi():
    if request.method == 'POST':
        jumlah_kapal = int(request.form['jumlah_kapal'])
        hasil_tangkapan = int(request.form['hasil_tangkapan'])
        alat_tangkap = request.form['alat_tangkap']
        musim = request.form['musim']
        zona = request.form['zona']

        skor = 0
        if jumlah_kapal > 20:
            skor += 1
        if hasil_tangkapan < 500:
            skor += 1
        if alat_tangkap.lower() == 'modern':
            skor += 1
        if musim.lower() in ['paceklik', 'musim sepi']:
            skor += 1
        if zona.lower() == 'zona merah':
            skor += 1

        status = 'Tinggi' if skor >= 3 else 'Rendah'
        probabilitas = min(90, 50 + skor * 10) if skor >= 3 else max(10, 30 - skor * 5)

        hasil = {
            'status': status,
            'probabilitas': probabilitas
        }

        return render_template('prediksi.html', hasil=hasil)
    
    return render_template('prediksi.html')

@app.route("/peta")
def peta():
    return render_template("peta.html")

@app.route('/statistik')
def statistik():
    return render_template('statistik.html')

@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

if __name__ == '__main__':
    app.run(debug=True)