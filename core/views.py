from django.shortcuts import render

# Create your views here.
def main(request):
    render_template = 'main.html'
    
    complete_anime = {
        'Tsukimichi Moonlit Fantasy': {
            'thumbnail':'https://doroni.me/images/anime/60d9a6966135b.jpg.webp',
            'synopsis': 'Makoto Misumi hanyalah seorang siswa sekolah menengah biasa ketika dia, karena keadaan tertentu yang dihadapi orang tuanya, dipanggil ke dunia lain untuk menjadi "pahlawan."',
            },
        'Tsukimichi Moonlit Fantasy Season 2': {
            'thumbnail':'https://doroni.me/images/anime/659c53dd27cf2.jpg.webp',
            'synopsis': 'Setelah Misumi Makoto mengalahkan Mitsurugi dan Sofia Bulga, umat manusia diselamatkan dari pasukan iblis yang menyerang—untuk saat ini. Sang dewi menyadari kekuatan Makoto yang semakin besar, dan dia melihatnya sebagai lawan yang tidak terlalu mengganggu.',
            },
        'Mushoku Tensei: Jobless Reincarnation': {
            'thumbnail':'https://doroni.me/images/anime/5ff06afb78f37.jpg.webp',
            'synopsis': 'Tewas saat menyelamatkan orang asing dari tabrakan lalu lintas, NEET berusia 34 tahun bereinkarnasi ke dunia sihir sebagai Rudeus Greyrat, bayi yang baru lahir. Dengan pengetahuan, pengalaman, dan penyesalan dari kehidupan sebelumnya, Rudeus bersumpah untuk menjalani hidup yang memuaskan dan tidak mengulangi kesalahan masa lalunya.',
            },
        'Mushoku Tensei: Jobless Reincarnation Part 2': {
            'thumbnail':'https://doroni.me/images/anime/61515004ac471.jpg.webp',
            'synopsis': 'Bagian kedua dari Mushoku Tensei: Isekai Ittara Honki Dasu',
            },
        'Mushoku Tensei: Jobless Reincarnation Season 2': {
            'thumbnail':'https://doroni.me/images/anime/64a1ced8ab354.jpg.webp',
            'synopsis': 'Musim kedua dari Mushoku Tensei: Isekai Ittara Honki Dasu.',
            },
        'Mushoku Tensei: Jobless Reincarnation Season 2 Part 2': {
            'thumbnail':'https://doroni.me/images/anime/6613114ee357f.jpg.webp',
            'synopsis': 'Second part of Mushoku Tensei II: Isekai Ittara Honki Dasu.',
            },
    }
    
    context = {
        'complete_anime':complete_anime,
    }
    return render(request,render_template,context)