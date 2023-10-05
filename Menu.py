import random
import string

makanan = [
        "apel", "pisang", "ceri", "jeruk", "peach", "pir", "plum", "anggur", "semangka", "nanas", "lemon", "jeruk nipis", "kiwi", "blueberry", "raspberry", "strawberry", "blackberry", "aprikot", "mangga", "papaya", "jambu biji", "fig", "kurma", "kentang", "wortel", "selery", "brokoli", "kembang kol", "bayam", "kale", "selada", "mentimun", "zucchini", "terong", "lada", "jamur", "kacang", "kacang polong", "jagung", "roti", "keju"
    ]

minuman = [
            "kacang tanah", "kacang almond", "kacang mete", "kacang walnut", "kacang filbert", "kacang macadamia", "kenari", "pistachio", "kayu manis", "jahe", "bawang putih", "bawang bombay", "tomat", "susu", "kopi", "teh", "air", "jus", "soda", "bir", "anggur merah"
        ]

menu = makanan + minuman


def makanan_minuman_random(num_words):
    
    result = " "
    for i in range(num_words):
        word = random.choice(menu)
        result += word.capitalize()
    return result

# add an delete menu funct

def add_menu_item(menu):
    new_item = input("Masukkan makanan/minuman baru: ")
    menu.append(new_item)
    print("Menu telah diupdate!")
    return menu

def remove_menu_item(menu):
    item_to_remove = input("Masukkan makanan/minuman yang ingin dihapus: ")
    if item_to_remove in menu:
        menu.remove(item_to_remove)
        print("Menu telah diupdate!")
    else:
        print("Makanan/minuman tidak ditemukan di menu.")
    return menu


def generate_pairing(menu):
    food = random.choice(menu)
    drink = random.choice(menu)
    while food == drink:
        drink = random.choice(menu)
    return f"{food.capitalize()} dan {drink.capitalize()}"

# Masukkan input
while True:
    answer = input("Bingung Mau Makan/Minum Apa? (y/n), atau mau nambah menu apa? (add/remove) ")
    if answer.lower() == "y":
        print("Cobain Ini Deh, enak tww: " + makanan_minuman_random(1))
        print("Atau cobain kombinasi ini: " + generate_pairing(menu))
        break
    elif answer.lower() == "n":
        print("Ok, jangan bingung ya!")
        break
    elif answer.lower() == "add":
        menu = add_menu_item(menu)
    elif answer.lower() == "remove":
        menu = remove_menu_item(menu)
    else:
        print("Maaf, sulit di mengerti. semoga harimu suram. Mohon jawab dengan 'y' atau 'n', atau ketik 'add' untuk menambahkan makanan/minuman baru, atau 'remove' untuk menghapus makanan/minuman dari menu.")

