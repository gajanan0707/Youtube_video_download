# Youtube_video_download
YouTube's videos Downloader is a Python Web application built with Django.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone git@github.com:gajanan0707/Youtube_video_download.git
$ cd youtube_videos_download
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.

![alt text](https://i.imgur.com/bkT7Egn.png)
![alt text](https://i.imgur.com/huiZU3p.png)
