
class Mod:
    __modid = ""
    __prj_id_curse = ""
    __prj_id_modrinth = ""
    __version = ""
    __modLoader = ""
    __dependencies = list()

    def __init__(self, modid : str, prj_id_curse : str, prj_id_modrinth : str, version : str, modLoader : str, dependencies : list[Dependencie]):
        self.__modid = modid
        self.__prj_id_curse = prj_id_curse
        self.__prj_id_modrinth = prj_id_modrinth
        self.__version = version
        self.__modLoader = modLoader
        self.__dependencies = dependencies

    def getModid(self) -> str:
        return self.__modid
    
    def getCurseId(self) -> str:
        return self.__prj_id_curse
    
    def getModrinthId(self) -> str:
        return self.__prj_id_modrinth
        
    def getVersion(self) -> str:
        return self.__version
    
    def getModLoader(self) -> str:
        return self.__modLoader
    
    def getDependencies(self) -> list[Dependencie]:
        return self.__dependencies
    
    def versionsRanges(self) -> list[str]:
        return []
    
class Dependencie:
    __dModid = ""
    __dSlug = ""
    __dIdCurse = ""
    __dIdModrinth = ""
    __dType = ""

    def __init__(self, dModid : str, dSlug : str, dIdCurse : str, dIdModrinth : str, dType : str):
        self.__dModid = dModid
        self.__dSlug = dSlug
        self.__dIdCurse = dIdCurse
        self.__dIdModrinth = dIdModrinth
        self.__dType = dType

    def getDModid(self) -> str:
        return self.__dModid
    def getDSlug(self) -> str:
        return self.__dSlug
    def getDIdCurse(self) -> str:
        return self.__dIdCurse
    def getDIdModrinth(self) -> str:
        return self.__dIdModrinth
    def getDType(self) -> str:
        return self.__dType
    
def defaultMcwDependencies() -> list[Dependencie]:
    return [
        Dependencie("addonslib", "addonslib", "1090999", "cl5ec0Qm", "required"),

        Dependencie("mcwroofs", "macaws-roofs", "352039", "B8jaH3P1", "optional"),
        Dependencie("mcwbridges", "macaws-bridges", "351725", "GURcjz8O", "optional"),
        Dependencie("mcwfences", "macaws-fences-and-walls", "453925", "GmwLse2I", "optional"),
        Dependencie("mcwfurnitures", "macaws-furniture", "359540", "dtWC90iB", "optional"),
        Dependencie("mcwstairs", "macaws-stairs", "1119394", "iP3wH1ha", "optional"),
        Dependencie("mcwdoors", "macaws-doors", "378646", "kNxa8z3e", "optional"),
        Dependencie("mcwtrpdoors", "macaws-trapdoors", "400933", "n2fvCDlM", "optional"),
        Dependencie("mcwwindows", "macaws-windows", "363569", "C7I0BCni", "optional"),
        Dependencie("mcwpaths", "macaws-paths-and-pavings", "629153", "VRLhWB91", "optional")
    ]