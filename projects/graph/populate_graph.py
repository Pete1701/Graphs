import random
import time

def populate_graph(self, num_users, avg_friendships):
    """
    Takes a number of users and an average number of friendships
    as arguments​

    Creates that number of users and a randomly distributed friendships
    between those users.

    The number of users must be greater than the average number of friendships.
    """
    # Reset graph
    self.last_id = 0
    self.users = {}
    self.friendships = {}​

    # Add users
    for i in range(num_users):
        self.add_user(f"User {i}")​

    # Create friendships
    possible_friendships = []​

    for user_id in self.users:
        for friend_id in range(user_id + 1, self.last_id + 1):
            possible_friendships.append((user_id, friend_id))​

    # Shuffle the possible friendships
    random.shuffle(possible_friendships)​

    # Add friendships
    for i in range(num_users * avg_friendships // 2):
        friendship = possible_friendships[i]
        self.add_friendship(friendship[0], friendship[1])

def populate_graph_2(self, num_users, avg_friendships):
    # Reset graph
    self.last_id = 0
    self.users = {}
    self.friendships = {}

    # Add users
    for i in range(num_users):
        self.add_user(f"User {i+1}")

    # Create friendships
    target_friendships = num_users * avg_friendships
    total_friendships = 0
    collisions = 0


    while total_friendships < target_friendships:
        user_id = random.randint(1, self.last_id)
        friend_id = random.randint(1, self.last_id)

        if self.add_friendship(user_id, friend_id):
            total_friendships += 2
        else:
            collisions += 1
    print(f"COLLISIONS: {collisions}")

def get_all_social_paths(self, user_id):
    q = Queue()
    # visited = set()
    visited = {}
    q.enqueue([user_id])
    while q.size() > 0:
        # u = q.dequeue()
        path = q.dequeue()
        u = path[-1]
        if u not in visited:
            # visited.add(u)
            visited[u] = path
            for neighbor in self.friendships[u]:
                # q.enqueue(neighbor)
                path_copy = list(path)
                path_copy.append(neighbor)
                q.enqueue(path_copy)
                
    return visited



# def get_all_social_paths(self, user_id):
#     visited = {}  # Note that this is a dictionary, not a set
#     path_queue = collections.deque()
#     path_queue.append([user_id])
#     while path_queue:
#         path = path_queue.popleft()
#         friend_id = path[-1]
#         for id in self.friendships[friend_id]:
#             if id not in visited:
#                 new_path = path.copy()
#                 new_path.append(id)
#                 path_queue.append(new_path)
#                 visited[friend_id] = path






