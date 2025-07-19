import streamlit as st
import re

# Data massa atom relatif (Ar) 
# Semua data atom relatif (Ar) mengacu pada 2007 Atomic IUPAC oleh Michael E.Wieser dan Michael Berglund
ar_data = {
    "H": 1, "C": 12, "O": 16, "N": 14, "Cl": 35.45, 
    "Br": 79.904, "B":  10.811, "Cr": 51.996, "Co": 58.933, "Cu":  63.546,
    "F": 18.998, "He": 4.002, "I":  126.904, "La": 138.905, "Pb": 207.2, "Li": 6.94,
    "Na": 22.99, "S": 32.06, "K": 39.10, "Mg": 24.31, "Ca": 40.08,
    "Fe": 55.85, "P": 30.97, "Zn": 65.38, "Al": 26.98, "Ar": 39.948, "Ba": 137.327,
    "Mn": 54.938, "Hg": 200.59, "Ne": 20.179, "Ni": 58.693, "Ag": 107.868, "K": 39.098,
    "Be": 9.012, "Rb": 85.4678, "Sc": 44.955, "Si":  28.085, "Xe": 131.293, "Pt": 195.084,
    "Ga":  69.723, "Ge": 72.64, "As": 74.921, "Kr": 83.798, "Sr":  87.62, "Pd": 106.42, "Cd": 112.411,
    "Cs": 132.905, "Ce": 140.116, "Bi": 208.980, "Ir": 192.217,
}

st.set_page_config(page_title="Kalkulator Berat Molekul", page_icon="🧪")

st.title("🧪 Kalkulator Berat Molekul Senyawa")
st.markdown("Masukkan rumus senyawa (misal: `H2O`, `HCl`, `NaOH`) lalu klik hitung. Untuk senyawa seperti (`Mg(OH)2`) tulis menjadi (`MgO2H2`).")

# Fungsi hitung berat molekul
def hitung_mr(rumus):
    pola = r'([A-Z][a-z]?)(\d*)'
    hasil = re.findall(pola, rumus) 
    total_mr = 0.0
    for unsur, jumlah in hasil:
        jumlah = int(jumlah) if jumlah else 1
        if unsur in ar_data:
            total_mr += ar_data[unsur] * jumlah
        else:
            st.error(f"Unsur '{unsur}' belum tersedia dalam data Ar Kami.")
            return None
    return total_mr

# Input
rumus = st.text_input("Rumus Senyawa:", value="H2O")

# Output
if st.button("Hitung"):
    mr = hitung_mr(rumus)
    if mr:
        st.success(f"Berat molekul (Mr) dari **{rumus}** adalah **{mr:.2f} g/mol**")

st.caption("© 2025 Kalkulator BM - Kelompok 6")
