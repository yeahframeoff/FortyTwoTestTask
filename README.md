42-test template
===========================

A Django 1.6+ project template

Use fortytwo_test_task.settings when deploying with getbarista.com

### Recomendations
* apps in apps/ folder
* use per-app templates folders
* use per-app static folders
* use migrations
* use settings.local for different environments
* common templates live in templates/
* common static lives in assets/
* management commands should be proxied to single word make commands, e.g make test

### What was done here
1. Main page that stores user info;
2. Middleware to save requests in database (`requests_saver` app);
3. Context processor that adds `django.conf.settings` into context as plain dictionary;
4. Image upload and resize to 200x200px maintaining aspect ratio.
