import webbrowser


class Node:
    """Classe représentant un noeud de l'arbre de décision."""

    def __init__(self, text, update_life=0, update_inventory=None):
        """Constructeur de la classe Node."""
        self.text = text
        self.choices = {}
        self.update_life = update_life
        self.update_inventory = update_inventory or {}

    def setChoice(self, choice_number, next_node):
        """Ajoute un choix à la liste des choix possibles."""
        self.choices[
            choice_number
        ] = next_node  # On ajoute le choix à la liste des choix possibles

    def getText(self):
        """Retourne le texte du noeud."""
        return self.text  # On retourne le texte du noeud

    def getNextNode(self, choice_number):
        """Retourne le noeud suivant en fonction du choix de l'utilisateur."""
        return self.choices.get(choice_number, None)

    def apply_changes(self, life, inventory):
        """Applique les changements de vie et d'inventaire."""
        life += (
            self.update_life
        )  # On ajoute la valeur de la modification de vie à la vie actuelle
        life = min(life, 100)  # On limite la vie à 100
        # Pour chaque item dans le dictionnaire des changements d'inventaire
        for item, count in self.update_inventory.items():
            # On ajoute la quantité de l'item à l'inventaire
            inventory[item] = inventory.get(item, 0) + count
            if inventory[item] <= 0:
                # On supprime l'item de l'inventaire si la quantité est négative ou nulle
                del inventory[item]
        return life, inventory

    def is_valid_choice(self, choice_number):
        """Retourne True si le choix est valide, False sinon."""
        return (
            choice_number in self.choices
        )  # On vérifie si le choix est dans la liste des choix possibles


def get_user_choice():
    """Demande à l'utilisateur de choisir un numéro de choix et le retourne."""
    while True:
        try:
            choice = int(input("Entrez le numéro de votre choix: "))
            if choice in [1, 2]:  # Si l'utilisateur entre 1 ou 2, on retourne ce choix
                return choice
            else:
                print("Erreur : Veuillez entrer 1 ou 2.")
        except ValueError:  # Si l'utilisateur entre autre chose qu'un nombre entier
            print("Erreur : Veuillez entrer un nombre entier.")


# Final nodes
end_node = Node("Fin de l'histoire. Vous êtes mort.")
escape_node = Node(
    "Félicitations ! Vous avez réussi à quitter l'île et vous êtes sauvé. Fin de l'histoire."
)


build_raft = Node(
    "Vous avez rassemblé les matériaux nécessaires pour construire un radeau, mais il y a un problème. \n\
    L'île semble être entourée de requins. \n\
    Que faites-vous ? \n\
        [1] Vous construisez un radeau solide et tentez de naviguer en évitant les requins. \n\
        [2] Vous abandonnez l'idée du radeau et cherchez d'autres moyens de quitter l'île."
)


signal_fire = Node(
    "Vous avez réussi à allumer un feu de détresse, mais la pluie commence à tomber. \n\
    Que faites-vous ? \n\
        [1] Vous protégez le feu avec votre corps et espérez que l'avion vous voit. \n\
        [2] Vous abandonnez le feu et essayez de trouver un autre moyen de signaler votre présence."
)


climbing_mountain = Node(
    "Vous décidez de gravir la montagne pour avoir une meilleure vue de l'île et chercher un moyen de quitter l'île. \n\
    Que faites-vous ? \n\
        [1] Vous escaladez la montagne avec précaution, en utilisant tout votre équipement. \n\
        [2] Vous décidez que l'escalade est trop risquée et cherchez un autre moyen de quitter l'île."
)
rescue_plane = Node(
    "Vous apercevez un avion de secours au loin. \n\
    Que faites-vous ? \n\
        [1] Vous utilisez un miroir pour refléter la lumière du soleil et attirer l'attention de l'avion. \n\
        [2] Vous allumez un feu de détresse sur la plage pour signaler votre présence."
)

