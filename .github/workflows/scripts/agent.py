import os
import json
import smtplib
import anthropic
from datetime import datetime, timedelta
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

ANTHROPIC_API_KEY  = os.environ["ANTHROPIC_API_KEY"]
GMAIL_USER         = os.environ["GMAIL_USER"]
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]
SUBSCRIBERS_FILE   = Path(__file__).parent.parent / "subscribers.json"

TEMAS = [
    "Mercado de capitais e CVM",
    "Energia elétrica e ANEEL",
    "Petróleo e gás (ANP)",
    "Telecomunicações e Anatel",
    "Data centers e infraestrutura digital",
    "Infraestrutura física, portos e ferrovias (ANTT/ANTAQ)",
    "Cripto e tokenização de ativos (BACEN)",
    "Inteligência artificial e regulação (ANPD/PL 2338)",
    "Minerais críticos e commodities (ANM)",
    "Direito concorrencial e antitruste (CADE)",
    "Regulação financeira e bancária (BACEN/Pix/Open Finance)",
]

SEMANA_A
