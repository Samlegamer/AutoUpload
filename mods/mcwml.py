from mod import Mod, Dependencie, defaultMcwDependencies

def depByVer() -> list[Dependencie]:
    __dep = list()
    __dep.append(Dependencie("blueskies", "blue-skies", "312918", "DOSy3C4M", "optional"))
    __dep.append(Dependencie("premiumwood", "premium-wood", "353515", "sTqfznK6", "optional"))
    return __dep

class McwML(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("mcwmoddinglegacy", "696071", "xlAXLJxe", version, modLoader, dependencies=defaultMcwDependencies()+depByVer())
    
    def versionsRanges(self) -> list[str]:
        match self.getVersion():
            case "1.16.5":
                return ["1.16.5"]
            case "1.17.1":
                return ["1.17.1"]
            case "1.18.2":
                return ["1.18.2"]
            case "1.19.2":
                return ["1.19.2"]
            case "1.19.3":
                return ["1.19.3", "1.19.4"]
            case "1.20.1":
                return ["1.20.1"]
            case "1.20.4":
                return ["1.20.4"]
            case "1.21.3":
                return ["1.21.3"]
            case "1.21.4":
                return ["1.21.4"]
            case "1.21.6":
                return ["1.21.6", "1.21.7", "1.21.8", "1.21.11"]
        return ["ERROR VERSION NOT REGISTRED"]