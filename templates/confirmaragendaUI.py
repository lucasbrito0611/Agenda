import streamlit as st
import pandas as pd
import time
from views import View

class ConfirmarAgendaUI:
    def main():
        st.header("Confirmar Agendamento")
        ConfirmarAgendaUI.listar()

    def listar():
        agendas = View.agenda_listar()
        if len(agendas) == 0:
            st.write("Nenhuma agenda cadastrada")
        else:  
            dic = []
            for obj in agendas: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            st.dataframe(df)

            op = st.selectbox("Selecione uma agenda para confirmar", agendas)
            id = op.get_id()
            conf = op.get_confirmado()
            if st.button("Confirmar"):
                if conf == True:
                    st.error('Agenda já confirmada!')
                    time.sleep(2)
                    st.rerun()
                else:
                    View.agenda_confirmar(id)
                    st.success('Agenda confirmada com sucesso!')
                    time.sleep(1)
                    st.rerun()