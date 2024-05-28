def make_album(artist_name, album_title, no_of_songs = None):
    
    if no_of_songs == None:
        album = {"ArtistName": artist_name,
             "AlbumTitle": album_title,
             "SongsReleased": no_of_songs
             }
    else:
        album = {"ArtistName": artist_name,
             "AlbumTitle": album_title
             }
    return album

album1 = make_album = ("Nitesh", "I wont give up", "4")
print(album1)
    
album2 = make_album = ("Arjun", "CMA")
print(album2)

album3 = make_album = ("Aman", "Social Manager", 2)
print(album3)
    