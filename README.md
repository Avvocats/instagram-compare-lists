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

### 📊 Come richiedere i file corretti su Instagram

---

#### 🇮🇹 Procedura in Italiano (Evitando foto e video)

##### 🖥️ Da PC (Sito Web - Consigliato)
* **Accedi a Instagram** ➔ Vai su [instagram.com](https://instagram.com) ed effettua l'accesso [https://facebook.com].
* **Apri le Impostazioni** ➔ Clicca sulle tre linee in basso a sinistra e seleziona **Impostazioni**.
* **Entra nel Centro Account** ➔ Clicca sulla voce **Centro gestione account** in alto a sinistra.
* **Seleziona i tuoi dati** ➔ Vai su **Le tue informazioni e autorizzazioni** ➔ Clicca su **Scarica o trasferisci informazioni** [https://facebook.com].
* **Avvia la richiesta** ➔ Clicca su **Richiedi un download** [https://facebook.com].
* **FILTRO FONDAMENTALE** ➔ Clicca su **Alcune delle tue informazioni** (NON su "Tutte le informazioni").
* **Isola i contatti** ➔ Scorri l'elenco, cerca **Follower e persone seguite** e metti la spunta solo su questa voce. Clicca su Avanti.
* **Destinazione** ➔ Scegli **Scarica sul dispositivo**.
* **Opzioni del file** ➔ Imposta il formato su **HTML** e l'intervallo di date su **Sempre**.
* **Invia** ➔ Clicca su **Invia la richiesta**.

##### 📱 Da Smartphone (Applicazione)
* **Apri il Profilo** ➔ Apri l'app di Instagram e vai sulla pagina del tuo profilo.
* **Apri il Menu** ➔ Tocca le tre linee in alto a destra per aprire le impostazioni generali.
* **Entra nel Centro Account** ➔ Tocca la voce **Centro gestione account** in alto.
* **Seleziona i tuoi dati** ➔ Vai su **Le tue informazioni e autorizzazioni** ➔ Scegli **Scarica o trasferisci informazioni**.
* **Avvia la richiesta** ➔ Tocca **Richiedi un download** [https://facebook.com].
* **FILTRO FONDAMENTALE** ➔ Tocca la voce **Alcune delle tue informazioni**.
* **Isola i contatti** ➔ Seleziona esclusivamente la casella **Follower e persone seguite**. Tocca Avanti.
* **Opzioni del file** ➔ Scegli **Scarica sul dispositivo**, verifica che il formato sia **HTML** e l'intervallo impostato su **Sempre**.
* **Invia** ➔ Tocca **Invia la richiesta**.
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

### 📊 How to request the correct files on Instagram

---

#### 🇬🇧 English Procedure (Avoiding photos and videos)

##### 🖥️ Via PC (Web Browser - Recommended)
* **Log in to Instagram** ➔ Go to [instagram.com](https://instagram.com) and log in [https://facebook.com].
* **Open Settings** ➔ Click the three lines in the bottom left corner and select **Settings**.
* **Enter Accounts Center** ➔ Click on **Accounts Center** in the top left menu.
* **Select Your Data** ➔ Go to **Your information and permissions** ➔ Click **Download or transfer information** [https://facebook.com].
* **Start Request** ➔ Click on **Request a download** [https://facebook.com].
* **CRITICAL FILTER** ➔ Click on **Some of your information** (DO NOT click "All available information").
* **Isolate Contacts** ➔ Scroll down, find **Followers and following**, and check only this box. Click Next.
* **Destination** ➔ Choose **Download to device**.
* **File Options** ➔ Set the format to **HTML** and the date range to **All time**.
* **Submit** ➔ Click **Submit request**.

##### 📱 Via Smartphone (App)
* **Open Profile** ➔ Open the Instagram app and go to your profile page.
* **Open Menu** ➔ Tap the three lines in the top right corner to open general settings.
* **Enter Accounts Center** ➔ Tap on **Accounts Center** at the top.
* **Select Your Data** ➔ Go to **Your information and permissions** ➔ Choose **Download or transfer information**.
* **Start Request** ➔ Tap **Request a download** [https://facebook.com].
* **CRITICAL FILTER** ➔ Tap on **Some of your information**.
* **Isolate Contacts** ➔ Select exclusively the **Followers and following** checkbox. Tap Next.
* **File Options** ➔ Choose **Download to device**, verify the format is **HTML**, and the date range is set to **All time**.
* **Submit** ➔ Tap **Submit request**.
