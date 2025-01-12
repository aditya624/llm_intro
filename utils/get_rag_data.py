import os
import sys
import json
from newspaper import Article
path_this = os.path.dirname(os.path.abspath(__file__))

urls = [
        # STY
        'https://bola.kompas.com/read/2025/01/09/18300018/shin-tae-yong-cinta-sepak-bola-indonesia-akademi-terus-berjalan?source=headline',
        'https://bandung.kompas.com/read/2025/01/09/201334078/dari-shin-tae-yong-ke-kluivert-tantangan-berat-pelatih-anyar-timnas',
        'https://surabaya.kompas.com/read/2025/01/09/185211678/meski-kecewa-sty-dipecat-suporter-di-surabaya-tetap-dukung-dan-optimistis',
        'https://surabaya.kompas.com/read/2025/01/09/173007778/sty-dipecat-kantor-pssi-blitar-jadi-sasaran-pelampiasan',
        'https://regional.kompas.com/read/2025/01/09/150724878/dari-shin-tae-yong-ke-patrick-kluivert-antara-kejutan-dan-harapan',
        'https://bola.kompas.com/read/2025/01/09/14253868/shin-tae-yong-timnas-indonesia-dan-hierarki-di-budaya-korea-selatan',
        'https://bola.kompas.com/read/2025/01/09/11561798/reaksi-jurnalis-korsel-terhadap-pemberhentian-shin-tae-yong',
        'https://www.kompas.com/tren/read/2025/01/09/091500865/patrick-kluivert-ungkap-alasan-mau-latih-timnas-indonesia-apa-katanya',
        'https://bola.kompas.com/read/2025/01/09/04380038/pssi-harus-bayar-puluhan-miliar-rupiah-sebagai-kompensasi-shin-tae-yong',
        'https://bola.kompas.com/read/2025/01/08/21193368/kata-kata-pertama-patrick-kluivert-sebagai-pelatih-timnas-indonesia',
        'https://bola.kompas.com/read/2025/01/08/13560818/kim-sang-sik-sulit-berkata-kata-sebut-shin-tae-yong-senior-yang-hebat',

        # Makan Siang Gratis
        'https://money.kompas.com/read/2025/01/09/204540026/luhut-klaim-rp-9-miliar-berputar-di-tiap-desa-karena-program-makan-bergizi',
        'https://www.kompas.com/jawa-timur/read/2025/01/08/084729688/peralatan-dapur-belum-lengkap-pelaksanaan-makan-bergizi-gratis-tidak',
        'https://nasional.kompas.com/read/2025/01/07/20050071/kepala-sekolah-sds-barunawati--program-makan-bergizi-bantu-penuhi-gizi-siswa',
        'https://nasional.kompas.com/read/2025/01/07/19530001/program-makan-bergizi-resmi-beroperasi-4-sppg-di-jakarta-jangkau-12.054',
        'https://nasional.kompas.com/read/2025/01/07/19452931/program-makan-bergizi-gratis-resmi-beroperasi-sppg-palmerah-salurkan-2987',
        'https://www.kompas.com/sulawesi-selatan/read/2025/01/07/151254688/program-makan-siang-gratis-di-maros-makan-pakai-wadah-plastik',
        'https://money.kompas.com/read/2025/01/07/133443626/zulhas-ungkap-anggaran-program-makan-gratis-tembus-rp-420-triliun',
        'https://www.kompas.com/jawa-timur/read/2025/01/07/101100988/apakah-ada-susu-ikan-maupun-susu-sapi-di-menu-makan-bergizi-gratis-',
        'https://surabaya.kompas.com/read/2025/01/06/212042678/distribusi-makan-siang-gratis-di-bojonegoro-belum-menyeluruh-dapur-sppg',
        'https://www.kompas.com/tren/read/2025/01/06/150000265/media-asing-soroti-makan-bergizi-gratis-singgung-stunting-dan-skema'
    ]

data = [] 
for u in urls:
    article = Article(u)
    article.download()
    article.parse()

    data.append({
        'title': article.title,
        'content': article.text,
        'url': u
    })

with open(os.path.join(path_this, '../data/rag/data.json'), 'w') as f_:
    json.dump(data, f_, indent=2)
