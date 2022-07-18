import configparser

from graph import Graph


def main():
    # Configure settings
    config = configparser.ConfigParser()
    config.read('config.cfg')
    azure_settings = config['azure']

    graph: Graph = Graph(azure_settings)

    # Acquiring all the teams in the organisation - the result is a list of dictionaries
    teams = get_teams(graph)

    # Adding a list of members to the teams
    teams_with_members = get_members(graph, teams)

# Returns a list of all the teams with all their attributes
def get_teams(graph: Graph):
    teams = graph.get_all_teams().get('value')

    return teams

def get_members(graph: Graph, teams):
    # Adding the members to each team
    for team in teams:
        teams_id = team.get('id')
        members = graph.get_members(teams_id)

        # Adding the members to the teams dictionary
        team['members'] = members.get('value')

    return teams


# Driver Code
if __name__ == "__main__":
    main()
