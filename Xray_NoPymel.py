import maya.cmds as cmds
cmds.setAttr("hardwareRenderingGlobals.xrayMode", 1 if cmds.getAttr("hardwareRenderingGlobals.xrayMode") == 0 else 0)
