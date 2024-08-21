from faker import Faker
import random
import datetime
import string

def generate_random_anime_by_string(jumlah_data_by_string):
    fake = Faker()
    list_by = random.sample(string.ascii_uppercase,26)
    anime_data_by_string = []
    
    for _ in range(jumlah_data_by_string):
        anime = {
            'id': str(random.randint(100, 999)),
            'list_by': random.choice(list_by),
            'title': fake.sentence(nb_words=6),
            'thumbnail': 'https://doroni.me/images/anime/633d819f00981.jpg.webp',  # Ganti dengan placeholder image
            'synopsis': fake.paragraph(nb_sentences=3),
        }
        anime_data_by_string.append(anime)
        
    return anime_data_by_string

def generate_random_anime_rilis_data(jumlah_data_anime_rilis):
    fake = Faker()
    hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    anime_data = []
    
    for _ in range(jumlah_data_anime_rilis):
        anime = {
            'id': str(random.randint(100, 999)),
            'day': random.choice(hari),
            'title': fake.sentence(nb_words=6),
            'thumbnail': 'https://doroni.me/images/anime/633d819f00981.jpg.webp',  # Ganti dengan placeholder image
            'synopsis': fake.paragraph(nb_sentences=3),
        }
        anime_data.append(anime)
        
    return anime_data


def generate_random_anime_complete_data(jumlah_data_anime_complete):
    fake = Faker()
    anime_data_complete = []
    
    for _ in range(jumlah_data_anime_complete):
        anime = {
            'id': str(random.randint(100, 999)),
            'title': fake.sentence(nb_words=10),
            'thumbnail': 'https://doroni.me/images/anime/633d819f00981.jpg.webp',  # Ganti dengan placeholder image
            'synopsis': fake.paragraph(nb_sentences=3),
        }
        anime_data_complete.append(anime)
        
    return anime_data_complete


def generate_random_anime_episode_data(jumlah_data_anime_episode):
    fake = Faker()
    anime_data_episode = []
    
    for _ in range(jumlah_data_anime_episode):
        anime = {
            'id': str(random.randint(100, 999)),
            'title': fake.sentence(nb_words=7),
            'thumbnail': 'https://doroni.me/images/anime/633d819f00981.jpg.webp',  # Ganti dengan placeholder image
            'synopsis': fake.paragraph(nb_sentences=3),
        }
        anime_data_episode.append(anime)
        
    return anime_data_episode


def generate_random_reaksi(jumlah_reaksi):
    fake = Faker()
    data_reaksi = []

    for _ in range(jumlah_reaksi):
        reaksi = {
            'id': str(random.randint(100, 999)),
            'sender': fake.name(),  # Nama pengirim yang random
            'date': fake.date_between(start_date='-1y', end_date='now').strftime('%d/%m/%Y %H:%M:%S'),
            'comment': fake.sentence(nb_words=random.randint(3, 10)),  # Kalimat dengan panjang yang bervariasi
            'like': random.randint(0, 1000),  # Jumlah like random
            'dislike': random.randint(0, 500),  # Jumlah dislike random (biasanya lebih sedikit dari like)
        }
        data_reaksi.append(reaksi)

    return data_reaksi


jumlah_reaksi = 15
jumlah_data_anime_episode = 12
jumlah_data_anime_complete = 7
jumlah_data_anime_rilis = 15
jumlah_data_anime_by_string = 50

anime_by_string = generate_random_anime_by_string(jumlah_data_anime_by_string)
reaksi = generate_random_reaksi(jumlah_reaksi)
anime_episode = generate_random_anime_episode_data(jumlah_data_anime_episode)
anime_rilis = generate_random_anime_rilis_data(jumlah_data_anime_rilis)
anime_complete = generate_random_anime_complete_data(jumlah_data_anime_complete)
