import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# 1. Get all posts
def get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    print("GET /posts:", response.status_code)
    print(response.json()[:2])  # Show first 2 posts

# 2. Create a new post
def create_post():
    payload = {
        "title": "Learning APIs",
        "body": "This is my first post using JSONPlaceholder!",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    print("POST /posts:", response.status_code)
    print(response.json())

# 3. Update a post
def update_post(post_id):
    payload = {
        "title": "Updated Title",
        "body": "Updated content.",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)
    print(f"PUT /posts/{post_id}:", response.status_code)
    print(response.json())

# 4. Delete a post
def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    print(f"DELETE /posts/{post_id}:", response.status_code)

# Run the functions
get_posts()
create_post()
update_post(1)
delete_post(1)