import streamlit as st
import pandas as pd
import os

st.title("garally de piezas de ceramica")

uploaded_file = st.file_uploader("upload CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    glaze_filter = st.selectbox("filter from esmalte", options=["ALL"] + df["tipo_esmaltado"].dropna().unique().tolist())
    if glaze_filter != "ALL":
        df = df[df["tipo_esmaltado"] == glaze_filter]
    
     # barro（土の種類）フィルター
    barro_filter = st.selectbox(
        "filter from tipo de barro",
        options=["ALL"] + df["tipo_barro"].dropna().unique().tolist()
    )
    if barro_filter != "ALL":
        df = df[df["tipo_barro"] == barro_filter]

    image_folder = "/Users/nishizakakumi/Desktop/ruta_foto"

    for i, row in df.iterrows():
        st.subheader(row["nombre_obra"])
        st.write(f"esmarte: {row['tipo_esmaltado']}, temperatura de coccion: {row['temperatura_coccion']}℃")

        fotos = [f.strip() for f in str(row["ruta_foto"]).split(",")]

        for foto in fotos:
            image_path = os.path.join(image_folder, foto)
            st.write(f"画像パス確認: {image_path}")
            if os.path.exists(image_path):
                st.image(image_path, width=300, caption=row["id_obra"])
            else:
                st.warning(f"No se encontró la foto: {image_path}")

        st.markdown("---")
