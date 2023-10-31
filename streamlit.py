import pickle
import streamlit as st

model = pickle.load(open('./dataset/usage.sav', 'rb'))

st.header('Software Revenue Insights', divider=True)

col1, col2 = st.columns(2)

with col1:
    st.write('**Pelanggan Memiliki Kantor Global?**')
    is_global = st.checkbox('Ceklis untuk Ya', key='is_global')

    st.write('**Pelanggan Merupakan Konsumen Besar?**')
    is_major = st.checkbox('Ceklis untuk Ya', key='is_major')

    st.write('**Pelanggan Merupakan SMC?**')
    is_smc = st.checkbox('Ceklis untuk Ya', key='is_smc')

with col2:
    st.write('**Bisnis Pelangan Bersifat Komersil?**')
    is_commercial = st.checkbox('Ceklis untuk Ya', key='is_commercial')

    st.write('**Pelanggan Menerima Dukungan Teknis?**')
    it_support = st.checkbox('Ceklis untuk Ya', key='it_support')

    st.write('**Pelanggan Diberi Diskon?**')
    is_discount = st.checkbox('Ceklis untuk Ya', key='is_discount')

it_spend = st.number_input('**Uang Yang Dihabiskan Pelanggan Untuk Pembelian TI**', 1161, 260000)
employee_count = st.number_input('**Jumlah Karyawan di Organisasi Pelanggan**', 10, 535)
pc_count = st.number_input('**Jumlah PC yang Digunakan Pelanggan**', 6, 407)
size = st.number_input('**Ukuran Pelanggan Berdasarkan Pendapatan Tahunan**', 10100, 766000)

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
