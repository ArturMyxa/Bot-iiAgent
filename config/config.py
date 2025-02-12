# import os
# from dotenv import load_dotenv

# load_dotenv()

# TELEGRAM_BOT_TOKEN = "7592753727:AAGI3aVDF4angQr5Nn9TMRNpwonBY7EWEtE"
# GOOGLE_SHEET_ID = "17Vkp9p_FLihy7IESWUs6eIvJVOoXGgUL"
# GOOGLE_SHEET_CONTACTS_ID = "16OWjP2rT8ObeGVibKX-a4jtRD4U_DkMU2Pllus9VRGc"
# GOOGLE_PROJECT_ID = "teleiagent"
# GOOGLE_PRIVATE_KEY_ID = "d525f29db58ca8cdfa15e324d0df7580814ea651"
# GOOGLE_PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCz..."
# GOOGLE_CLIENT_EMAIL = "sheetsbot@teleiagent.iam.gserviceaccount.com"
# GOOGLE_CLIENT_ID = "110530763400503171328"
# GOOGLE_CLIENT_X509_CERT_URL = "https://www.googleapis.com/robot/v1/metadata/x509/sheetsbot%40teleiagent.iam.gserviceaccount.com"

import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")
GOOGLE_CREDS_JSON = os.getenv("GOOGLE_CREDS_JSON")