#!/usr/bin/env python3

from math import log10
from random import sample
from time import sleep, time
from multiprocessing.pool import ThreadPool
import os

NOMBRE_MOTS_A_RETENIR = 30
TEMPS_AFFICHAGE = 5
TEMPS_ECRITURE = 20

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
'endroit', 'ennemi', 'escalier', 'esprit', 'état', 'être', 'exemple', 'fait', 'film', 'flic', 
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

def obtenir_les_mots_ecrits(temps_ecriture: float):
    mots_ecrits: list[str] = list()
    while True:
        temps_avant_ecriture = time()
        mot = obtenir_mot_avec_temps(temps=temps_ecriture, 
                                     message_debut=f"[{round(temps_ecriture, 1)}s] >>> ", 
                                     message_stop=" (stop)")
        temps_apres_ecriture = time()
        temps_ecriture -= temps_apres_ecriture - temps_avant_ecriture
        if mot is None:
            return mots_ecrits
        mots_ecrits.append(mot)

def memorisation(nombre_de_mot: int, temps_affichage: float, temps_ecriture: float):
    mots_a_retenir = obtenir_et_afficher_les_mots_a_retenir(nombre_de_mots=nombre_de_mot,
                                                            temps_affichage=temps_affichage)
    obtenir_les_mots_ecrits(temps_ecriture=temps_ecriture)

    print("\n\n -- Mot a retenir -- ")
    print("\n".join(mots_a_retenir))

memorisation(nombre_de_mot=NOMBRE_MOTS_A_RETENIR, temps_affichage=TEMPS_AFFICHAGE, temps_ecriture=TEMPS_ECRITURE)







