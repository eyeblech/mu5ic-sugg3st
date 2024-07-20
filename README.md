
# Introduction

"Python script to get notified of a random music to listen to, on Discord, using Spotify API and Discord Webhook."

# Getting Started


## Step 1: Set up a Discord Webhook
* Open your Discord server.

* Go to Server Settings > Integrations > Webhooks.

* Click "New Webhook" and customize it as you like.

* Copy the Webhook URL.

## Step 2: Set Up Spotify API Access
* Create a Spotify Developer Account:

* Go to the Spotify Developer Dashboard and log in with your Spotify account.
  Create a New Spotify App:

* Click "Create an App" and fill in the required fields (App name, App   description, etc)
* After creating the app, you'll receive a "Client ID" and "Client Secret." Save these credentials.
### Get Access Token:

* Use the Spotify Web API Console or the Authorization Code Flow to get an access token.
* For simplicity, you can manually obtain a token via the Web API Console:
* Go to the Spotify Web API Console.
  Log in with your Spotify account and click "Get Token" to authorize and get an   access token.

```sh
curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"

```
* replace the client_id and client_secret before sending the request to get your access token

## Step 3: Preparing the Python Script
* Install required libraries 

```sh
pip install requests
```
* copy the python script and make a new python file `song-notifier.py`


* Replace Placeholder Values

  Open the `song-notifier.py` file and replace

  `client_id`, `client_secret`,`access_token` and 
  `YOUR_DISCORD_WEBHOOK_URL`

* you can always modify the genre e.g `metal,rock,pop,rap,country e.t.c`, to get recommended genre specified songs
![genre](https://github.com/user-attachments/assets/dc172486-8e65-43f3-97d8-2014b7e201f1)



## Running locally/cloud

* You can use Google Console , AWS or Heroku e.t.c
* "Instead, you choose to run it locally, create a cron job so that it can automatically run at specified intervals of time."

```sh
crontab -e
```
```sh
0 */8 * * * /usr/bin/python /home/samsep10l/Desktop/song-notifier.py
```

* to list cron jobs
```sh
crontab -l
```
![python](https://github.com/user-attachments/assets/1e63fbe7-f187-4801-9fad-63be961d68bd)
![notify](https://github.com/user-attachments/assets/ec5031e7-aeab-46e0-a6f0-4d5d03ba8e48)




