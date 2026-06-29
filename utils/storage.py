from google.cloud import storage
from google.oauth2 import service_account
import streamlit as st

BUCKET_NAME = "bucket-copa-ana-flavia"

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

client = storage.Client(
    credentials=credentials,
    project=credentials.project_id
)

bucket = client.bucket(BUCKET_NAME)


def baixar_imagem(nome):
    blob = bucket.blob(f"imagens_jogadores/{nome}")
    return blob.download_as_bytes()