from mod import Mod, Dependencie, defaultMcwDependencies

def depByVer() -> list[Dependencie]:
    __dep = list()
    __dep.append(Dependencie("mysticsbiomes", "mystics-biomes", "397962", "kUpOjknA", "required"))
    return __dep

class McwMysticsBiomes(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("mcwmysticbiomes", "683252", "XQ6CZtXV", version, modLoader, dependencies=defaultMcwDependencies()+depByVer())
    
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
        return ["ERROR VERSION NOT REGISTRED"]