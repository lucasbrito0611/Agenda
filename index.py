from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manteragendaUI import ManterAgendaUI
from templates.abriragendaUI import AbrirAgendaUI
from templates.loginUI import LoginUI
from templates.agendahojeUI import AgendaHojeUI
from templates.servicoreajusteUI import ServicoReajusteUI
from templates.abrircontaUI import AbrirContaUI
from templates.editarperfilUI import EditarPerfilUI
from templates.agendarhorarioUI import AgendarHorarioUI
from templates.visualizaragendaUI import VisualizarAgendaUI
from templates.confirmaragendaUI import ConfirmarAgendaUI
from views import View

import streamlit as st

class IndexUI:
    def sidebar():
      if "cliente_id" not in st.session_state:
        op = st.sidebar.selectbox("Menu", ["Login", "Abrir conta no Sistema"])
        if op == "Login": LoginUI.main()
        if op == "Abrir conta no Sistema": AbrirContaUI.main()
      else:
          st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
          if st.sidebar.button('Logout'):
             del st.session_state["cliente_id"]
             del st.session_state["cliente_nome"]
             st.rerun()

          clientes = View.cliente_listar()
          if st.session_state["cliente_nome"] != clientes[0].get_nome():
            op1 = st.sidebar.selectbox("Menu", ["Agenda de Hoje", "Agendar Horário", "Visualizar Agendamentos", "Editar Perfil"])
            if op1 == "Agenda de Hoje": AgendaHojeUI.main()
            if op1 == "Agendar Horário": AgendarHorarioUI.main()
            if op1 == "Visualizar Agendamentos": VisualizarAgendaUI.main()
            if op1 == "Editar Perfil": EditarPerfilUI.main()
          else:
            op2 = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda", "Abrir Agenda do Dia", "Agenda de Hoje", "Reajuste de Preço", "Confirmar Agendamento", "Editar Perfil"])
            if op2 == "Manter Clientes": ManterClienteUI.main()
            if op2 == "Manter Serviços": ManterServicoUI.main()
            if op2 == "Manter Agenda": ManterAgendaUI.main()
            if op2 == "Abrir Agenda do Dia": AbrirAgendaUI.main()
            if op2 == "Agenda de Hoje": AgendaHojeUI.main()
            if op2 == "Reajuste de Preço": ServicoReajusteUI.main()
            if op2 == "Confirmar Agendamento": ConfirmarAgendaUI.main()
            if op2 == "Editar Perfil": EditarPerfilUI.main()

    def main():
      View.cliente_admin()
      IndexUI.sidebar()

IndexUI.main()


