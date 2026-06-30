from mod import Mod, Dependencie, defaultMcwDependencies

def depByVer(modLoader : str) -> list[Dependencie]:
    __dep = list()
    if modLoader.__contains__("fabric"):
        __dep.append(Dependencie("traverse", "traverse", "308777", "kXygSBVI", "required"))
        __dep.append(Dependencie("cinderscapes", "cinderscapes", "391429", "QC4wcUXZ", "required"))
        __dep.append(Dependencie("terrestria", "terrestria", "323974", "lsUDPMOT", "required"))
    else:
        __dep.append(Dependencie("traverse", "traverse-reforged", "267769", "null", "required"))
        __dep.append(Dependencie("cinderscapes", "cinderscapes-reforged", "525270", "dRbmgGMG", "required"))
        __dep.append(Dependencie("terrestria", "terrestria-reforged", "525277", "aGMdHeMl", "required"))
    return __dep

class McwTMC(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("mcwterraformersmc", "558344", "5uSvd1Ca", version, modLoader, dependencies=defaultMcwDependencies()+depByVer(version))
    
    def versionsRanges(self) -> list[str]:
        match self.getVersion():
            case "1.18.2":
                return ["1.18.2"]
            case "1.19.2":
                return ["1.19.2"]
            case "1.19.3":
                return ["1.19.3", "1.19.4"]
            case "1.20.1":
                return ["1.20.1"]
            case "1.21.1":
                return ["1.21.1"]
        return ["ERROR VERSION NOT REGISTRED"]