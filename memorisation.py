#!/usr/bin/env python3

from math import log10
from random import sample
from time import sleep, time
from multiprocessing.pool import ThreadPool
import os
from typing import Iterable

NOMBRE_MOTS_A_RETENIR = 5
TEMPS_AFFICHAGE = 5
TEMPS_ECRITURE = 20
NOMBRE_DIFFERENCE_MAX = 2

MOTS = ['abandonner', 'accepter', 'accompagner', 'acheter', 'adorer', 'agir', 'aider', 'aimer', 
'ajouter', 'aller', 'amener', 'amuser', 'annoncer', 'apercevoir', 'apparaître', 'appeler', 
'apporter', 'apprendre', 'approcher', 'arranger', 'arrêter', 'arriver', 'asseoir', 'assurer', 
'attaquer', 'atteindre', 'attendre', 'avancer', 'avoir', 'baisser', 'battre', 'boire', 'bouger', 
'brûler', 'cacher', 'calmer', 'casser', 'cesser', 'changer', 'chanter', 'charger', 'chercher', 
'choisir', 'commencer', 'comprendre', 'compter', 'conduire', 'connaître', 'continuer', 'coucher', 
'couper', 'courir', 'couvrir', 'craindre', 'crier', 'croire', 'danser', 'décider', 'découvrir', 
'dégager', 'demander', 'descendre', 'désoler', 'détester', 'détruire', 'devenir', 'deviner', 
'devoir', 'dire', 'disparaître', 'donner', 'dormir', 'échapper', 'écouter', 'écrire', 'éloigner', 
'embrasser', 'emmener', 'empêcher', 'emporter', 'enlever', 'entendre', 'entrer', 'envoyer', 
'espérer', 'essayer', 'être', 'éviter', 'excuser', 'exister', 'expliquer', 'faire', 'falloir', 
'fermer', 'filer', 'finir', 'foutre', 'frapper', 'gagner', 'garder', 'glisser', 'habiter', 
'ignorer', 'imaginer', 'importer', 'inquiéter', 'installer', 'intéresser', 'inviter', 'jeter', 
'jouer', 'jurer', 'lâcher', 'laisser', 'lancer', 'lever', 'lire', 'maintenir', 'manger', 'manquer', 
'marcher', 'marier', 'mener', 'mentir', 'mettre', 'monter', 'montrer', 'mourir', 'naître', 
'obliger', 'occuper', 'offrir', 'oser', 'oublier', 'ouvrir', 'paraître', 'parler', 'partir', 
'passer', 'payer', 'penser', 'perdre', 'permettre', 'plaire', 'pleurer', 'porter', 'poser', 
'pousser', 'pouvoir', 'préférer', 'prendre', 'préparer', 'présenter', 'prévenir', 'prier', 
'promettre', 'proposer', 'protéger', 'quitter', 'raconter', 'ramener', 'rappeler', 'recevoir', 
'reconnaître', 'réfléchir', 'refuser', 'regarder', 'rejoindre', 'remarquer', 'remettre', 'remonter',
'rencontrer', 'rendre', 'rentrer', 'répéter', 'répondre', 'reposer', 'reprendre', 'ressembler', 
'rester', 'retenir', 'retirer', 'retourner', 'retrouver', 'réussir', 'réveiller', 'revenir', 
'rêver', 'revoir', 'rire', 'risquer', 'rouler', 'sauter', 'sauver', 'savoir', 'sembler', 'sentir', 
'séparer', 'serrer', 'servir', 'sortir', 'souffrir', 'sourire', 'souvenir', 'suffire', 'suivre', 
'taire', 'tendre', 'tenir', 'tenter', 'terminer', 'tirer', 'tomber', 'toucher', 'tourner', 
'traîner', 'traiter', 'travailler', 'traverser', 'tromper', 'trouver', 'tuer', 'utiliser', 
'valoir', 'vendre', 'venir', 'vivre', 'voir', 'voler', 'vouloir', 'aide', 'chef', 'enfant',
'garde', 'gauche', 'geste', 'gosse', 'livre', 'merci', 'mort', 'ombre', 'part', 'poche', 
'professeur', 'tour', 'fois', 'madame', 'paix', 'voix', 'affaire', 'année', 'arme', 'armée', 
'attention', 'balle', 'boîte', 'bouche', 'carte', 'cause', 'chambre', 'chance', 'chose', 'classe', 
'confiance', 'couleur', 'cour', 'cuisine', 'dame', 'dent', 'droite', 'école', 'église', 'envie', 
'épaule', 'époque', 'équipe', 'erreur', 'espèce', 'face', 'façon', 'faim', 'famille', 'faute', 
'femme', 'fenêtre', 'fête', 'fille', 'fleur', 'force', 'forme', 'guerre', 'gueule', 'habitude', 
'heure', 'histoire', 'idée', 'image', 'impression', 'jambe', 'joie', 'journée', 'langue', 'lettre',
'lèvre', 'ligne', 'lumière', 'main', 'maison', 'maman', 'manière', 'marche', 'merde', 'mère', 
'minute', 'musique', 'nuit', 'odeur', 'oreille', 'parole', 'partie', 'peau', 'peine', 'pensée', 
'personne', 'peur', 'photo', 'pièce', 'pierre', 'place', 'police', 'porte', 'présence', 'prison', 
'putain', 'question', 'raison', 'réponse', 'robe', 'route', 'salle', 'scène', 'seconde', 'sécurité',
'semaine', 'situation', 'soeur', 'soirée', 'sorte', 'suite', 'table', 'terre', 'tête', 'vérité', 
'ville', 'voiture', 'avis', 'bois', 'bras', 'choix', 'corps', 'cours', 'gars', 'mois', 'pays', 
'prix', 'propos', 'sens', 'temps', 'travers', 'vieux', 'accord', 'agent', 'amour', 'appel', 'arbre',
'argent', 'avenir', 'avion', 'bateau', 'bébé', 'besoin', 'bonheur', 'bonjour', 'bord', 'boulot',
'bout', 'bruit', 'bureau', 'café', 'camp', 'capitaine', 'chat', 'chemin', 'chéri', 'cheval', 
'cheveu', 'chien', 'ciel', 'client', 'cœur', 'coin', 'colonel', 'compte', 'copain', 'côté', 'coup', 
'courant', 'début', 'départ', 'dieu', 'docteur', 'doigt', 'dollar', 'doute', 'droit', 'effet', 
'endroit', 'ennemi', 'escalier', 'esprit', 'état', 'exemple', 'fait', 'film', 'flic', 
'fond', 'français', 'frère', 'front', 'garçon', 'général', 'genre', 'goût', 'gouvernement', 'grand',
'groupe', 'haut', 'homme', 'honneur', 'hôtel', 'instant', 'intérêt', 'intérieur', 'jardin', 'jour', 
'journal', 'lieu', 'long', 'maître', 'mari', 'mariage', 'matin', 'médecin', 'mètre', 'milieu', 
'million', 'moment', 'monde', 'monsieur', 'mouvement', 'moyen', 'noir', 'nouveau', 'numéro', 'oeil',
'oiseau', 'oncle', 'ordre', 'papa', 'papier', 'parent', 'passage', 'passé', 'patron', 'père', 
'petit', 'peuple', 'pied', 'plaisir', 'plan', 'point', 'pouvoir', 'premier', 'présent', 'président',
'prince', 'problème', 'quartier', 'rapport', 'regard', 'reste', 'retard', 'retour', 'rêve', 
'revoir', 'salut', 'sang', 'secret', 'seigneur', 'sentiment', 'service', 'seul', 'siècle', 'signe', 
'silence', 'soir', 'soldat', 'soleil', 'sourire', 'souvenir', 'sujet', 'téléphone', 'tout', 'train',
'travail', 'trou', 'truc', 'type', 'vent', 'ventre', 'verre', 'village', 'visage', 'voyage', 'fils',
'gens', 'bleu', 'super', 'autre', 'bizarre', 'difficile', 'drôle', 'étrange', 'facile', 'grave',
'impossible', 'jeune', 'juste', 'libre', 'malade', 'même', 'pauvre', 'possible', 'propre', 'rouge',
'sale', 'simple', 'tranquille', 'triste', 'vide', 'bonne', 'toute', 'doux', 'faux', 'français',
'gros', 'heureux', 'mauvais', 'sérieux', 'vieux', 'vrai', 'ancien', 'beau', 'blanc', 'certain',
'chaud', 'cher', 'clair', 'content', 'dernier', 'désolé', 'différent', 'droit', 'entier', 'fort',
'froid', 'gentil', 'grand', 'haut', 'humain', 'important', 'joli', 'léger', 'long', 'meilleur', 
'mort', 'noir', 'nouveau', 'pareil', 'petit', 'plein', 'premier', 'prêt', 'prochain', 'quoi',
'seul', 'tout', 'vert', 'vivant']

