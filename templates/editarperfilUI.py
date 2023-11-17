import streamlit as st
import time
from views import View

class EditarPerfilUI:
    def main():
        st.header('Editar Perfil')
        EditarPerfilUI.editar()

    def editar():
        id = st.session_state["cliente_id"]

        if st.session_state['cliente_nome'] == 'admin':
            nome = st.session_state['cliente_nome']
            email = st.text_input('E-mail')
            telefone = st.text_input('Telefone')
            senha = st.text_input('Senha')
        else:
            nome = st.text_input('Nome')
            email = st.text_input('E-mail')
            telefone = st.text_input('Telefone')
            senha = st.text_input('Senha')

        if st.button('Editar'):
            View.editar_perfil(id, nome, email, telefone, senha)
            st.success('Perfil editado com sucesso!')
            time.sleep(1)
            st.rerun()