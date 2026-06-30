import unittest
import scripts

class ScriptFunc(unittest.TestCase):
    def testgetModObj(self):
        self.assertEqual(scripts.getModObj("addonslib", "1.20.1", "forge").getModid(), "addonslib", "Error testgetModObj")

    def testgetModLoader(self):
        self.assertEqual(scripts.getModLoader("addonslib-fabric-1.21.1-1.11.jar"), "fabric", "Error testgetModLoader")
        self.assertEqual(scripts.getModLoader("addonslib-forge-1.21.1-1.11.jar"), "forge", "Error testgetModLoader")
        self.assertEqual(scripts.getModLoader("addonslib-neoforge-1.21.1-1.11.jar"), "neoforge", "Error testgetModLoader")
        self.assertEqual(scripts.getModLoader("addonslib-1.16.5-3.7.jar"), "forge", "Error testgetModLoader")

    def testgetVersion(self):
        self.assertEqual(scripts.getVersion("addonslib", "addonslib-fabric-1.21.1-1.11.jar"), "1.21.1-1.11", "Error testgetVersion")

    def testextractMCVersion(self):
        self.assertEqual(scripts.extractMCVersion("addonslib", "addonslib-fabric-1.21.1-1.11.jar"), "1.21.1", "Error testextractMCVersion")

    def testgetMCVersions(self):
        self.assertEqual(scripts.getMCVersions(scripts.getModObj("addonslib", "1.20.1", "forge")), ["1.20.1"], "Error testgetMCVersions")


if __name__ == "__main__":
    unittest.main()
    print("All Test Pass !")