#!/usr/bin/python

'''spotify playlist downloader via command-line browsing'''
'''user must make sure his/her playlist is public during the download process'''

import sys
import os
import requests
import json
import urllib
import urllib2

def http_request_response(url, values, req_type):
	if req_type == 'GET':
		request = urllib2.Request(url, headers = values)
	elif req_type == 'POST':
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

def get_user_playlists(data):
	playlist_names = []
	playlist_ids = []
	playlist_owners = []
	#url = generate_url(username, 0)
	#data, success = get_data(url)
	#if success:
	for i in range(len(data['items'])):
		playlist_names.append(data['items'][i]['name'])
		playlist_ids.append(data['items'][i]['id'])
		playlist_owners.append(data['items'][i]['owner']['id'])
	return playlist_names, playlist_ids, playlist_owners

def get_songs_from_playlist(data):
	song_name = ''
	song_album = ''
	song_artists = []
	song = []
	songs_dict = {}
	songs_list = []
	song_val = {}
	#print songs_response['items'][5]['track']['album']['name']
	#print songs_response['items'][5]['track']['artists'][0]['name']
	#print songs_response['items'][5]['track']['name']

	#url = generate_url(username, 0)
	#data, success = get_data(url)
	#if success:
	for i in range(len(data['items'])):
		single_song_artists = []
		song_name = data['items'][i]['track']['name']
		song_album = data['items'][i]['track']['album']['name']
		for j in range(len(data['items'][i]['track']['artists'])):
			single_song_artists.append(data['items'][i]['track']['artists'][j]['name'])
		song_artist = single_song_artists
		song.append(i)
		song.append(song_album)
		song.append(song_name)
		song.append(song_album)
		songs_list.append(song)
		#song_val_dict.update()
		songs_dict.update({i+1: {'name': song_name, 'artists': song_artist, 'album': song_album}})
	#print songs_list
	#print '\n'
	#for val in songs_list:
	#	songs_dict[val[0]] = val[:]

	
	return songs_dict

def main():
	client_id = 'd56ed89f1ba04b3e89a6e3df3a99b91c'
	client_secret = 'ac839d4102a24c62b28008675161ef07'
	redirect_uri = 'http://www.google.com'

	username = raw_input("Spotify Username: ")
	#check if username valid

	auth_url = "https://accounts.spotify.com/api/token"
	auth_values = {'grant_type': 'client_credentials','scope': 'user-read-private', 'client_id': client_id, 'client_secret': client_secret}
	auth_response = http_request_response(auth_url, auth_values, 'POST')
	
	access_token = auth_response['access_token']
	
	playlists_url = "https://api.spotify.com/v1/users/" + username + "/playlists"
	playlists_values = {'Authorization': 'Bearer ' + access_token}
	playlists_response = http_request_response(playlists_url, playlists_values, 'GET')
	
	#auth_success = authenticate_user(username, password)

	playlist_names, playlist_ids, playlist_owners = get_user_playlists(playlists_response)
	display_playlists(playlist_names) #with numbers
	
	playlist_choice = int(raw_input("Which playlist would you like to download? "))
	playlist_id = playlist_ids[playlist_choice-1]
	playlist_owner = playlist_owners[playlist_choice-1]

	songs_url = "https://api.spotify.com/v1/users/" + playlist_owner + "/playlists/" + playlist_id + "/tracks"
	songs_values = {'Authorization': 'Bearer ' + access_token}
	songs_response = http_request_response(songs_url, songs_values, 'GET')
	#use exceptions?!
	
#create dict of songs
	songs_dict = get_songs_from_playlist(songs_response)
	print songs_dict #need album name, track name, and artist name


#destination = playlists[download_choice] + ".zip" #save to zip file?!
#add auth etc error checking too
#download form youtube?!

if __name__ == "__main__": main()
