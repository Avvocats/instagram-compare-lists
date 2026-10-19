# Incolla la tua lista di "Following" (chi segui) in mezzo alle tre virgolette
following_grezzo = """
INCOLLA QUI LA LISTA DEI FOLLOWING SCARICATA DA INSTAGRAM
"""

# Incolla la tua lista di "Followers" (chi ti segue) in mezzo alle tre virgolette
followers_grezzo = """
INCOLLA QUI LA LISTA DEI FOLLOWERS SCARICATA DA INSTAGRAM
"""

def pulisce_e_confronta():
    # Pulisce i nomi da spazi, date e maiuscole
    following = set(line.strip().lower() for line in following_grezzo.split('\n') if line.strip())
    followers = set(line.strip().lower() for line in followers_grezzo.split('\n') if line.strip())
    
    # Trova la differenza reale
    non_ricambiano = following - followers
    
    print("--- RISULTATO CONFRONTO ---")
    print(f"Persone che segui: {len(following)}")
    print(f"Persone che ti seguono: {len(followers)}")
    print(f"Persone che TI HANNO RIMOSSO: {len(non_ricambiano)}\n")
    
    for utente in sorted(non_ricambiano):
        print(f"- {utente}")

# Questa riga ora è corretta senza doppie lettere!
pulisce_e_confronta()
