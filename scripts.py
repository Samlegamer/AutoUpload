from mod import Mod
from mods.addonslibmod import AddonsLibMod
from mods.mcwbop import McwBOP
from mods.mcwbyg import McwBYG
from mods.mcwquark import McwQuark
from mods.mcwru import McwRU
from mods.mcwtmc import McwTMC
from mods.mcwml import McwML
from mods.mcwaurora import McwAurora
from mods.mcwabnormals import McwAbnormals
from mods.mcwsajevius import McwSajevius
from pathlib import Path
import os
import curse.uploaderCurseForge
import modrinth.uploaderModrinth
from dotenv import load_dotenv

def getModObj(modid : str, version : str, modLoader : str) -> Mod:
    match modid:
        case "addonslib":
            return AddonsLibMod(version, modLoader)
        case "mcwbiomesoplenty":
            return McwBOP(version, modLoader)
        case "mcwbyg":
            return McwBYG(version, modLoader)
        case "mcwquark":
            return McwQuark(version, modLoader)
        case "mcwregionsunexplored":
            return McwRU(version, modLoader)
        case "mcwterraformersmc":
            return McwTMC(version, modLoader)
        case "mcwmoddinglegacy":
            return McwML(version, modLoader)
        case "mcwaurora":
            return McwAurora(version, modLoader)
        case "mcwabnormals":
            return McwAbnormals(version, modLoader)
        case "mcwsajevius":
            return McwSajevius(version, modLoader)
    return Mod("null", "0", "0", "none", "none")

def getModLoader(name_file : str) -> str: 
    if name_file.__contains__("fabric"):
        return "fabric"
    elif name_file.__contains__("neoforge"):
        return "neoforge"
    else:
        return "forge"
    
def getVersion(modid : str, name_file : str) -> str:
    modloader = getModLoader(name_file=name_file)
    version = name_file.replace(modid+"-", "").replace(modloader+"-", "").replace(".jar", "")
    return version

def extractMCVersion(modid : str, name_file : str) -> str:
    version_mod = getVersion(modid=modid, name_file=name_file)
    version_mc = version_mod.split("-")[0]
    return version_mc

def getMCVersions(mod : Mod) -> list[str]:
    return mod.versionsRanges()

def getFileInDir(modid : str, dir : str) -> list[Path]:
    filesToUpload = list()
    for file in Path(dir).iterdir():
        if file.is_file() and file.name.__contains__(".jar") and file.name.__contains__(modid):
            print(file.name)
            filesToUpload.append(file)
    return filesToUpload

if __name__ == "__main__":
    load_dotenv()
    modid = str(input("Enter the modid : ")) # ex: addonslib
    dir = "libs"
    filesToUpload = getFileInDir(modid, dir)
    changelog = str(input("Enter the changelog : ")) # ex: fix bug 1

    for file in filesToUpload:
        version_mc = extractMCVersion(modid=modid, name_file=file.name)
        modLoader = getModLoader(name_file=file.name)
        mod = getModObj(modid=modid, version=version_mc, modLoader=modLoader)
        versions = getMCVersions(mod=mod)
        version_number = getVersion(modid=modid, name_file=file.name)

        TOKEN_CURSEFORGE = str(os.getenv("TOKEN_CURSEFORGE", ""))
        TOKEN_MODRINTH = str(os.getenv("TOKEN_MODRINTH", ""))
        if mod.getCurseId() != 0:
            curse.uploaderCurseForge.makeAVersion(token=TOKEN_CURSEFORGE, jar=file, dir=dir, changelog=changelog, mod=mod)
        if mod.getModrinthId() != 0:
            modrinth.uploaderModrinth.makeAVersion(token=TOKEN_MODRINTH, jar=file, dir=dir, changelog=changelog, mod=mod, version_number=version_number)
    print("Finish Upload")