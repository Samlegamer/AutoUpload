import httpx
import json
from pathlib import Path
from mod import Mod

def dependencies(mod : Mod) -> list:
    __dep = list()
    for depedencie in mod.getDependencies():
        id_modrinth = depedencie.getDIdModrinth()
        if id_modrinth != "null":
            __dep.append({
                "version_id":"null",
                "project_id":id_modrinth,
                "file_name":"null",
                "dependency_type":"optional"
            })
    return __dep

def makeAVersion(token : str, jar : Path, dir : str, changelog : str, mod : Mod, version_number : str):
    json_payload = json.dumps({
        "project_id": mod.getModrinthId(),             # ID du projet Modrinth
        "name": mod.getModid() + " " + version_number,              # Nom affiché
        "version_number": version_number,            # Version
        "changelog": changelog,
        "version_type": "release",            # release | beta | alpha
        "game_versions": mod.versionsRanges(),
        "loaders": [mod.getModLoader()],
        "featured": True,
        "dependencies": dependencies(mod),
        "file_parts": ["file"],
        "primary_file": "file"
    })

    headers = {
        "Authorization": token,
        "User-Agent": "MyProject/1.0"
    }

    with open(dir+"/"+jar.name, "rb") as f:
        files = {
            "data": (None, json_payload, "application/json"),
            "file": (jar.name, f, "application/java-archive"),
        }

        r = httpx.post(
            url="https://api.modrinth.com/v2/version",
            headers=headers,
            files=files,
        )

        print(r.status_code)
        print(r.text)
        r.raise_for_status()