from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 9365736
    API_HASH = "3fa1b478ca72a73d267e10188556cc34"
    # the name to display in your alive message
    ALIVE_NAME = "هادي"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://hbifpcsx:H1KGLnvFlLPFs5u9g6tjhNb9bbdA8zmc@salt.db.elephantsql.com/hbifpcsx"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "1BJWap1wBu8MYaAS7Xcbnl4M-qym80Q7WcoTR0c38A_Hf3S3t2qL1dE1vPeT2_FGmwC9n9DV1rQzhdTiQdH-5u4BiCEfbAtUacCwThZK_MK6I0Dib1-fZMpRKK-zChLp9YqRUvu_A2hYGShzq2pgr517mFjqmiqzoZ2R0AferTduQaWrRGPSLf0zFUF0W14HjqRu9IZfQTJcM82mZ7yjEiLqhHRcGF_m-uxcB3Xr-EzNRUOhmkqSdCc2aQC-3KzxMXzZQzlrT_Gpomv8e00xGAcbiyVx1OTtC09mOjOSlBvWPVfnYoHi8D-9ZcJvNyg_1x5QEyAEUNuHJQuhh4jUwsDmQL1JIXrc="
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "5111897157:AAGKx8QRGetJKugii06AwtLoHqE51AyYMbs"
    TG_BOT_USERNAME = "Q71bot"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001659591037
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = [5049024596]
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
