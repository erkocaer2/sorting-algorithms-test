from sorting_algorithms import bubble_sort

def main():
    ornek_liste = [64, 34, 25, 12, 22, 11, 90]
    print("Sıralanmamış liste: ", ornek_liste)
    
    sirali_liste = bubble_sort(ornek_liste)
    print("Sıralanmış liste:   ", sirali_liste)

if __name__ == "__main__":
    main()