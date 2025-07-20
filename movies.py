def add_movie():
     movie_name = input("What movie would you like to add? ")

     with open("movie.txt","w") as file:
         file.write(movie_name + "\n")
         file.close()

        print("Movie added")

def view_movie():

    with open("movie.txt","r") as file:
        for line in file:
            print(line.strip().split())
        file.close()

def menu():

 user_option = input("Which movie would you like to see? (1-watch movie,2-watch all movies,3-exit ")
    while True:
        if user_option == "1"
            print("")
        elif user_option == "2"
            print("")
        elif user_option == "Exit"
            print("Goodbye")
            break
        else:
            print("Invalid option")

menu()