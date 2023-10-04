from zeep import Client, Settings
import yaml

with open('config/config.yaml', 'rb') as file:
    data = yaml.safe_load(file)

wsdl = data['address']

settings = Settings(strict=False)
client = Client(wsdl=wsdl, settings=settings)


def check_text(text):
    return client.service.checkText(text)[0]['s']