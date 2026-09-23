from mod import Mod, Dependencie, getVersionRange

def depByVer(version : str, modLoader : str) -> list[Dependencie]:
    __dep = list()
    if modLoader.__contains__("forge"): # forge and neoforge
        __dep.append(Dependencie("curios", "curios", "309927", "vvuO3ImH", "required"))
        if not getVersionRange(version, "1.16.5", "1.18.2", "1.19"):
            __dep.append(Dependencie("sizeshiftingpotions", "size-shifting-potions", "447440", "rfj2v0X6", "optional"))
    elif modLoader.__contains__("fabric"):
        if getVersionRange(version, "26.3", "26.2", "26.1", "26.1.1", "26.1.2", "1.21.11"):
            __dep.append(Dependencie("trinkets_updated", "trinkets-updated", "1509777", "XaT8sLP6", "required"))
        __dep.append(Dependencie("fabric_api", "fabric-api", "306612", "P7dR8mSH", "required"))
        __dep.append(Dependencie("sizeshiftingpotions", "size-shifting-potions", "447440", "rfj2v0X6", "optional"))
    return __dep

def idCurseByModLoader(modLoader : str) -> str:
    if modLoader.__contains__("fabric"):
        return "583242"
    return "531848"

class PotionRing(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("potionring", idCurseByModLoader(modLoader), "VZywdkA8", version, modLoader, dependencies=depByVer(version, modLoader))
    
    def versionsRanges(self) -> list[str]:
        match self.getVersion():
            case "1.16.5":
                return ["1.16.5"]
            case "1.18.2":
                return ["1.18.2"]
            case "1.19.2":
                return ["1.19.2"]
            case "1.20.1":
                return ["1.20.1", "1.20.4"]
            case "1.20.6":
                return ["1.20.6"]
            case "1.21.1":
                return ["1.21.1"]
            case "1.21.4":
                return ["1.21.4"]
            case "1.21.5":
                return ["1.21.5"]
            case "1.21.6":
                return ["1.21.6", "1.21.7", "1.21.8"]
            case "1.21.10":
                return ["1.21.10"]
            case "1.21.11":
                return ["1.21.11"]
            case "26.1":
                return ["26.1", "26.1.1", "26.1.2"]
            case "26.2":
                return ["26.2"]
            case "26.3":
                return ["26.3"]
        return ["ERROR VERSION NOT REGISTRED"]