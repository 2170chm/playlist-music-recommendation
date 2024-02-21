import helpers
import collections
import random

# The recommender algorithm

# Input format: [song_name-artist_name].
input_playlist=["Life Goes On-2Pac", "Toss It Up-2Pac", "Temptations-2Pac", "Changes-2Pac", "Dear Mama-2Pac"]
NUM_TO_RECOMMEND=5
input_playlist=set(input_playlist)

# Read graph
G=helpers.read_graph()

# Compute weights between neighboring playlists and input playlist
playlist_to_weight=collections.defaultdict(int)
for input_song in input_playlist:
    for neighbor_playlist in G.neighbors(input_song):
        playlist_to_weight[neighbor_playlist]+=G.edges[input_song,neighbor_playlist]["weight"]

print(f'neighbor playlists length: {len(playlist_to_weight)}')
# TODO：edge counted twice?
# Compute weights between songs of neighboring playlists (excluding input songs) and the input playlist
song_to_weight=collections.defaultdict(int)
# # For Analysis:
# song_count=collections.defaultdict(int)
for p in playlist_to_weight.keys():
    for song in G.neighbors(p):
        if(song not in input_playlist):
            song_to_weight[song]=G.edges[p,song]["weight"]+playlist_to_weight[p]
            # # For Analysis:
            # song_count[song]+=1
# most_frequent_songs=sorted(song_count, key=song_count.get, reverse=True)[:10]
# for song in most_frequent_songs:
#     print(song, song_count[song])

# Select 10 different songs to recommend

# Choose songs to recommend based on their probabilities
songs_to_recommend = []
while len(songs_to_recommend) < NUM_TO_RECOMMEND and len(song_to_weight) > 0:
    chosen_song = random.choices(population=[song for song, _ in song_to_weight.items()], weights=[prob for _, prob in song_to_weight.items()])[0]
    if chosen_song not in songs_to_recommend:
        del song_to_weight[chosen_song]
        songs_to_recommend.append(chosen_song)

print(songs_to_recommend)

