# GTIYW

The clean, fast and right way to start a new Django `3.1` powered website.

## Getting Started

Setup project environment.

```bash
$ python manage.py migrate
$ python manage.py createsuperuser --username=joe --email=joe@example.com
$ python manage.py runserver [port]
```

## Features

An application that accepts the names of skills that we need to learn for a career.

For example, to become a web developer, we need to learn:

    HTML5
    CSS3
    JavaScript
    Backend language (PHP, Node.js, Python, ASP.NET, or Java)
    Bootstrap 4
    WordPress
    Backend Framework (Laravel, Codeigniter, Django, Flask, etc.)
    etc.

After entering the skills, there will be a “Generate Career Path” button. It instructs our program to search YouTube and select relevant videos/playlists according to each skill. In case there are many similar videos for skill then it will select the one with the most views, comments, likes, etc.

The program then groups these videos according to skills and display their thumbnail, title, and link in the GUI.

It will also analyze the duration of each video, aggregate them, and then inform us about how much time it will take to learn this career path.

Now, as a user, we can watch these videos which are ordered in a step by step manner to become a master in this career.
