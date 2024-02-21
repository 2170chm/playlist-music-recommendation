Project Setup: (Python 3.7 or above)
1. Download the dataset from https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge/dataset_files
2. Unzip the dataset and place the "spotify_million_playlist_dataset" in the root directory
3. Run generate_network.py to generate graphs. All .gml files generated are placed in graphs/. Other .gml files need to be in graphs/ as well for read_graph() to detect.
4. To analyze graphs call analyze_graph in herlpers.py.
5. Run recommender.py to recommend songs. 
