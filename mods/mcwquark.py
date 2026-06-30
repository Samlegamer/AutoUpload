from mod import Mod, Dependencie, defaultMcwDependencies

def depByVer(version : str) -> list[Dependencie]:
    __dep = list()
    __dep.append(Dependencie("quark", "quark", "243121", "qnQsVE2z", "required"))

    if version == "1.20.1" | "1.21.1":
        __dep.append(Dependencie("zeta", "zeta", "968868", "MVARlG2f", "required"))
    else:
        __dep.append(Dependencie("autoreglib", "autoreglib", "250363", "NvZ9ZhwE", "required"))
    return __dep

class McwQuark(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("mcwquark", "1091564", "uLtxXFVm", version, modLoader, dependencies=defaultMcwDependencies()+depByVer(version))
    
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