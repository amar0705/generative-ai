# In this exercise, you will create a simple, Instagram-like web application using Flask. 
# This application will not involve any databases or user authentication; instead, data will be stored in Python data structures 
# (Use Dictionary).

# Your application should support the following operations:

# Post Creation: An endpoint should allow the creation of a new post with a username and a caption. For simplicity, 
# a "post" will be a dictionary with username and caption keys. Post Viewing: The application should have an endpoint that lists all posts. 
# Post Deletion: The application should allow the deletion of a post, given its unique ID.
# Use Python's data structures (like list and dictionary) to store the posts. 
# You can assume that the server will not be shut down, so data persistence between runs is not necessary.

from flask import Flask, jsonify, request;

app = Flask(__name__)

posts = []
next_post_id = 1

@app.route("/", methods = ['GET'])
def get_posts():
    return jsonify(posts)

@app.route("/posts", methods = ["POST"])
def create_post():
    next_post_id
    data = request.get.json()
    username = data.get("username")
    caption = data.get("caption")

    if not username or not caption:
        return jsonify({'error':"Fields required"})
    
    post = {
        'id': next_post_id,
        'username': username,
        'caption': caption
    }

    posts.append(post)
    next_post_id += 1
    return jsonify({'message':'post created successfully', 'post':post})

@app.route('/posts/:id', methods = ['DELETE'])
def delete_post(id):
    for post in posts:
        if(post['id'] == id):
            posts.remove(post)
            return jsonify({'message':"Post deleted"})
        
    return jsonify({'error':"Not Found"})

if __name__ == '__main__':
    app.run(debug = True)