wild_animal_encounter = Node(
    "Vous êtes confronté à un animal sauvage, et votre couteau se brise pendant le combat. \n\
    Que faites-vous ? \n\
        [1] Vous utilisez vos compétences en arts martiaux pour combattre l'animal. \n\
        [2] Vous essayez de fuir et de trouver un endroit sûr pour vous cacher."
)
meet_other_survivors = Node(
    "Vous rencontrez d'autres survivants sur l'île. \n\
    Que faites-vous ? \n\
        [1] Vous décidez de travailler ensemble pour trouver un moyen de quitter l'île. \n\
        [2] Vous continuez à explorer l'île seul."
)

discover_cave = Node(
    "Vous découvrez une mystérieuse grotte qui semble mener à un réseau souterrain. \n\
    Que faites-vous ? \n\
        [1] Vous explorez prudemment le réseau souterrain, en suivant les marques laissées par d'autres explorateurs. \n\
        [2] Vous décidez que le réseau souterrain est trop dangereux et continuez à chercher un moyen de quitter l'île."
)


find_map = Node(
    "Vous trouvez une carte qui semble indiquer la présence d'un trésor caché, mais elle est partiellement détruite. \n\
    Que faites-vous ? \n\
        [1] Vous essayez de déchiffrer la carte et de suivre les indices restants. \n\
        [2] Vous ignorez la carte et continuez à chercher un moyen de quitter l'île."
)


explore_island = Node(
    "Vous décidez d'explorer l'île, mais vous découvrez que le terrain est difficile et dangereux. \n\
    Que faites-vous ? \n\
        [1] Vous partez en direction de la forêt, en affrontant les dangers qui s'y trouvent. \n\
        [2] Vous suivez la plage pour explorer les environs, en évitant les zones dangereuses."
)


build_shelter = Node(
    "Vous décidez de construire un abri pour vous protéger, mais vous vous rendez compte que les matériaux sont limités. \n\
    Que faites-vous ensuite ? \n\
        [1] Vous partez à la recherche de nourriture, en prenant des risques pour trouver des ressources. \n\
        [2] Vous explorez l'île pour en savoir plus sur votre situation, malgré les dangers potentiels."
)


root = Node(
    "\n \nVous êtes co-pilote d'avion pour une entreprise de livraison, et votre avion se crashe sur une île déserte. \n\
    Vous êtes sur la plage et devant vous se trouve les restes de l'avion et des centaines de colis tombés de la soute. \n\
    Que faites-vous ? \n\
        [1] Fouiller le corps du pilote pour récupérer des objets \n\
        [2] Fouiller les colis sur la plage pour récupérer des objets \n",
)

# Liaison des choix
root.setChoice(1, build_shelter)
root.setChoice(2, explore_island)

build_shelter.setChoice(1, meet_other_survivors)
build_shelter.setChoice(2, explore_island)

explore_island.setChoice(1, find_map)
explore_island.setChoice(2, wild_animal_encounter)

find_map.setChoice(1, discover_cave)
find_map.setChoice(2, meet_other_survivors)

discover_cave.setChoice(1, wild_animal_encounter)
discover_cave.setChoice(2, signal_fire)

wild_animal_encounter.setChoice(1, meet_other_survivors)
wild_animal_encounter.setChoice(2, rescue_plane)

meet_other_survivors.setChoice(1, build_raft)
meet_other_survivors.setChoice(2, rescue_plane)

rescue_plane.setChoice(1, escape_node)
rescue_plane.setChoice(2, end_node)

build_raft.setChoice(1, escape_node)
build_raft.setChoice(2, end_node)

signal_fire.setChoice(1, escape_node)
signal_fire.setChoice(2, end_node)

# Ajout d'objets aux noeuds
root.update_inventory = {"montre": 1, "couteau": 1}
root.update_life = -5
build_shelter.update_inventory = {"bois": 5, "corde": 2, "nourriture": 10}
build_shelter.update_life = -10
explore_island.update_inventory = {"boussole": 1}
explore_island.update_life = -5
find_map.update_inventory = {"carte_au_tresor": 1}
find_map.update_life = 10
discover_cave.update_inventory = {"torche": 1}
wild_animal_encounter.update_inventory = {"couteau": 1}
wild_animal_encounter.update_life = -35
meet_other_survivors.update_inventory = {"nourriture": -4, "chaussures": 2}
meet_other_survivors.update_life = 5
rescue_plane.update_inventory = {"miroir": 1}
rescue_plane.update_life = -5
build_raft.update_inventory = {"bois": 10, "corde": 5, "voile": 1}
build_raft.update_life = -10


