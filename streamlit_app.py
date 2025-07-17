import streamlit as st
import pandas as pd
import os

st.title("Galería de piezas de cerámica")

# CSVファイルアップロード
uploaded_file = st.file_uploader("Sube tu archivo CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    # esmaltado（釉薬の種類）フィルター
    glaze_filter = st.selectbox(
        "Filtrar por tipo de esmaltado",
        options=["ALL"] + df["tipo_esmaltado"].dropna().unique().tolist()
    )
    if glaze_filter != "ALL":
        df = df[df["tipo_esmaltado"] == glaze_filter]

    # barro（土の種類）フィルター
    barro_filter = st.selectbox(
        "Filtrar por tipo de barro",
        options=["ALL"] + df["tipo_barro"].dropna().unique().tolist()
    )
    if barro_filter != "ALL":
        df = df[df["tipo_barro"] == barro_filter]

    # 画像ファイルはCSVと同じフォルダにある想定（相対パス）
    image_folder = "."

    for _, row in df.iterrows():
        st.subheader(row["nombre_obra"])
        st.write(f"Esmalte: {row['tipo_esmaltado']}, Temperatura de cocción: {row['temperatura_coccion']}℃")

        # ruta_foto列は「IMG_0083.jpg, IMG_0084.jpg」のようにカンマ区切り想定
        fotos = [f.strip() for f in str(row["ruta_foto"]).split(",")]

        for foto in fotos:
            image_path = os.path.join(image_folder, foto)
            st.write(f"画像パス確認: {image_path}")
            if os.path.exists(image_path):
                st.image(image_path, width=300, caption=row["id_obra"])
            else:
                st.warning(f"No se encontró la foto: {image_path}")

        st.markdown("---")
