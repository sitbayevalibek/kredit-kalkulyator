import streamlit as st

def credit_decision(yosh, jins, ish, uy, oylik_miqdori, oylik_xarajatlari, oy, plastik_karta, p2p_xarajatlari, foiz):
    # Yosh
    xarajat = (oylik_miqdori * oylik_xarajatlari / 100)
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
    elif p2p_xarajatlari >= 100_000:
        narx += 500_000

    # Kredit miqdorini hisoblash
    kredit_miqdori = ((oylik_miqdori - xarajat) * oy) / (foiz / 100) - narx
    return kredit_miqdori


def main():
    # Streamlit interfeysini yaratish
    st.title("Kredit Kalkuyator")
    
    # Foydalanuvchidan ma'lumotlarni kiritish
    yosh = int(st.slider("Yoshingiz", 18, 80))
    jins = st.radio("Jinsingiz", ["Erkak", "Ayol"])
    ish = st.radio("Doimiy ish joyingiz", ["Bor", "Yo'q"])
    uy = st.radio("Uyingiz", ["Bor", "Yo'q"])
    oylik_miqdori = int(st.slider("Oylik daromadingiz (UZS)", 1000000, 20000000, step=1000000))
    oylik_xarajatlari = float(st.slider("Oylik xarajatlari (%)", 10, 80, step=5))
    foiz = int(st.radio("Yillik foiz stavkasi", [20, 25]))
    oy = int(st.slider("Kredit muddati (oylar)", 12, 36, step=12))
    plastik_karta = st.radio("Plastik karta mavjudligi", ["Bor", "Yo'q"])
    p2p_xarajatlari = int(st.slider("P2P o'tkazmalari (UZS)", 100000, 500000, step=100000))

    # Kreditni baholash funktsiyasini chaqirish
    if st.button('Submit'):
        natija = credit_decision(yosh, jins, ish, uy, oylik_miqdori, oylik_xarajatlari, oy, plastik_karta, p2p_xarajatlari, foiz)
        st.write("Berilishi mumkin bo'lgan kredit miqdori (UZS):")
        if natija <= 0:
            st.error("Kredit berilmaydi")
        else:
            st.success(natija)


if __name__ == "__main__":
    main()
