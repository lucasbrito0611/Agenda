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
            st.write("Nenhum horário cadastrado")
        else:
            tabela = []
            
            for agenda in View.agenda_listar():
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

            op = st.selectbox("Selecione uma agenda para confirmar", agendas)
            id = op.get_id()
            idCliente = op.get_id_cliente()
            idServico = op.get_id_servico()
            conf = op.get_confirmado()
            if st.button("Confirmar"):
                if conf == True:
                    st.error('Agenda já confirmada!')
                    time.sleep(2)
                    st.rerun()
                elif idCliente == 0 or idServico == 0:
                    st.error('Você não pode confirmar uma agenda sem cliente ou sem serviço!')
                    time.sleep(2)
                    st.rerun()
                else:
                    View.agenda_confirmar(id)
                    st.success('Agenda confirmada com sucesso!')
                    time.sleep(1)
                    st.rerun()