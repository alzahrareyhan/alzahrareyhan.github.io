import streamlit as st

st.title("PT BENGAWAN SOLO")
st.write("PROGRAM HITUNG GAJI KARYAWAN")


nama= st.text_input("Masukkan Nama",)
jabatan = st.selectbox(
     'Masukkan Jabatan',
     ('-','Supervisor', 'Qc', 'Produksi', 'Finishing','Sopir'))
   
harikerja= st.number_input("Jumlah hari kerja",0)
jamlembur= st.number_input("Jumlah jam lembur",0)
hitung= st.button("Hitung Gaji")

gapok  = 2000000
tunhar = 10000*harikerja
tunkom = 20000*harikerja

if jabatan == "supervisor" or jabatan == "Supervisor":
    tunjab= 300000
elif jabatan == "qc" or jabatan =="Qc":
    tunjab= 200000
elif jabatan == "produksi" or jabatan =="Produksi":
    tunjab= 200000
elif jabatan == "finishing" or jabatan =="Finishing":
    tunjab= 100000
elif jabatan == "sopir" or jabatan =="Sopir":
    tunjab= 50000
else:
    tunjab=0

if (jamlembur>0):
    upahlembur = jamlembur*5000
else:
    upahlembur = 0

hasil = gapok + tunhar + tunkom + tunjab + upahlembur

potbpjs = 1/100*hasil
totdit  = hasil-potbpjs

if hitung:
    st.text(f"Karyawan Yang Bernama        : {nama}")
    st.text(f"Jabatan                      : {jabatan}")
    hasil = gapok + tunhar + tunkom + tunjab + upahlembur
    st.text("============================================")
    st.text(f".....Gaji Pokok              Rp{gapok}")
    st.text(f".....Tunjangan Jabatan       Rp{tunjab}")
    st.text(f".....Tunjangan Harian        Rp{tunhar}")
    st.text(f".....Tunjangan Konsumsi      Rp{tunkom}")
    st.text(f".....Upah Lembur             Rp{upahlembur}")
    st.text("............................................")
    st.text(f".....Total Gaji              Rp{hasil}")
    st.text("............................................")
    st.text(f".....Potongan BPJS           Rp{potbpjs}")
    st.text(f".....Gaji yang diterima       Rp{totdit}")
    st.text("............................................")






