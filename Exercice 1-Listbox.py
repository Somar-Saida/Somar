import tkinter as tk

def afficher_selection():
    # Obtenir les indices sélectionnés
    indices_selectionnes = listbox.curselection()
    # Obtenir les éléments 
    concepts_selectionnes = [listbox.get(i) for i in indices_selectionnes]
    print("Concepts sélectionnés :")
    for concept in concepts_selectionnes:
        print("-", concept)

# Création de la fenêtre
window = tk.Tk()
window.title("Concepts en Cybersécurité")

# Création de la Listbox avec sélection multiple
listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)
concepts = ["Phishing", "Malware", "Firewall", "Chiffrement", "VPN"]
for concept in concepts:
    listbox.insert(tk.END, concept)
listbox.pack()

# Bouton pour afficher la sélection
bouton_afficher = tk.Button(window, text="Afficher", command=afficher_selection)
bouton_afficher.pack()

# Lancement d'application
window.mainloop()