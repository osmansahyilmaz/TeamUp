# main.py
from cursor_utils import execute_query, fetch_all

# Utility function to print the contents of a table
def print_table(table_name):    query = f"SELECT * FROM {table_name} LIMIT 10"
    records = fetch_all(query)
    print(f"Latest Contents of {table_name}:")
    for record in records:
        print(record)
    print("\n")

# CRUD operations for Artists table
def create_artist(art_id, name, biography, monthly_listening):
    print_table("Artists")  # Print before operation
    query = "INSERT INTO Artists (art_id, name, biography, monthly_listening) VALUES (%s, %s, %s, %s)"
    params = (art_id, name, biography, monthly_listening)
    execute_query(query, params)
    print_table("Artists")  # Print after operation

def update_artist(art_id, new_name):
    print_table("Artists") # Print before operation
    query = "UPDATE Artists SET name = %s WHERE art_id = %s"
    params = (new_name,art_id)
    execute_query(query, params)
    print_table("Artists") # Print after operation

def delete_artist(art_id):
    print_table("Artists") # Print before operation
    query = "DELETE FROM Artists WHERE art_id = %s"
    params = (art_id,)
    execute_query(query, params)
    print_table("Artists") # Print after operation

# CRUD operations for Albums_consisted_of table
def create_album(alb_id, aname):
    print_table("Albums_consisted_of")  # Print before operation
    query = "INSERT INTO Albums_consisted_of (alb_id, aname) VALUES (%s, %s)"
    params = (alb_id, aname)
    execute_query(query, params)
    print_table("Albums_consisted_of")  # Print after operation

# CRUD operations for Genres table
def create_genre(gid, gname):
    print_table("Genres")  # Print before operation
    query = "INSERT INTO Genres (gid, gname) VALUES (%s, %s)"
    params = (gid, gname)
    execute_query(query, params)
    print_table("Genres")  # Print after operation

def read_genres():
    query = "SELECT * FROM Genres"
    return fetch_all(query)

# CRUD operations for Songs_Belong_to table

def create_song(sid, length, sname, art_id, gid, alb_id):
    print_table("Songs_Belong_to")  # Print before operation
    query = """INSERT INTO Songs_Belong_to (sid, length, sname, art_id, gid, alb_id) 
               VALUES (%s, %s, %s, %s, %s, %s)"""
    params = (sid, length, sname, art_id, gid, alb_id)
    execute_query(query, params)
    print_table("Songs_Belong_to")  # Print after operation

def read_songs():
    query = "SELECT * FROM Songs_Belong_to"
    return fetch_all(query)

def update_song(sid, new_length, new_sname, new_art_id, new_gid, new_alb_id):
    print_table("Songs_Belong_to")  # Print before operation
    query = """UPDATE Songs_Belong_to 
               SET length = %s, sname = %s, art_id = %s, gid = %s, alb_id = %s 
               WHERE sid = %s"""
    params = (new_length, new_sname, new_art_id, new_gid, new_alb_id, sid)
    execute_query(query, params)
    print_table("Songs_Belong_to")  # Print after operation

def delete_song(sid):
    print_table("Songs_Belong_to")  # Print before operation
    query = "DELETE FROM Songs_Belong_to WHERE sid = %s" 
    params = (sid,)
    execute_query(query, params)
    print_table("Songs_Belong_to")  # Print after operation

# Testing the functions
if __name__ == "__main__":

    # Create new artists
    create_artist("20000", "Motive", "motive@mob", 12321)
    create_artist("20001", "Canozan", "canozan@cnzn", 11111)
    create_artist("20002", "Teoman", "teoman@tmn", 22222)
    create_artist("20003", "Pinhani", "pinhani@pnh", 33333)
    create_artist("20004", "Melike Sahin", "melikesahin@mlkshn", 30040)
    create_artist("20005", "Sezen Aksu", "sezenaksu@sznks", 59000)
    create_artist("20006", "Can Bonomo", "canbonomo@cnbnm", 40909)
    create_artist("20007", "Ajda Pekkan", "ajdapekkan@ajdpkkn", 60000)
    create_artist("20008", "Sena Sener", "senasener@snsnr", 39000)
    create_artist("20009", "Duman", "duman@dmn", 50909)

    # Create new albums
    create_album("50000", "ROMANTIK")
    create_album("50001", "Derleme")
    create_album("50002", "Gonulcelen")
    create_album("50003", "Kedikoy")
    create_album("50004", "Pusulam Ruzgar")
    create_album("50005", "Optum")
    create_album("50006", "Kara Konular")
    create_album("50007", "Super Star, Vol.2")
    create_album("50008", "Teni Tenime")
    create_album("50009", "Darmaduman")


    # Create new genre
    create_genre("30000", "Turkish Rap")
    create_genre("30001", "Alternative")
    create_genre("30002", "Acoustic Rock")
    create_genre("30003", "Turkish Rock")
    create_genre("30004", "Blues")
    create_genre("30005", "Classical")
    create_genre("30006", "Pop")
    create_genre("30007", "Country")
    create_genre("30008", "Reggae")
    create_genre("30009", "Indie")


    # Create new song
    create_song("40000", 190, "LOADED", "20000", "30000", "50000")
    create_song("40001", 180, "Bazen", "20001", "30001", "50001")
    create_song("40002", 170, "Gonullcelen", "20002", "30002", "50002")
    create_song("40003", 160, "Nehirler Durmaz", "20003", "30003", "50003")
    create_song("40004", 240, "Pusulam Ruzgar", "20004", "30004", "50004")
    create_song("40005", 240, "Vay", "20005", "30005", "50005")
    create_song("40006", 235, "Tukeniyor Omrum", "20006", "30006", "50006")
    create_song("40007", 195, "Haykiracak Nefesim Kalmasa Bile", "20007", "30007", "50007")
    create_song("40008", 195, "Teni Tenime", "20008", "30008", "50008")
    create_song("40009", 250, "Yurek", "20009", "30009", "50009")


    # Update song
    update_song("40009", 250, "Updated Song", "20009", "30009", "50009")

    # Delete song
    delete_song("40009")

    # Update artist
    update_artist("20000", "Moti(Updated)")

    # Delete artists
    delete_artist("20000")