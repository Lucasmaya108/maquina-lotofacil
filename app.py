import streamlit as st
import json
from motor import simular_jogos

ESTADO_ARQ = "estado.json"

def carregar_estado():
    try:
        with open(ESTADO_ARQ, "r") as f:
            return json.load(f)
    except:
        return {"pausado": False}

def salvar_estado(estado):
    with open(ESTADO_ARQ, "w") as f:
        json.dump(estado, f)

estado = carregar_estado()

st.set_page_config(page_title="Máquina Lotofácil", layout="centered")
st.title("🧠 Máquina Lotofácil – Versão Fechada")

if estado["pausado"]:
    st.warning("⏸ Máquina PAUSADA")
else:
    st.success("🟢 Máquina ATIVA")

col1, col2 = st.columns(2)

with col1:
    if st.button("▶️ Executar Máquina"):
        if estado["pausado"]:
            st.error("Máquina pausada. Retire a pausa.")
        else:
            jogos = simular_jogos(5)
            st.subheader("🎯 Jogos Gerados")
            for j in jogos:
                st.write(j)

with col2:
    if st.button("⏸ Pausar / Retomar"):
        estado["pausado"] = not estado["pausado"]
        salvar_estado(estado)
        st.experimental_rerun()