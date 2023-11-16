import streamlit as st
import pandas as pd
import time
from views import View

class AgendarHorarioUI:
    def main():
        st.header('Agendar Horário')
        AgendarHorarioUI.listar()
    
    def listar():
        st.write('Horários da semana')

        agendas = View.agenda_semanal()
        servicos = View.servico_listar()
        if len(agendas) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in agendas: dic.append(obj.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df)

            op1 = st.selectbox('Selecione um horário', agendas)
            id = op1.get_id()
            op2 = st.selectbox('Selecione um serviço', servicos)
            id_servico = op2.get_id()
            id_cliente = st.session_state["cliente_id"]

            if st.button('Agendar'):
                View.agendar_horario(id, id_cliente, id_servico)
                st.success('Horário agendado com sucesso!')
                time.sleep(1)
                st.rerun()