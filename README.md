# Social Media Backend

This is the backend for a simple social media app created using Django Rest Framework (DRF).

## Features
- User authentication and authorization
- Post creation, editing, and deletion
- Commenting on posts
- Liking and unliking posts
- Following and unfollowing users

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mv-anirudh/SocialMedia.git
    cd SocialMedia
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt  # Or use `pipenv install` if using Pipfile
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

### API Endpoints

- **Authentication**
  - `POST /api/auth/login/`
  - `POST /api/auth/register/`
  - `POST /api/auth/logout/`

- **Posts**
  - `GET /api/posts/`
  - `POST /api/posts/`
  - `GET /api/posts/{id}/`
  - `PUT /api/posts/{id}/`
  - `DELETE /api/posts/{id}/`

- **Comments**
  - `GET /api/posts/{post_id}/comments/`
  - `POST /api/posts/{post_id}/comments/`
  - `DELETE /api/comments/{id}/`

- **Likes**
  - `POST /api/posts/{post_id}/like/`
  - `DELETE /api/posts/{post_id}/like/`

- **Follows**
  - `POST /api/users/{user_id}/follow/`
  - `DELETE /api/users/{user_id}/follow/`

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a Pull Request

## License

This project is licensed under the MIT License.