def display_story(node, life, inventory):
    """Affiche l'histoire en fonction des choix de l'utilisateur"""
    while node is not None:
        print("\n" + "=" * 60)  # soulignement du titre
        print(node.getText())  # affichage du texte du noeud
        print("-" * 60)  # ligne de séparation
        print(f"Vie: {life}")
        inventory_lst = [(value, key) for key, value in inventory.items()]
        inventory_str = ""
        for i in inventory_lst:
            inventory_str += f"{i[0]} {i[1]}, "
        print(f"Inventaire: {inventory_str}")

        if life <= 0:
            print("\nVous n'avez plus de vie. Fin de l'histoire.")
            break
        if node == end_node or node == escape_node:
            break
        choice = get_user_choice()
        # vérification de la validité du choix
        while not node.is_valid_choice(choice):
            print(
                "\nErreur : choix non valide. Veuillez entrer un numéro d'option valide."
            )
            choice = get_user_choice()  # choix de l'utilisateur
        # mise à jour de la vie et de l'inventaire
        life, inventory = node.apply_changes(life, inventory)
        node = node.getNextNode(choice)  # passage au noeud suivant


def tree_size_height_arity(node):
    """Retourne la taille, la hauteur et l'arité de l'arbre"""
    if node is None:
        return 0, 0, 0

    max_height = 0  # hauteur de l'arbre = 0 (pour le noeud courant)
    total_size = 1  # taille de l'arbre = 1 (pour le noeud courant)
    # arité de l'arbre = nombre de choix possibles
    max_arity = len(node.choices)

    for _, child_node in node.choices.items():  # parcours des enfants
        child_size, child_height, child_arity = tree_size_height_arity(child_node)
        # taille de l'arbre = taille de l'arbre courant + taille des enfants
        total_size += child_size
        # hauteur de l'arbre = hauteur de l'arbre courant + hauteur des enfants
        max_height = max(max_height, child_height)
        # arité de l'arbre = arité de l'arbre courant + arité des enfants
        max_arity = max(max_arity, child_arity)

    return total_size, max_height + 1, max_arity


# Calcul et affichage de la taille, la hauteur et l'arité de l'arbre
size, height, arity = tree_size_height_arity(root)  # appel de la fonction
print(
    f"La taille de l'arbre est {size}, sa hauteur est {height} et son arité est {arity}.\n"
)


# Initialisez la vie et l'inventaire
initial_life = 50
initial_inventory = {}

# Lancement de l'histoire
if __name__ == "__main__":
    while True:
        print("\n=== MENU ===")
        print("1. Jouer")
        print("2. Règles")
        print("3. Crédits")
        print("4. Dépôt GitHub")
        print("5. Quitter")

        # Boucle principale pour gérer les choix de l'utilisateur
        choice = input("Entrez le numéro de votre choix: ")
        if choice == "1":
            display_story(
                root, initial_life, initial_inventory
            )  # affichage de l'histoire
        elif choice == "2":
            print("\n=== RÈGLES DU JEU ===")
            print(
                "Le but de jeu est de survivre sur une île déserte. Vous devez faire des choix qui vous permettront de survivre. Vous pouvez choisir entre plusieurs options. Chaque option a un impact sur votre vie et votre inventaire. Si votre vie tombe à 0, vous mourrez. Si vous trouvez un trésor, vous gagnez la partie."
            )
        elif choice == "3":
            print("\n=== CRÉDITS ===")
            print("Développé par : Nicolas Salacroup et Eric Hubert")
            print("Version : 1.0")
        elif choice == "4":
            print("\nOuverture du dépôt GitHub...")
            webbrowser.open(
                "https://github.com/justniicolas/choice_game"
            )  # ouverture du dépôt GitHub
        elif choice == "5":
            print("\nMerci d'avoir joué !")
            break
        else:
            print(
                "\nErreur : choix non valide. Veuillez entrer un numéro d'option valide."
            )
