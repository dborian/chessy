***This project is licensed under the GNU GPLv3.  
Any redistribution must provide the full source code and keep this license.***

# Chessy — Prototype de jeu d’échecs RPG (Python / pygame)

## 🧩 Description

**Chessy** est un **prototype de jeu d’échecs** développé en Python avec **pygame**, pensé comme une base évolutive vers une approche **RPG / expérientielle** des échecs.

Le projet se concentre actuellement sur :
- la logique du plateau
- la sélection et le déplacement des pièces
- la visualisation des coups possibles
- une architecture claire et auditable

⚠️ **Ce projet est un prototype** :
- toutes les règles ne sont pas encore implémentées
- certaines mécaniques sont incomplètes ou expérimentales
- le code est amené à changer fortement

---

## ♟️ Principe actuel du jeu

- Le joueur déplace un curseur sur le plateau
- Une pièce est sélectionnée via le clavier
- Les cases accessibles sont affichées
- Un déplacement n’est possible que vers une case valide
- Le plateau est mis à jour dynamiquement

L’objectif actuel n’est **pas** de proposer un moteur d’échecs finalisé, mais une **base technique et logique solide**.

---

## 🧠 Vision à long terme — Échecs RPG

À terme, **Chessy** a vocation à s’éloigner des échecs strictement classiques pour explorer une approche **RPG / narrative / systémique**.

### 🔮 Règles et mécaniques prévues

- Pièces avec **caractéristiques** (portée, capacité spéciale, état)
- Évolution des pièces au fil de la partie
- Actions alternatives au simple déplacement (capacités, effets)
- Plateau pouvant évoluer dynamiquement
- États temporaires (affaiblissement, bonus, blocages)
- Variantes de règles selon le mode de jeu

### 🧙‍♂️ Approche RPG

- Les pièces ne sont plus seulement des symboles, mais des **entités**
- Chaque pièce pourra avoir un rôle ou une identité
- Certaines règles classiques pourront être détournées ou réinterprétées
- Le jeu privilégiera la **lisibilité du code et des règles**, afin que toute modification reste visible et compréhensible

---

## 🛠️ Technologies utilisées

- **Python 3**
- **pygame**
- Architecture orientée données
- Séparation logique / affichage / ressources

---

## 🚧 État du projet

- [x] Plateau 8×8
- [x] Chargement des textures
- [x] Sélection et déplacements de base
- [x] Visualisation des coups possibles
- [ ] Règles complètes des échecs
- [ ] Mécaniques RPG
- [ ] Modes de jeu alternatifs
- [ ] Interface avancée

---

## 👤 Auteur

Projet développé par **dborian**.

Toute contribution, fork ou expérimentation est bienvenue tant qu’elle respecte l’esprit du projet :  
**code visible, règles explicites, modifications transparentes**.
