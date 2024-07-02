# Social Sync

### A Graph-Based Approach to Friend Recommendations on Social Media

## Overview

Social Sync is a comprehensive friend recommendation system designed for social media platforms. It utilizes graph theory to suggest potential friends based on shared mutual friends, geographic proximity, and common interests. This system aims to enhance user engagement while maintaining privacy and scalability.

## Problem Statement

Design and implement a friend recommendation system for social media that:

- Analyzes user network graphs.
- Suggests friends based on mutual connections, location, and interests.
- Enhances social connectivity.
- Ensures user privacy and system scalability.

## Why a Graph-Based Approach?

- **Mutual Friend Recommendations:** Discover new connections by leveraging mutual friends.
- **Location-Based Suggestions:** Connect with users nearby.
- **User Search:** Easily locate and connect with users in the network.
- **Friends List Management:** Seamlessly view and manage your friends list.
- **Broadcasting Messages:** Share event details with interested users.
- **Interest-Based Clustering:** Admins can access clusters of users with shared interests.

## Features

### Admin Features

- **Broadcast Messages:** Admins can broadcast messages to all nodes.
- **Clustering Based on Interests:** Manages clustering and visualization.
  - **Functions:**
    - `cluster(self)`: Manages clustering and visualization.
    - `create_random_graph(self, vertices)`: Generates a random graph from a list of vertices.
    - `visualize_graphs(self, G1, G2, G3)`: Visualizes three graphs using Matplotlib.

### User Features

- **Friend Recommendations:**
  - Based on mutual friends.
  - Users can select a User ID from the table to follow.
  - **Functions:**
    - `recommend()`: Identifies mutual connections using cycles detected between users.
    - `detect_cycle_between()`: Uses DFS to find cycles between two vertices.

- **Location-Based Recommendations:**
  - Users enter a distance range to see nearby cities using BFS.
  - Lists user accounts in the starting city for the user to follow.
  - **Function:**
    - `bfs(graph, start_vertex, max_distance)`: Finds all cities within the specified range.

- **Find Friends of Friends:**
  - **Function:**
    - `find_friends_friends(user)`: Fetches transitive followings and recommendations for the user.

### Transitive Closure
- **Purpose:** Enhances the recommendation process by considering indirect connections.
- **Function:** 
  - `transitive_closure(graph)`: Computes the transitive closure of the graph to identify all reachable nodes from any given node, helping in broader friend recommendations.

## Implementation

### Challenges

- **CSV File Usage:** Real-time updates involve constant reading and writing to the CSV file.
- **Self-Recommendation Issue:** Ensuring users are not recommended to themselves.

### Future Prospects

Machine learning, network analysis, and user behavior modeling will shape the next generation of friend recommendation systems, further enriching social interactions.

## File Descriptions

- **login.py:** Contains the user login functionality.
- **predefined_prompt.py:** Implements the core graph functionalities for user recommendations and location-based services.

## Usage

1. **Setup:**
   - Ensure all required libraries are installed.
   - Prepare the CSV files (`user.csv` and `connections.csv`) with the necessary user data and connections.

2. **Run the system:**
   - Execute the Python scripts to start the recommendation system.
   - Use the provided functions to explore recommendations and user connections.

3. **Admin Operations:**
   - Use admin features to broadcast messages and manage user clusters.