CHARACTERES_SPECIAUX: dict[int, str] = {219:'U', 238:'i', 207:'I', 200:'E', 212:'O', 217:'U', 
252:'u', 218:'U', 234:'e', 220:'U', 193:'A', 201:'E', 255:'y', 251:'u', 202:'E', 210:'O', 216:'O',
229:'a', 198:'AE', 231:'c', 239:'i', 214:'O', 194:'A', 242:'o', 192:'A', 243:'o', 199:'C', 196:'A',
206:'I', 203:'E', 227:'a', 245:'o', 235:'e', 249:'u', 204:'I', 253:'y', 236:'i', 197:'A', 232:'e',
244:'o', 211:'O', 233:'e', 221:'Y', 228:'a', 246:'o', 224:'a', 205:'I', 208:'D', 195:'A', 230:'ae',
226:'a', 250:'u', 209:'N', 241:'n', 223:'B', 225:'a', 213:'O', 237:'i'}


def obtenir_et_afficher_les_mots_a_retenir(nombre_de_mots: int, temps_affichage: float):
    mots_a_retenir = sample(MOTS, nombre_de_mots)
    for (i, mot) in enumerate(mots_a_retenir):
        print(f"{i+1:{1+int(log10(len(mots_a_retenir)))}} - {mot}")
    sleep(temps_affichage)
    os.system("cls" if os.name=="nt" else "clear")
    return mots_a_retenir

