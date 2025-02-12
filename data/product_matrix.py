# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# from config.config import GOOGLE_SHEET_ID, GOOGLE_SHEET_CONTACTS_ID
# import os
# import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# def get_product_data():
#     scope = [
#         "https://spreadsheets.google.com/feeds",
#         "https://www.googleapis.com/auth/spreadsheets",
#         "https://www.googleapis.com/auth/drive.file",
#         "https://www.googleapis.com/auth/drive"
#     ]

#     creds_dict = {
#         "type": "service_account",
#         "project_id": os.getenv("GOOGLE_PROJECT_ID"),
#         "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
#         "private_key": os.getenv("GOOGLE_PRIVATE_KEY", '').replace("\\n", "\n"),
#         "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
#         "client_id": os.getenv("GOOGLE_CLIENT_ID"),
#         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#         "token_uri": "https://oauth2.googleapis.com/token",
#         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#         "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_X509_CERT_URL")
#     }

#     try:
#         creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
#         client = gspread.authorize(creds)
#         sheet = client.open_by_key(GOOGLE_SHEET_ID).sheet1
#         data = sheet.get_all_records()
#         return data
#     except Exception as e:
#         logger.error(f"Ошибка при получении данных из Google Sheets: {e}")
#         return []

# def save_contact_info(user_id, engine_brand, phone_number):
#     scope = [
#         "https://spreadsheets.google.com/feeds",
#         "https://www.googleapis.com/auth/spreadsheets",
#         "https://www.googleapis.com/auth/drive.file",
#         "https://www.googleapis.com/auth/drive"
#     ]

#     creds_dict = {
#         "type": "service_account",
#         "project_id": os.getenv("GOOGLE_PROJECT_ID"),
#         "private_key_id": os.getenv("GOOGLE_PRIVATE_KEY_ID"),
#         "private_key": os.getenv("GOOGLE_PRIVATE_KEY", '').replace("\\n", "\n"),
#         "client_email": os.getenv("GOOGLE_CLIENT_EMAIL"),
#         "client_id": os.getenv("GOOGLE_CLIENT_ID"),
#         "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#         "token_uri": "https://oauth2.googleapis.com/token",
#         "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#         "client_x509_cert_url": os.getenv("GOOGLE_CLIENT_X509_CERT_URL")
#     }

#     try:
#         creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
#         client = gspread.authorize(creds)
#         sheet = client.open_by_key(GOOGLE_SHEET_CONTACTS_ID).sheet1
#         sheet.append_row([str(user_id), engine_brand, phone_number])
#         logger.info(f"Контактные данные сохранены: {user_id}, {engine_brand}, {phone_number}")
#     except Exception as e:
#         logger.error(f"Ошибка при сохранении контактных данных: {e}")
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
from dotenv import load_dotenv

load_dotenv()

def get_google_sheets_client():
    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        os.getenv('GOOGLE_CREDS_JSON'), scope)
    return gspread.authorize(credentials)

def get_product_data():
    client = get_google_sheets_client()
    sheet = client.open_by_key(os.getenv('GOOGLE_SHEET_ID')).worksheet("ProductMatrix")
    return sheet.get_all_records()

def save_contact_info(chat_id, engine_brand, phone):
    client = get_google_sheets_client()
    sheet = client.open_by_key(os.getenv('GOOGLE_SHEET_ID')).worksheet("Leads")
    sheet.append_row([chat_id, engine_brand, phone, str(datetime.now())])