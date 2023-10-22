import pickle
import streamlit as st

model = pickle.load(open('./dataset/usage.sav', 'rb'))

st.header('Software Revenue Insights', divider=True)

st.write('**Apakah Pelanggan Memiliki Kantor Global?**')
is_global = st.checkbox('Ceklis untuk Ya', key='is_global')

st.write('**Apakah Pelanggan Merupakan Konsumen Besar di Industri Mereka?**')
is_major = st.checkbox('Ceklis untuk Ya', key='is_major')

st.write('**Apakah Pelanggan Merupakan Small Medium Corporation (SMC)?**')
is_smc = st.checkbox('Ceklis untuk Ya', key='is_smc')

st.write('**Apakah Bisnis Pelangan Bersifat Komersil?**')
is_commercial = st.checkbox('Ceklis untuk Ya', key='is_commercial')

it_spend = st.number_input('**Uang Yang Dihabiskan Pelanggan Untuk Pembelian TI**')
employee_count = st.number_input('**Jumlah Karyawan di Organisasi Pelanggan**')
pc_count = st.number_input('**Jumlah PC yang Digunakan Pelanggan**')
size = st.number_input('**Ukuran Pelanggan Berdasarkan Pendapatan Tahunan**')

st.write('**Apakah Pelanggan Menerima Dukungan Teknis?**')
it_support = st.checkbox('Ceklis untuk Ya', key='it_support')

st.write('**Apakah Pelanggan Diberi Diskon?**')
is_discount = st.checkbox('Ceklis untuk Ya', key='is_discount')

if st.button('Submit'):
    result = model.predict([
        [
            int(is_global),
            int(is_major),
            int(is_smc),
            int(is_commercial),
            it_spend,
            employee_count,
            pc_count,
            size,
            int(it_support),
            int(is_discount),
        ],
    ])

    st.write('Revenue Pelanggan dalam USD : ', result[0])
