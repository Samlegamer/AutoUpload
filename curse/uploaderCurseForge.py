import json
import httpx
from pathlib import Path
from mod import Mod

def __ModLoader(modLoader : str) -> str:
    if modLoader.__contains__("fabric"):
        return "Fabric"
    elif modLoader.__contains__("neoforge"):
        return "NeoForge"
    else:
        return "Forge"
    
def __Type(type : str) -> str:
    if type.__contains__("optional"):
        return "optionalDependency"
    else:
        return "requiredDependency"

def dependencies(mod : Mod) -> list:
    __dep = list()
    for depedencie in mod.getDependencies():
        id_curse = depedencie.getDIdCurse()
        if id_curse != "null":
            __dep.append({
                        "slug": depedencie.getDSlug(),
                        "projectID": id_curse,
                        "type": __Type(depedencie.getDType())
                    })
    return __dep

def makeAVersion(token : str, jar : Path, dir : str, changelog : str, mod : Mod):
    maj_modLoader = __ModLoader(mod.getModLoader())
    CURSE_ID = int(mod.getCurseId())
    print(jar.name)
    
    metadata = json.dumps({
        "displayName": jar.name.replace(".jar", ""),
        "changelog": changelog,
        "changelogType": "markdown",
        "releaseType": "release",
        "gameVersionNames": mod.versionsRanges() + [maj_modLoader],
        "relations": {
            "projects": dependencies(mod)
        }
    })

    print(metadata)

    headers = {
        "X-Api-Token": token,
        "User-Agent": "MyProject/1.0"
    }
    
    print(headers)

    print("Start loop")
    with open(dir+"/"+jar.name, "rb") as f:
        files = {
            "metadata": (None, metadata, "application/json"),
            "file": (jar.name, f, "application/java-archive")
        }

        r = httpx.post(
            url=f"https://minecraft.curseforge.com/api/projects/{CURSE_ID}/upload-file",
            headers=headers,
            files=files,
        )

    print(r.status_code)
    print(r.text)