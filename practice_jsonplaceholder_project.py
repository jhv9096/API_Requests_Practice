import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# 1. Get all posts
def get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    print("\n📥 GET /posts")
    print("Status:", response.status_code)
    print("First 2 posts:", response.json()[:2])

# 2. Create a new post
def create_post():
    payload = {
        "title": "Learning APIs",
        "body": "This is my first post using JSONPlaceholder!",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    print("\n📝 POST /posts")
    print("Status:", response.status_code)
    post = response.json()
    print("Created Post:", post)
    return post["id"]  # Return the ID of the new post

# 3. Get a specific post
def get_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    print(f"\n🔍 GET /posts/{post_id}")
    print("Status:", response.status_code)
    print("Post:", response.json())

# 4. Update a post
def update_post(post_id):
    payload = {
        "title": "Updated Title",
        "body": "Updated content.",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=payload)
    print(f"\n✏️ PUT /posts/{post_id}")
    print("Status:", response.status_code)
    print("Updated Post:", response.json())

# 5. Delete a post
def delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    print(f"\n🗑️ DELETE /posts/{post_id}")
    print("Status:", response.status_code)

# Run the flow
get_posts()
new_post_id = create_post()
get_post(new_post_id)
update_post(new_post_id)
get_post(new_post_id)
delete_post(new_post_id)
get_post(new_post_id)  # This will likely return an empty object or 404