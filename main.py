import configparser

from graph import Graph

# Define an API call here
def make_graph_call(graph: Graph):
    res = graph.api_call()
    return res

def main():
    # Load settings
    config = configparser.ConfigParser()
    config.read('config.cfg')
    azure_settings = config['azure']

    graph: Graph = Graph(azure_settings)

    # Call the function
    make_graph_call(graph)

# Driver Code
if __name__ == "__main__":
    main()