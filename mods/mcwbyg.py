from mod import Mod, Dependencie, defaultMcwDependencies

def depByVer(version : str, modLoader : str) -> list[Dependencie]:
    __dep = list()

    if version != "1.20.1" | "1.21.1" | "1.21.4" | "1.21.8":
        if modLoader.__contains__("fabric"):
            __dep.append(Dependencie("biomesyougo", "oh-the-biomes-youll-go-fabric", "391378", "uE1WpIAk", "required"))
        else:
            __dep.append(Dependencie("biomesyougo", "oh-the-biomes-youll-go", "247560", "uE1WpIAk", "required"))
    else:
        __dep.append(Dependencie("biomeswevegone", "oh-the-biomes-weve-gone", "1070751", "NTi7d3Xc", "required"))
    
    if version != "1.16.5":
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

class McwBYG(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("mcwbyg", "535960", "s4B19O5h", version, modLoader, dependencies=defaultMcwDependencies()+depByVer(version, modLoader))
    
    def versionsRanges(self) -> list[str]:
        isForge = False

        if self.getModLoader().__contains__("forge"):
            isForge = True

        result = self.versionRangesOlder()
        if result != "NONE":
            return result

        result = self.versionRangesSniffer(isForge=isForge)
        if result != "NONE":
            return result
        
        return ["ERROR VERSION NOT REGISTRED"]
    
    def versionRangesOlder(self) -> list[str]:
        match self.getVersion():
            case "1.16.5":
                return ["1.16.5"]
            case "1.18.2":
                return ["1.18.2"]
            case "1.19":
                return ["1.19", "1.19.2"]
            case "1.19.3":
                return ["1.19.3", "1.19.4"]
        return "NONE"
    
    def versionRangesSniffer(self, isForge : bool) -> list[str]:
        match self.getVersion():
            case "1.20.1":
                return ["1.20.1"]
            case "1.21.1":
                return ["1.21.1"]
            case "1.21.4":
                if not isForge:
                    return ["1.21.4", "1.21.8", "1.21.10", "1.21.11"]
                else:
                    return ["1.21.4"]
            case "1.21.8":
                return ["1.21.8", "1.21.10", "1.21.11"]
        return "NONE"