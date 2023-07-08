import streamlit as st

def credit_decision(yosh, jins, ish, uy, oylik_miqdori, oy, plastik_karta, p2p_xarajatlari, foiz):
    # Kerakli hisobotni yaratish va natijani qaytarish
    # Hisobotni ma'lumotlarga asosan hisoblash
    # Natijani qaytarish
    if 18 <= yosh <= 80 and jins == "Erkak" or jins == "Ayol" and ish== "Bor" and uy=="Bor" and oylik_miqdori ==1000_000  and oy==1 and     plastik_karta=="Bor" and 1000_000 <= p2p_xarajatlari <= 2000_000 and foiz==20:
        kredit_miqdori = (oylik_miqdori*oy)/(foiz/100)
        return kredit_miqdori
def main():
    # Streamlit interfeysini yaratish
    st.title("Kreditni baholash tizimi")

    # Foydalanuvchidan ma'lumotlarni kiritish
    yosh = st.slider("Yoshingiz", 18, 80)
    jins = st.radio("Jinsingiz", ["Erkak", "Ayol"])
    ish = st.radio("Ish joyingiz", ["Bor", "Yo'q"])
    uy = st.radio("Uy egasi", ["Bor", "Yo'q"])
    oylik_miqdori = st.slider("Oylik daromadingiz", 1000_000, 20_000_000, step=1000_000)
    # kredit_miqdori = st.slider("Kredit miqdori", 10_000_000, 100_000_000,  step=10_000_000)
    foiz = st.radio("Yillik foiz stavkasi", [20, 25])
    oy = st.slider("Kredit muddati (oylar)", 12, 36, step=12)
    plastik_karta = st.radio("Plastik karta mavjudligi", ["Bor", "Yo'q"])
    p2p_xarajatlari = st.slider("P2P xarajatlari", 1000_000, 5000_000, step=1000_000)

    # Kreditni baholash funktsiyasini chaqirish
    # natija = int(credit_decision(yosh, jins, ish, uy, oylik_miqdori,  oy, plastik_karta, p2p_xarajatlari, foiz))
    if st.button('Submit'):
      natija = int(credit_decision(yosh, jins, ish, uy, oylik_miqdori,  oy, plastik_karta, p2p_xarajatlari, foiz))
      st.write("Berilishi mumkin bo'lgan kredit:")
      st.success(natija)
    # Natijani ekranga chiqarish
    # st.write("Berilishi mumkin bo'lgan kredit:", natija, "so'm")



if __name__ == "__main__":
    main()
