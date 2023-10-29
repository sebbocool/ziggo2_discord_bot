from os import environ

testing = True


# Discord
TOKEN = environ.get("DISCORD_TOKEN_ZIGGO2")

if testing:
    TOKEN = "MTE2Njg0MTY4MTg0NTQ0MDU4Mw.GBGHIJ.91B7yz7gbthR4vH9Zetpt2OUp3dD8oRrM0iF0I"

# DeepL
DEEPLTOKEN = environ.get("DEEPL_TOKEN")
