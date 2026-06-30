from mod import Mod, Dependencie, defaultMcwDependencies

def depByVer() -> list[Dependencie]:
    __dep = list()
    __dep.append(Dependencie("betterlands", "betterlands", "482870", "null", "optional"))
    __dep.append(Dependencie("shroomed", "shroomed", "493665", "null", "optional"))
    return __dep

class McwSajevius(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("mcwsajevius", "551280", "QntvByoy", version, modLoader, dependencies=defaultMcwDependencies()+depByVer())
    
    def versionsRanges(self) -> list[str]:
        match self.getVersion():
            case "1.16.5":
                return ["1.16.5"]
        return ["ERROR VERSION NOT REGISTRED"]