#!/usr/bin/python

'''spotify playlist downloader via command-line browsing'''
'''user must make sure his/her playlist is public during the download process'''

import sys
import os
import requests
import json
import urllib
import urllib2

def http_request_response(url, values):
	data = urllib.urlencode(values)
	request = urllib2.Request(url, data)
	response = json.load(urllib2.urlopen(request))
	return response

def display_playlists(playlists):
	for i in range(len(playlists)):
		print i+1, playlists[i]

def get_data(url):
	headers = {'Accept': 'application/json', 'Authorization': 'Bearer BQCHJLyIg5dqE8haHyC9R0i_U7RP3kviwmdzhR4RMQfGNFnthfjmIlJcZCLC7cDN1wBymrtFGy2LsEMjtopqpCN7ICYzVYTt1_m-c-8AeVtHadRw0SVR4oBb2_N1_iIXD3KpIB7yn4UcvnytRHCsJ561zvcAbg'}	
	r = requests.get(url, headers=headers)
	json_data = r.json()
	return json_data, r.status_code

def generate_url(username, playlist_choice):
	playlist_id = playlist_choice#?!?!?!
	url = "https://api.spotify.com/v1/users/" + username + "/playlists/"
	if playlist_choice > 0:
		url = url + playlist_id + "/tracks/" #use actual playlist id-conversion
	return url

def get_user_playlists(username):
	playlists = []
	url = generate_url(username, 0)
	data, success = get_data(url)
	if success:
		for i in range(len(data['items'])):
        		playlists.append(data['items'][i]['name'])
	return playlists

def get_songs_from_playlist(username, playlist_choice):
	songs_list = []
	url = generate_url(username, playlist_choice)
	data, success = get_data(url)
	if success:
		for i in range(len(data['items'])):
			songs_list.append(data['items'][i]['name'])
	return songs_list

def main():
	client_id = 'd56ed89f1ba04b3e89a6e3df3a99b91c'
	client_secret = 'ac839d4102a24c62b28008675161ef07'
	redirect_uri = 'http://www.google.com'

	username = raw_input("Spotify Username: ")
	#check if username valid

	auth_url = "https://accounts.spotify.com/api/token"
	auth_values = {'grant_type': 'client_credentials','scope': 'user-read-private', 'client_id': client_id, 'client_secret': client_secret}
	auth_response = http_request_response(auth_url, auth_values)
	print auth_response
	access_token = auth_response['access_token']

	#auth_success = authenticate_user(username, password)

	#get_user_playlists(username)
	#use exceptions?!
	#display_playlists(playlists) #with numbers
	#playlist_choice = raw_input("Which playlist would you like to download? ")
	#get_songs_from_playlist(username, playlist_choice)

#destination = playlists[download_choice] + ".zip" #save to zip file?!
#add auth etc error checking too
#download form youtube?!

if __name__ == "__main__": main()
