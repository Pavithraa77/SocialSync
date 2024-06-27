from master_graph import *
import csv
from master_graph_city import *
from collections import deque

# Creating instance of users
main_server = Graph()
# Creating instnce of cities
south_india_graph = Graph1()

# Function to store the accounts in respective locations
# O(V)


def link_accounts_and_cities(south_india_graph, main_server):
    user_accounts = main_server.vertices()
    for i in user_accounts:
        city = i.location
        find_city = south_india_graph.get_vertex(city)
        find_city.user_accounts.append(i)

# Breadth First Search at the same time , checks for range distance
# O(V+E)


def bfs(graph, start_vertex, max_distance):
    visited = set()
    queue = deque([(start_vertex, 0)])
    surrounding_cities = []

    while queue:
        current_vertex, distance = queue.popleft()
        visited.add(current_vertex)

        if distance <= max_distance:
            surrounding_cities.append(current_vertex.city)

            for neighbor, edge in graph.outgoing[current_vertex].items():
                if neighbor not in visited:
                    queue.append((neighbor, distance + edge.weight))

    return surrounding_cities


# Functino to populate the nodes
def populate():

    # Add cities as vertices
    cities = [
        "Bangalore",
        "Chennai",
        "Hyderabad",
        "Kochi",
        "Mysore",
        "Thiruvananthapuram",
        "Coimbatore",
        "Mangalore",
        "Vijayawada",
        "Visakhapatnam"
    ]

    for city in cities:
        south_india_graph.insertVertex(city)

    # Add edges with distances
    distances = {
        ("Bangalore", "Chennai"): 350,
        ("Bangalore", "Hyderabad"): 570,
        ("Bangalore", "Kochi"): 530,
        ("Bangalore", "Mysore"): 145,
        ("Bangalore", "Thiruvananthapuram"): 730,
        ("Bangalore", "Coimbatore"): 370,
        ("Bangalore", "Mangalore"): 350,
        ("Bangalore", "Vijayawada"): 680,
        ("Bangalore", "Visakhapatnam"): 1080,
        ("Chennai", "Hyderabad"): 630,
        ("Chennai", "Kochi"): 690,
        ("Chennai", "Mysore"): 480,
        ("Chennai", "Thiruvananthapuram"): 720,
        ("Chennai", "Coimbatore"): 500,
        ("Chennai", "Mangalore"): 710,
        ("Chennai", "Vijayawada"): 430,
        ("Chennai", "Visakhapatnam"): 800,
        ("Hyderabad", "Kochi"): 1050,
        ("Hyderabad", "Mysore"): 770,
        ("Hyderabad", "Thiruvananthapuram"): 1270,
        ("Hyderabad", "Coimbatore"): 950,
        ("Hyderabad", "Mangalore"): 750,
        ("Hyderabad", "Vijayawada"): 270,
        ("Hyderabad", "Visakhapatnam"): 700,
        ("Kochi", "Mysore"): 530,
        ("Kochi", "Thiruvananthapuram"): 220,
        ("Kochi", "Coimbatore"): 190,
        ("Kochi", "Mangalore"): 420,
        ("Kochi", "Vijayawada"): 1130,
        ("Kochi", "Visakhapatnam"): 1660,
        ("Mysore", "Thiruvananthapuram"): 640,
        ("Mysore", "Coimbatore"): 260,
        ("Mysore", "Mangalore"): 260,
        ("Mysore", "Vijayawada"): 710,
        ("Mysore", "Visakhapatnam"): 1210,
        ("Thiruvananthapuram", "Coimbatore"): 430,
        ("Thiruvananthapuram", "Mangalore"): 620,
        ("Thiruvananthapuram", "Vijayawada"): 1190,
        ("Thiruvananthapuram", "Visakhapatnam"): 1520,
        ("Coimbatore", "Mangalore"): 400,
        ("Coimbatore", "Vijayawada"): 910,
        ("Coimbatore", "Visakhapatnam"): 1420,
        ("Mangalore", "Vijayawada"): 890,
        ("Mangalore", "Visakhapatnam"): 1430,
        ("Vijayawada", "Visakhapatnam"): 430
    }

    for (city1, city2), distance in distances.items():
        south_india_graph.insert_edge(city1, city2, distance)

    with open('user.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            main_server.insertVertex(row['User ID'], row['Password'], row['Name'], int(row['Age']),
                                     row['Gender'], int(row['Phone']), row['Email'], row['Location'], row['Interest'])

    with open('connections.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            main_server.insert_edge(row['Source'], row['Target'])

    link_accounts_and_cities(south_india_graph, main_server)

    return main_server, south_india_graph
