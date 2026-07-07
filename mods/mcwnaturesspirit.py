from mod import Mod, Dependencie, defaultMcwDependencies

def depByVer(modLoader : str) -> list[Dependencie]:
    __dep = list()
    __dep.append(Dependencie("natures_spirit", "natures-spirit", "1044992", "WBvnqHfV", "required"))
    __dSlug = ""
    __dIdCurse = ""
    __dIdModrinth = "kkmrDlKT"

    if modLoader.__contains__("fabric"):
        __dSlug = "terrablender-fabric"
        __dIdCurse = "565956"
    elif modLoader.__contains__("neoforge"):
        __dSlug = "terrablender-neoforge"
        __dIdCurse = "940057"
    else:
        __dSlug = "terrablender"
        __dIdCurse = "563928"
    __dep.append(Dependencie("terrablender", __dSlug, __dIdCurse, __dIdModrinth, "required"))

    return __dep

class McwNaturesSpirit(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("mcwnaturesspirit", "714367", "z9puNODX", version, modLoader, dependencies=defaultMcwDependencies()+depByVer(modLoader))
    
    def versionsRanges(self) -> list[str]:
        match self.getVersion():
            case "1.20.1":
                return ["1.20.1"]
            case "1.21.1":
                return ["1.21.1"]
        return ["ERROR VERSION NOT REGISTRED"]