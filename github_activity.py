import argparse
import json
import urllib.request
import urllib.error
from datetime import datetime

# URL base del API de GitHub
BASE_URL = "https://api.github.com/users/"

def fetch_github_activity(username):
    """Obtiene la actividad reciente del usuario desde el API de GitHub."""
    url = f"{BASE_URL}{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: Usuario '{username}' no encontrado.")
        elif e.code == 403:
            print("Error: Límite de solicitudes alcanzado. Intenta de nuevo más tarde.")
        else:
            print(f"Error HTTP: {e.code}")
    except urllib.error.URLError as e:
        print(f"Error de red: {e.reason}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return None

def display_activity(events, event_type=None, limit=10):
    """Muestra la actividad reciente del usuario en un formato más descriptivo."""
    if not events:
        print("No se encontraron eventos recientes.")
        return

    print("\nActividad reciente:")
    filtered_events = [event for event in events if event_type is None or event.get("type") == event_type]

    if not filtered_events:
        print(f"No se encontraron eventos del tipo '{event_type}'. Tipos válidos incluyen: PushEvent, CreateEvent, etc.")
        return

    print(f"{'Tipo de Evento':<20} {'Repositorio':<30} {'Fecha':<20}")
    print("-" * 70)

    for event in filtered_events[:limit]:  # Limitar al número especificado
        event_type = event.get("type", "Evento desconocido")
        repo_name = event.get("repo", {}).get("name", "Repositorio desconocido")
        created_at = event.get("created_at", "Fecha desconocida")
        readable_date = (
            datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%d-%m-%Y %H:%M:%S")
            if created_at != "Fecha desconocida"
            else created_at
        )

        print(f"{event_type:<20} {repo_name:<30} {readable_date:<20}")

def save_activity_to_file(events, filename="activity_log.txt", limit=10):
    """Guarda la actividad reciente en un archivo."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"{'Tipo de Evento':<20} {'Repositorio':<30} {'Fecha':<20}\n")
            file.write("-" * 70 + "\n")

            for event in events[:limit]:
                event_type = event.get("type", "Evento desconocido")
                repo_name = event.get("repo", {}).get("name", "Repositorio desconocido")
                created_at = event.get("created_at", "Fecha desconocida")
                readable_date = (
                    datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ").strftime("%d-%m-%Y %H:%M:%S")
                    if created_at != "Fecha desconocida"
                    else created_at
                )
                file.write(f"{event_type:<20} {repo_name:<30} {readable_date:<20}\n")

        print(f"Actividad guardada en el archivo '{filename}'.")
    except Exception as e:
        print(f"Error al guardar la actividad en el archivo: {e}")

def main():
    parser = argparse.ArgumentParser(description="Obtén la actividad reciente de un usuario de GitHub.")
    parser.add_argument("username", help="Nombre de usuario de GitHub")
    parser.add_argument("--event", help="Filtra la actividad por tipo de evento (opcional)", default=None)
    parser.add_argument("--limit", help="Cantidad de eventos a mostrar (opcional, por defecto 10)", type=int, default=10)
    parser.add_argument("--save", help="Guarda la actividad en un archivo (opcional)", action="store_true")
    args = parser.parse_args()

    print(f"Obteniendo actividad reciente para el usuario: {args.username}")
    events = fetch_github_activity(args.username)

    if events:
        display_activity(events, event_type=args.event, limit=args.limit)

        if args.save:
            save_activity_to_file(events, limit=args.limit)

if __name__ == "__main__":
    main()
