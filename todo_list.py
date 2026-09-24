import json


class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)

    def remove_todo(self, todo):
        self.todos.remove(todo)

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.todos, f, ensure_ascii=False)

    def load_from_file(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            self.todos = json.load(f)


todo_list = TodoList()

while True:
    print("\nTodo List Uygulaması")
    print("1. Todo ekle")
    print("2. Todo sil")
    print("3. Todo'ları göster")
    print("4. Todo'ları kaydet")
    print("5. Todo'ları yükle")
    print("6. Çıkış")

    choice = input("Seçiminizi yapın (1-6): ")

    if choice == "1":
        todo = input("Eklemek istediğiniz todo'yu girin: ")
        todo_list.add_todo(todo)
        print(f"'{todo}' eklendi.")

    elif choice == "2":
        todo = input("Silmek istediğiniz todo'yu girin: ")

        if todo in todo_list.todos:
            todo_list.remove_todo(todo)
            print(f"'{todo}' silindi.")
        else:
            print(f"'{todo}' bulunamadı.")

    elif choice == "3":
        print("\nTodo Listesi:")

        if len(todo_list.todos) == 0:
            print("Henüz todo eklenmedi.")
        else:
            for idx, todo in enumerate(todo_list.todos, start=1):
                print(f"{idx}. {todo}")

    elif choice == "4":
        filename = input("Kaydetmek istediğiniz dosya adını girin: ")
        todo_list.save_to_file(filename)
        print(f"Todo'lar '{filename}' dosyasına kaydedildi.")

    elif choice == "5":
        filename = input("Yüklemek istediğiniz dosya adını girin: ")

        try:
            todo_list.load_from_file(filename)
            print(f"Todo'lar '{filename}' dosyasından yüklendi.")

        except FileNotFoundError:
            print(f"'{filename}' dosyası bulunamadı.")

    elif choice == "6":
        print("Uygulamadan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim! Lütfen 1-6 arasında bir sayı girin.")