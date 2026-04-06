import datetime

def simdiki_tarih():
    return datetime.datetime.now()

def tarih_bilesenleri():
    x = datetime.datetime.now()
    return {
        "yil": x.year,
        "ay": x.month,
        "gun": x.day,
        "saat": x.hour,
        "dakika": x.minute
    }

def tarih_olustur(yil, ay, gun, saat=0, dakika=0, saniye=0):
    return datetime.datetime(yil, ay, gun, saat, dakika, saniye)

def gun_adi():
    return datetime.datetime.now().strftime("%A")

def ay_adi():
    return datetime.datetime.now().strftime("%B")

def formatli_tarih():
    return datetime.datetime.now().strftime("%d/%m/%Y")

def formatli_saat():
    return datetime.datetime.now().strftime("%H:%M:%S")

def haftanin_gunu_index():
    return datetime.datetime.now().weekday()

def bugun_tarih():
    return datetime.date.today()

def tarih_karsilastir(t1, t2):
    return "t1 daha yeni" if t1 > t2 else "t2 daha yeni"

def gun_farki(t1, t2):
    return (t1 - t2).days

def iso_format(tarih):
    return tarih.isoformat()

def tarih_to_string():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def string_to_tarih(tarih_str):
    return datetime.datetime.strptime(tarih_str, "%Y-%m-%d")

def yas_gun(dogum_tarihi):
    return (datetime.datetime.now() - dogum_tarihi).days