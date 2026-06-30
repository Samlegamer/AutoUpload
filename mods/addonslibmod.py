from mod import Mod

class AddonsLibMod(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("addonslib", "1090999", "cl5ec0Qm", version, modLoader, list())
    
    def versionsRanges(self) -> list[str]:
        isFabric = False

        if self.getModLoader().__contains__("fabric"):
            isFabric = True

        result = self.versionRangesOlder(isFabric)
        if result != "NONE":
            return result

        result = self.versionRangesSniffer()
        if result != "NONE":
            return result
        
        return ["ERROR VERSION NOT REGISTRED"]
    
    def versionRangesOlder(self, isFabric : bool) -> list[str]:
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
                if isFabric:
                    return ["1.19.3"]
                else:
                    return ["1.19.3", "1.19.4"]
            case "1.19.4":
                return ["1.19.4"]
        return "NONE"
    
    def versionRangesSniffer(self) -> list[str]:
        match self.getVersion():
            case "1.20.1":
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
                return ["1.21.5"]
            case "1.21.6":
                return ["1.21.6", "1.21.7", "1.21.8", "1.21.10"]
            case "1.21.11":
                return ["1.21.11"]
            case "26.1.2":
                return ["26.1.2"]
        return "NONE"