import json

print("=================================")
print("      iPhone Hunter PL v1.0")
print("=================================")

with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

print(f"Lokalizacja: {config['location']['city']}")
print(f"Promień: {config['location']['radius_km']} km")
print(f"Sprawdzanie co: {config['check_interval']} sekund")

print("\nMonitorowane modele:")

for model, cena in config["models"].items():
    print(f"{model} <= {cena} zł")