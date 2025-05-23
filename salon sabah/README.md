# Salon Sabah - Application de Gestion

Application web complète pour la gestion d'un salon de coiffure, combinant une interface utilisateur moderne avec un système de réservation.

## Technologies utilisées

- **Backend**: Django + Django REST Framework
- **Frontend**: React.js
- **Base de données**: MySQL

## Installation

### Backend (Django)

1. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Configurer la base de données dans `.env`

4. Appliquer les migrations :
```bash
python manage.py migrate
```

5. Créer un superutilisateur :
```bash
python manage.py createsuperuser
```

### Frontend (React)

1. Installer les dépendances :
```bash
cd frontend
npm install
```

2. Lancer l'application :
```bash
npm start
```

## Structure du projet

```
salon-sabah/
├── backend/              # Application Django
│   ├── api/             # API REST
│   ├── reservations/    # App de gestion des réservations
│   └── manage.py
├── frontend/            # Application React
│   ├── src/
│   └── package.json
└── requirements.txt
```

## Fonctionnalités

- 🏠 Page d'accueil avec présentation du salon
- 📸 Galerie de photos
- 💰 Liste des tarifs
- 📅 Système de réservation en ligne
- 👩‍💼 Interface d'administration pour la gestion des rendez-vous 