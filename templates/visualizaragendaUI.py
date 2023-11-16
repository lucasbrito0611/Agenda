import streamlit as st
import pandas as pd
from views import View

class VisualizarAgendaUI:
    def main():
        st.header('Visualizar agendamentos')
        VisualizarAgendaUI.listar()

    def listar():
        dataini_str = st.text_input('Digite a data inicial no formato *dd/mm/aaaa*')
        datafin_str = st.text_input('Digite a data final no formato *dd/mm/aaaa*')

        id = st.session_state["cliente_id"]

        if st.button('Visualizar'):
            agendas = View.agenda_visualizar(id, dataini_str, datafin_str)
            if len(agendas) == 0:
                st.write("Nenhum horário cadastrado")
            else:
                dic = []
                for obj in agendas: dic.append(obj.to_json())
                df = pd.DataFrame(dic)
                st.dataframe(df)