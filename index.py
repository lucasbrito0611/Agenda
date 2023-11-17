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
    def menu_visitante():
      op = st.sidebar.selectbox("Menu", ["Login", "Abrir conta no Sistema"])
      if op == "Login": LoginUI.main()
      if op == "Abrir conta no Sistema": AbrirContaUI.main()
    def menu_cliente():
      op = st.sidebar.selectbox("Menu", ["Agenda de Hoje", "Agendar Horário", "Visualizar Agendamentos", "Editar Perfil"])
      if op == "Agenda de Hoje": AgendaHojeUI.main()
      if op == "Agendar Horário": AgendarHorarioUI.main()
      if op == "Visualizar Agendamentos": VisualizarAgendaUI.main()
      if op == "Editar Perfil": EditarPerfilUI.main()
    def menu_admin():
      op = st.sidebar.selectbox("Menu", ["Manter Clientes", "Manter Serviços", "Manter Agenda", "Abrir Agenda do Dia", "Agenda de Hoje", "Reajuste de Preço", "Confirmar Agendamento", "Editar Perfil"])
      if op == "Manter Clientes": ManterClienteUI.main()
      if op == "Manter Serviços": ManterServicoUI.main()
      if op == "Manter Agenda": ManterAgendaUI.main()
      if op == "Abrir Agenda do Dia": AbrirAgendaUI.main()
      if op == "Agenda de Hoje": AgendaHojeUI.main()
      if op == "Reajuste de Preço": ServicoReajusteUI.main()
      if op == "Confirmar Agendamento": ConfirmarAgendaUI.main()
      if op == "Editar Perfil": EditarPerfilUI.main()
    def logout():
      if st.sidebar.button('Logout'):
        del st.session_state["cliente_id"]
        del st.session_state["cliente_nome"]
        st.rerun()
    def sidebar():
      if "cliente_id" not in st.session_state:
        IndexUI.menu_visitante()
      else:
          if st.session_state["cliente_nome"] != "admin":
            IndexUI.menu_cliente()
          else:
            IndexUI.menu_admin()
            
          st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
          IndexUI.logout()

    def main():
      View.cliente_admin()
      IndexUI.sidebar()

IndexUI.main()