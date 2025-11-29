import streamlit as st
import pandas as pd
import json
import os
import matplotlib.pyplot as plt

DATA_FILE = "data.json"

# ===================== Fungsi Membaca & Menyimpan =====================
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ===================== Streamlit App =====================
st.set_page_config(page_title="Mini Finance App", layout="wide")
st.title("💰 Mini Finance App")

# Load data
data = load_data()
df = pd.DataFrame(data)

# --------------------- Form Input Transaksi ---------------------
st.subheader("Tambah Transaksi")
with st.form("form_transaction", clear_on_submit=True):
    col1, col2, col3 = st.columns([1,1,2])
    t_type = col1.selectbox("Jenis", ["Masuk", "Keluar"])
    amount = col2.number_input("Jumlah (Rp)", min_value=0, step=1000)
    category = col3.text_input("Kategori")
    submitted = st.form_submit_button("Tambah")
    if submitted:
        data.append({
            "type": t_type.lower(),
            "amount": float(amount),
            "category": category
        })
        save_data(data)
        st.success("Transaksi berhasil ditambahkan!")
        df = pd.DataFrame(data)

# --------------------- Ringkasan ---------------------
st.subheader("Ringkasan Keuangan")
if not df.empty:
    total_income = df[df["type"]=="masuk"]["amount"].sum()
    total_expense = df[df["type"]=="keluar"]["amount"].sum()
    balance = total_income - total_expense
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Pemasukan", f"Rp {total_income:,.0f}")
    col2.metric("Total Pengeluaran", f"Rp {total_expense:,.0f}")
    col3.metric("Sisa Saldo", f"Rp {balance:,.0f}")
else:
    st.info("Belum ada transaksi.")

# --------------------- Tabel Transaksi ---------------------
st.subheader("Daftar Transaksi")
if not df.empty:
    st.dataframe(df)
else:
    st.write("Belum ada transaksi.")

# --------------------- Grafik Pengeluaran ---------------------
st.subheader("Grafik Pengeluaran per Kategori")
if not df.empty:
    expense_df = df[df["type"]=="keluar"].groupby("category")["amount"].sum()
    if not expense_df.empty:
        fig, ax = plt.subplots(figsize=(5,3))  # ukurannya lebih kecil
        expense_df.plot(kind="bar", ax=ax, color="#f44336")
        ax.set_ylabel("Jumlah (Rp)")
        ax.set_xlabel("Kategori")
        ax.set_title("Pengeluaran per Kategori")
        plt.xticks(rotation=30)
        plt.tight_layout()
        st.pyplot(fig, use_container_width=False)  # jangan otomatis lebar penuh
    else:
        st.info("Belum ada pengeluaran.")
else:
    st.info("Belum ada transaksi.")



# --------------------- Export ---------------------
st.subheader("Export Data")
col1, col2 = st.columns(2)
with col1:
    if st.button("Export ke Excel"):
        if not df.empty:
            file_name = "laporan_keuangan.xlsx"
            df.to_excel(file_name, index=False)
            st.success(f"Data berhasil diexport ke {file_name}")
        else:
            st.warning("Belum ada data untuk diexport.")
with col2:
    if st.button("Export ke JSON"):
        if not df.empty:
            file_name = "laporan_keuangan.json"
            df.to_json(file_name, orient="records", indent=4)
            st.success(f"Data berhasil diexport ke {file_name}")
        else:
            st.warning("Belum ada data untuk diexport.")
