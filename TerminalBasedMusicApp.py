import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import random
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
songs={   
    1:{"name":"Darkhaast","artist":"Arijit Singh and Sunidhi Chauhan","file":"darkhaast.mp3","duration":"7:11","mood":"Emotional"},
    2:{"name":"Tose Naina","artist":"Arijit Singh","file":"tosenaina.mp3","duration":"4:24","mood":"Sad"},
    3:{"name":"Chahun Main Ya Naa","artist":"Arijit Singh","file":"chahunmainyanaa.mp3","duration":"4:00","mood":"Romantic"},
    4:{"name":"Lae Dooba","artist":"Sunidhi Chauhan","file":"laedooba.mp3","duration":"3:55","mood":"Emotional"},
    5:{"name":"Chaandaniya","artist":"Shankar Mahadevan","file":"chaandaniya.mp3","duration":"4:08","mood":"Peaceful"},
    6:{"name":"O Rangrez","artist":"Shreya Ghoshal","file":"orangrez.mp3","duration":"6:25","mood":"Peaceful"},
    7:{"name":"Finding Her","artist":"Instrumental","file":"findingher.mp3","duration":"3:32","mood":"Peaceful"},
    8:{"name":"Roke Na Ruke Naina","artist":"Arijit Singh","file":"rokenarukenaina.mp3","duration":"4:38","mood":"Sad"},
    9:{"name":"Samjhawan","artist":"Arijit Singh","file":"samjhawan.mp3","duration":"4:25","mood":"Emotional"},
    10:{"name":"Zara Sa","artist":"KK","file":"zarasa.mp3","duration":"5:07","mood":"Romantic"}
}
my_playlists={}
queue=[]
def shuffle_songs():
    a=random.randint(1,11)
    play_song(a)
def close_app():
   clear_screen()
   print("App is closed.")
def play_song(x):
    os.startfile(songs[x]['file'])
def open_songs():
    clear_screen()
    print("---------- Song Library ----------\n")
    for i in range(1,11):
        print(f"{i}. {songs[i]['name']} - {songs[i]['artist']} ({songs[i]['duration']})")
    print("11. Menu")
    print("12. Shuffle songs")
    x=int(input("Enter a number: "))
    if x==11:
        open_menu()
    elif x==12:
        shuffle_songs()
    elif 1<=x<=10:
        play_song(x)
    else:
        print("Invalid input.")
def open_playlists():
    clear_screen()
    print("---------- Playlists ----------\n")
    print("1. Create playlist")
    print("2. My playlists")
    print("3. Menu")
    x=int(input("Enter number: "))
    if x==1:
        playlist_name=input("Enter name of the playlist you want to make: ")
        my_playlists[playlist_name]=[]
        print("Playlist created successfully.")
        open_playlists()
    elif x==2:
        clear_screen()
        if not my_playlists:
            print("No playlists created.")
            input("Press enter to return to menu...")
            open_menu()
        else:
            print("---------- My playlists ----------\n")
            for i,name in enumerate(my_playlists.keys(),start=1):
                print(f"{i}.{name}")
            input("Press enter to return to menu...")
            open_menu()
    elif x==3:
        open_menu()
    else:
        print("Invalid input.")
def open_queue():
    clear_screen()
    print("---------- Queue ----------\n")
    print("1. Add song to queue")
    print("2. Check queue")
    print("3. Menu")
    x=int(input("Enter a number: "))
    if x==3:
        open_menu()
    elif x==1:
        clear_screen()
        print("---------- Edit queue ----------\n")
        for i in range(1,11):
            print(f"{i}. {songs[i]['name']} - {songs[i]['artist']} ({songs[i]['duration']})")
        x=int(input("Enter number of the song you want to add to queue: "))
        queue.append(songs[x]['name'])
        clear_screen()
        open_queue()
    elif x==2:
        clear_screen()
        print("---------- Queue ----------\n")
        j=1
        for i in queue:
            print(f"{j}. {i}")
            j=j+1
        input("Press enter to return to menu...")
        open_menu()
    else:
        print("Invalid input.")
def mood():
    clear_screen()
    print("---------- Moods ----------\n")
    print("1. Romantic")
    print("2. Peaceful")
    print("3. Sad")
    print("4. Emotional")
    print("5. Menu")
    x=int(input("Enter a number according to your mood: "))
    if x==1:
        clear_screen()
        mood_list=[]
        print("---------- Romantic ----------\n")
        j=1
        for i in range(1,11):
            if songs[i]['mood']=='Romantic':
                mood_list.append(i)
                print(f"{j}. {songs[i]['name']}")
                j=j+1
        y=int(input("Enter the number of song you want to play: "))
        if 1<=y<=len(mood_list):
            play_song(mood_list[y-1])
        else:
            print("Invalid input.")
        input("Press enter to return to menu...")
        open_menu()
    elif x==2:
        clear_screen()
        mood_list=[]
        print("---------- Peaceful ----------\n")
        j=1
        for i in range(1,11):
            if songs[i]['mood']=='Peaceful':
                mood_list.append(i)
                print(f"{j}. {songs[i]['name']}")
                j=j+1
        y=int(input("Enter the number of song you want to play: "))
        if 1<=y<=len(mood_list):
            play_song(mood_list[y-1])
        else:
            print("Invalid input.")
        input("Press enter to return to menu...")
        open_menu()
    elif x==3:
        clear_screen()
        mood_list=[]
        print("---------- Sad ----------\n")
        j=1
        for i in range(1,11):
            if songs[i]['mood']=='Sad':
                mood_list.append(i)
                print(f"{j}. {songs[i]['name']}")
                j=j+1
        y=int(input("Enter the number of song you want to play: "))
        if 1<=y<=len(mood_list):
            play_song(mood_list[y-1])
        else:
            print("Invalid input.")
        input("Press enter to return to menu...")
        open_menu()
    elif x==4:
        clear_screen()
        mood_list=[]
        print("---------- Emotional ----------\n")
        j=1
        for i in range(1,11):
            if songs[i]['mood']=='Emotional':
                mood_list.append(i)
                print(f"{j}. {songs[i]['name']}")
                j=j+1
        y=int(input("Enter the number of song you want to play: "))
        if 1<=y<=len(mood_list):
            play_song(mood_list[y-1])
        else:
            print("Invalid input.")
        input("Press enter to return to menu...")
        open_menu()
    elif x==5:
        open_menu()
    else:
        clear_screen()
        print("Invalid input.")
        input("Press enter to return to menu...")
        open_menu()
def open_menu():
    clear_screen()
    print("---------- WELCOME TO APPLE MUSIC ----------\n")
    print("1. Songs")
    print("2. Playlists")
    print("3. Queue")
    print("4. Choose song according to mood")
    print("0. Close app\n")
    x=int(input("Enter number: "))
    if x==0:
        close_app()
    elif x==1:
        open_songs()
    elif x==2:
        open_playlists()
    elif x==3:
        open_queue()
    elif x==4:
        mood()
    else:
        print("Invalid input.")
open_menu()