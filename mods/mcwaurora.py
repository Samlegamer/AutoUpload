from mod import Mod, Dependencie, defaultMcwDependencies

def depByVer(version : str) -> list[Dependencie]:
    __dep = list()
    __dep.append(Dependencie("blueprint", "blueprint", "382216", "VsM5EDoI", "required"))
    __dep.append(Dependencie("enhancedmushrooms", "enhanced-mushrooms", "383725", "4Zf7J76Q", "optional"))
    if version == "1.16.5":
        __dep.append(Dependencie("bayoublues", "bayou-blues", "452344", "OpVMENj4", "optional"))
        __dep.append(Dependencie("abundance", "abundance", "452345", "5an0Vkka", "optional"))
    if version == "1.21.1":
        __dep.append(Dependencie("nomansland", "no-mans-land", "538493", "kjZCvAn6", "optional"))
    return __dep

class McwAurora(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("mcwaurora", "648883", "vPHgBokb", version, modLoader, dependencies=defaultMcwDependencies()+depByVer(version))
    
    def versionsRanges(self) -> list[str]:
        match self.getVersion():
            case "1.16.5":
                return ["1.16.5"]
            case "1.18.2":
                return ["1.18.2"]
            case "1.20.1":
                return ["1.20.1"]
            case "1.21.1":
                return ["1.21.1"]
        return ["ERROR VERSION NOT REGISTRED"]