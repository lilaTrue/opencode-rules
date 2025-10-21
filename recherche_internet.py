import requests
import json
import urllib.parse

def recherche_rapide(query):
    """
    Effectue une recherche rapide sur DuckDuckGo et retourne les résultats.
    """
    encoded_query = urllib.parse.quote(query)
    url = f"https://api.duckduckgo.com/?q={encoded_query}&format=json"
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}, timeout=10)
        response.raise_for_status()  # Vérifie si la requête a réussi
        data = response.json()

        results = []

        # Résumé principal si disponible
        if 'AbstractText' in data and data['AbstractText']:
            results.append({
                'title': data.get('Heading', 'Résumé'),
                'url': data.get('AbstractURL', ''),
                'snippet': data['AbstractText']
            })

        # Résultats connexes (RelatedTopics)
        if 'RelatedTopics' in data:
            for topic in data['RelatedTopics'][:10]:  # Augmente à 10 pour plus de résultats
                if 'Text' in topic and 'FirstURL' in topic:
                    results.append({
                        'title': topic.get('Text', ''),
                        'url': topic['FirstURL'],
                        'snippet': topic.get('Text', '')
                    })
                elif 'Topics' in topic:
                    # Sous-topics
                    for subtopic in topic['Topics'][:5]:
                        if 'Text' in subtopic and 'FirstURL' in subtopic:
                            results.append({
                                'title': subtopic.get('Text', ''),
                                'url': subtopic['FirstURL'],
                                'snippet': subtopic.get('Text', '')
                            })

        return results[:10]  # Limite à 10 résultats

    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la recherche : {e}")
        return []

if __name__ == "__main__":
    query = input("Entrez votre requête de recherche : ")
    results = recherche_rapide(query)

    if results:
        print(f"\nRésultats pour '{query}' :\n")
        for i, result in enumerate(results, 1):
            print(f"{i}. Titre : {result['title']}")
            print(f"   URL : {result['url']}")
            if 'snippet' in result:
                print(f"   Extrait : {result['snippet']}")
            print("---")
    else:
        print("Aucun résultat trouvé ou erreur lors de la recherche.")