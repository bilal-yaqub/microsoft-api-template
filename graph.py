# Importing the dependencies
from configparser import SectionProxy
from azure.identity import ClientSecretCredential
from msgraph.core import GraphClient

class Graph:
    # Declaring mappings
    settings: SectionProxy
    client_credential: ClientSecretCredential
    app_client: GraphClient

    # Setting up the variables needed to make a call to the graph API
    def __init__(self, config: SectionProxy):
        self.settings = config

        if not hasattr(self, 'client_credential'):
            client_id = self.settings['clientId']
            tenant_id = self.settings['tenantId']
            client_secret = self.settings['clientSecret']

            self.client_credential = ClientSecretCredential(tenant_id, client_id, client_secret)

        if not hasattr(self, 'app_client'):
            self.app_client = GraphClient(credential=self.client_credential,
                                          scopes=['https://graph.microsoft.com/.default'])


    # Define an API call here
    def api_call(self):
        #TO-DO
        return

