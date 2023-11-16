import streamlit as st
import time
from views import View

class EditarPerfilUI:
    def main():
        st.header('Editar Perfil')
        EditarPerfilUI.editar()

    def editar():
        nome = st.text_input('Nome')
        email = st.text_input('E-mail')
        telefone = st.text_input('Telefone')
        senha = st.text_input('Senha')

        id = st.session_state["cliente_id"]

        if st.button('Editar'):
            View.editar_perfil(id, nome, email, telefone, senha)
            st.success('Perfil editado com sucesso!')
            time.sleep(1)
            st.rerun()