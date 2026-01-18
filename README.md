# Aplikacja do ankiet/głosowań online

### Technologie

- Backend: Django 
- Frontend: NextJS
- Bazy danych: MySQL

### Uruchomienie aplikacji
Aplikacja ma utworzone obrazy docker jest utworzony odpowiedni plik docker-compose.yml, który pozwala na proste uruchomienie całej aplikacji.

- Frontend będzie działał na http://localhost:3000/
- Backend będzie działał na http://localhost:8000/
- PMA będzie uruchomione na http://localhost:8080/
- Zostanie automatycznie utworzony wolumen bazy danych w ./db
- Baza danych zostanie automatycznie migrowana podczas uruchomienia aplikacji

### Aplikacja ma następujące funkcjonalności:

- Logowanie i rejestracja
  ![login screen](https://github.com/atakowiec/python-polls-app/blob/media/media/login.png?raw=true)
- Tworzenie głosowań po zalogowaniu
  ![create screen](https://github.com/atakowiec/python-polls-app/blob/media/media/create.png?raw=true)
- Lista wszystkich głosowań
  ![poll list](https://github.com/atakowiec/python-polls-app/blob/media/media/poll_list.png?raw=true)
- Lista własnych głosowań
  ![profile](https://github.com/atakowiec/python-polls-app/blob/media/media/profile.png?raw=true)
- Głosowanie z informacjami o serwerze real-time
  ![profile](https://github.com/atakowiec/python-polls-app/blob/media/media/poll.png?raw=true)