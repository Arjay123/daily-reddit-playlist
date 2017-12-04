# Daily-Reddit-Playlist

A web application built with Django and ReactJS that creates Spotify (possible other apps in the future) playlists based off of a subreddit's (i.e. /r/hiphopheads) song submissions for the previous day.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installation

It's recommended to use [vagrant](https://www.vagrantup.com/docs/installation/) to create your dev environment. Otherwise, ensure your dev environment is ubuntu 14.04.

If you already have the trusty64 box, make sure it is at least version 20170810.0.0.

- Check Version [`vagrant box list`](https://www.vagrantup.com/docs/cli/box.html#box-list)
- Update Version [`vagrant box update --box ubuntu/trusty64`](https://www.vagrantup.com/docs/cli/box.html#box-update)

If using vagrant:

1. Fork and clone the repository on your host
2. Navigate to the repo root (directory with the Vagrantfile)
3. Start up the vagrant server `vagrant up`
4. Ssh to the vagrant server `vagrant ssh`
5. Navigate to the shared folder `cd /vagrant`
6. Run the shell script `./ubuntu_script.sh` (ensure the shell script has execution access `chmod +x ubuntu_script.sh`)

If using other dev env (with ubuntu 14.04):

1. Fork and clone the repository on your server
2. Navigate to the repo root
3. Run the shell script `./ubuntu_script.sh` (ensure the shell script has execution access `chmod +x ubuntu_script.sh`)


## Running the tests

TODO

## Deployment

TODO

## Built With

* [Django](https://www.djangoproject.com/)
* [React](https://reactjs.org/)
* [SpotifyAPI](https://developer.spotify.com/web-api/)
* [RedditAPI](https://developer.spotify.com/web-api/)

## Contributing

TODO


## Authors

* **Arjay Nguyen** - *Initial work* - [Arjay123](https://github.com/Arjay123)

## License

TODO


## TODO

- Python script to parse previous day's song submissions
- Connect to spotify to get playlist info
- UI/UX Improvements
