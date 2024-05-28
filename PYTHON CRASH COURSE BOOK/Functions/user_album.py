albums = []

def make_album(artist_name, album_title, no_of_songs = None):
    
    album = {}
    
    album[artist_name] = album_title
    
    return album


while True:
    
    artist_name = input("Enter artist name: ")
    album_title = input("Enter album title: ")
    
    another_try = input("Type quit to exit: ")
    
    if another_try == "quit":
        break
    else:
        final_album = make_album(artist_name, album_title)
        albums.append(final_album)
        
        print(albums)
    