def obtenir_mot_avec_temps(temps: float, message_debut: str = "", message_stop: str = ""):
    thread = ThreadPool(processes=1)
    resultat_async = thread.apply_async(input, (message_debut,))
    try:
        return resultat_async.get(temps)
    except:
        thread.terminate()
        print(message_stop)

def obtenir_nombre_differences(mot1: str, mot2: str):
    matrice = [[0 for _ in range(len(mot2) + 1)] for _ in range(len(mot1) + 1)]
    for i in range(len(mot1) + 1):
        matrice[i][0] = i
    for j in range(len(mot2) + 1):
        matrice[0][j] = j
    for i in range(1, len(mot1) + 1):
        for j in range(1, len(mot2) + 1):
            if (mot1[i-1] == mot2[j-1]):
                matrice[i][j] = matrice[i-1][j-1]
            else:
                matrice[i][j] = min(matrice[i][j-1], matrice[i-1][j], matrice[i-1][j-1]) + 1
    return matrice[-1][-1]

def convertir_en_ascii_minuscule(chaine: str):
        def ascii_char(charactere: str):
            numero_ascii = ord(charactere)
            if numero_ascii < 128:
                return charactere
            try:
                return CHARACTERES_SPECIAUX[numero_ascii]
            except KeyError:
                return " "
        return " ".join("".join(ascii_char(c) for c in chaine.lower()).split())

def obtenir_a_retenir_proche(mot_ecrit: str, mots_a_retenir: Iterable[str], nombre_difference_max: int):
    mot_ecrit = convertir_en_ascii_minuscule(mot_ecrit)
    for mot_a_retenir in mots_a_retenir:
        mot_a_retenir_convertit = convertir_en_ascii_minuscule(mot_a_retenir)
        if obtenir_nombre_differences(mot_ecrit, mot_a_retenir_convertit) <= nombre_difference_max:
            return mot_a_retenir
    return None

def obtenir_les_mots_retenus(temps_ecriture: float, mots_a_retenir: list[str], 
            nombre_de_difference_max: int):
    mots_retenus: list[str] = list()
    ensemble_a_retenir = set(mots_a_retenir)
    while True:
        temps_avant_ecriture = time()
        mot = obtenir_mot_avec_temps(temps=temps_ecriture, 
                                     message_debut=f"[{round(temps_ecriture, 1)}s] >>> ", 
                                     message_stop="(stop)")
        temps_apres_ecriture = time()
        temps_ecriture -= temps_apres_ecriture - temps_avant_ecriture
        if mot is None:
            break
        mot_proche = obtenir_a_retenir_proche(mot, ensemble_a_retenir, nombre_de_difference_max)
        if mot_proche is not None:
            ensemble_a_retenir.remove(mot_proche)
            mots_retenus.append(mot_proche)
            print("ok" + (f" ({mot_proche})" if mot_proche != mot else ""))
        else:
            print("erreur")
        if len(ensemble_a_retenir) == 0:
            break
        print("")
    return mots_retenus


def afficher_mots_retenus_et_non_retenus(mots_retenus: list[str], mots_a_retenir: list[str]):
    def afficher_liste(liste: list[str], nom: str):
        print(f"\n -- {nom} ({len(liste)}) -- ")
        if len(liste) == 0:
            print("\t(aucun)")
        else:
            print("\n".join(f"\t{e}" for e in liste))
    ensemble_retenus = set(mots_retenus)
    mot_non_retenus = list(m for m in mots_a_retenir if m not in ensemble_retenus)
    print()
    afficher_liste(mots_retenus, "Mot retenus")
    afficher_liste(mot_non_retenus, "Mot non retenus")
    print()

def memorisation(nombre_de_mot: int, temps_affichage: float, temps_ecriture: float, 
            nombre_de_difference_max: int):
    mots_a_retenir = obtenir_et_afficher_les_mots_a_retenir(nombre_de_mots=nombre_de_mot,
                                                            temps_affichage=temps_affichage)
    mot_retenus = obtenir_les_mots_retenus(temps_ecriture=temps_ecriture, 
                                           mots_a_retenir=mots_a_retenir, 
                                           nombre_de_difference_max=nombre_de_difference_max)
    afficher_mots_retenus_et_non_retenus(mots_retenus=mot_retenus, mots_a_retenir=mots_a_retenir)


memorisation(nombre_de_mot=NOMBRE_MOTS_A_RETENIR, temps_affichage=TEMPS_AFFICHAGE, 
             temps_ecriture=TEMPS_ECRITURE, nombre_de_difference_max=NOMBRE_DIFFERENCE_MAX)