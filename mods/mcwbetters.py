from mod import Mod, Dependencie, defaultMcwDependencies

def depByVer(version : str, modLoader : str) -> list[Dependencie]:
    __dep = list()
    if version == "1.16.5":
        __dep.append(Dependencie("betternether", "betternether-reforged", "526921", "null", "optional"))
        __dep.append(Dependencie("betterendforge", "betterend-re-forked", "537247", "null", "optional"))
    elif modLoader.__contains__("fabric") and (version != "1.21.11" and version != "26.2"):
        __dep.append(Dependencie("betterend", "betterend", "413596", "gc8OEnCC", "optional"))
        __dep.append(Dependencie("betternether", "betternether", "311377", "MpzVLzy5", "optional"))
    elif modLoader.__contains__("forge") and version == "1.20.1":
        __dep.append(Dependencie("betterend", "betterend-forge", "1435127", "aSIFLYIc", "optional"))
        __dep.append(Dependencie("betternether", "betternether-forge", "1436171", "3mHSCaYw", "optional"))
    else:
        __dep.append(Dependencie("betterend", "betterend-neoforge", "1422294", "IcERKldh", "optional"))
        __dep.append(Dependencie("betternether", "betternether-neoforge", "1422293", "fxX3RlL5", "optional"))
    return __dep

class McwBetters(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("mcwbetters", "620582", "YwnqoRu0", version, modLoader, dependencies=defaultMcwDependencies()+depByVer(version, modLoader))
    
    def versionsRanges(self) -> list[str]:
        match self.getVersion():
            case "1.16.5":
                return ["1.16.5"]
            case "1.18.2":
                return ["1.18.2"]
            case "1.19.2":
                return ["1.19.2"]
            case "1.20.1":
                return ["1.20.1"]
            case "1.21.1":
                return ["1.21.1"]
            case "1.21.11":
                return ["1.21.11"]
            case "26.2":
                return ["26.2"]
        return ["ERROR VERSION NOT REGISTRED"]