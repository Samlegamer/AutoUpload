from mod import Mod, Dependencie, defaultMcwDependencies

def depByVer() -> list[Dependencie]:
    __dep = list()
    __dep.append(Dependencie("regionsunexplored", "regions-unexplored", "659110", "Tkikq67H", "required"))
    return __dep

class McwRU(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("mcwregionsunexplored", "605641", "4d7eGKIA", version, modLoader, dependencies=defaultMcwDependencies()+depByVer())
    
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