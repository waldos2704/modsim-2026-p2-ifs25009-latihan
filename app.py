import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

<<<<<<< HEAD
# =====================================================
# FUNGSI BANTU (HELPER FUNCTIONS)
# =====================================================
def format_angka_otomatis(value):
    """
    Format angka dengan skala otomatis (Rb, Jt, M)
    
    Parameters:
    - value: Angka yang akan diformat
    
    Returns:
    - String yang sudah diformat
    """
    if value is None or pd.isna(value):
        return "0"
    
    if isinstance(value, str):
        try:
            value = float(value.replace(".", "").replace(",", "."))
        except:
            return value

    
    try:
        v = abs(float(value))
    except (ValueError, TypeError):
        return str(value)
    
    if v >= 1_000_000_000:
        return f"Rp {value/1_000_000_000:.2f} M"
    elif v >= 1_000_000:
        return f"Rp {value/1_000_000:.2f} Jt"
    elif v >= 1_000:
        return f"Rp {value/1_000:.2f} Rb"
    else:
        return f"Rp {value:,.0f}".replace(",", ".")

def format_angka_tanpa_rp(value):
    """
    Format angka tanpa 'Rp' di depan (untuk hover)
    
    Parameters:
    - value: Angka yang akan diformat
    
    Returns:
    - String yang sudah diformat tanpa 'Rp'
    """
    result = format_angka_otomatis(value)
    if result.startswith("Rp "):
        return result[3:]
    return result

def tambahkan_hover_uang(fig, df, kolom, tipe="bar"):
    """
    Tambahkan hover template untuk visualisasi uang
    
    Parameters:
    - fig: Figure Plotly
    - df: DataFrame
    - kolom: Nama kolom yang berisi data uang
    - tipe: Jenis plot ('bar', 'line', 'hbar', 'scatter')
    """
    if tipe == "hbar":
        fig.update_traces(
            customdata=df[kolom].apply(format_angka_tanpa_rp),
            hovertemplate="<b>%{y}</b><br>Rp%{customdata}<extra></extra>"
        )
    elif tipe == "line":
        fig.update_traces(
            customdata=df[kolom].apply(format_angka_tanpa_rp),
            hovertemplate="%{x}<br>Rp%{customdata}<extra></extra>"
        )
    else:  # bar, scatter, dll
        fig.update_traces(
            customdata=df[kolom].apply(format_angka_tanpa_rp),
            hovertemplate="<b>%{x}</b><br>Rp%{customdata}<extra></extra>"
        )
    return fig

# =====================================================
# KONFIGURASI APLIKASI
# =====================================================
=======
# ======================
# KONFIGURASI HALAMAN
# ======================
>>>>>>> d9d902fd0db33f5b5e900034ce9a130bf48a2e55
st.set_page_config(
    page_title="Dashboard Kuesioner",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Visualisasi Kuesioner")
st.markdown("Visualisasi interaktif hasil kuesioner menggunakan Streamlit & Plotly")

# ======================
# LOAD FILE LANGSUNG
# ======================
try:
    df = pd.read_excel("data_kuesioner.xlsx")

except FileNotFoundError:
    st.error("File 'data_kuesioner.xlsx' tidak ditemukan.")
    st.stop()

# Ambil hanya kolom numerik
df = df.select_dtypes(include="number")

if df.empty:
    st.error("Tidak ada data numerik di dalam file.")
    st.stop()

# ======================
# PREPROCESSING
# ======================
df_long = df.melt(
    var_name="Pertanyaan",
    value_name="Skor"
)

df_long = df_long.dropna()

# Kategori sentimen
def kategori(skor):
    if skor <= 2:
        return "Negatif"
    elif skor == 3:
        return "Netral"
    else:
        return "Positif"

df_long["Kategori"] = df_long["Skor"].apply(kategori)

# ======================
# METRICS
# ======================
col1, col2, col3 = st.columns(3)

col1.metric("📄 Jumlah Responden", df.shape[0])
col2.metric("❓ Jumlah Pertanyaan", df.shape[1])
col3.metric("⭐ Rata-rata Skor", round(df_long["Skor"].mean(), 2))

st.divider()

# ======================
# 1️⃣ BAR CHART
# ======================
st.subheader("1️⃣ Distribusi Jawaban Keseluruhan")

dist_all = df_long["Skor"].value_counts().sort_index()

fig1 = px.bar(
    x=dist_all.index.astype(str),
    y=dist_all.values,
    labels={"x": "Skor", "y": "Jumlah"},
    text=dist_all.values
)

st.plotly_chart(fig1, use_container_width=True)

# ======================
# 2️⃣ PIE CHART
# ======================
st.subheader("2️⃣ Proporsi Jawaban")

fig2 = px.pie(
    names=dist_all.index.astype(str),
    values=dist_all.values,
    hole=0.4
)

st.plotly_chart(fig2, use_container_width=True)

# ======================
# 3️⃣ STACKED BAR
# ======================
st.subheader("3️⃣ Distribusi per Pertanyaan")

stacked = df_long.groupby(["Pertanyaan", "Skor"]).size().reset_index(name="Jumlah")

fig3 = px.bar(
    stacked,
    x="Pertanyaan",
    y="Jumlah",
    color="Skor",
    barmode="stack"
)

st.plotly_chart(fig3, use_container_width=True)

# ======================
# 4️⃣ RATA-RATA
# ======================
st.subheader("4️⃣ Rata-rata Skor per Pertanyaan")

mean_score = df.mean().reset_index()
mean_score.columns = ["Pertanyaan", "Rata-rata Skor"]

fig4 = px.bar(
    mean_score,
    x="Pertanyaan",
    y="Rata-rata Skor",
    text="Rata-rata Skor"
)

fig4.update_traces(texttemplate="%.2f")

st.plotly_chart(fig4, use_container_width=True)

# ======================
# 5️⃣ SENTIMEN
# ======================
st.subheader("5️⃣ Distribusi Kategori")

sentimen = df_long["Kategori"].value_counts().reset_index()
sentimen.columns = ["Kategori", "Jumlah"]

fig5 = px.bar(
    sentimen,
    x="Kategori",
    y="Jumlah",
    color="Kategori",
    text="Jumlah"
)

st.plotly_chart(fig5, use_container_width=True)

# ======================
# HEATMAP
# ======================
st.subheader("🔥 Heatmap Rata-rata")

heatmap_data = df.mean().to_frame(name="Rata-rata")

fig6 = go.Figure(
    data=go.Heatmap(
        z=[heatmap_data["Rata-rata"]],
        x=heatmap_data.index,
        y=["Skor"]
    )
)

st.plotly_chart(fig6, use_container_width=True)

# ======================
# BOXPLOT
# ======================
st.subheader("📦 Boxplot Distribusi")

fig7 = px.box(
    df_long,
    x="Pertanyaan",
    y="Skor"
)

st.plotly_chart(fig7, use_container_width=True)
