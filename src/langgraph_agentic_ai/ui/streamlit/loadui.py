import streamlit as st
import os
from datetime import date

from langchain_core.message import AIMessage, HumanMessage
from src.langgrap_agentic_ai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config() #config
        self.user_controls = {}