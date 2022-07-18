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


    # Aquiring all the teams in the organisation 
    def get_all_teams(self):
        endpoint = '/groups'
        select = 'id, displayName'

        request_url = f'{endpoint}?$select={select}'

        response = self.app_client.get(request_url)
        return response.json()

    # Getting a list of all the members of the team
    def get_members(self, team_id):
        endpoint = f'/groups/{team_id}/members'
        select = 'id, userPrincipalName'

        request_url = f'{endpoint}?$select={select}'

        response = self.app_client.get(request_url)
        return response.json()
