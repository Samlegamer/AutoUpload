from mod import Mod, Dependencie, defaultMcwDependencies

def depByVer(version : str, modLoader : str) -> list[Dependencie]:
    __dep = list()
    __dep.append(Dependencie("biomesoplenty", "biomes-o-plenty", "220318", "HXF82T3G", "required"))
    if version != "1.16.5" or "1.17.1":
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

    if version != "1.16.5" or "1.17.1" or "1.18.2" or "1.19" or "1.19.3":
        __dep.append(Dependencie("glitchcore", "glitchcore", "955399", "s3dmwKy5", "required"))
    return __dep

class McwBOP(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("mcwbiomesoplenty", "533382", "Tanquv9C", version, modLoader, dependencies=defaultMcwDependencies()+depByVer(version, modLoader))
    
    def versionsRanges(self) -> list[str]:
        isFabric = False
        isNeo = False

        if self.getModLoader().__contains__("fabric"):
            isFabric = True
        if self.getModLoader().__contains__("neoforge"):
            isNeo = True

        result = self.versionRangesOlder()
        if result != "NONE":
            return result

        result = self.versionRangesSniffer(isFabric=isFabric, isNeo=isNeo)
        if result != "NONE":
            return result
        
        return ["ERROR VERSION NOT REGISTRED"]
    
    def versionRangesOlder(self) -> list[str]:
        match self.getVersion():
            case "1.16.5":
                return ["1.16.5"]
            case "1.17.1":
                return ["1.17.1"]
            case "1.18.2":
                return ["1.18.2"]
            case "1.19":
                return ["1.19", "1.19.2"]
            case "1.19.3":
                return ["1.19.3", "1.19.4"]
        return "NONE"
    
    def versionRangesSniffer(self, isFabric : bool, isNeo : bool) -> list[str]:
        match self.getVersion():
            case "1.20.1":
                if isFabric:
                    return ["1.20.1", "1.20.4"]
                else:
                    return ["1.20.1"]
            case "1.20.4":
                return ["1.20.4"]
            case "1.20.6":
                return ["1.20.6"]
            case "1.21.1":
                return ["1.21.1"]
            case "1.21.3":
                return ["1.21.3"]
            case "1.21.4":
                return ["1.21.4"]
            case "1.21.5":
                if isNeo or isFabric:
                    return ["1.21.5", "1.21.6", "1.21.7", "1.21.8"]
                else:
                    return ["1.21.5"]
            case "1.21.6":
                return ["1.21.6", "1.21.7", "1.21.8"]
            case "1.21.10":
                return ["1.21.10", "1.21.11"]
            case "26.1.2":
                return ["26.1.2"]
            case "26.2":
                return ["26.2"]
        return "NONE"