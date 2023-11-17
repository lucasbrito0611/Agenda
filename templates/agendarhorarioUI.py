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
            tabela = []
    
            for agenda in agendas:
                id = agenda.get_id()
                data = agenda.get_data()
                conf = agenda.get_confirmado()
                idCliente = int(agenda.get_id_cliente())
                idServico = int(agenda.get_id_servico())

                if idCliente != 0 and idServico != 0:
                    for cliente in View.cliente_listar():
                        if idCliente == cliente.get_id():
                            idCliente = cliente.get_nome()
                    
                    for servico in View.servico_listar():
                        if idServico == servico.get_id():
                            idServico = servico.get_descricao()

                tabela.append([id, data, conf, idCliente, idServico])

            df = pd.DataFrame(tabela, columns=['Id', 'Data', 'Confirmado', 'Cliente', 'Serviço'])

            st.dataframe(df, use_container_width=True)

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