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
    
def __JavaVersion(mod : Mod) -> str:
    if mod.getVersion().__contains__("1.16.5"):
        return "Java 8"
    elif mod.getVersion().__contains__("1.17.1"):
        return "Java 16"
    elif any(v in mod.getVersion() for v in ("1.18.2", "1.19", "1.19.2", "1.19.3", "1.19.4", "1.20.1", "1.20.4")):
        return "Java 17"
    elif mod.getVersion().__contains__("26.1.2"):
        return "Java 25"
    else:
        return "Java 21"

def dependencies(mod : Mod) -> list:
    __dep = list()
    for depedencie in mod.getDependencies():
        id_curse = int(depedencie.getDIdCurse())
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
    __java = __JavaVersion(mod)

    metadata = {
        "displayName": jar.name.replace(".jar", ""),
        "changelog": changelog,
        "changelogType": "markdown",
        "releaseType": "release",
        "gameVersionNames": (
            mod.versionsRanges()
            + [maj_modLoader]
            + [__java, "Client", "Server"]
        )
    }

    deps = dependencies(mod)
    if deps:
        metadata["relations"] = {
            "projects": deps
        }

    metadata = json.dumps(metadata)

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