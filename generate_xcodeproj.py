#!/usr/bin/env python3
"""Generate BetTracker.xcodeproj/project.pbxproj"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(BASE, 'BetTracker.xcodeproj', 'project.pbxproj')
os.makedirs(os.path.dirname(OUT), exist_ok=True)

# ── UUIDs ──────────────────────────────────────────────────────────────────
# File references
FR_APP      = 'AA00000000000000000000A1'
FR_BET      = 'AA00000000000000000000A2'
FR_CLAUDE   = 'AA00000000000000000000A3'
FR_ESPN     = 'AA00000000000000000000A4'
FR_CONTENT  = 'AA00000000000000000000A5'
FR_BETCARD  = 'AA00000000000000000000A6'
FR_ADDBET   = 'AA00000000000000000000A7'
FR_SETTINGS = 'AA00000000000000000000A8'
FR_ASSETS   = 'AA00000000000000000000A9'
FR_PRODUCT  = 'AA00000000000000000000B1'

# Build files
BF_APP      = 'BB00000000000000000000A1'
BF_BET      = 'BB00000000000000000000A2'
BF_CLAUDE   = 'BB00000000000000000000A3'
BF_ESPN     = 'BB00000000000000000000A4'
BF_CONTENT  = 'BB00000000000000000000A5'
BF_BETCARD  = 'BB00000000000000000000A6'
BF_ADDBET   = 'BB00000000000000000000A7'
BF_SETTINGS = 'BB00000000000000000000A8'
BF_ASSETS   = 'BB00000000000000000000A9'

# Groups
GRP_ROOT     = 'CC0000000000000000000001'
GRP_APP      = 'CC0000000000000000000002'
GRP_MODELS   = 'CC0000000000000000000003'
GRP_SERVICES = 'CC0000000000000000000004'
GRP_VIEWS    = 'CC0000000000000000000005'
GRP_PRODUCTS = 'CC0000000000000000000006'

TARGET   = 'DD0000000000000000000001'
PH_SRC   = 'EE0000000000000000000001'
PH_RES   = 'EE0000000000000000000002'
PH_FWK   = 'EE0000000000000000000003'

CFG_DBG_TGT = 'FF0000000000000000000001'
CFG_REL_TGT = 'FF0000000000000000000002'
CFG_DBG_PRJ = 'FF0000000000000000000003'
CFG_REL_PRJ = 'FF0000000000000000000004'
CL_TGT      = 'GG0000000000000000000001'
CL_PRJ      = 'GG0000000000000000000002'
PROJECT     = 'HH0000000000000000000001'

# ── project.pbxproj ────────────────────────────────────────────────────────
pbx = f'''// !$*UTF8*$!
{{
\tarchiveVersion = 1;
\tclasses = {{
\t}};
\tobjectVersion = 77;
\tobjects = {{

/* Begin PBXBuildFile section */
\t\t{BF_APP}      /* BetTrackerApp.swift in Sources */  = {{isa = PBXBuildFile; fileRef = {FR_APP};      }};
\t\t{BF_BET}      /* Bet.swift in Sources */             = {{isa = PBXBuildFile; fileRef = {FR_BET};      }};
\t\t{BF_CLAUDE}   /* ClaudeService.swift in Sources */   = {{isa = PBXBuildFile; fileRef = {FR_CLAUDE};   }};
\t\t{BF_ESPN}     /* ESPNService.swift in Sources */     = {{isa = PBXBuildFile; fileRef = {FR_ESPN};     }};
\t\t{BF_CONTENT}  /* ContentView.swift in Sources */     = {{isa = PBXBuildFile; fileRef = {FR_CONTENT};  }};
\t\t{BF_BETCARD}  /* BetCardView.swift in Sources */     = {{isa = PBXBuildFile; fileRef = {FR_BETCARD};  }};
\t\t{BF_ADDBET}   /* AddBetView.swift in Sources */      = {{isa = PBXBuildFile; fileRef = {FR_ADDBET};   }};
\t\t{BF_SETTINGS} /* SettingsView.swift in Sources */    = {{isa = PBXBuildFile; fileRef = {FR_SETTINGS}; }};
\t\t{BF_ASSETS}   /* Assets.xcassets in Resources */     = {{isa = PBXBuildFile; fileRef = {FR_ASSETS};   }};
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
\t\t{FR_APP}      = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = BetTrackerApp.swift; sourceTree = "<group>"; }};
\t\t{FR_BET}      = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = Bet.swift;           sourceTree = "<group>"; }};
\t\t{FR_CLAUDE}   = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ClaudeService.swift;  sourceTree = "<group>"; }};
\t\t{FR_ESPN}     = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ESPNService.swift;    sourceTree = "<group>"; }};
\t\t{FR_CONTENT}  = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = ContentView.swift;    sourceTree = "<group>"; }};
\t\t{FR_BETCARD}  = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = BetCardView.swift;    sourceTree = "<group>"; }};
\t\t{FR_ADDBET}   = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = AddBetView.swift;     sourceTree = "<group>"; }};
\t\t{FR_SETTINGS} = {{isa = PBXFileReference; lastKnownFileType = sourcecode.swift; path = SettingsView.swift;   sourceTree = "<group>"; }};
\t\t{FR_ASSETS}   = {{isa = PBXFileReference; lastKnownFileType = folder.assetcatalog; path = Assets.xcassets;   sourceTree = "<group>"; }};
\t\t{FR_PRODUCT}  = {{isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = BetTracker.app; sourceTree = BUILT_PRODUCTS_DIR; }};
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
\t\t{PH_FWK} = {{
\t\t\tisa = PBXFrameworksBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t}};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
\t\t{GRP_ROOT} = {{
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t{GRP_APP} /* BetTracker */,
\t\t\t\t{GRP_PRODUCTS} /* Products */,
\t\t\t);
\t\t\tsourceTree = "<group>";
\t\t}};
\t\t{GRP_APP} = {{
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t{FR_APP} /* BetTrackerApp.swift */,
\t\t\t\t{GRP_MODELS} /* Models */,
\t\t\t\t{GRP_SERVICES} /* Services */,
\t\t\t\t{GRP_VIEWS} /* Views */,
\t\t\t\t{FR_ASSETS} /* Assets.xcassets */,
\t\t\t);
\t\t\tpath = BetTracker;
\t\t\tsourceTree = "<group>";
\t\t}};
\t\t{GRP_MODELS} = {{
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t{FR_BET} /* Bet.swift */,
\t\t\t);
\t\t\tpath = Models;
\t\t\tsourceTree = "<group>";
\t\t}};
\t\t{GRP_SERVICES} = {{
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t{FR_CLAUDE} /* ClaudeService.swift */,
\t\t\t\t{FR_ESPN} /* ESPNService.swift */,
\t\t\t);
\t\t\tpath = Services;
\t\t\tsourceTree = "<group>";
\t\t}};
\t\t{GRP_VIEWS} = {{
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t{FR_CONTENT} /* ContentView.swift */,
\t\t\t\t{FR_BETCARD} /* BetCardView.swift */,
\t\t\t\t{FR_ADDBET} /* AddBetView.swift */,
\t\t\t\t{FR_SETTINGS} /* SettingsView.swift */,
\t\t\t);
\t\t\tpath = Views;
\t\t\tsourceTree = "<group>";
\t\t}};
\t\t{GRP_PRODUCTS} = {{
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t{FR_PRODUCT} /* BetTracker.app */,
\t\t\t);
\t\t\tname = Products;
\t\t\tsourceTree = "<group>";
\t\t}};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
\t\t{TARGET} /* BetTracker */ = {{
\t\t\tisa = PBXNativeTarget;
\t\t\tbuildConfigurationList = {CL_TGT} /* Build configuration list for PBXNativeTarget "BetTracker" */;
\t\t\tbuildPhases = (
\t\t\t\t{PH_SRC} /* Sources */,
\t\t\t\t{PH_FWK} /* Frameworks */,
\t\t\t\t{PH_RES} /* Resources */,
\t\t\t);
\t\t\tbuildRules = (
\t\t\t);
\t\t\tdependencies = (
\t\t\t);
\t\t\tname = BetTracker;
\t\t\tproductName = BetTracker;
\t\t\tproductReference = {FR_PRODUCT} /* BetTracker.app */;
\t\t\tproductType = "com.apple.product-type.application";
\t\t}};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
\t\t{PROJECT} /* Project object */ = {{
\t\t\tisa = PBXProject;
\t\t\tattributes = {{
\t\t\t\tBuildIndependentTargetsInParallel = 1;
\t\t\t\tLastSwiftUpdateCheck = 1530;
\t\t\t\tLastUpgradeCheck = 1530;
\t\t\t\tTargetAttributes = {{
\t\t\t\t\t{TARGET} = {{
\t\t\t\t\t\tCreatedOnToolsVersion = 15.3;
\t\t\t\t\t}};
\t\t\t\t}};
\t\t\t}};
\t\t\tbuildConfigurationList = {CL_PRJ} /* Build configuration list for PBXProject "BetTracker" */;
\t\t\tcompatibilityVersion = "Xcode 14.0";
\t\t\tdevelopmentRegion = en;
\t\t\thasScannedForEncodings = 0;
\t\t\tknownRegions = (
\t\t\t\ten,
\t\t\t\tBase,
\t\t\t);
\t\t\tmainGroup = {GRP_ROOT};
\t\t\tproductRefGroup = {GRP_PRODUCTS} /* Products */;
\t\t\tprojectDirPath = "";
\t\t\tprojectRoot = "";
\t\t\ttargets = (
\t\t\t\t{TARGET} /* BetTracker */,
\t\t\t);
\t\t}};
/* End PBXProject section */

/* Begin PBXResourcesBuildPhase section */
\t\t{PH_RES} = {{
\t\t\tisa = PBXResourcesBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t\t{BF_ASSETS} /* Assets.xcassets in Resources */,
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t}};
/* End PBXResourcesBuildPhase section */

/* Begin PBXSourcesBuildPhase section */
\t\t{PH_SRC} = {{
\t\t\tisa = PBXSourcesBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t\t{BF_APP}      /* BetTrackerApp.swift in Sources */,
\t\t\t\t{BF_BET}      /* Bet.swift in Sources */,
\t\t\t\t{BF_CLAUDE}   /* ClaudeService.swift in Sources */,
\t\t\t\t{BF_ESPN}     /* ESPNService.swift in Sources */,
\t\t\t\t{BF_CONTENT}  /* ContentView.swift in Sources */,
\t\t\t\t{BF_BETCARD}  /* BetCardView.swift in Sources */,
\t\t\t\t{BF_ADDBET}   /* AddBetView.swift in Sources */,
\t\t\t\t{BF_SETTINGS} /* SettingsView.swift in Sources */,
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t}};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
\t\t{CFG_DBG_TGT} /* Debug */ = {{
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {{
\t\t\t\tASSTCAT_COMPILER_APPICON_NAME = AppIcon;
\t\t\t\tCODE_SIGN_STYLE = Automatic;
\t\t\t\tCURRENT_PROJECT_VERSION = 1;
\t\t\t\tDEVELOPMENT_ASSET_PATHS = "";
\t\t\t\tENABLE_PREVIEWS = YES;
\t\t\t\tGENERATE_INFOPLIST_FILE = YES;
\t\t\t\tINFOPLIST_KEY_NSCameraUsageDescription = "Take a photo of your bet slip";
\t\t\t\tINFOPLIST_KEY_NSPhotoLibraryUsageDescription = "Select a photo of your bet slip";
\t\t\t\tINFOPLIST_KEY_UIApplicationSceneManifest_Generation = YES;
\t\t\t\tINFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents = YES;
\t\t\t\tINFOPLIST_KEY_UILaunchScreen_Generation = YES;
\t\t\t\tINFOPLIST_KEY_UISupportedInterfaceOrientations_iPad = "UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
\t\t\t\tINFOPLIST_KEY_UISupportedInterfaceOrientations_iPhone = "UIInterfaceOrientationPortrait UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 17.0;
\t\t\t\tLD_RUNPATH_SEARCH_PATHS = (
\t\t\t\t\t"$(inherited)",
\t\t\t\t\t"@executable_path/Frameworks",
\t\t\t\t);
\t\t\t\tMARKETING_VERSION = 1.0;
\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.bettracker.app;
\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSUPPORTS_MACCATALYST = NO;
\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;
\t\t\t\tSWIFT_VERSION = 5.0;
\t\t\t\tTARGETED_DEVICE_FAMILY = "1,2";
\t\t\t}};
\t\t\tname = Debug;
\t\t}};
\t\t{CFG_REL_TGT} /* Release */ = {{
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {{
\t\t\t\tASSTCAT_COMPILER_APPICON_NAME = AppIcon;
\t\t\t\tCODE_SIGN_STYLE = Automatic;
\t\t\t\tCURRENT_PROJECT_VERSION = 1;
\t\t\t\tDEVELOPMENT_ASSET_PATHS = "";
\t\t\t\tENABLE_PREVIEWS = YES;
\t\t\t\tGENERATE_INFOPLIST_FILE = YES;
\t\t\t\tINFOPLIST_KEY_NSCameraUsageDescription = "Take a photo of your bet slip";
\t\t\t\tINFOPLIST_KEY_NSPhotoLibraryUsageDescription = "Select a photo of your bet slip";
\t\t\t\tINFOPLIST_KEY_UIApplicationSceneManifest_Generation = YES;
\t\t\t\tINFOPLIST_KEY_UIApplicationSupportsIndirectInputEvents = YES;
\t\t\t\tINFOPLIST_KEY_UILaunchScreen_Generation = YES;
\t\t\t\tINFOPLIST_KEY_UISupportedInterfaceOrientations_iPad = "UIInterfaceOrientationPortrait UIInterfaceOrientationPortraitUpsideDown UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
\t\t\t\tINFOPLIST_KEY_UISupportedInterfaceOrientations_iPhone = "UIInterfaceOrientationPortrait UIInterfaceOrientationLandscapeLeft UIInterfaceOrientationLandscapeRight";
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 17.0;
\t\t\t\tLD_RUNPATH_SEARCH_PATHS = (
\t\t\t\t\t"$(inherited)",
\t\t\t\t\t"@executable_path/Frameworks",
\t\t\t\t);
\t\t\t\tMARKETING_VERSION = 1.0;
\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.bettracker.app;
\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSUPPORTS_MACCATALYST = NO;
\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;
\t\t\t\tSWIFT_VERSION = 5.0;
\t\t\t\tTARGETED_DEVICE_FAMILY = "1,2";
\t\t\t}};
\t\t\tname = Release;
\t\t}};
\t\t{CFG_DBG_PRJ} /* Debug */ = {{
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {{
\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;
\t\t\t\tASSET_CATALOG_COMPILER_OPTIMIZATION = space;
\t\t\t\tCLANG_ANALYZER_NONNULL = YES;
\t\t\t\tCLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
\t\t\t\tCLANG_ENABLE_MODULES = YES;
\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;
\t\t\t\tCLANG_ENABLE_OBJC_WEAK = YES;
\t\t\t\tCLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
\t\t\t\tCLANG_WARN_BOOL_CONVERSION = YES;
\t\t\t\tCLANG_WARN_COMMA = YES;
\t\t\t\tCLANG_WARN_CONSTANT_CONVERSION = YES;
\t\t\t\tCLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
\t\t\t\tCLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
\t\t\t\tCLANG_WARN_DOCUMENTATION_COMMENTS = YES;
\t\t\t\tCLANG_WARN_EMPTY_BODY = YES;
\t\t\t\tCLANG_WARN_ENUM_CONVERSION = YES;
\t\t\t\tCLANG_WARN_INFINITE_RECURSION = YES;
\t\t\t\tCLANG_WARN_INT_CONVERSION = YES;
\t\t\t\tCLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
\t\t\t\tCLANG_WARN_OBJC_IMPLICIT_RETAIN_CYCLE = YES;
\t\t\t\tCLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
\t\t\t\tCLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
\t\t\t\tCLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
\t\t\t\tCLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
\t\t\t\tCLANG_WARN_STRICT_PROTOTYPES = YES;
\t\t\t\tCLANG_WARN_SUSPICIOUS_MOVE = YES;
\t\t\t\tCLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
\t\t\t\tCLANG_WARN_UNREACHABLE_CODE = YES;
\t\t\t\tCLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
\t\t\t\tCOPY_PHASE_STRIP = NO;
\t\t\t\tDEBUG_INFORMATION_FORMAT = dwarf;
\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;
\t\t\t\tENABLE_TESTABILITY = YES;
\t\t\t\tENABLE_USER_SCRIPT_SANDBOXING = YES;
\t\t\t\tGCC_C_LANGUAGE_STANDARD = gnu17;
\t\t\t\tGCC_DYNAMIC_NO_PIC = NO;
\t\t\t\tGCC_NO_COMMON_BLOCKS = YES;
\t\t\t\tGCC_OPTIMIZATION_LEVEL = 0;
\t\t\t\tGCC_PREPROCESSOR_DEFINITIONS = (
\t\t\t\t\t"DEBUG=1",
\t\t\t\t\t"$(inherited)",
\t\t\t\t);
\t\t\t\tGCC_WARN_64_TO_32_BIT_CONVERSION = YES;
\t\t\t\tGCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
\t\t\t\tGCC_WARN_UNDECLARED_SELECTOR = YES;
\t\t\t\tGCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
\t\t\t\tGCC_WARN_UNUSED_FUNCTION = YES;
\t\t\t\tGCC_WARN_UNUSED_VARIABLE = YES;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 17.0;
\t\t\t\tMTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
\t\t\t\tMTL_FAST_MATH = YES;
\t\t\t\tONLY_ACTIVE_ARCH = YES;
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG;
\t\t\t\tSWIFT_OPTIMIZATION_LEVEL = "-Onone";
\t\t\t}};
\t\t\tname = Debug;
\t\t}};
\t\t{CFG_REL_PRJ} /* Release */ = {{
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {{
\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;
\t\t\t\tASSET_CATALOG_COMPILER_OPTIMIZATION = space;
\t\t\t\tCLANG_ANALYZER_NONNULL = YES;
\t\t\t\tCLANG_ANALYZER_NUMBER_OBJECT_CONVERSION = YES_AGGRESSIVE;
\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
\t\t\t\tCLANG_ENABLE_MODULES = YES;
\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;
\t\t\t\tCLANG_ENABLE_OBJC_WEAK = YES;
\t\t\t\tCLANG_WARN_BLOCK_CAPTURE_AUTORELEASING = YES;
\t\t\t\tCLANG_WARN_BOOL_CONVERSION = YES;
\t\t\t\tCLANG_WARN_COMMA = YES;
\t\t\t\tCLANG_WARN_CONSTANT_CONVERSION = YES;
\t\t\t\tCLANG_WARN_DEPRECATED_OBJC_IMPLEMENTATIONS = YES;
\t\t\t\tCLANG_WARN_DIRECT_OBJC_ISA_USAGE = YES_ERROR;
\t\t\t\tCLANG_WARN_DOCUMENTATION_COMMENTS = YES;
\t\t\t\tCLANG_WARN_EMPTY_BODY = YES;
\t\t\t\tCLANG_WARN_ENUM_CONVERSION = YES;
\t\t\t\tCLANG_WARN_INFINITE_RECURSION = YES;
\t\t\t\tCLANG_WARN_INT_CONVERSION = YES;
\t\t\t\tCLANG_WARN_NON_LITERAL_NULL_CONVERSION = YES;
\t\t\t\tCLANG_WARN_OBJC_IMPLICIT_RETAIN_CYCLE = YES;
\t\t\t\tCLANG_WARN_OBJC_LITERAL_CONVERSION = YES;
\t\t\t\tCLANG_WARN_OBJC_ROOT_CLASS = YES_ERROR;
\t\t\t\tCLANG_WARN_QUOTED_INCLUDE_IN_FRAMEWORK_HEADER = YES;
\t\t\t\tCLANG_WARN_RANGE_LOOP_ANALYSIS = YES;
\t\t\t\tCLANG_WARN_STRICT_PROTOTYPES = YES;
\t\t\t\tCLANG_WARN_SUSPICIOUS_MOVE = YES;
\t\t\t\tCLANG_WARN_UNGUARDED_AVAILABILITY = YES_AGGRESSIVE;
\t\t\t\tCLANG_WARN_UNREACHABLE_CODE = YES;
\t\t\t\tCLANG_WARN__DUPLICATE_METHOD_MATCH = YES;
\t\t\t\tCOPY_PHASE_STRIP = NO;
\t\t\t\tDEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
\t\t\t\tENABLE_NS_ASSERTIONS = NO;
\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;
\t\t\t\tENABLE_USER_SCRIPT_SANDBOXING = YES;
\t\t\t\tGCC_C_LANGUAGE_STANDARD = gnu17;
\t\t\t\tGCC_NO_COMMON_BLOCKS = YES;
\t\t\t\tGCC_WARN_64_TO_32_BIT_CONVERSION = YES;
\t\t\t\tGCC_WARN_ABOUT_RETURN_TYPE = YES_ERROR;
\t\t\t\tGCC_WARN_UNDECLARED_SELECTOR = YES;
\t\t\t\tGCC_WARN_UNINITIALIZED_AUTOS = YES_AGGRESSIVE;
\t\t\t\tGCC_WARN_UNUSED_FUNCTION = YES;
\t\t\t\tGCC_WARN_UNUSED_VARIABLE = YES;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 17.0;
\t\t\t\tMTL_FAST_MATH = YES;
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSWIFT_COMPILATION_MODE = wholemodule;
\t\t\t\tVALIDATE_PRODUCT = YES;
\t\t\t}};
\t\t\tname = Release;
\t\t}};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
\t\t{CL_PRJ} /* Build configuration list for PBXProject "BetTracker" */ = {{
\t\t\tisa = XCConfigurationList;
\t\t\tbuildConfigurations = (
\t\t\t\t{CFG_DBG_PRJ} /* Debug */,
\t\t\t\t{CFG_REL_PRJ} /* Release */,
\t\t\t);
\t\t\tdefaultConfigurationIsVisible = 0;
\t\t\tdefaultConfigurationName = Release;
\t\t}};
\t\t{CL_TGT} /* Build configuration list for PBXNativeTarget "BetTracker" */ = {{
\t\t\tisa = XCConfigurationList;
\t\t\tbuildConfigurations = (
\t\t\t\t{CFG_DBG_TGT} /* Debug */,
\t\t\t\t{CFG_REL_TGT} /* Release */,
\t\t\t);
\t\t\tdefaultConfigurationIsVisible = 0;
\t\t\tdefaultConfigurationName = Release;
\t\t}};
/* End XCConfigurationList section */

\t}};
\trootObject = {PROJECT} /* Project object */;
}}
'''

with open(OUT, 'w') as f:
    f.write(pbx)

print(f"Generated: {OUT}")
