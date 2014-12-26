#!/usr/bin/python

'''spotify playlist downloader via command-line browsing'''

import sys
import os
import requests
import json

def authenticate_user(username, password):
	scope = "playlist-read-private"
	return 1

def display_playlists(playlists):
	for i in range(len(playlists)):
		print i+1, playlists[i]

def get_data(url):
	headers = {'Accept': 'application/json', 'Authorization': 'Bearer BQCHJLyIg5dqE8haHyC9R0i_U7RP3kviwmdzhR4RMQfGNFnthfjmIlJcZCLC7cDN1wBymrtFGy2LsEMjtopqpCN7ICYzVYTt1_m-c-8AeVtHadRw0SVR4oBb2_N1_iIXD3KpIB7yn4UcvnytRHCsJ561zvcAbg'}	
	r = requests.get(url, headers=headers)
	json_data = r.json()
	return json_data, r.status_code

def generate_url(username):
	url = "https://api.spotify.com/v1/users/" + username + "/playlists"
	return url

def get_user_playlists(data):
	playlists = []
	for i in range(len(data['items'])):
        	playlists.append(data['items'][i]['name'])
	return playlists

def get_songs_from_playlist(url):
	songs_list = []
	response = requests.get(url)

def main():
	username = raw_input("Spotify Username: ")
	password = raw_input("Password: ")

	auth_success = authenticate_user(username, password)

	url = generate_url(username)
	data, success = get_data(url)

	#use exception instead
	if success:
		playlists = get_user_playlists(data)
		display_playlists(playlists) #with numbers

	download_choice = raw_input("Which playlist would you like to download? ")

#destination = playlists[download_choice] + ".zip" #save to zip file?!

#download form youtube?!

if __name__ == "__main__": main()
