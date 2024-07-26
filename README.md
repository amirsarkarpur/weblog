# My Django Blog Project

This is a Django-based blog project that allows users to view and interact with blog posts.

## Features

- View categories and posts
- View post details including comments and likes
- Pin posts
- User authentication and authorization

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

4. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

6. **Open your web browser and go to** `http://127.0.0.1:8000/`

## Usage

- Go to the admin panel at `http://127.0.0.1:8000/admin/` to add categories, posts, and manage comments.
- View the list of posts by category and interact with them.

## Models

- `Post`: Represents a blog post.
- `Category`: Represents the category of a blog post.
- `Comment`: Represents a comment on a blog post.
- `Like`: Represents a like on a blog post.
- `Pin`: Represents a pinned post by a user.

## Views

- `show_category`: Displays the list of categories.
- `post_list`: Displays the list of posts in a category.
- `post_detail`: Displays the details of a specific post.
- `pin_list`: Displays the list of pinned posts by the user.

## URL Configuration

- `path('', views.show_category, name='show_category')`
- `path('post/<int:post_id>/', views.post_detail, name='post_detail')`
- `path('llists/<int:category_id>/', views.post_list, name='post_list')`
- `path('pin/', views.pin_list, name='pin_list')`

## License

This project is licensed under the MIT License.
