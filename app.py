import streamlit as st

def credit_decision(yosh, jins, ish, uy, oylik_miqdori, oylik_xarajatlari, oy, plastik_karta, p2p_xarajatlari, foiz):
    # Yosh
    xarajat = (oylik_miqdori*oylik_xarajatlari/100)
    narx = 0
    if 18 <= yosh <= 30:
        narx += 10_000_000
    elif 30 < yosh <= 60:
        narx += 5_000_000
    elif 60 < yosh <= 80:
        narx += 10_000_000
    else:
        return "Noto'g'ri yosh kiritildi."

    # Jins
    if jins == "Erkak":
        narx += 0
    elif jins == "Ayol":
        narx += 5_000_000

    # Ish joyi
    if ish == "Bor":
        narx += 10_000_000
    elif ish == "Yo'q":
        narx += 20_000_000

    # Uy
    if uy == "Bor":
        narx += 10_000_000
    elif uy == "Yo'q":
        narx += 25_000_000

    # Plastik karta
    if plastik_karta == "Yo'q":
        narx += 5_000_000
    elif plastik_karta == "Bor":
        narx += 0

    # P2P xarajatlari
    if p2p_xarajatlari >= 200_000:
        narx += 0
    elif p2p_xarajatlari >=100_000:
        narx += 500_000


    # Kredit miqdorini hisoblash
    kredit_miqdori = ((oylik_miqdori-xarajat)* oy) / (foiz / 100) - narx
    return kredit_miqdori


    # Uyining mavjudligiga qarab kreditni baholash
    if uy == "Bor":
        narx = 10_000_000
        kredit_miqdori = ((oylik_miqdori-xarajat)* oy)/(foiz/100) + narx
    if uy == "Yo'q":
        narx = 25_000_000
        kredit_miqdori = ((oylik_miqdori-xarajat)* oy)/(foiz/100) - narx
        return kredit_miqdori
    # Plastik karta mavjudligiga qarab kreditni baholash
    if plastik_karta == "Yo'q":
        narx = 5000_000
        kredit_miqdori = ((oylik_miqdori-xarajat)* oy)/(foiz/100) - narx
    if plastik_karta == "Bor":
        narx = 5000_000
        kredit_miqdori = ((oylik_miqdori-xarajat)* oy)/(foiz/100) + narx
        return kredit_miqdori
    # P2P xarajatlari bo'yicha kreditni baholash
    if p2p_xarajatlari >= 100_000:
        narx = 1_000_000
        kredit_miqdori = ((oylik_miqdori-xarajat)* oy)/(foiz/100) + narx
    if p2p_xarajatlari >=500_000:
        narx = 5_000_000
        kredit_miqdori = ((oylik_miqdori-xarajat)* oy)/(foiz/100) + narx
        return kredit_miqdori
def main():
    # Streamlit interfeysini yaratish
    st.title("Kreditni baholash tizimi")

    # Foydalanuvchidan ma'lumotlarni kiritish
    yosh = int(st.slider("Yoshingiz", 18, 80))
    jins = st.radio("Jinsingiz", ["Erkak", "Ayol"])
    ish = st.radio("Ish joyingiz", ["Bor", "Yo'q"])
    uy = st.radio("Uyingiz", ["Bor", "Yo'q"])
    oylik_miqdori = int(st.slider("Oylik daromadingiz", 1000_000, 20_000_000, step=1000_000))
    oylik_xarajatlari = float(st.slider("Oylik xarajatlari (%)", 10, 80, step=5))
    # kredit_miqdori = st.slider("Kredit miqdori", 10_000_000, 100_000_000,  step=10_000_000)
    foiz = st.radio("Yillik foiz stavkasi", [20, 25])
    oy = st.slider("Kredit muddati (oylar)", 12, 36, step=12)
    plastik_karta = st.radio("Plastik karta mavjudligi", ["Bor", "Yo'q"])
    p2p_xarajatlari = int(st.slider("P2P xarajatlari", 100_000, 500_000, step=100_000))

    # Kreditni baholash funktsiyasini chaqirish
    # natija = int(credit_decision(yosh, jins, ish, uy, oylik_miqdori,  oy, plastik_karta, p2p_xarajatlari, foiz))
    if st.button('Submit'):
        natija = credit_decision(yosh, jins, ish, uy, oylik_miqdori,  oy, plastik_karta, oylik_xarajatlari, p2p_xarajatlari, foiz)
        st.write("Berilishi mumkin bo'lgan kredit:")
        if natija <= 0:
           st.error("Kredit berilmaydi")
        else:
          st.success(natija)

if __name__ == "__main__":
    main()
