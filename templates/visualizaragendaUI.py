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