import streamlit as st
from PIL import Image

#Memunculkan tampilan samping
st.sidebar.title('Menu')
with st.sidebar:
    option = st.radio('Pilihan:',['Tentang Aplikasi dan Kesadahan Total','Perhitungan Nilai PPM Kesadahan Total'])

#Halaman Tentang Aplikasi dan Kesadahan Total
if option == 'Tentang Aplikasi dan Kesadahan Total':
    st.title('Selamat Datang Diwebapps Kelompok 5 :computer:')
    st.subheader('Penjelasan Aplikasi')
    st.write('Aplikasi ini dibuat untuk mempermudah dalam melakukan perhitungan PPM Kesadahan Total yang sering dilakukan saat melakukan suatu analisis dilaboratorium dan harus dilakukan dalam waktu yang singkat. Dengan adanya perkembangan teknologi, aplikasi perhitungan pun dapat dibuat untuk mempermudah dan meminimalisir terjadinya kesalahan dalam perhitungan PPM Kesadahan Total yang dilakukan saat proses analisis dilaboratorium. ')
    st.subheader('Penjelasan Kesadahan Total')
    st.image(Image.open('Rumus PPM.jpg'))
    st.write(' Kesadahan total adalah jumlah ion–ion kalsium dan magnesium yang dapat ditentukan melalui titrasi menggunakan EDTA (Etilen Diamin Tetra Asetat) sebagai titran dengan menggunakan indikator EBT, selain itu kesadahan total juga dapat dilakukan dengan proses analisis lainnya. Hasil dari analisis tersebut kemudian dilakukan perhitungan dengan mencari nilai PPM Kesadahan Total dari sampel yang telah dianalisis.  ')


    
    
#Halaman Perhitungan Nilai PPM Kesadahan Total
if option == 'Perhitungan Nilai PPM Kesadahan Total':
    st.title('Perhitungan Nilai PPM Kesadahan Total')
    
    Molaritas = st.number_input('Masukan Nilai Molaritas Titran (mmol/ml)')
    Volume1 = st.number_input('Masukan Nilai Volume Titran (ml)')
    Nama_BM = st.selectbox('BM (mg/mmol)', ['Pilih BM','BM CaCO3 100 mg/mmol','BM Ca 40 mg/mmol'])
    Nilai_BM = st.selectbox('Nilai BM (mg/mmol)', ['Pilih Nilai BM',100,40])
    FP = st.selectbox('Nilai FP', ['Pilih Nilai FP',1,100/50,100/25,250/50,100/10])
    Volume2 = st.number_input('Masukan Nilai Volume Sampel (L)')
    Hitung = st.button('Hitung Nilai PPM Kesadahan Total')
 
    if Hitung:
        Nilai_PPM_Kesadahan_Total = (Molaritas*Volume1*Nilai_BM*FP)/Volume2
        st.success(f'Nilai PPM Kesadahan Total Adalah {Nilai_PPM_Kesadahan_Total} mg/L')
        
        