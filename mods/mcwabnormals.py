from mod import Mod, Dependencie, defaultMcwDependencies

def depByVer(version : str) -> list[Dependencie]:
    __dep = list()
    __dep.append(Dependencie("blueprint", "blueprint", "382216", "VsM5EDoI", "required"))
    __dep.append(Dependencie("atmospheric", "atmospheric", "362393", "U9sJOFmJ", "optional"))
    __dep.append(Dependencie("autumnity", "autumnity", "365045", "cRh6MJ6n", "optional"))
    __dep.append(Dependencie("buzzierbees", "buzzier-bees", "355458", "b7vOFSIp", "optional"))
    __dep.append(Dependencie("environmental", "environmental", "388992", "OqtiAZcV", "optional"))
    __dep.append(Dependencie("upgradeaquatic", "upgrade-aquatic", "326895", "gTuTFFyz", "optional"))
    __dep.append(Dependencie("endergetic", "endergetic", "291509", "cPle5Z8G", "optional"))
    if version == "1.19.2" | "1.20.1" | "1.21.1":
        __dep.append(Dependencie("cavernsandchasms", "caverns-and-chasms", "438005", "tfjmPSbI", "optional"))
    return __dep

class McwAurora(Mod):
    def __init__(self, version : str, modLoader : str):
        super().__init__("mcwabnormals", "621057", "jZrq3qzM", version, modLoader, dependencies=defaultMcwDependencies()+depByVer(version))
    
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