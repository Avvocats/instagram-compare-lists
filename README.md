# Instagram Unfollower Tracker

[IT] Questo è uno script in Python semplice, open-source e privato al 100% per scoprire chi ti ha rimosso o chi non ricambia il "segui" su Instagram. Funziona interamente offline sul tuo computer, senza inviare dati personali su Internet.

[EN] A simple, open-source, and 100% private Python script to find out who unfollowed you or doesn't follow you back on Instagram. It runs completely offline on your computer, ensuring your personal data never leaves your machine.

---

## 🇮🇹 Istruzioni in Italiano

### Come usare lo script:

1. **Scarica i dati da Instagram**:
   - Vai sul tuo profilo > Centro gestione account > Le tue informazioni e autorizzazioni > Scarica o trasferisci informazioni [https://facebook.com].
   - Seleziona solo **Follower e persone seguite**.
   - Scegli il formato **HTML** ed estrai il file ZIP sul tuo PC [https://facebook.com].

2. **Copia i contatti da LibreOffice Calc**:
   - Apri `following.html` (chi segui) nel browser, seleziona tutto (`CTRL + A`), copia e incollalo nella **Colonna A** di LibreOffice Calc usando *Incolla speciale > Testo non formattato* (selezionando solo "Tabulazione" come separatore).
   - Fai lo stesso con `followers.html` (chi ti segue) nella **Colonna B**.

3. **Fai girare il codice**:
   - Apri il file `main.py` con un editor di testo (es. Notepad++).
   - Incolla la Colonna A in mezzo alle prime tre virgolette `"""` e la Colonna B in mezzo alle seconde tre virgolette `"""`.
   - Carica il file su un compilatore online come **OnlineGDB** (puoi anche staccare il Wi-Fi dopo aver caricato la pagina per massima privacy) e clicca su **Run**.

4. **Leggi il risultato**:
   - In fondo al riquadro di output troverai la lista puntata con i nomi precisi dei profili che non ti seguono più.

---

## 🇬🇧 English Instructions

### How to use the script:

1. **Download your Instagram data**:
   - Go to your Profile > Accounts Center > Your information and permissions > Download or transfer information [https://facebook.com].
   - Select **Followers and following** only.
   - Choose the **HTML** format and extract the downloaded ZIP file on your PC [https://facebook.com].

2. **Copy contacts via LibreOffice Calc**:
   - Open `following.html` in your browser, select all (`CTRL + A`), copy, and paste it into **Column A** of LibreOffice Calc using *Paste Special > Unformatted Text* (select only "Tab" as the separator).
   - Do the exact same thing with `followers.html` into **Column B**.

3. **Run the code**:
   - Open the `main.py` file with a text editor (like Notepad++).
   - Paste Column A between the first set of triple quotes `"""` and Column B between the second set of triple quotes `"""`.
   - Upload the file to an online compiler like **OnlineGDB** (you can disconnect your Wi-Fi after loading the page for maximum privacy) and click **Run**.

4. **Check the results**:
   - At the bottom of the output window, you will see a clean, bulleted list of the exact usernames that unfollowed you or do not follow you back.
