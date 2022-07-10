# Pre setup

## Virtual environment

After downloading the project - create a virtual environment:

```
python -m venv venv
```

## Install requirements

```
pip install -r requirements.txt
```

## Build docker containers

Build app and database containers:

```
docker-compose build
```

# Usage

## User

App is using token authentication. To use the recipe app you must have a user with its own token.

### Create a user

```
http://127.0.0.1:8000/api/user/create/
```

### Get the token

After you create a user pass your data to get the token. Use it through the app to get access to the endpoints.

```
http://127.0.0.1:8000/api/user/token/
```

### Update your user's data

```
http://127.0.0.1:8000/api/user/me/
```

You can update your email, password, and name.

## Tags

### List all tags and create new tags:

```
http://127.0.0.1:8000/api/recipe/tags/
```

## Ingredients

### List all ingredients and create new ingredients:

```
http://127.0.0.1:8000/api/recipe/ingredients/
```

## Recipes

### List all recipes and create new recipes:

```
http://127.0.0.1:8000/api/recipe/recipes/
```

### Retrieve, update and delete recipe:

```
http://127.0.0.1:8000/api/recipe/recipes/id/
```

Where ```id``` is the id of the recipe. Example:

```
http://127.0.0.1:8000/api/recipe/recipes/1/
```

This endpoint for the recipe with the ```id=1```.

### Upload an image for recipe:

Each recipe can have an image. To upload it go to the ```url```:

```
http://127.0.0.1:8000/api/recipe/recipes/id/upload-image/
```

As in the detail view, you should pass the ```id``` to upload an image for the specific recipe. Example:

```
http://127.0.0.1:8000/api/recipe/recipes/1/upload-image/
```

Upload an image for the recipe with ```id=1```.

### Filtering recipes by tags and ingredients:

```
http://127.0.0.1:8000/api/recipe/recipes/?tags=tag_id&ingredients=ingredient_id
```

Recipe include tag with ```id=tag_id``` and ingredient with ```id=ingredient_id```. Example:

```
http://127.0.0.1:8000/api/recipe/recipes/?tags=2&ingredients=1
```

### Filtering tags and ingredients:

If you want to see only assigned tags for recipes just set ```?assigned_only=1``` in the url as a parameter. Example:

```
http://127.0.0.1:8000/api/recipe/tags/?assigned_only=1
```

Not assigned only:

```
http://127.0.0.1:8000/api/recipe/tags/?assigned_only=0
```

Same with ingredients. Examples:

```
http://127.0.0.1:8000/api/recipe/ingredients/?assigned_only=1
```

```
http://127.0.0.1:8000/api/recipe/ingredients/?assigned_only=0
```

# Test

## To run all suits of unit tests:

```
docker-compose run --rm app sh -c "python manage.py test"
```
