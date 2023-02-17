from rest_framework import viewsets,permissions,generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
import time
import requests
import urllib
import urllib.parse
from bs4 import BeautifulSoup as bs
from .models import user,match,static
from .serializers import userSerializer,matchSerializer,statSerializer
from django.db.models import Q



class UserAPI(APIView):
    def get(self,request,sname):
        s_name=''
        for i in sname:
            if i!=' ':
                s_name+=i
        users=user.objects.filter(Q(name__iexact=s_name))
        serializer=userSerializer(users,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

def getAPIkey():
    f=open("C:/devrent/back2/user/riot_api.txt","r")
    return f.read()

def aug_img(name):
    aug={'TFT6_Augment_ForceOfNature': 'NewRecruit3.png', 'TFT6_Augment_FirstAidKit': 'FirstAidKit1.png', 'TFT6_Augment_MaxLevel10': 'LevelUp3.png', 'TFT6_Augment_ItemGrabBag1': 'ItemGrabBag1.png', 'TFT6_Augment_ItemGrabBag2': 'ItemGrabBag3.png', 'TFT6_Augment_Windfall': 'Windfall3.png', 'TFT6_Augment_GrandGambler': 'GrandGambler3.png', 'TFT6_Augment_CalculatedLoss': 'CalculatedLoss2.png', 'TFT6_Augment_SalvageBin': 'Salvage2.png', 'TFT6_Augment_SlowAndSteady': 'SlowAndSteady3.png', 'TFT6_Augment_PortableForge': 'PortableForge2.png', 'TFT6_Augment_HighEndShopping': 'HighEnd3.png', 'TFT6_Augment_Diversify1': 'StandUnited1.png', 'TFT6_Augment_Diversify2': 'StandUnited2.png', 'TFT6_Augment_Diversify3': 'StandUnited3.png', 'TFT6_Augment_BandOfThieves2': 'BandThieves3.png', 'TFT6_Augment_Featherweights1': 'Featherweights1.png', 'TFT6_Augment_Featherweights2': 'Featherweights2.png', 'TFT6_Augment_Featherweights3': 'Featherweights3.png', 'TFT6_Augment_HyperRoll': 'Hyperroll2.png', 'TFT6_Augment_MetabolicAccelerator': 'MetabolicAccel2.png', 'TFT6_Augment_MakeshiftArmor1': 'Makeshift1.png', 'TFT6_Augment_MakeshiftArmor2': 'Makeshift2.png', 'TFT6_Augment_Ascension': 'Ascension2.png', 'TFT6_Augment_BinaryAirdrop': 'BinaryAirdrop3.png', 'TFT6_Augment_ClearMind': 'ClearMind2.png', 'TFT6_Augment_ThriftShop': 'WiseSpending3.png', 'TFT6_Augment_Recombobulator': 'Recombobulator-I.png', 'TFT6_Augment_RadiantRelics': 'RadiantRelic-III.png', 'TFT6_Augment_JeweledLotus': 'Jeweled-Lotus-II.png', 'TFT6_Augment_VerdantVeil': 'Verdant-Veil-III.png', 'TFT6_Augment_TinyTitans': 'Tiny-Titans-I.png', 'TFT6_Augment_ComponentGrabBag': 'ComponentGrabBag-II.png', 'TFT6_Augment_Twins2': 'Double-Trouble-II.png', 'TFT6_Augment_Twins3': 'Double-Trouble-III.png', 'TFT6_Augment_FuturePeepers2': 'Future-Sight-III.png', 'TFT6_Augment_TrueTwos': 'True-Twos-II.png', 'TFT6_Augment_TriForce1': 'Tri-Force-I.png', 'TFT6_Augment_TriForce2': 'Tri-Force-II.png', 'TFT6_Augment_TriForce3': 'Tri-Force-III.png', 'TFT6_Augment_TheGoldenEgg': 'The-Golden-Egg-III.png', 'TFT7_Augment_ThinkFast': 'Think-Fast-III.TFT_Set7.png', 'TFT7_Augment_Bloodlust1': 'Combat-Training-II.TFT_Set7.png', 'TFT7_Augment_SacrificialPact': 'Sacrificial-Pact-III.TFT_Set7.png', 'TFT7_Augment_PandorasBench': 'Pandoras-Bench-I.TFT_Set7.png', 'TFT7_Augment_AxiomArc2': 'Axiom-Arc-II.TFT_Set7.png', 'TFT7_Augment_ClutteredMind': 'Dizzy-II.TFT_Set7.png', 'TFT6_Augment_TradeSector': 'Trade2.png', 'TFT6_Augment_Distancing': 'Exiles1.png', 'TFT6_Augment_Distancing2': 'Exiles2.png', 'TFT6_Augment_ThreesCompany': 'Threes-Company-II.png', 'TFT7_Augment_UrfsGrabBag2': 'Urfs-Grab-Bag-III.TFT_Set7.png', 'TFT7_Augment_LivingForge': 'Living-Forge-III.TFT_Set7.png', 'TFT7_Augment_AFK': 'AFK-I.TFT_Set7.png', 'TFT7_Augment_BandOfThieves1': 'BandThieves1.png', 'TFT7_Augment_LategameSpecialist': 'Late-Game-Specialist-I.TFT_Set7.png', 'TFT7_Augment_Preparation': 'Preparation-I.TFT_Set7.png', 'TFT7_Augment_BigFriend': 'Big-Friend-I.TFT_Set7.png', 'TFT7_Augment_LastStand': 'Last-Stand-II.TFT_Set7.png', 'TFT6_Augment_TargetDummies': 'PhonyFrontline2.png', 'TFT7_Augment_CursedCrown': 'CursedCrown-III.TFT_Set7.png', 'TFT6_Augment_CyberneticImplants1': 'Cybernetic1.png', 'TFT6_Augment_CelestialBlessing1': 'CelestialBlessing1.png', 'TFT6_Augment_SecondWind1': 'Second--Wind-I.png', 'TFT6_Augment_CyberneticShell1': 'Cybernetic-Shell-I.png', 'TFT6_Augment_CyberneticUplink1': 'Cybernetic-Uplink-I.png', 'TFT6_Augment_CyberneticImplants3': 'Cybernetic3.png', 'TFT6_Augment_CyberneticShell3': 'Cybernetic-Shell-III.png', 'TFT6_Augment_CyberneticUplink3': 'Cybernetic-Uplink-III.png', 'TFT6_Augment_RichGetRicher': 'RichGetRicher2.png', 'TFT6_Augment_RichGetRicherPlus': 'RichGetRicher2.png', 'TFT6_Augment_Electrocharge1': 'Electrocharge-I.png', 'TFT6_Augment_LudensEcho1': 'Ludens-Echo-I.png', 'TFT6_Augment_CelestialBlessing2': 'CelestialBlessing2.png', 'TFT6_Augment_CelestialBlessing3': 'CelestialBlessing3.png', 'TFT6_Augment_SecondWind2': 'Second--Wind-II.png', 'TFT6_Augment_ThrillOfTheHunt1': 'ThrillHunt1.png', 'TFT6_Augment_ThrillOfTheHunt2': 'ThrillHunt2.png', 'TFT6_Augment_LudensEcho2': 'Ludens-Echo-II.png', 'TFT6_Augment_LudensEcho3': 'Ludens-Echo-III.png', 'TFT6_Augment_Electrocharge2': 'Electrocharge-II.png', 'TFT6_Augment_Electrocharge3': 'Electrocharge-III.png', 'TFT6_Augment_CyberneticImplants2': 'Cybernetic2.png', 'TFT6_Augment_CyberneticShell2': 'Cybernetic-Shell-II.png', 'TFT6_Augment_CyberneticUplink2': 'Cybernetic-Uplink-II.png', 'TFT6_Augment_SunfireBoard': 'SunfireBoard2.png', 'TFT6_Augment_WindfallPlus': 'Windfall3.png', 'TFT6_Augment_WindfallPlusPlus': 'Windfall3.png', 'TFT7_Augment_FirstAidKit2': 'FirstAidKit2.png', 'TFT7_Augment_BigFriend2': 'Big-Friend-II.TFT_Set7.png', 'TFT7_Augment_Preparation2': 'Preparation-II.TFT_Set7.png', 'TFT7_Augment_Preparation3': 'Preparation-III.TFT_Set7.png', 'TFT6_Augment_TradeSectorPlus': 'Trade2.png', 'TFT8_Augment_ThreatMaxHealth': 'ThreatLevelMaxiumum-II.TFT_Set8.png', 'TFT8_Augment_AceEmblem': 'Ace-Crest.TFT_Set8.png', 'TFT8_Augment_AceEmblem2': 'Ace-Crown.TFT_Set8.png', 'TFT8_Augment_ADMINEmblem': 'ADMIN-Crest.TFT_Set8.png', 'TFT8_Augment_ADMINEmblem2': 'ADMIN-Crown.TFT_Set8.png', 'TFT8_Augment_AnimaSquadEmblem': 'Anima-Squad-Crest.TFT_Set8.png', 'TFT8_Augment_AnimaSquadEmblem2': 'Anima-Squad-Crown.TFT_Set8.png', 'TFT8_Augment_BrawlerEmblem': 'Brawler-Crest.TFT_Set8.png', 'TFT8_Augment_BrawlerEmblem2': 'Brawler-Crown.TFT_Set8.png', 'TFT8_Augment_ChannelerEmblem': 'Spellslinger-Crest.TFT_Set8.png', 'TFT8_Augment_ChannelerEmblem2': 'Spellslinger-Crown.TFT_Set8.png', 'TFT8_Augment_CivilianEmblem': 'Civilian-Crest.TFT_Set8.png', 'TFT8_Augment_CivilianEmblem2': 'Civilian-Crown.TFT_Set8.png', 'TFT8_Augment_DeadeyeEmblem': 'Sureshot-Crest.TFT_Set8.png', 'TFT8_Augment_DeadeyeEmblem2': 'Sureshot-Crown.TFT_Set8.png', 'TFT8_Augment_DefenderEmblem': 'Defender-Crest.TFT_Set8.png', 'TFT8_Augment_DefenderEmblem2': 'Defender-Crown.TFT_Set8.png', 'TFT8_Augment_DuelistEmblem': 'Duelist-Crest.TFT_Set8.png', 'TFT8_Augment_DuelistEmblem2': 'Duelist-Crown.TFT_Set8.png', 'TFT8_Augment_ExoPrimeEmblem': 'Mecha-Prime-Crest.TFT_Set8.png', 'TFT8_Augment_ExoPrimeEmblem2': 'Mecha-Prime-Crown.TFT_Set8.png', 'TFT8_Augment_GenAETrait2': 'Gadgeteens-Crown-III.TFT_Set8.png', 'TFT8_Augment_AegisEmblem': 'Aegis-Crest.TFT_Set8.png', 'TFT8_Augment_AegisEmblem2': 'Aegis-Crown.TFT_Set8.png', 'TFT8_Augment_HackerEmblem': 'Hacker-Crest.TFT_Set8.png', 'TFT8_Augment_HackerEmblem2': 'Hacker-Crown.TFT_Set8.png', 'TFT8_Augment_HeartEmblem': 'Heart-Crest.TFT_Set8.png', 'TFT8_Augment_HeartEmblem2': 'Heart-Crown.TFT_Set8.png', 'TFT8_Augment_InterPolarisEmblem': 'Lasercorps-Crest.TFT_Set8.png', 'TFT8_Augment_InterPolarisEmblem2': 'Lasercorps-Crown.TFT_Set8.png', 'TFT8_Augment_MascotEmblem': 'Mascot-Crest.TFT_Set8.png', 'TFT8_Augment_MascotEmblem2': 'Mascot-Crown.TFT_Set8.png', 'TFT8_Augment_OxForceEmblem': 'Ox-Force-Crest.TFT_Set8.png', 'TFT8_Augment_OxForceEmblem2': 'Ox-Force-Crown.TFT_Set8.png', 'TFT8_Augment_PranksterEmblem': 'Prankster-Crest.TFT_Set8.png', 'TFT8_Augment_PranksterEmblem2': 'Prankster-Crown.TFT_Set8.png', 'TFT8_Augment_ReconEmblem': 'Recon-Crest.TFT_Set8.png', 'TFT8_Augment_ReconEmblem2': 'Recon-Crown.TFT_Set8.png', 'TFT8_Augment_RenegadeEmblem': 'Renegade-Crest.TFT_Set8.png', 'TFT8_Augment_RenegadeEmblem2': 'Renegade-Crown.TFT_Set8.png', 'TFT8_Augment_StarGuardianEmblem': 'Star-Guardian-Crest.TFT_Set8.png', 'TFT8_Augment_StarGuardianEmblem2': 'Star-Guardian-Crown.TFT_Set8.png', 'TFT8_Augment_UndergroundTheTrait2': 'The-Underground-Crown-III.TFT_Set8.png', 'TFT6_Augment_WoodlandCharm': 'WoodlandCharm3.png', 'TFT7_Augment_LuckyGloves': 'Lucky-Gloves-III.png', 'TFT7_Augment_ScopedWeapons1': 'ScopedWeapons2.png', 'TFT6_Augment_Battlemage1': 'Battlemage-I-A.png', 'TFT6_Augment_Battlemage2': 'Battlemage-II-A.png', 'TFT6_Augment_Battlemage3': 'Battlemage-III-A.png', 'TFT6_Augment_MeleeStarBlade1': 'CQCTraining1.png', 'TFT6_Augment_MeleeStarBlade2': 'CQCTraining2.png', 'TFT6_Augment_MeleeStarBlade3': 'CQCTraining3.png', 'TFT7_Augment_BirthdayPresents': 'Golden-Gifts-III.png', 'TFT7_Augment_Consistency': 'Consistency-I.png', 'TFT8_Augment_AnimaSquadTrait': 'Anima-Squad-Heart.TFT_Set8.png', 'TFT8_Augment_StarGuardianTrait': 'Star-Guardian-Heart.TFT_Set8.png', 'TFT8_Augment_InterPolarisTrait': 'Lasercorps-Heart.TFT_Set8.png', 'TFT8_Augment_OxForceTrait': 'Ox-Force-Heart.TFT_Set8.png', 'TFT8_Augment_GenAETrait': 'Gadgeteens-Heart-II.TFT_Set8.png', 'TFT8_Augment_MascotTrait': 'Mascot-Heart.TFT_Set8.png', 'TFT8_Augment_DefenderTrait': 'Defender-Heart.TFT_Set8.png', 'TFT8_Augment_ChannelerTrait': 'Spellslinger-Heart.TFT_Set8.png', 'TFT8_Augment_BrawlerTrait': 'Brawler-Heart.TFT_Set8.png', 'TFT8_Augment_DuelistTrait': 'Duelist-Heart.TFT_Set8.png', 'TFT8_Augment_HeartTrait': 'Heart-Heart.TFT_Set8.png', 'TFT8_Augment_DeadeyeTrait': 'Sureshot-Heart.TFT_Set8.png', 'TFT8_Augment_ReconTrait': 'Recon-Heart.TFT_Set8.png', 'TFT8_Augment_RenegadeTrait': 'Renegade-Heart.TFT_Set8.png', 'TFT8_Augment_UndergroundTheTrait': 'The-Underground-Heart-II.TFT_Set8.png', 'TFT8_Augment_SupersTrait': 'Supers-Heart-II.TFT_Set8.png', 'TFT8_Augment_SupersTrait2': 'Supers-Crown-III.TFT_Set8.png', 'TFT8_Augment_ADMINTrait': 'ADMIN-Heart.TFT_Set8.png', 'TFT8_Augment_HackerTrait': 'Hacker-Heart.TFT_Set8.png', 'TFT6_Augment_TomeOfTraits1': 'AncientArchives2.png', 'TFT7_Augment_TomeOfTraits2': 'AncientArchives3.png', 'TFT6_Augment_Traitless2': 'BuiltDifferent2.png', 'TFT6_Augment_Traitless3': 'BuiltDifferent3.png', 'TFT6_Augment_FuturePeepers': 'Future-Sight-I.png', 'TFT6_Augment_GachaAddict': 'GoldenTicket3.png'}
    return aug[name]

def hero_aug(name):
    aug={'TFT8_Augment_BelVethVoidmother': 'TFT8_BelVeth.TFT_Set8.png', 'TFT8_Augment_AurelionSolImpact': 'TFT8_AurelionSol.TFT_Set8.png', 'TFT8_Augment_ChoGathMR': 'TFT8_Chogath.TFT_Set8.png', 'TFT8_Augment_RammusArmor': 'TFT8_Rammus.TFT_Set8.png', 'TFT8_Augment_VelkozFrostburn': 'TFT8_Velkoz.TFT_Set8.png', 'TFT8_Augment_ZacSupersize': 'TFT8_Zac.TFT_Set8.png', 'TFT8_Augment_SonaExile': 'TFT8_Sona.TFT_Set8.png', 'TFT8_Augment_SonaSupport': 'TFT8_Sona.TFT_Set8.png', 'TFT8_Augment_AlistarAoEPulverizer': 'TFT8_Alistar.TFT_Set8.png', 'TFT8_Augment_JaxASCarry': 'TFT8_Jax.TFT_Set8.png', 'TFT8_Augment_SennaASCarry': 'TFT8_Senna.TFT_Set8.png', 'TFT8_Augment_NilahReflection': 'TFT8_Nilah.TFT_Set8.png', 'TFT8_Augment_ZoeDoubleTrouble': 'TFT8_Zoe.TFT_Set8.png', 'TFT8_Augment_SennaSupport': 'TFT8_Senna.TFT_Set8.png', 'TFT8_Augment_AlistarBeefUp': 'TFT8_Alistar.TFT_Set8.png', 'TFT8_Augment_RivenReverberation': 'TFT8_Riven.TFT_Set8.png', 'TFT8_Augment_AnnieCarry': 'TFT8_Annie.TFT_Set8.png', 'TFT8_Augment_AnnieSupport': 'TFT8_Annie.TFT_Set8.png', 'TFT8_Augment_CamilleCarry': 'TFT8_Camille.TFT_Set8.png', 'TFT8_Augment_LeeSinSupport': 'TFT8_LeeSin.TFT_Set8.png', 'TFT8_Augment_RellSupport': 'TFT8_Rell.TFT_Set8.png', 'TFT8_Augment_YuumiSupport': 'TFT8_Yuumi.TFT_Set8.png', 'TFT8_Augment_ViSupport': 'TFT8_Vi.TFT_Set8.png', 'TFT8_Augment_SivirSupport': 'TFT8_Sivir.TFT_Set8.png', 'TFT8_Augment_KaisaStarCrossed': 'TFT8_Kaisa.TFT_Set8.png', 'TFT8_Augment_YasuoCarry': 'TFT8_Yasuo.TFT_Set8.png', 'TFT8_Augment_LeBlancGlitch': 'TFT8_Leblanc.TFT_Set8.png', 'TFT8_Augment_FioraCarry': 'TFT8_Fiora.TFT_Set8.png', 'TFT8_Augment_EzrealSupport': 'TFT8_Ezreal.TFT_Set8.png', 'TFT8_Augment_JinxCarry': 'TFT8_Jinx.TFT_Set8.png', 'TFT8_Augment_MalphiteCarry': 'TFT8_Malphite.TFT_Set8.png', 'TFT8_Augment_NasusCarry': 'TFT8_Nasus.TFT_Set8.png', 'TFT8_Augment_DravenCarry': 'TFT8_Draven.TFT_Set8.png', 'TFT8_Augment_KaisaCarry': 'TFT8_Kaisa.TFT_Set8.png', 'TFT8_Augment_GalioCarry': 'TFT8_Galio.TFT_Set8.png', 'TFT8_Augment_GalioSupport': 'TFT8_Galio.TFT_Set8.png', 'TFT8_Augment_AurelionSolCarry': 'TFT8_AurelionSol.TFT_Set8.png', 'TFT8_Augment_JaxSupport': 'TFT8_Jax.TFT_Set8.png', 'TFT8_Augment_LuxCarry': 'TFT8_Lux.TFT_Set8.png', 'TFT8_Augment_PoppyCarry': 'TFT8_Poppy.TFT_Set8.png', 'TFT8_Augment_ApheliosSupport': 'TFT8_Aphelios.TFT_Set8.png', 'TFT8_Augment_LuxSupport': 'TFT8_Lux.TFT_Set8.png', 'TFT8_Augment_GangplankSupport': 'TFT8_Gangplank.TFT_Set8.png', 'TFT8_Augment_SylasCarry': 'TFT8_Sylas.TFT_Set8.png', 'TFT8_Augment_SylasSupport': 'TFT8_Sylas.TFT_Set8.png', 'TFT8_Augment_SettCarry': 'TFT8_Sett.TFT_Set8.png', 'TFT8_Augment_KayleCarry': 'TFT8_Kayle.TFT_Set8.png', 'TFT8_Augment_KayleSupport': 'TFT8_Kayle.TFT_Set8.png', 'TFT8_Augment_EkkoSupport': 'TFT8_Ekko.TFT_Set8.png', 'TFT8_Augment_MordekaiserCarry': 'TFT8_Mordekaiser.TFT_Set8.png', 'TFT8_Augment_VelkozSupport': 'TFT8_Velkoz.TFT_Set8.png', 'TFT8_Augment_SettSupport': 'TFT8_Sett.TFT_Set8.png', 'TFT8_Augment_TalonCarry': 'TFT8_Talon.TFT_Set8.png', 'TFT8_Augment_MissFortuneCarry': 'TFT8_MissFortune.TFT_Set8.png', 'TFT8_Augment_ChoGathCarry': 'TFT8_Chogath.TFT_Set8.png', 'TFT8_Augment_SyndraSupport': 'TFT8_Syndra.TFT_Set8.png', 'TFT8_Augment_RammusCarry': 'TFT8_Rammus.TFT_Set8.png', 'TFT8_Augment_LeonaCarry': 'TFT8_Leona.TFT_Set8.png', 'TFT8_Augment_NunuSupport': 'TFT8_Nunu.TFT_Set8.png', 'TFT8_Augment_FiddlesticksCarry': 'TFT8_Fiddlesticks.TFT_Set8.png', 'TFT8_Augment_UrgotCarry': 'TFT8_Urgot.TFT_Set8.png', 'TFT8_Augment_JannaSupport': 'TFT8_Janna.TFT_Set8.png', 'TFT8_Augment_SamiraCarry': 'TFT8_Samira.TFT_Set8.png', 'TFT8_Augment_TaliyahSupport': 'TFT8_Taliyah.TFT_Set8.png', 'TFT8_Augment_ZedSupport': 'TFT8_Zed.TFT_Set8.png', 'TFT8_Augment_BlitzcrankCarry': 'TFT8_Blitzcrank.TFT_Set8.png', 'TFT8_Augment_UrgotSupport': 'TFT8_Urgot.TFT_Set8.png', 'TFT8_Augment_BlitzcrankSupport': 'TFT8_Blitzcrank.TFT_Set8.png', 'TFT8_Augment_MordekaiserSupport': 'TFT8_Mordekaiser.TFT_Set8.png', 'TFT8_Augment_ApheliosCarry': 'TFT8_Aphelios.TFT_Set8.png', 'TFT8_Augment_LuluSupport': 'TFT8_Lulu.TFT_Set8.png', 'TFT8_Augment_LeonaSupport': 'TFT8_Leona.TFT_Set8.png', 'TFT8_Augment_SejuaniCarry': 'TFT8_Sejuani.TFT_Set8.png', 'TFT8_Augment_SyndraCarry': 'TFT8_Syndra.TFT_Set8.png', 'TFT8_Augment_WukongSupport': 'TFT8_Wukong.TFT_Set8.png', 'TFT8_Augment_AsheCarry': 'TFT8_Ashe.TFT_Set8.png', 'TFT8_Augment_AsheSupport': 'TFT8_Ashe.TFT_Set8.png', 'TFT8_Augment_NilahSupport': 'TFT8_Nilah.TFT_Set8.png', 'TFT8_Augment_VayneSupport': 'TFT8_Vayne.TFT_Set8.png', 'TFT8_Augment_RivenSupport': 'TFT8_Riven.TFT_Set8.png', 'TFT8_Augment_ZoeSupport': 'TFT8_Zoe.TFT_Set8.png', 'TFT8_Augment_LeBlancSupport': 'TFT8_Leblanc.TFT_Set8.png', 'TFT8_Augment_LeeSinCarry': 'TFT8_LeeSin.TFT_Set8.png', 'TFT8_Augment_YuumiCarry': 'TFT8_Yuumi.TFT_Set8.png', 'TFT8_Augment_FiddlesticksSupport': 'TFT8_Fiddlesticks.TFT_Set8.png', 'TFT8_Augment_PoppySupport': 'TFT8_Poppy.TFT_Set8.png', 'TFT8_Augment_JannaCarry': 'TFT8_Janna.TFT_Set8.png', 'TFT8_Augment_RenegadePartners': 'TFT8_Viego.TFT_Set8.png', 'TFT8_Augment_TaliyahCarry': 'TFT8_Taliyah.TFT_Set8.png', 'TFT8_Augment_ZedCarry': 'TFT8_Zed.TFT_Set8.png', 'TFT8_Augment_SivirCarry': 'TFT8_Sivir.TFT_Set8.png', 'TFT8_Augment_RenektonCarry': 'TFT8_Renekton.TFT_Set8.png', 'TFT8_Augment_ViCarry': 'TFT8_Vi.TFT_Set8.png', 'TFT8_Augment_RenektonSupport': 'TFT8_Renekton.TFT_Set8.png', 'TFT8_Augment_RellCarry': 'TFT8_Rell.TFT_Set8.png', 'TFT8_Augment_FioraSupport': 'TFT8_Fiora.TFT_Set8.png', 'TFT8_Augment_DravenSupport': 'TFT8_Draven.TFT_Set8.png', 'TFT8_Augment_YasuoSupport': 'TFT8_Yasuo.TFT_Set8.png', 'TFT8_Augment_NasusSupport': 'TFT8_Nasus.TFT_Set8.png', 'TFT8_Augment_SorakaSupport': 'TFT8_Soraka.TFT_Set8.png', 'TFT8_Augment_LuluCarry': 'TFT8_Lulu.TFT_Set8.png', 'TFT8_Augment_SorakaCarry': 'TFT8_Soraka.TFT_Set8.png', 'TFT8_Augment_VayneCarry': 'TFT8_Vayne.TFT_Set8.png', 'TFT8_Augment_MalphiteSupport': 'TFT8_Malphite.TFT_Set8.png', 'TFT8_Augment_BelVethCarry': 'TFT8_BelVeth.TFT_Set8.png', 'TFT8_Augment_EkkoCarry': 'TFT8_Ekko.TFT_Set8.png', 'TFT8_Augment_GangplankCarry': 'TFT8_Gangplank.TFT_Set8.png', 'TFT8_Augment_JinxSupport': 'TFT8_Jinx.TFT_Set8.png', 'TFT8_Augment_MissFortuneSupport': 'TFT8_MissFortune.TFT_Set8.png', 'TFT8_Augment_CamilleSupport': 'TFT8_Camille.TFT_Set8.png', 'TFT8_Augment_WukongCarry': 'TFT8_Wukong.TFT_Set8.png', 'TFT8_Augment_SejuaniSupport': 'TFT8_Sejuani.TFT_Set8.png', 'TFT8_Augment_ZacSupport': 'TFT8_Zac.TFT_Set8.png', 'TFT8_Augment_NunuCarry': 'TFT8_Nunu.TFT_Set8.png', 'TFT8_Augment_ViegoCarry': 'TFT8_Viego.TFT_Set8.png', 'TFT8_Augment_SamiraSupport': 'TFT8_Samira.TFT_Set8.png', 'TFT8_Augment_TalonSupport': 'TFT8_Talon.TFT_Set8.png', 'TFT8_Augment_EzrealCarry': 'TFT8_Ezreal.TFT_Set8.png'}
    return aug[name]


def pet_K(name):
    pet={13010: '비트메이커 오시아', 13011: '비트메이커 오시아', 13012: '비트메이커 오시아', 13019: '용 춤꾼 오시아', 13020: '용 춤꾼 오시아', 13021: '용 춤꾼 오시아', 13001: '오시아', 13002: '오시아', 13003: '오시아', 13007: '팝의 여왕 오시아', 13008: '팝의 여왕 오시아', 13009: '팝의 여왕 오시아', 13013: '천재 오시아', 13014: '천재 오시아', 13015: '천재 오시아', 13016: '신난 오시아', 13017: '신난 오시아', 13018: '신난 오시아', 13004: '독주자 오시아', 13005: '독주자 오시아', 13006: '독주자 오시아', 25001: '아오 신', 25002: '아오 신', 25003: '아오 신', 25010: '암흑의 별 아오 신', 25011: '암흑의 별 아오 신', 25012: '암흑의 별 아오 신', 25013: '신성한 아오 신', 25014: '신성한 아오 신', 25015: '신성한 아오 신', 25004: '장로 아오 신', 25005: '장로 아오 신', 25006: '장로 아오 신', 25007: '불꽃놀이 아오 신', 25008: '불꽃놀이 아오 신', 25009: '불꽃놀이 아오 신', 25019: '하늘빛 붓꼬리 아오 신', 25020: '하늘빛 붓꼬리 아오 신', 25021: '하늘빛 붓꼬리 아오 신', 25022: '돌풍의 화신 붓꼬리 아오 신', 25023: '돌풍의 화신 붓꼬리 아오 신', 25024: '돌풍의 화신 붓꼬리 아오 신', 25025: '잉걸불 붓꼬리 아오 신', 25026: '잉걸불 붓꼬리 아오 신', 25027: '잉걸불 붓꼬리 아오 신', 25028: '검은불꽃 붓꼬리 아오 신', 25029: '검은불꽃 붓꼬리 아오 신', 25030: '검은불꽃 붓꼬리 아오 신', 25031: '대지 붓꼬리 아오 신', 25032: '대지 붓꼬리 아오 신', 25033: '대지 붓꼬리 아오 신', 25016: '별의 창조자 아오 신', 25017: '별의 창조자 아오 신', 25018: '별의 창조자 아오 신', 25034: '물장구 아오 신', 25035: '물장구 아오 신', 25036: '물장구 아오 신', 39001: '뽀글이', 39002: '뽀글이', 39003: '뽀글이', 39019: '사자춤 뽀글이', 39020: '사자춤 뽀글이', 39021: '사자춤 뽀글이', 39004: '개구리 뽀글이', 39005: '개구리 뽀글이', 39006: '개구리 뽀글이', 39007: '꿀벌 뽀글이', 39008: '꿀벌 뽀글이', 39009: '꿀벌 뽀글이', 39010: '불혀 뽀글이', 39011: '불혀 뽀글이', 39012: '불혀 뽀글이', 39013: '심해 뽀글이', 39014: '심해 뽀글이', 39015: '심해 뽀글이', 39016: '아이스크림 콘 뽀글이', 39017: '아이스크림 콘 뽀글이', 39018: '아이스크림 콘 뽀글이', 51003: '남작이', 51006: '슈퍼특공대 남작이', 51009: '오디세이 남작이', 51012: '별 수호자 남작이', 51015: '별의 숙적 남작이', 51018: '우주의 무법자 남작이', 24013: '검은 안개 방울이', 24014: '검은 안개 방울이', 24015: '검은 안개 방울이', 24016: '핏빛달 방울이', 24017: '핏빛달 방울이', 24018: '핏빛달 방울이', 24001: '방울이', 24002: '방울이', 24003: '방울이', 24019: '도자기 방울이', 24020: '도자기 방울이', 24021: '도자기 방울이', 24007: '달콤 가득 방울이', 24008: '달콤 가득 방울이', 24009: '달콤 가득 방울이', 24004: '천둥 번개 방울이', 24005: '천둥 번개 방울이', 24006: '천둥 번개 방울이', 24010: '성탄절 방울이', 24011: '성탄절 방울이', 24012: '성탄절 방울이', 17016: '꿀벌 총총이', 17017: '꿀벌 총총이', 17018: '꿀벌 총총이', 17001: '총총이', 17002: '총총이', 17003: '총총이', 17013: '이쉬탈 총총이', 17014: '이쉬탈 총총이', 17015: '이쉬탈 총총이', 17010: '군단 총총이', 17011: '군단 총총이', 17012: '군단 총총이', 17007: '모래몰이 총총이', 17008: '모래몰이 총총이', 17009: '모래몰이 총총이', 17019: '감시자 총총이', 17004: '얼음 정수 총총이', 17005: '얼음 정수 총총이', 17006: '얼음 정수 총총이', 17020: '생일 꽃 케익', 52001: '깡충이', 52002: '깡충이', 52003: '깡충이', 52019: '설맞이 축제 깡충이', 52020: '설맞이 축제 깡충이', 52021: '설맞이 축제 깡충이', 52022: '도자기 깡충이', 52023: '도자기 깡충이', 52024: '도자기 깡충이', 52025: '빨간 토끼 깡충이', 52026: '빨간 토끼 깡충이', 52027: '빨간 토끼 깡충이', 52028: '연꽃 깡충이', 52029: '연꽃 깡충이', 52030: '연꽃 깡충이', 52031: '맛있는 깡충이', 52032: '맛있는 깡충이', 52033: '맛있는 깡충이', 52004: '초코 가득 깡충이', 52005: '초코 가득 깡충이', 52006: '초코 가득 깡충이', 52007: '전투 토끼 깡충이', 52008: '전투 토끼 깡충이', 52009: '전투 토끼 깡충이', 52010: '빨간 모자 깡충이', 52011: '빨간 모자 깡충이', 52012: '빨간 모자 깡충이', 52013: '우주 그루브 깡충이', 52014: '우주 그루브 깡충이', 52015: '우주 그루브 깡충이', 52016: '바나나 깡충이', 52017: '바나나 깡충이', 52018: '바나나 깡충이', 54001: '미니 애니', 54002: '미니 판다 애니', 48001: '미니 애쉬', 48002: '미니 용술사 애쉬', 34001: '미니 에코', 35001: '미니 징크스', 35002: '미니 불꽃놀이 징크스', 45001: '미니 카이사', 45002: '미니 용술사 카이사', 44001: '미니 리 신', 44002: '미니 용술사 리 신', 50001: '미니 럭스', 50002: '미니 별 수호자 럭스', 37001: '미니 바이', 38001: '미니 야스오', 38002: '미니 용술사 야스오', 27004: '아틀란티스 배불뚝이', 27005: '아틀란티스 배불뚝이', 27006: '아틀란티스 배불뚝이', 27001: '배불뚝이', 27002: '배불뚝이', 27003: '배불뚝이', 27007: '바위 배불뚝이', 27008: '바위 배불뚝이', 27009: '바위 배불뚝이', 27010: '불꽃 배불뚝이', 27011: '불꽃 배불뚝이', 27012: '불꽃 배불뚝이', 27016: '꿀벌 배불뚝이', 27017: '꿀벌 배불뚝이', 27018: '꿀벌 배불뚝이', 27022: '새해 야수 배불뚝이', 27023: '새해 야수 배불뚝이', 27024: '새해 야수 배불뚝이', 27019: '설맞이 축제 배불뚝이', 27020: '설맞이 축제 배불뚝이', 27021: '설맞이 축제 배불뚝이', 27034: '현자 배불뚝이', 27035: '현자 배불뚝이', 27036: '현자 배불뚝이', 27013: '판다 배불뚝이', 27014: '판다 배불뚝이', 27015: '판다 배불뚝이', 27025: '어푸푸 마을 배불뚝이', 27026: '어푸푸 마을 배불뚝이', 27027: '어푸푸 마을 배불뚝이', 27028: '안전 요원 배불뚝이', 27029: '안전 요원 배불뚝이', 27030: '안전 요원 배불뚝이', 27031: '구릿빛 배불뚝이', 27032: '구릿빛 배불뚝이', 27033: '구릿빛 배불뚝이', 53001: '수염냥', 53002: '수염냥', 53003: '수염냥', 53004: '별 수호자 수염냥', 53005: '별 수호자 수염냥', 53006: '별 수호자 수염냥', 53007: '슈퍼특공대 수염냥', 53008: '슈퍼특공대 수염냥', 53009: '슈퍼특공대 수염냥', 53010: '꿰맨 수염냥', 53011: '꿰맨 수염냥', 53012: '꿰맨 수염냥', 53013: '별의 숙적 수염냥', 53014: '별의 숙적 수염냥', 53015: '별의 숙적 수염냥', 53016: '암흑의 별 수염냥', 53017: '암흑의 별 수염냥', 53018: '암흑의 별 수염냥', 19016: '우주 징징이', 19017: '우주 징징이', 19018: '우주 징징이', 19007: '행성 파괴자 징징이', 19008: '행성 파괴자 징징이', 19009: '행성 파괴자 징징이', 19010: '새콤달콤 징징이', 19011: '새콤달콤 징징이', 19012: '새콤달콤 징징이', 19019: 'K/DA ALL OUT 징징이', 19020: 'K/DA ALL OUT 징징이', 19021: 'K/DA ALL OUT 징징이', 19022: 'K/DA POP/STARS 징징이', 19023: 'K/DA POP/STARS 징징이', 19024: 'K/DA POP/STARS 징징이', 19004: '오디세이 징징이', 19005: '오디세이 징징이', 19006: '오디세이 징징이', 19001: '징징이', 19002: '징징이', 19003: '징징이', 19013: '아이스크림 콘 징징이', 19014: '아이스크림 콘 징징이', 19015: '아이스크림 콘 징징이', 19025: '선인장 징징이', 19026: '선인장 징징이', 19027: '선인장 징징이', 19028: '하이 눈 징징이', 19029: '하이 눈 징징이', 19030: '하이 눈 징징이', 19031: '질서의 징징이', 19032: '질서의 징징이', 19033: '질서의 징징이', 19034: '옥수수 징징이', 19035: '옥수수 징징이', 19036: '옥수수 징징이', 19037: '무법자 징징이', 19038: '무법자 징징이', 19039: '무법자 징징이', 20001: '어둠전사', 20002: '어둠전사', 20003: '어둠전사', 20013: '석회석 어둠전사', 20014: '석회석 어둠전사', 20015: '석회석 어둠전사', 20016: '우주 어둠전사', 20017: '우주 어둠전사', 20018: '우주 어둠전사', 20019: '프로젝트: 어둠전사', 20020: '프로젝트: 어둠전사', 20021: '프로젝트: 어둠전사', 20004: '다르킨 어둠전사', 20005: '다르킨 어둠전사', 20006: '다르킨 어둠전사', 20007: '은하계 학살자 어둠전사', 20008: '은하계 학살자 어둠전사', 20009: '은하계 학살자 어둠전사', 20010: '나무껍질 어둠전사', 20011: '나무껍질 어둠전사', 20012: '나무껍질 어둠전사', 21016: '우주 별고래', 21017: '우주 별고래', 21018: '우주 별고래', 21004: '행성 파괴자 별고래', 21005: '행성 파괴자 별고래', 21006: '행성 파괴자 별고래', 21007: '은하계 학살자 별고래', 21008: '은하계 학살자 별고래', 21009: '은하계 학살자 별고래', 21010: '액체괴물 별고래', 21011: '액체괴물 별고래', 21012: '액체괴물 별고래', 21019: '비단잉어왕 별고래 ', 21020: '비단잉어왕 별고래 ', 21021: '비단잉어왕 별고래 ', 21013: '악마 별고래', 21014: '악마 별고래', 21015: '악마 별고래', 21001: '별고래', 21002: '별고래', 21003: '별고래', 29001: '퐁당이', 29002: '퐁당이', 29003: '퐁당이', 29022: '도자기 퐁당이', 29023: '도자기 퐁당이', 29024: '도자기 퐁당이', 29025: '운수 대통 퐁당이', 29026: '운수 대통 퐁당이', 29027: '운수 대통 퐁당이', 29028: '행운의 국수 퐁당이', 29029: '행운의 국수 퐁당이', 29030: '행운의 국수 퐁당이', 29031: '불닭 퐁당이', 29032: '불닭 퐁당이', 29033: '불닭 퐁당이', 29034: '달콤한 꽃잎 퐁당이', 29035: '달콤한 꽃잎 퐁당이', 29036: '달콤한 꽃잎 퐁당이', 29019: 'U.R.F. 퐁당이', 29020: 'U.R.F. 퐁당이', 29021: 'U.R.F. 퐁당이', 29004: '비단인어 퐁당이', 29005: '비단인어 퐁당이', 29006: '비단인어 퐁당이', 29007: '젤리 퐁당이', 29008: '젤리 퐁당이', 29009: '젤리 퐁당이', 29010: '와플 퐁당이', 29011: '와플 퐁당이', 29012: '와플 퐁당이', 29013: '무지갯빛 퐁당이', 29014: '무지갯빛 퐁당이', 29015: '무지갯빛 퐁당이', 29016: '어둠의 인도자 퐁당이', 29017: '어둠의 인도자 퐁당이', 29018: '어둠의 인도자 퐁당이', 42001: '꽥꽥이', 42002: '꽥꽥이', 42003: '꽥꽥이', 42025: '흥겨운 꽥꽥이', 42026: '흥겨운 꽥꽥이', 42027: '흥겨운 꽥꽥이', 42028: '수룡 꽥꽥이', 42029: '수룡 꽥꽥이', 42030: '수룡 꽥꽥이', 42031: '달빛 학자 꽥꽥이', 42032: '달빛 학자 꽥꽥이', 42033: '달빛 학자 꽥꽥이', 42034: '불꽃놀이 꽥꽥이', 42035: '불꽃놀이 꽥꽥이', 42036: '불꽃놀이 꽥꽥이', 42037: '말썽꾸러기 꽥꽥이', 42038: '말썽꾸러기 꽥꽥이', 42039: '말썽꾸러기 꽥꽥이', 42004: '꿀벌 꽥꽥이', 42005: '꿀벌 꽥꽥이', 42006: '꿀벌 꽥꽥이', 42007: '배달의 기수 꽥꽥이', 42008: '배달의 기수 꽥꽥이', 42009: '배달의 기수 꽥꽥이', 42010: '파자마 파티 꽥꽥이', 42011: '파자마 파티 꽥꽥이', 42012: '파자마 파티 꽥꽥이', 42013: '아이스크림 콘 꽥꽥이', 42014: '아이스크림 콘 꽥꽥이', 42015: '아이스크림 콘 꽥꽥이', 42016: '자운 꽥꽥이', 42017: '자운 꽥꽥이', 42018: '자운 꽥꽥이', 42019: '필트오버 꽥꽥이', 42020: '필트오버 꽥꽥이', 42021: '필트오버 꽥꽥이', 42022: '최고의 꽥꽥이', 42023: '최고의 꽥꽥이', 42024: '최고의 꽥꽥이', 47001: '용발굽', 47002: '용발굽', 47003: '용발굽', 47004: '비단잉어 용발굽', 47005: '비단잉어 용발굽', 47006: '비단잉어 용발굽', 47007: '분노날개 용발굽', 47008: '분노날개 용발굽', 47009: '분노날개 용발굽', 47010: '비취 용발굽', 47011: '비취 용발굽', 47012: '비취 용발굽', 47013: '어둠강림 용발굽', 47014: '어둠강림 용발굽', 47015: '어둠강림 용발굽', 47016: '만년서리 용발굽', 47017: '만년서리 용발굽', 47018: '만년서리 용발굽', 23016: '파알랑이', 23017: '파알랑이', 23018: '파알랑이', 23001: '팔랑이', 23002: '팔랑이', 23003: '팔랑이', 23013: '불닭 팔랑이', 23014: '불닭 팔랑이', 23015: '불닭 팔랑이', 23007: '인어 팔랑이', 23008: '인어 팔랑이', 23009: '인어 팔랑이', 23022: '사교계 팔랑이', 23023: '사교계 팔랑이', 23024: '사교계 팔랑이', 23004: '장미꽃 팔랑이', 23005: '장미꽃 팔랑이', 23006: '장미꽃 팔랑이', 23020: '환호의 팔랑이', 23010: '흡혈귀 팔랑이', 23011: '흡혈귀 팔랑이', 23012: '흡혈귀 팔랑이', 23019: '승리의 팔랑이', 30001: '으르렁이', 30002: '으르렁이', 30003: '으르렁이', 30019: '탄산 으르렁이', 30020: '탄산 으르렁이', 30021: '탄산 으르렁이', 30022: '제트 엔진 으르렁이', 30023: '제트 엔진 으르렁이', 30024: '제트 엔진 으르렁이', 30025: '마법공학 으르렁이', 30026: '마법공학 으르렁이', 30027: '마법공학 으르렁이', 30028: '펄스 건 으르렁이', 30029: '펄스 건 으르렁이', 30030: '펄스 건 으르렁이', 30031: '현상금 사냥꾼 으르렁이', 30032: '현상금 사냥꾼 으르렁이', 30033: '현상금 사냥꾼 으르렁이', 30004: '슈리마 으르렁이', 30005: '슈리마 으르렁이', 30006: '슈리마 으르렁이', 30007: '황금 으르렁이', 30008: '황금 으르렁이', 30009: '황금 으르렁이', 30010: '천공의 화신 으르렁이', 30011: '천공의 화신 으르렁이', 30012: '천공의 화신 으르렁이', 30013: '어둠의 인도자 으르렁이', 30014: '어둠의 인도자 으르렁이', 30015: '어둠의 인도자 으르렁이', 30016: '칸메이 으르렁이', 30017: '칸메이 으르렁이', 30018: '칸메이 으르렁이', 18010: '검은 안개 돌돌이', 18011: '검은 안개 돌돌이', 18012: '검은 안개 돌돌이', 18001: '돌돌이', 18002: '돌돌이', 18003: '돌돌이', 18016: '마법공학 돌돌이', 18017: '마법공학 돌돌이', 18018: '마법공학 돌돌이', 18013: '군단 돌돌이', 18014: '군단 돌돌이', 18015: '군단 돌돌이', 18007: '모래몰이 돌돌이', 18008: '모래몰이 돌돌이', 18009: '모래몰이 돌돌이', 18019: ' 감시자 돌돌이', 18021: '환호의 돌돌이', 18004: '얼음 정수 돌돌이', 18005: '얼음 정수 돌돌이', 18006: '얼음 정수 돌돌이', 18020: '승리의 돌돌이', 7004: '맹렬한 수호대장', 7005: '맹렬한 수호대장', 7006: '맹렬한 수호대장', 7001: '보석박이 수호대장', 7002: '보석박이 수호대장', 7003: '보석박이 수호대장', 7021: '호랑이띠 해 수호대장', 7022: '호랑이띠 해 수호대장', 7023: '호랑이띠 해 수호대장', 7013: '군림하는 수호대장', 7014: '군림하는 수호대장', 7015: '군림하는 수호대장', 7007: '그늘보석 수호대장', 7008: '그늘보석 수호대장', 7009: '그늘보석 수호대장', 7010: '하늘보석 수호대장', 7011: '하늘보석 수호대장', 7012: '하늘보석 수호대장', 7016: '태양의 자손 수호대장', 7017: '태양의 자손 수호대장', 7018: '태양의 자손 수호대장', 7020: '환호의 수호대장', 7019: '승리의 수호대장', 1016: '그림자 가면 유령이', 1017: '그림자 가면 유령이', 1018: '그림자 가면 유령이', 1007: '달빛 발톱 유령이', 1008: '달빛 발톱 유령이', 1009: '달빛 발톱 유령이', 1004: '불꽃 유령이', 1005: '불꽃 유령이', 1006: '불꽃 유령이', 1020: '환호의 유령이', 1010: '맹독 유령이', 1011: '맹독 유령이', 1012: '맹독 유령이', 1022: '화염의 유령이', 1023: '화염의 유령이', 1024: '화염의 유령이', 1025: '장로 유령이', 1026: '장로 유령이', 1027: '장로 유령이', 1028: '바다의 유령이', 1029: '바다의 유령이', 1030: '바다의 유령이', 1031: '대지의 유령이', 1032: '대지의 유령이', 1033: '대지의 유령이', 1034: '바람의 유령이', 1035: '바람의 유령이', 1036: '바람의 유령이', 1013: '암흑 물질 유령이', 1014: '암흑 물질 유령이', 1015: '암흑 물질 유령이', 1021: '감시자 유령이', 1001: '그림자 군도 유령이', 1002: '그림자 군도 유령이', 1003: '그림자 군도 유령이', 1019: '승리의 유령이', 41001: '말캉이', 41002: '말캉이', 41003: '말캉이', 41025: '복숭아 말캉이', 41026: '복숭아 말캉이', 41027: '복숭아 말캉이', 41028: '새우맛 말캉이', 41029: '새우맛 말캉이', 41030: '새우맛 말캉이', 41031: '따뜻한 수프 말캉이', 41032: '따뜻한 수프 말캉이', 41033: '따뜻한 수프 말캉이', 41034: '도자기 말캉이', 41035: '도자기 말캉이', 41036: '도자기 말캉이', 41037: '황금빛 커스터드 말캉이', 41038: '황금빛 커스터드 말캉이', 41039: '황금빛 커스터드 말캉이', 41004: '꿀벌 말캉이', 41005: '꿀벌 말캉이', 41006: '꿀벌 말캉이', 41007: '마법공학 말캉이', 41008: '마법공학 말캉이', 41009: '마법공학 말캉이', 41010: '불꽃 말캉이', 41011: '불꽃 말캉이', 41012: '불꽃 말캉이', 41013: '아케이드 말캉이', 41014: '아케이드 말캉이', 41015: '아케이드 말캉이', 41016: '아이스크림 콘 말캉이', 41017: '아이스크림 콘 말캉이', 41018: '아이스크림 콘 말캉이', 41019: '팝 그루브 말캉이', 41020: '팝 그루브 말캉이', 41021: '팝 그루브 말캉이', 41022: '피자 냠냠 말캉이', 41023: '피자 냠냠 말캉이', 41024: '피자 냠냠 말캉이', 2001: '데마시아 짹짹이', 2002: '데마시아 짹짹이', 2003: '데마시아 짹짹이', 2016: '길 잃은 짹짹이', 2017: '길 잃은 짹짹이', 2018: '길 잃은 짹짹이', 2004: '눈꽃 버찌 짹짹이', 2005: '눈꽃 버찌 짹짹이', 2006: '눈꽃 버찌 짹짹이', 2013: '열대 짹짹이', 2014: '열대 짹짹이', 2015: '열대 짹짹이', 2010: '장미꽃 짹짹이', 2011: '장미꽃 짹짹이', 2012: '장미꽃 짹짹이', 2023: '바람의 짹짹이', 2024: '바람의 짹짹이', 2025: '바람의 짹짹이', 2026: '화염의 짹짹이', 2027: '화염의 짹짹이', 2028: '화염의 짹짹이', 2029: '바다의 짹짹이', 2030: '바다의 짹짹이', 2031: '바다의 짹짹이', 2032: '대지의 짹짹이', 2033: '대지의 짹짹이', 2034: '대지의 짹짹이', 2035: '장로 짹짹이', 2036: '장로 짹짹이', 2037: '장로 짹짹이', 2019: '별 수호자 짹짹이', 2020: '별 수호자 짹짹이', 2021: '별 수호자 짹짹이', 2022: '승리의 짹짹이', 2007: '새벽빛 짹짹이', 2008: '새벽빛 짹짹이', 2009: '새벽빛 짹짹이', 3016: '툰드라 뿔보', 3017: '툰드라 뿔보', 3018: '툰드라 뿔보', 3007: '나무껍질 뿔보', 3008: '나무껍질 뿔보', 3009: '나무껍질 뿔보', 3013: '아이스크림 콘 뿔보', 3014: '아이스크림 콘 뿔보', 3015: '아이스크림 콘 뿔보', 3020: 'K/DA ALL OUT 뿔보', 3021: 'K/DA ALL OUT 뿔보', 3022: 'K/DA ALL OUT 뿔보', 3023: 'K/DA POP/STARS 뿔보', 3024: 'K/DA POP/STARS 뿔보', 3025: 'K/DA POP/STARS 뿔보', 3026: '새해 야수 뿔보', 3027: '새해 야수 뿔보', 3028: '새해 야수 뿔보', 3029: '설맞이 축제 뿔보', 3030: '설맞이 축제 뿔보', 3031: '설맞이 축제 뿔보', 3010: '사자 기운 뿔보', 3011: '사자 기운 뿔보', 3012: '사자 기운 뿔보', 3001: '이글이글 뿔보', 3002: '이글이글 뿔보', 3003: '이글이글 뿔보', 3019: '승리의 뿔보', 3004: '공허에 물든 뿔보', 3005: '공허에 물든 뿔보', 3006: '공허에 물든 뿔보', 16010: '검은 안개 톡톡이', 16011: '검은 안개 톡톡이', 16012: '검은 안개 톡톡이', 16007: '화학공학 톡톡이', 16008: '화학공학 톡톡이', 16009: '화학공학 톡톡이', 16013: '군단 톡톡이', 16014: '군단 톡톡이', 16015: '군단 톡톡이', 16016: '꽃잎 무희 톡톡이', 16017: '꽃잎 무희 톡톡이', 16018: '꽃잎 무희 톡톡이', 16004: '페트리사이트 톡톡이', 16005: '페트리사이트 톡톡이', 16006: '페트리사이트 톡톡이', 16021: '별 수호자 톡톡이', 16022: '별 수호자 톡톡이', 16023: '별 수호자 톡톡이', 16001: '톡톡이', 16002: '톡톡이', 16003: '톡톡이', 16020: '환호의 톡톡이', 16019: '승리의 톡톡이', 43001: '뿜뿜이', 43002: '뿜뿜이', 43003: '뿜뿜이', 43004: '불혀 뿜뿜이', 43005: '불혀 뿜뿜이', 43006: '불혀 뿜뿜이', 43007: '아이스크림 콘 뿜뿜이', 43008: '아이스크림 콘 뿜뿜이', 43009: '아이스크림 콘 뿜뿜이', 43010: '멋쟁이 뿜뿜이', 43011: '멋쟁이 뿜뿜이', 43012: '멋쟁이 뿜뿜이', 43013: '빛나는 뿜뿜이', 43014: '빛나는 뿜뿜이', 43015: '빛나는 뿜뿜이', 43016: '프로젝트: 뿜뿜이', 43017: '프로젝트: 뿜뿜이', 43018: '프로젝트: 뿜뿜이', 55001: '투덜이', 55002: '투덜이', 55003: '투덜이', 55004: '슈퍼특공대 투덜이', 55005: '슈퍼특공대 투덜이', 55006: '슈퍼특공대 투덜이', 55007: '별 수호자 투덜이', 55008: '별 수호자 투덜이', 55009: '별 수호자 투덜이', 55010: '암흑의 별 투덜이', 55011: '암흑의 별 투덜이', 55012: '암흑의 별 투덜이', 55013: '신바람난 투덜이', 55014: '신바람난 투덜이', 55015: '신바람난 투덜이', 55016: '별의 숙적 투덜이', 55017: '별의 숙적 투덜이', 55018: '별의 숙적 투덜이', 4019: '우주비행사 두더지 광부', 4020: '우주비행사 두더지 광부', 4021: '우주비행사 두더지 광부', 4028: '혼돈의 두더지 광부', 4029: '혼돈의 두더지 광부', 4030: '혼돈의 두더지 광부', 4013: '덤벙대는 두더지 광부', 4014: '덤벙대는 두더지 광부', 4015: '덤벙대는 두더지 광부', 4010: '민물 두더지 광부', 4011: '민물 두더지 광부', 4012: '민물 두더지 광부', 4001: '말랑코 두더지 광부', 4002: '말랑코 두더지 광부', 4003: '말랑코 두더지 광부', 4025: '철갑의 두더지 광부', 4026: '철갑의 두더지 광부', 4027: '철갑의 두더지 광부', 4022: '질서의 두더지 광부', 4023: '질서의 두더지 광부', 4024: '질서의 두더지 광부', 4007: '하늘춤 두더지 광부', 4008: '하늘춤 두더지 광부', 4009: '하늘춤 두더지 광부', 4004: '불꽃 작렬 두더지 광부', 4005: '불꽃 작렬 두더지 광부', 4006: '불꽃 작렬 두더지 광부', 4016: '독성 줄줄 두더지 광부', 4017: '독성 줄줄 두더지 광부', 4018: '독성 줄줄 두더지 광부', 5010: '검은 안개 룬정령', 5011: '검은 안개 룬정령', 5012: '검은 안개 룬정령', 5001: '파수꾼 룬정령', 5002: '파수꾼 룬정령', 5003: '파수꾼 룬정령', 5013: '빙하 룬정령', 5014: '빙하 룬정령', 5015: '빙하 룬정령', 5004: '덩굴 룬정령', 5005: '덩굴 룬정령', 5006: '덩굴 룬정령', 5007: '묘목 룬정령', 5008: '묘목 룬정령', 5009: '묘목 룬정령', 5016: '벚꽃 룬정령', 5017: '벚꽃 룬정령', 5018: '벚꽃 룬정령', 5019: '생일 케이크정령', 31001: '날쌘발', 31002: '날쌘발', 31003: '날쌘발', 31004: '어둠의 인도자 날쌘발', 31005: '어둠의 인도자 날쌘발', 31006: '어둠의 인도자 날쌘발', 31007: '구원받은 자 날쌘발', 31008: '구원받은 자 날쌘발', 31009: '구원받은 자 날쌘발', 31010: '킨코우 날쌘발', 31011: '킨코우 날쌘발', 31012: '킨코우 날쌘발', 31013: '신록의 날쌘발', 31014: '신록의 날쌘발', 31015: '신록의 날쌘발', 31016: '망각의 날쌘발', 31017: '망각의 날쌘발', 31018: '망각의 날쌘발', 22016: '아케이드 번쩍이', 22017: '아케이드 번쩍이', 22018: '아케이드 번쩍이', 22013: '검은 안개 번쩍이', 22014: '검은 안개 번쩍이', 22015: '검은 안개 번쩍이', 22001: '번쩍이', 22002: '번쩍이', 22003: '번쩍이', 22004: '수정 번쩍이', 22005: '수정 번쩍이', 22006: '수정 번쩍이', 22010: '하이 눈 번쩍이', 22011: '하이 눈 번쩍이', 22012: '하이 눈 번쩍이', 22019: 'K/DA ALL OUT 번쩍이', 22020: 'K/DA ALL OUT 번쩍이', 22021: 'K/DA ALL OUT 번쩍이', 22022: 'K/DA POP/STARS 번쩍이', 22023: 'K/DA POP/STARS 번쩍이', 22024: 'K/DA POP/STARS 번쩍이', 22025: '스피드광 번쩍이', 22026: '스피드광 번쩍이', 22027: '스피드광 번쩍이', 22028: '마법공학 번쩍이', 22029: '마법공학 번쩍이', 22030: '마법공학 번쩍이', 22031: '펄스 건 번쩍이', 22032: '펄스 건 번쩍이', 22033: '펄스 건 번쩍이', 22034: '신바람난 번쩍이', 22035: '신바람난 번쩍이', 22036: '신바람난 번쩍이', 22037: '풍선껌 레이서 번쩍이', 22038: '풍선껌 레이서 번쩍이', 22039: '풍선껌 레이서 번쩍이', 22007: '아이스크림 콘 번쩍이', 22008: '아이스크림 콘 번쩍이', 22009: '아이스크림 콘 번쩍이', 6032: '혼돈의 펭구', 6033: '혼돈의 펭구', 6034: '혼돈의 펭구', 6001: '펭구 깃털기사', 6002: '펭구 깃털기사', 6003: '펭구 깃털기사', 6004: '까마귀 군주 깃털기사', 6005: '까마귀 군주 깃털기사', 6006: '까마귀 군주 깃털기사', 6038: 'e스포츠 펭구', 6007: '얼음 정수 깃털기사', 6008: '얼음 정수 깃털기사', 6009: '얼음 정수 깃털기사', 6025: 'K/DA ALL OUT 깃털기사', 6026: 'K/DA ALL OUT 깃털기사', 6027: 'K/DA ALL OUT 깃털기사', 6028: 'K/DA POP/STARS 깃털기사', 6029: 'K/DA POP/STARS 깃털기사', 6030: 'K/DA POP/STARS 깃털기사', 6054: '용 조련사 펭구', 6055: '용 조련사 펭구', 6056: '용 조련사 펭구', 6035: '질서의 펭구', 6036: '질서의 펭구', 6037: '질서의 펭구', 6016: '벚꽃 깃털기사', 6017: '벚꽃 깃털기사', 6018: '벚꽃 깃털기사', 6010: '불닭 깃털기사', 6011: '불닭 깃털기사', 6012: '불닭 깃털기사', 6031: '몰락한 펭구', 6019: '칸메이 깃털기사', 6020: '칸메이 깃털기사', 6021: '칸메이 깃털기사', 6022: '아카나 깃털기사', 6023: '아카나 깃털기사', 6024: '아카나 깃털기사', 6039: '검은불꽃 붓꼬리 깃털기사', 6040: '검은불꽃 붓꼬리 깃털기사', 6041: '검은불꽃 붓꼬리 깃털기사', 6042: '잉걸불 붓꼬리 깃털기사', 6043: '잉걸불 붓꼬리 깃털기사', 6044: '잉걸불 붓꼬리 깃털기사', 6045: '돌풍의 화신 붓꼬리 깃털기사', 6046: '돌풍의 화신 붓꼬리 깃털기사', 6047: '돌풍의 화신 붓꼬리 깃털기사', 6048: '대지 붓꼬리 깃털기사', 6049: '대지 붓꼬리 깃털기사', 6050: '대지 붓꼬리 깃털기사', 6051: '하늘빛 붓꼬리 깃털기사', 6052: '하늘빛 붓꼬리 깃털기사', 6053: '하늘빛 붓꼬리 깃털기사', 6013: '병아리 깃털기사', 6014: '병아리 깃털기사', 6015: '병아리 깃털기사', 40001: '요롱뇽', 40002: '요롱뇽', 40003: '요롱뇽', 40004: '꿀벌 요롱뇽', 40005: '꿀벌 요롱뇽', 40006: '꿀벌 요롱뇽', 40007: '빛나는 요롱뇽', 40008: '빛나는 요롱뇽', 40009: '빛나는 요롱뇽', 40010: '리오', 40011: '리오', 40012: '리오', 40013: '새콤달콤 요롱뇽', 40014: '새콤달콤 요롱뇽', 40015: '새콤달콤 요롱뇽', 40016: '마법공학 요롱뇽', 40017: '마법공학 요롱뇽', 40018: '마법공학 요롱뇽', 40019: '화학공학 요롱뇽', 40020: '화학공학 요롱뇽', 40021: '화학공학 요롱뇽', 40022: '물방울무늬 요롱뇽', 40023: '물방울무늬 요롱뇽', 40024: '물방울무늬 요롱뇽', 46001: '용멍이', 46002: '용멍이', 46003: '용멍이', 46004: '꿀벌 용멍이', 46005: '꿀벌 용멍이', 46006: '꿀벌 용멍이', 46007: '장미꽃 용멍이', 46008: '장미꽃 용멍이', 46009: '장미꽃 용멍이', 46010: '비취 용멍이', 46011: '비취 용멍이', 46012: '비취 용멍이', 46013: '별 용멍이', 46014: '별 용멍이', 46015: '별 용멍이', 46016: '사랑스러운 용멍이', 46017: '사랑스러운 용멍이', 46018: '사랑스러운 용멍이', 14016: '베이스 여왕 키키', 14017: '베이스 여왕 키키', 14018: '베이스 여왕 키키', 14010: '비트메이커 키키', 14011: '비트메이커 키키', 14012: '비트메이커 키키', 14004: '열정적인 키키', 14005: '열정적인 키키', 14006: '열정적인 키키', 14013: '천재 키키', 14014: '천재 키키', 14015: '천재 키키', 14019: '짜릿짜릿 키키', 14020: '짜릿짜릿 키키', 14021: '짜릿짜릿 키키', 14022: '신바람난 키키', 14023: '신바람난 키키', 14024: '신바람난 키키', 14025: '마법공학 키키', 14026: '마법공학 키키', 14027: '마법공학 키키', 14028: '아케이드 키키', 14029: '아케이드 키키', 14030: '아케이드 키키', 14031: '펄스 건 키키', 14032: '펄스 건 키키', 14033: '펄스 건 키키', 14001: '키키', 14002: '키키', 14003: '키키', 14007: '독주자 키키', 14008: '독주자 키키', 14009: '독주자 키키', 10004: '풍선껌 말랑이', 10005: '풍선껌 말랑이', 10006: '풍선껌 말랑이', 10001: '말랑이', 10002: '말랑이', 10003: '말랑이', 10007: '생강편 말랑이', 10008: '생강편 말랑이', 10009: '생강편 말랑이', 10010: '알사탕 말랑이', 10011: '알사탕 말랑이', 10012: '알사탕 말랑이', 10013: '상큼앵두 말랑이', 10014: '상큼앵두 말랑이', 10015: '상큼앵두 말랑이', 10019: '도자기 말랑이', 10020: '도자기 말랑이', 10021: '도자기 말랑이', 10022: '행운의 등불 말랑이', 10023: '행운의 등불 말랑이', 10024: '행운의 등불 말랑이', 10025: '불꽃놀이 말랑이', 10026: '불꽃놀이 말랑이', 10027: '불꽃놀이 말랑이', 10028: '사자춤 말랑이', 10029: '사자춤 말랑이', 10030: '사자춤 말랑이', 10031: '사나운 말랑이', 10032: '사나운 말랑이', 10033: '사나운 말랑이', 10016: '당분 과충전 말랑이', 10017: '당분 과충전 말랑이', 10018: '당분 과충전 말랑이', 11028: '혼돈의 꿀렁이', 11029: '혼돈의 꿀렁이', 11030: '혼돈의 꿀렁이', 11016: '샛별 꿀렁이', 11017: '샛별 꿀렁이', 11018: '샛별 꿀렁이', 11010: '그늘진 꿀렁이', 11011: '그늘진 꿀렁이', 11012: '그늘진 꿀렁이', 11013: '불꽃놀이 꿀렁이', 11014: '불꽃놀이 꿀렁이', 11015: '불꽃놀이 꿀렁이', 11001: '꿀렁이', 11002: '꿀렁이', 11003: '꿀렁이', 11004: '마지막 소원 꿀렁이', 11005: '마지막 소원 꿀렁이', 11006: '마지막 소원 꿀렁이', 11007: '사랑에 빠진 꿀렁이', 11008: '사랑에 빠진 꿀렁이', 11009: '사랑에 빠진 꿀렁이', 11019: '행운의 꿀렁이', 11020: '행운의 꿀렁이', 11021: '행운의 꿀렁이', 11025: '신록의 꿀렁이', 11026: '신록의 꿀렁이', 11027: '신록의 꿀렁이', 11022: '질서의 꿀렁이', 11023: '질서의 꿀렁이', 11024: '질서의 꿀렁이', 12016: '타락한 라라', 12017: '타락한 라라', 12018: '타락한 라라', 12025: '라라 박사', 12026: '라라 박사', 12027: '라라 박사', 12013: '불꽃놀이 라라', 12014: '불꽃놀이 라라', 12015: '불꽃놀이 라라', 12004: '용감무쌍 라라', 12005: '용감무쌍 라라', 12006: '용감무쌍 라라', 12007: '꼬맹이 라라', 12008: '꼬맹이 라라', 12009: '꼬맹이 라라', 12022: '새해 야수 라라', 12023: '새해 야수 라라', 12024: '새해 야수 라라', 12019: '설맞이 축제 라라', 12020: '설맞이 축제 라라', 12021: '설맞이 축제 라라', 12001: '라라', 12002: '라라', 12003: '라라', 12010: '햇살기운 라라', 12011: '햇살기운 라라', 12012: '햇살기운 라라', 15010: '비트메이커 멜리스마', 15011: '비트메이커 멜리스마', 15012: '비트메이커 멜리스마', 15004: '열정적인 멜리스마', 15005: '열정적인 멜리스마', 15006: '열정적인 멜리스마', 15025: '연꽃 무희 멜리스마', 15026: '연꽃 무희 멜리스마', 15027: '연꽃 무희 멜리스마', 15028: '축제의 불꽃 멜리스마', 15029: '축제의 불꽃 멜리스마', 15030: '축제의 불꽃 멜리스마', 15031: '도자기 멜리스마', 15032: '도자기 멜리스마', 15033: '도자기 멜리스마', 15034: '천상의 비취 멜리스마', 15035: '천상의 비취 멜리스마', 15036: '천상의 비취 멜리스마', 15037: '행운의 토끼 멜리스마', 15038: '행운의 토끼 멜리스마', 15039: '행운의 토끼 멜리스마', 15001: '멜리스마', 15002: '멜리스마', 15003: '멜리스마', 15007: '팝의 여왕 멜리스마', 15008: '팝의 여왕 멜리스마', 15009: '팝의 여왕 멜리스마', 15013: '천재 멜리스마', 15014: '천재 멜리스마', 15015: '천재 멜리스마', 15016: '그림자 비트 멜리스마', 15017: '그림자 비트 멜리스마', 15018: '그림자 비트 멜리스마', 15019: '칸메이 멜리스마', 15020: '칸메이 멜리스마', 15021: '칸메이 멜리스마', 15022: '아카나 멜리스마', 15023: '아카나 멜리스마', 15024: '아카나 멜리스마', 9016: '영원한 살랑꼬리', 9017: '영원한 살랑꼬리', 9018: '영원한 살랑꼬리', 9004: '요정 살랑꼬리', 9005: '요정 살랑꼬리', 9006: '요정 살랑꼬리', 9025: 'K/DA ALL OUT 살랑꼬리', 9026: 'K/DA ALL OUT 살랑꼬리', 9027: 'K/DA ALL OUT 살랑꼬리', 9028: 'K/DA POP/STARS 살랑꼬리', 9029: 'K/DA POP/STARS 살랑꼬리', 9030: 'K/DA POP/STARS 살랑꼬리', 9010: '이슬송이 살랑꼬리', 9011: '이슬송이 살랑꼬리', 9012: '이슬송이 살랑꼬리', 9007: '제왕 살랑꼬리', 9008: '제왕 살랑꼬리', 9009: '제왕 살랑꼬리', 9001: '달빛 살랑꼬리', 9002: '달빛 살랑꼬리', 9003: '달빛 살랑꼬리', 9019: '칸메이 살랑꼬리', 9020: '칸메이 살랑꼬리', 9021: '칸메이 살랑꼬리', 9022: '아카나 살랑꼬리', 9023: '아카나 살랑꼬리', 9024: '아카나 살랑꼬리', 9013: '야생 살랑꼬리', 9014: '야생 살랑꼬리', 9015: '야생 살랑꼬리', 15: '아케인 도깨비', 6: '혼돈의 도깨비', 1: '강도깨비', 17: '알 도깨비', 18: '사우나 도깨비', 5: '만두 도깨비', 14: '질서의 도깨비', 16: '식물 친구 도깨비', 4: '비취 황제 도깨비', 3: '별 수호자 도깨비', 19: '슈퍼특공대 도깨비', 2: 'UFO 도깨비', 8007: '화산호 첨벙둥이', 8008: '화산호 첨벙둥이', 8009: '화산호 첨벙둥이', 8004: '화려한 첨벙둥이', 8005: '화려한 첨벙둥이', 8006: '화려한 첨벙둥이', 8001: '비취 첨벙둥이', 8002: '비취 첨벙둥이', 8003: '비취 첨벙둥이', 8013: '장미꽃 첨벙둥이', 8014: '장미꽃 첨벙둥이', 8015: '장미꽃 첨벙둥이', 8019: '하늘빛 붓꼬리 첨벙둥이', 8020: '하늘빛 붓꼬리 첨벙둥이', 8021: '하늘빛 붓꼬리 첨벙둥이', 8022: '대지 붓꼬리 첨벙둥이', 8023: '대지 붓꼬리 첨벙둥이', 8024: '대지 붓꼬리 첨벙둥이', 8025: '잉걸불 붓꼬리 첨벙둥이', 8026: '잉걸불 붓꼬리 첨벙둥이', 8027: '잉걸불 붓꼬리 첨벙둥이', 8028: '검은불꽃 붓꼬리 첨벙둥이', 8029: '검은불꽃 붓꼬리 첨벙둥이', 8030: '검은불꽃 붓꼬리 첨벙둥이', 8031: '돌풍의 화신 붓꼬리 첨벙둥이', 8032: '돌풍의 화신 붓꼬리 첨벙둥이', 8033: '돌풍의 화신 붓꼬리 첨벙둥이', 8010: '파도샘 첨벙둥이', 8011: '파도샘 첨벙둥이', 8012: '파도샘 첨벙둥이', 8016: '성탄절 첨벙둥이', 8017: '성탄절 첨벙둥이', 8018: '성탄절 첨벙둥이', 26004: '검은 안개 크릉이', 26005: '검은 안개 크릉이', 26006: '검은 안개 크릉이', 26013: '핏빛달 크릉이', 26014: '핏빛달 크릉이', 26015: '핏빛달 크릉이', 26025: '혼돈의 크릉이', 26026: '혼돈의 크릉이', 26027: '혼돈의 크릉이', 26001: '크릉이', 26002: '크릉이', 26003: '크릉이', 26007: '새콤달콤 크릉이', 26008: '새콤달콤 크릉이', 26009: '새콤달콤 크릉이', 26016: '황금 크릉이', 26017: '황금 크릉이', 26018: '황금 크릉이', 26022: '용족 크릉이', 26023: '용족 크릉이', 26024: '용족 크릉이', 26019: '질서의 크릉이', 26020: '질서의 크릉이', 26021: '질서의 크릉이', 26028: '작은 상어 크릉이', 26029: '작은 상어 크릉이', 26030: '작은 상어 크릉이', 26031: '안전 요원 크릉이', 26032: '안전 요원 크릉이', 26033: '안전 요원 크릉이', 26034: '과일 스무디 크릉이', 26035: '과일 스무디 크릉이', 26036: '과일 스무디 크릉이', 26037: '구릿빛 크릉이', 26038: '구릿빛 크릉이', 26039: '구릿빛 크릉이', 26040: '스쿠버 상어 크릉이 ', 26041: '스쿠버 상어 크릉이 ', 26042: '스쿠버 상어 크릉이 ', 26010: '천둥괴물 크릉이', 26011: '천둥괴물 크릉이', 26012: '천둥괴물 크릉이'}
    return pet[name]

def pet_img(id):
    pet={13010: 'Tooltip_AkaliDragon_Beatmaker_Tier1.png', 13011: 'Tooltip_AkaliDragon_Beatmaker_Tier2.png', 13012: 'Tooltip_AkaliDragon_Beatmaker_Tier3.png', 13019: 'Tooltip_AkaliDragon_Set7LaunchBattlePass_Dragonmancer_Tier1.LL_AkaliDragon_Set7LaunchBattlePass.png', 13020: 'Tooltip_AkaliDragon_Set7LaunchBattlePass_Dragonmancer_Tier2.LL_AkaliDragon_Set7LaunchBattlePass.png', 13021: 'Tooltip_AkaliDragon_Set7LaunchBattlePass_Dragonmancer_Tier3.LL_AkaliDragon_Set7LaunchBattlePass.png', 13001: 'Tooltip_AkaliDragon_Ossia_Tier1.png', 13002: 'Tooltip_AkaliDragon_Ossia_Tier2.png', 13003: 'Tooltip_AkaliDragon_Ossia_Tier3.png', 13007: 'Tooltip_AkaliDragon_Popqueen_Tier1.png', 13008: 'Tooltip_AkaliDragon_Popqueen_Tier2.png', 13009: 'Tooltip_AkaliDragon_Popqueen_Tier3.png', 13013: 'Tooltip_AkaliDragon_Prodigy_Tier1.png', 13014: 'Tooltip_AkaliDragon_Prodigy_Tier2.png', 13015: 'Tooltip_AkaliDragon_Prodigy_Tier3.png', 13016: 'Tooltip_AkaliDragon_PumpedUp_Tier1.png', 13017: 'Tooltip_AkaliDragon_PumpedUp_Tier2.png', 13018: 'Tooltip_AkaliDragon_PumpedUp_Tier3.png', 13004: 'Tooltip_AkaliDragon_Soloist_Tier1.png', 13005: 'Tooltip_AkaliDragon_Soloist_Tier2.png', 13006: 'Tooltip_AkaliDragon_Soloist_Tier3.png', 25001: 'Tooltip_AoShin_Base_Classic_Tier1.png', 25002: 'Tooltip_AoShin_Base_Classic_Tier2.png', 25003: 'Tooltip_AoShin_Base_Classic_Tier3.png', 25010: 'Tooltip_AoShin_Base_DarkStar_Tier1.png', 25011: 'Tooltip_AoShin_Base_DarkStar_Tier2.png', 25012: 'Tooltip_AoShin_Base_DarkStar_Tier3.png', 25013: 'Tooltip_AoShin_Base_Divine_Tier1.png', 25014: 'Tooltip_AoShin_Base_Divine_Tier2.png', 25015: 'Tooltip_AoShin_Base_Divine_Tier3.png', 25004: 'Tooltip_AoShin_Base_Elder_Tier1.png', 25005: 'Tooltip_AoShin_Base_Elder_Tier2.png', 25006: 'Tooltip_AoShin_Base_Elder_Tier3.png', 25007: 'Tooltip_AoShin_Base_Firecracker_Tier1.png', 25008: 'Tooltip_AoShin_Base_Firecracker_Tier2.png', 25009: 'Tooltip_AoShin_Base_Firecracker_Tier3.png', 25019: 'Tooltip_AoShin_SpiritFairy_SpiritFairy1_Tier1.png', 25020: 'Tooltip_AoShin_SpiritFairy_SpiritFairy1_Tier2.png', 25021: 'Tooltip_AoShin_SpiritFairy_SpiritFairy1_Tier3.png', 25022: 'Tooltip_AoShin_SpiritFairy_SpiritFairy2_Tier1.png', 25023: 'Tooltip_AoShin_SpiritFairy_SpiritFairy2_Tier2.png', 25024: 'Tooltip_AoShin_SpiritFairy_SpiritFairy2_Tier3.png', 25025: 'Tooltip_AoShin_SpiritFairy_SpiritFairy3_Tier1.png', 25026: 'Tooltip_AoShin_SpiritFairy_SpiritFairy3_Tier2.png', 25027: 'Tooltip_AoShin_SpiritFairy_SpiritFairy3_Tier3.png', 25028: 'Tooltip_AoShin_SpiritFairy_SpiritFairy4_Tier1.png', 25029: 'Tooltip_AoShin_SpiritFairy_SpiritFairy4_Tier2.png', 25030: 'Tooltip_AoShin_SpiritFairy_SpiritFairy4_Tier3.png', 25031: 'Tooltip_AoShin_SpiritFairy_SpiritFairy5_Tier1.png', 25032: 'Tooltip_AoShin_SpiritFairy_SpiritFairy5_Tier2.png', 25033: 'Tooltip_AoShin_SpiritFairy_SpiritFairy5_Tier3.png', 25016: 'Tooltip_AoShin_Base_StarForger_Tier1.png', 25017: 'Tooltip_AoShin_Base_StarForger_Tier2.png', 25018: 'Tooltip_AoShin_Base_StarForger_Tier3.png', 25034: 'Tooltip_AoShin_PoolParty_Swimmer1_Tier1.LL_AoShin_PoolParty.png', 25035: 'Tooltip_AoShin_PoolParty_Swimmer1_Tier2.LL_AoShin_PoolParty.png', 25036: 'Tooltip_AoShin_PoolParty_Swimmer1_Tier3.LL_AoShin_PoolParty.png', 39001: 'Tooltip_BallDragon_Base_Classic_Tier1.LL_BallDragon_Base.png', 39002: 'Tooltip_BallDragon_Base_Classic_Tier2.LL_BallDragon_Base.png', 39003: 'Tooltip_BallDragon_Base_Classic_Tier3.LL_BallDragon_Base.png', 39019: 'Tooltip_BallDragon_LunarNewYear2023_Mythic_Tier1.LL_BallDragon_LunarNewYear2023.png', 39020: 'Tooltip_BallDragon_LunarNewYear2023_Mythic_Tier2.LL_BallDragon_LunarNewYear2023.png', 39021: 'Tooltip_BallDragon_LunarNewYear2023_Mythic_Tier3.LL_BallDragon_LunarNewYear2023.png', 39004: 'Tooltip_BallDragon_Base_Variant1_Tier1.LL_BallDragon_Base.png', 39005: 'Tooltip_BallDragon_Base_Variant1_Tier2.LL_BallDragon_Base.png', 39006: 'Tooltip_BallDragon_Base_Variant1_Tier3.LL_BallDragon_Base.png', 39007: 'Tooltip_BallDragon_Base_Variant2_Tier1.LL_BallDragon_Base.png', 39008: 'Tooltip_BallDragon_Base_Variant2_Tier2.LL_BallDragon_Base.png', 39009: 'Tooltip_BallDragon_Base_Variant2_Tier3.LL_BallDragon_Base.png', 39010: 'Tooltip_BallDragon_Base_Variant3_Tier1.LL_BallDragon_Base.png', 39011: 'Tooltip_BallDragon_Base_Variant3_Tier2.LL_BallDragon_Base.png', 39012: 'Tooltip_BallDragon_Base_Variant3_Tier3.LL_BallDragon_Base.png', 39013: 'Tooltip_BallDragon_Base_Variant4_Tier1.LL_BallDragon_Base.png', 39014: 'Tooltip_BallDragon_Base_Variant4_Tier2.LL_BallDragon_Base.png', 39015: 'Tooltip_BallDragon_Base_Variant4_Tier3.LL_BallDragon_Base.png', 39016: 'Tooltip_BallDragon_Base_Variant5_Tier1.LL_BallDragon_Base.png', 39017: 'Tooltip_BallDragon_Base_Variant5_Tier2.LL_BallDragon_Base.png', 39018: 'Tooltip_BallDragon_Base_Variant5_Tier3.LL_BallDragon_Base.png', 51003: 'Tooltip_Baron_Base_Classic_Tier3.LL_Baron_Base.png', 51006: 'Tooltip_Baron_Base_Variant1_Tier3.LL_Baron_Base.png', 51009: 'Tooltip_Baron_Base_Variant2_Tier3.LL_Baron_Base.png', 51012: 'Tooltip_Baron_Base_Variant3_Tier3.LL_Baron_Base.png', 51015: 'Tooltip_Baron_Base_Variant4_Tier3.LL_Baron_Base.png', 51018: 'Tooltip_Baron_Base_Variant5_Tier3.LL_Baron_Base.png', 24013: 'Tooltip_Bellswayer_BlackMist_Tier1.png', 24014: 'Tooltip_Bellswayer_BlackMist_Tier2.png', 24015: 'Tooltip_Bellswayer_BlackMist_Tier3.png', 24016: 'Tooltip_Bellswayer_BloodMoon_Tier1.png', 24017: 'Tooltip_Bellswayer_BloodMoon_Tier2.png', 24018: 'Tooltip_Bellswayer_BloodMoon_Tier3.png', 24001: 'Tooltip_Bellswayer_Classic_Tier1.png', 24002: 'Tooltip_Bellswayer_Classic_Tier2.png', 24003: 'Tooltip_Bellswayer_Classic_Tier3.png', 24019: 'Tooltip_Bellswayer_Set4UpdateBattlePass_LunarRevel2021_Tier1.png', 24020: 'Tooltip_Bellswayer_Set4UpdateBattlePass_LunarRevel2021_Tier2.png', 24021: 'Tooltip_Bellswayer_Set4UpdateBattlePass_LunarRevel2021_Tier3.png', 24007: 'Tooltip_Bellswayer_SugarRush_Tier1.png', 24008: 'Tooltip_Bellswayer_SugarRush_Tier2.png', 24009: 'Tooltip_Bellswayer_SugarRush_Tier3.png', 24004: 'Tooltip_Bellswayer_Thunderstorm_Tier1.png', 24005: 'Tooltip_Bellswayer_Thunderstorm_Tier2.png', 24006: 'Tooltip_Bellswayer_Thunderstorm_Tier3.png', 24010: 'Tooltip_Bellswayer_Yuletide_Tier1.png', 24011: 'Tooltip_Bellswayer_Yuletide_Tier2.png', 24012: 'Tooltip_Bellswayer_Yuletide_Tier3.png', 17016: 'Tooltip_Buglet_Beevil_Tier1.png', 17017: 'Tooltip_Buglet_Beevil_Tier2.png', 17018: 'Tooltip_Buglet_Beevil_Tier3.png', 17001: 'Tooltip_Buglet_Flutterbug_Tier1.png', 17002: 'Tooltip_Buglet_Flutterbug_Tier2.png', 17003: 'Tooltip_Buglet_Flutterbug_Tier3.png', 17013: 'Tooltip_Buglet_Ixtali_Tier1.png', 17014: 'Tooltip_Buglet_Ixtali_Tier2.png', 17015: 'Tooltip_Buglet_Ixtali_Tier3.png', 17010: 'Tooltip_Buglet_Legionnaire_Tier1.png', 17011: 'Tooltip_Buglet_Legionnaire_Tier2.png', 17012: 'Tooltip_Buglet_Legionnaire_Tier3.png', 17007: 'Tooltip_Buglet_Sandbringer_Tier1.png', 17008: 'Tooltip_Buglet_Sandbringer_Tier2.png', 17009: 'Tooltip_Buglet_Sandbringer_Tier3.png', 17019: 'Tooltip_Buglet_Sentinel_Sentinel1_Tier1.png', 17004: 'Tooltip_Buglet_TrueIce_Tier1.png', 17005: 'Tooltip_Buglet_TrueIce_Tier2.png', 17006: 'Tooltip_Buglet_TrueIce_Tier3.png', 17020: 'Tooltip_Buglet_Anniversary_Variant1_Tier1.LL_Buglet_Anniversary.png', 52001: 'Tooltip_Bunny_Base_Classic_Tier1.LL_Bunny_Base.png', 52002: 'Tooltip_Bunny_Base_Classic_Tier2.LL_Bunny_Base.png', 52003: 'Tooltip_Bunny_Base_Classic_Tier3.LL_Bunny_Base.png', 52019: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel1_Tier1.LL_Bunny_LunarNewYear2023.png', 52020: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel1_Tier2.LL_Bunny_LunarNewYear2023.png', 52021: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel1_Tier3.LL_Bunny_LunarNewYear2023.png', 52022: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel2_Tier1.LL_Bunny_LunarNewYear2023.png', 52023: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel2_Tier2.LL_Bunny_LunarNewYear2023.png', 52024: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel2_Tier3.LL_Bunny_LunarNewYear2023.png', 52025: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel3_Tier1.LL_Bunny_LunarNewYear2023.png', 52026: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel3_Tier2.LL_Bunny_LunarNewYear2023.png', 52027: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel3_Tier3.LL_Bunny_LunarNewYear2023.png', 52028: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel4_Tier1.LL_Bunny_LunarNewYear2023.png', 52029: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel4_Tier2.LL_Bunny_LunarNewYear2023.png', 52030: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel4_Tier3.LL_Bunny_LunarNewYear2023.png', 52031: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel5_Tier1.LL_Bunny_LunarNewYear2023.png', 52032: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel5_Tier2.LL_Bunny_LunarNewYear2023.png', 52033: 'Tooltip_Bunny_LunarNewYear2023_LunarRevel5_Tier3.LL_Bunny_LunarNewYear2023.png', 52004: 'Tooltip_Bunny_Base_Variant1_Tier1.LL_Bunny_Base.png', 52005: 'Tooltip_Bunny_Base_Variant1_Tier2.LL_Bunny_Base.png', 52006: 'Tooltip_Bunny_Base_Variant1_Tier3.LL_Bunny_Base.png', 52007: 'Tooltip_Bunny_Base_Variant2_Tier1.LL_Bunny_Base.png', 52008: 'Tooltip_Bunny_Base_Variant2_Tier2.LL_Bunny_Base.png', 52009: 'Tooltip_Bunny_Base_Variant2_Tier3.LL_Bunny_Base.png', 52010: 'Tooltip_Bunny_Base_Variant3_Tier1.LL_Bunny_Base.png', 52011: 'Tooltip_Bunny_Base_Variant3_Tier2.LL_Bunny_Base.png', 52012: 'Tooltip_Bunny_Base_Variant3_Tier3.LL_Bunny_Base.png', 52013: 'Tooltip_Bunny_Base_Variant4_Tier1.LL_Bunny_Base.png', 52014: 'Tooltip_Bunny_Base_Variant4_Tier2.LL_Bunny_Base.png', 52015: 'Tooltip_Bunny_Base_Variant4_Tier3.LL_Bunny_Base.png', 52016: 'Tooltip_Bunny_Base_Variant5_Tier1.LL_Bunny_Base.png', 52017: 'Tooltip_Bunny_Base_Variant5_Tier2.LL_Bunny_Base.png', 52018: 'Tooltip_Bunny_Base_Variant5_Tier3.LL_Bunny_Base.png', 54001: 'Tooltip_ChibiAnnie_Base_Classic_Tier1.CHIBI_Annie_Base.png', 54002: 'Tooltip_ChibiAnnie_LunarNewYear2023_Panda_Tier1.CHIBI_Annie_LunarNewYear2023.png', 48001: 'Tooltip_ChibiAshe_Base_Classic_Tier1.CHIBI_Ashe_Base.png', 48002: 'Tooltip_ChibiAshe_Dragonmancer_Dragonmancer1_Tier1.CHIBI_Ashe_Dragonmancer.png', 34001: 'Tooltip_ChibiEkko_Base_Classic_Tier1.png', 35001: 'Tooltip_ChibiJinx_Base_Classic_Tier1.png', 35002: 'Tooltip_ChibiJinx_Firecracker_Firecracker1_Tier1.png', 45001: 'Tooltip_ChibiKaisa_Base_Classic_Tier1.CHIBI_Kaisa_Base.png', 45002: 'Tooltip_ChibiKaisa_Dragonmancer_Dragonmancer1_Tier1.CHIBI_Kaisa_Dragonmancer.png', 44001: 'Tooltip_ChibiLeeSin_Base_Classic_Tier1.CHIBI_LeeSin_Base.png', 44002: 'Tooltip_ChibiLeeSin_Dragonmancer_Dragonmancer1_Tier1.CHIBI_LeeSin_Dragonmancer.png', 50001: 'Tooltip_ChibiLux_Base_Classic_Tier1.CHIBI_Lux_Base.png', 50002: 'Tooltip_ChibiLux_StarGuardian_StarGuardian1_Tier1.CHIBI_Lux_StarGuardian.png', 37001: 'Tooltip_ChibiVi_Base_Classic_Tier1.png', 38001: 'Tooltip_ChibiYasuo_Base_Classic_Tier1.CHIBI_Yasuo_Base.png', 38002: 'Tooltip_ChibiYasuo_Dragonmancer_Dragonmancer1_Tier1.CHIBI_Yasuo_Dragonmancer.png', 27004: 'Tooltip_Choncc_Atlantean_Tier1.png', 27005: 'Tooltip_Choncc_Atlantean_Tier2.png', 27006: 'Tooltip_Choncc_Atlantean_Tier3.png', 27001: 'Tooltip_Choncc_Classic_Tier1.png', 27002: 'Tooltip_Choncc_Classic_Tier2.png', 27003: 'Tooltip_Choncc_Classic_Tier3.png', 27007: 'Tooltip_Choncc_EarthTitan_Tier1.png', 27008: 'Tooltip_Choncc_EarthTitan_Tier2.png', 27009: 'Tooltip_Choncc_EarthTitan_Tier3.png', 27010: 'Tooltip_Choncc_Fireborn_Tier1.png', 27011: 'Tooltip_Choncc_Fireborn_Tier2.png', 27012: 'Tooltip_Choncc_Fireborn_Tier3.png', 27016: 'Tooltip_Choncc_Honeybuzz_Tier1.png', 27017: 'Tooltip_Choncc_Honeybuzz_Tier2.png', 27018: 'Tooltip_Choncc_Honeybuzz_Tier3.png', 27022: 'Tooltip_Choncc_Set4Update_LunarBeast_Tier1.png', 27023: 'Tooltip_Choncc_Set4Update_LunarBeast_Tier2.png', 27024: 'Tooltip_Choncc_Set4Update_LunarBeast_Tier3.png', 27019: 'Tooltip_Choncc_Set4Update_LunarRevel2021_Tier1.png', 27020: 'Tooltip_Choncc_Set4Update_LunarRevel2021_Tier2.png', 27021: 'Tooltip_Choncc_Set4Update_LunarRevel2021_Tier3.png', 27034: 'Tooltip_Choncc_Dragon_Mythic_Tier1.LL_Set7LaunchBattlePass_Chroncc.png', 27035: 'Tooltip_Choncc_Dragon_Mythic_Tier2.LL_Set7LaunchBattlePass_Chroncc.png', 27036: 'Tooltip_Choncc_Dragon_Mythic_Tier3.LL_Set7LaunchBattlePass_Chroncc.png', 27013: 'Tooltip_Choncc_PreciousPanda_Tier1.png', 27014: 'Tooltip_Choncc_PreciousPanda_Tier2.png', 27015: 'Tooltip_Choncc_PreciousPanda_Tier3.png', 27025: 'Tooltip_Choncc_PoolParty_Swimmer1_Tier1.png', 27026: 'Tooltip_Choncc_PoolParty_Swimmer1_Tier2.png', 27027: 'Tooltip_Choncc_PoolParty_Swimmer1_Tier3.png', 27028: 'Tooltip_Choncc_PoolParty_Swimmer2_Tier1.png', 27029: 'Tooltip_Choncc_PoolParty_Swimmer2_Tier2.png', 27030: 'Tooltip_Choncc_PoolParty_Swimmer2_Tier3.png', 27031: 'Tooltip_Choncc_PoolParty_Swimmer3_Tier1.png', 27032: 'Tooltip_Choncc_PoolParty_Swimmer3_Tier2.png', 27033: 'Tooltip_Choncc_PoolParty_Swimmer3_Tier3.png', 53001: 'Tooltip_CreepyCat_Base_Classic_Tier1.LL_CreepyCat_Base.png', 53002: 'Tooltip_CreepyCat_Base_Classic_Tier2.LL_CreepyCat_Base.png', 53003: 'Tooltip_CreepyCat_Base_Classic_Tier3.LL_CreepyCat_Base.png', 53004: 'Tooltip_CreepyCat_Base_Variant1_Tier1.LL_CreepyCat_Base.png', 53005: 'Tooltip_CreepyCat_Base_Variant1_Tier2.LL_CreepyCat_Base.png', 53006: 'Tooltip_CreepyCat_Base_Variant1_Tier3.LL_CreepyCat_Base.png', 53007: 'Tooltip_CreepyCat_Base_Variant2_Tier1.LL_CreepyCat_Base.png', 53008: 'Tooltip_CreepyCat_Base_Variant2_Tier2.LL_CreepyCat_Base.png', 53009: 'Tooltip_CreepyCat_Base_Variant2_Tier3.LL_CreepyCat_Base.png', 53010: 'Tooltip_CreepyCat_Base_Variant3_Tier1.LL_CreepyCat_Base.png', 53011: 'Tooltip_CreepyCat_Base_Variant3_Tier2.LL_CreepyCat_Base.png', 53012: 'Tooltip_CreepyCat_Base_Variant3_Tier3.LL_CreepyCat_Base.png', 53013: 'Tooltip_CreepyCat_Base_Variant4_Tier1.LL_CreepyCat_Base.png', 53014: 'Tooltip_CreepyCat_Base_Variant4_Tier2.LL_CreepyCat_Base.png', 53015: 'Tooltip_CreepyCat_Base_Variant4_Tier3.LL_CreepyCat_Base.png', 53016: 'Tooltip_CreepyCat_Base_Variant5_Tier1.LL_CreepyCat_Base.png', 53017: 'Tooltip_CreepyCat_Base_Variant5_Tier2.LL_CreepyCat_Base.png', 53018: 'Tooltip_CreepyCat_Base_Variant5_Tier3.LL_CreepyCat_Base.png', 19016: 'Tooltip_DSSquid_Base_Cosmic_Tier1.png', 19017: 'Tooltip_DSSquid_Base_Cosmic_Tier2.png', 19018: 'Tooltip_DSSquid_Base_Cosmic_Tier3.png', 19007: 'Tooltip_DSSquid_Base_Dreadnova_Tier1.png', 19008: 'Tooltip_DSSquid_Base_Dreadnova_Tier2.png', 19009: 'Tooltip_DSSquid_Base_Dreadnova_Tier3.png', 19010: 'Tooltip_DSSquid_Base_Fruitytooty_Tier1.png', 19011: 'Tooltip_DSSquid_Base_Fruitytooty_Tier2.png', 19012: 'Tooltip_DSSquid_Base_Fruitytooty_Tier3.png', 19019: 'Tooltip_DSSquid_KDAEvelynn_KDA1_Tier1.png', 19020: 'Tooltip_DSSquid_KDAEvelynn_KDA1_Tier2.png', 19021: 'Tooltip_DSSquid_KDAEvelynn_KDA1_Tier3.png', 19022: 'Tooltip_DSSquid_KDAEvelynn_KDA2_Tier1.png', 19023: 'Tooltip_DSSquid_KDAEvelynn_KDA2_Tier2.png', 19024: 'Tooltip_DSSquid_KDAEvelynn_KDA2_Tier3.png', 19004: 'Tooltip_DSSquid_Base_Odyssey_Tier1.png', 19005: 'Tooltip_DSSquid_Base_Odyssey_Tier2.png', 19006: 'Tooltip_DSSquid_Base_Odyssey_Tier3.png', 19001: 'Tooltip_DSSquid_Base_Squink_Tier1.png', 19002: 'Tooltip_DSSquid_Base_Squink_Tier2.png', 19003: 'Tooltip_DSSquid_Base_Squink_Tier3.png', 19013: 'Tooltip_DSSquid_Base_Sugarcone_Tier1.png', 19014: 'Tooltip_DSSquid_Base_Sugarcone_Tier2.png', 19015: 'Tooltip_DSSquid_Base_Sugarcone_Tier3.png', 19025: 'Tooltip_DSSquid_HighNoon_Variant1_Tier1.png', 19026: 'Tooltip_DSSquid_HighNoon_Variant1_Tier2.png', 19027: 'Tooltip_DSSquid_HighNoon_Variant1_Tier3.png', 19028: 'Tooltip_DSSquid_HighNoon_Variant2_Tier1.png', 19029: 'Tooltip_DSSquid_HighNoon_Variant2_Tier2.png', 19030: 'Tooltip_DSSquid_HighNoon_Variant2_Tier3.png', 19031: 'Tooltip_DSSquid_HighNoon_Variant3_Tier1.png', 19032: 'Tooltip_DSSquid_HighNoon_Variant3_Tier2.png', 19033: 'Tooltip_DSSquid_HighNoon_Variant3_Tier3.png', 19034: 'Tooltip_DSSquid_HighNoon_Variant4_Tier1.png', 19035: 'Tooltip_DSSquid_HighNoon_Variant4_Tier2.png', 19036: 'Tooltip_DSSquid_HighNoon_Variant4_Tier3.png', 19037: 'Tooltip_DSSquid_HighNoon_Variant5_Tier1.png', 19038: 'Tooltip_DSSquid_HighNoon_Variant5_Tier2.png', 19039: 'Tooltip_DSSquid_HighNoon_Variant5_Tier3.png', 20001: 'Tooltip_DSSwordGuy_Abyssia_Tier1.png', 20002: 'Tooltip_DSSwordGuy_Abyssia_Tier2.png', 20003: 'Tooltip_DSSwordGuy_Abyssia_Tier3.png', 20013: 'Tooltip_DSSwordGuy_Calcite_Tier1.png', 20014: 'Tooltip_DSSwordGuy_Calcite_Tier2.png', 20015: 'Tooltip_DSSwordGuy_Calcite_Tier3.png', 20016: 'Tooltip_DSSwordGuy_Cosmic_Tier1.png', 20017: 'Tooltip_DSSwordGuy_Cosmic_Tier2.png', 20018: 'Tooltip_DSSwordGuy_Cosmic_Tier3.png', 20019: 'Tooltip_DSSwordGuy_Project_Cybernetic_Tier1.png', 20020: 'Tooltip_DSSwordGuy_Project_Cybernetic_Tier2.png', 20021: 'Tooltip_DSSwordGuy_Project_Cybernetic_Tier3.png', 20004: 'Tooltip_DSSwordGuy_Darkin_Tier1.png', 20005: 'Tooltip_DSSwordGuy_Darkin_Tier2.png', 20006: 'Tooltip_DSSwordGuy_Darkin_Tier3.png', 20007: 'Tooltip_DSSwordGuy_GalaxySlayer_Tier1.png', 20008: 'Tooltip_DSSwordGuy_GalaxySlayer_Tier2.png', 20009: 'Tooltip_DSSwordGuy_GalaxySlayer_Tier3.png', 20010: 'Tooltip_DSSwordGuy_Willowbark_Tier1.png', 20011: 'Tooltip_DSSwordGuy_Willowbark_Tier2.png', 20012: 'Tooltip_DSSwordGuy_Willowbark_Tier3.png', 21016: 'Tooltip_DSWhale_Cosmic_Tier1.png', 21017: 'Tooltip_DSWhale_Cosmic_Tier2.png', 21018: 'Tooltip_DSWhale_Cosmic_Tier3.png', 21004: 'Tooltip_DSWhale_Dreadnova_Tier1.png', 21005: 'Tooltip_DSWhale_Dreadnova_Tier2.png', 21006: 'Tooltip_DSWhale_Dreadnova_Tier3.png', 21007: 'Tooltip_DSWhale_GalaxySlayer_Tier1.png', 21008: 'Tooltip_DSWhale_GalaxySlayer_Tier2.png', 21009: 'Tooltip_DSWhale_GalaxySlayer_Tier3.png', 21010: 'Tooltip_DSWhale_Goo_Tier1.png', 21011: 'Tooltip_DSWhale_Goo_Tier2.png', 21012: 'Tooltip_DSWhale_Goo_Tier3.png', 21019: 'Tooltip_DSWhale_Koi_Koi_Tier1.LL_DSWhale_Koi.png', 21020: 'Tooltip_DSWhale_Koi_Koi_Tier2.LL_DSWhale_Koi.png', 21021: 'Tooltip_DSWhale_Koi_Koi_Tier3.LL_DSWhale_Koi.png', 21013: 'Tooltip_DSWhale_Orcus_Tier1.png', 21014: 'Tooltip_DSWhale_Orcus_Tier2.png', 21015: 'Tooltip_DSWhale_Orcus_Tier3.png', 21001: 'Tooltip_DSWhale_Starmaw_Tier1.png', 21002: 'Tooltip_DSWhale_Starmaw_Tier2.png', 21003: 'Tooltip_DSWhale_Starmaw_Tier3.png', 29001: 'Tooltip_Dowsie_Base_Classic_Tier1.png', 29002: 'Tooltip_Dowsie_Base_Classic_Tier2.png', 29003: 'Tooltip_Dowsie_Base_Classic_Tier3.png', 29022: 'Tooltip_Dowsie_LunarNewYear_LunarRevel1_Tier1.png', 29023: 'Tooltip_Dowsie_LunarNewYear_LunarRevel1_Tier2.png', 29024: 'Tooltip_Dowsie_LunarNewYear_LunarRevel1_Tier3.png', 29025: 'Tooltip_Dowsie_LunarNewYear_LunarRevel2_Tier1.png', 29026: 'Tooltip_Dowsie_LunarNewYear_LunarRevel2_Tier2.png', 29027: 'Tooltip_Dowsie_LunarNewYear_LunarRevel2_Tier3.png', 29028: 'Tooltip_Dowsie_LunarNewYear_LunarRevel3_Tier1.png', 29029: 'Tooltip_Dowsie_LunarNewYear_LunarRevel3_Tier2.png', 29030: 'Tooltip_Dowsie_LunarNewYear_LunarRevel3_Tier3.png', 29031: 'Tooltip_Dowsie_LunarNewYear_LunarRevel4_Tier1.png', 29032: 'Tooltip_Dowsie_LunarNewYear_LunarRevel4_Tier2.png', 29033: 'Tooltip_Dowsie_LunarNewYear_LunarRevel4_Tier3.png', 29034: 'Tooltip_Dowsie_LunarNewYear_LunarRevel5_Tier1.png', 29035: 'Tooltip_Dowsie_LunarNewYear_LunarRevel5_Tier2.png', 29036: 'Tooltip_Dowsie_LunarNewYear_LunarRevel5_Tier3.png', 29019: 'Tooltip_Dowsie_URF_Seal_Tier1.png', 29020: 'Tooltip_Dowsie_URF_Seal_Tier2.png', 29021: 'Tooltip_Dowsie_URF_Seal_Tier3.png', 29004: 'Tooltip_Dowsie_Base_Variant1_Tier1.png', 29005: 'Tooltip_Dowsie_Base_Variant1_Tier2.png', 29006: 'Tooltip_Dowsie_Base_Variant1_Tier3.png', 29007: 'Tooltip_Dowsie_Base_Variant2_Tier1.png', 29008: 'Tooltip_Dowsie_Base_Variant2_Tier2.png', 29009: 'Tooltip_Dowsie_Base_Variant2_Tier3.png', 29010: 'Tooltip_Dowsie_Base_Variant3_Tier1.png', 29011: 'Tooltip_Dowsie_Base_Variant3_Tier2.png', 29012: 'Tooltip_Dowsie_Base_Variant3_Tier3.png', 29013: 'Tooltip_Dowsie_Base_Variant4_Tier1.png', 29014: 'Tooltip_Dowsie_Base_Variant4_Tier2.png', 29015: 'Tooltip_Dowsie_Base_Variant4_Tier3.png', 29016: 'Tooltip_Dowsie_Base_Variant5_Tier1.png', 29017: 'Tooltip_Dowsie_Base_Variant5_Tier2.png', 29018: 'Tooltip_Dowsie_Base_Variant5_Tier3.png', 42001: 'Tooltip_Duckbill_Base_Classic_Tier1.png', 42002: 'Tooltip_Duckbill_Base_Classic_Tier2.png', 42003: 'Tooltip_Duckbill_Base_Classic_Tier3.png', 42025: 'Tooltip_Duckbill_LunarNewYear_LunarRevel1_Tier1.png', 42026: 'Tooltip_Duckbill_LunarNewYear_LunarRevel1_Tier2.png', 42027: 'Tooltip_Duckbill_LunarNewYear_LunarRevel1_Tier3.png', 42028: 'Tooltip_Duckbill_LunarNewYear_LunarRevel2_Tier1.png', 42029: 'Tooltip_Duckbill_LunarNewYear_LunarRevel2_Tier2.png', 42030: 'Tooltip_Duckbill_LunarNewYear_LunarRevel2_Tier3.png', 42031: 'Tooltip_Duckbill_LunarNewYear_LunarRevel3_Tier1.png', 42032: 'Tooltip_Duckbill_LunarNewYear_LunarRevel3_Tier2.png', 42033: 'Tooltip_Duckbill_LunarNewYear_LunarRevel3_Tier3.png', 42034: 'Tooltip_Duckbill_LunarNewYear_LunarRevel4_Tier1.png', 42035: 'Tooltip_Duckbill_LunarNewYear_LunarRevel4_Tier2.png', 42036: 'Tooltip_Duckbill_LunarNewYear_LunarRevel4_Tier3.png', 42037: 'Tooltip_Duckbill_LunarNewYear_LunarRevel5_Tier1.png', 42038: 'Tooltip_Duckbill_LunarNewYear_LunarRevel5_Tier2.png', 42039: 'Tooltip_Duckbill_LunarNewYear_LunarRevel5_Tier3.png', 42004: 'Tooltip_Duckbill_Base_Variant1_Tier1.png', 42005: 'Tooltip_Duckbill_Base_Variant1_Tier2.png', 42006: 'Tooltip_Duckbill_Base_Variant1_Tier3.png', 42007: 'Tooltip_Duckbill_Base_Variant2_Tier1.png', 42008: 'Tooltip_Duckbill_Base_Variant2_Tier2.png', 42009: 'Tooltip_Duckbill_Base_Variant2_Tier3.png', 42010: 'Tooltip_Duckbill_Base_Variant3_Tier1.png', 42011: 'Tooltip_Duckbill_Base_Variant3_Tier2.png', 42012: 'Tooltip_Duckbill_Base_Variant3_Tier3.png', 42013: 'Tooltip_Duckbill_Base_Variant4_Tier1.png', 42014: 'Tooltip_Duckbill_Base_Variant4_Tier2.png', 42015: 'Tooltip_Duckbill_Base_Variant4_Tier3.png', 42016: 'Tooltip_Duckbill_Base_Variant5_Tier1.png', 42017: 'Tooltip_Duckbill_Base_Variant5_Tier2.png', 42018: 'Tooltip_Duckbill_Base_Variant5_Tier3.png', 42019: 'Tooltip_Duckbill_Base_Variant6_Tier1.png', 42020: 'Tooltip_Duckbill_Base_Variant6_Tier2.png', 42021: 'Tooltip_Duckbill_Base_Variant6_Tier3.png', 42022: 'Tooltip_Duckbill_Base_Variant7_Tier1.png', 42023: 'Tooltip_Duckbill_Base_Variant7_Tier2.png', 42024: 'Tooltip_Duckbill_Base_Variant7_Tier3.png', 47001: 'Tooltip_ElegantDragon_Base_Classic_Tier1.LL_ElegantDragon_Base.png', 47002: 'Tooltip_ElegantDragon_Base_Classic_Tier2.LL_ElegantDragon_Base.png', 47003: 'Tooltip_ElegantDragon_Base_Classic_Tier3.LL_ElegantDragon_Base.png', 47004: 'Tooltip_ElegantDragon_Base_Variant1_Tier1.LL_ElegantDragon_Base.png', 47005: 'Tooltip_ElegantDragon_Base_Variant1_Tier2.LL_ElegantDragon_Base.png', 47006: 'Tooltip_ElegantDragon_Base_Variant1_Tier3.LL_ElegantDragon_Base.png', 47007: 'Tooltip_ElegantDragon_Base_Variant2_Tier1.LL_ElegantDragon_Base.png', 47008: 'Tooltip_ElegantDragon_Base_Variant2_Tier2.LL_ElegantDragon_Base.png', 47009: 'Tooltip_ElegantDragon_Base_Variant2_Tier3.LL_ElegantDragon_Base.png', 47010: 'Tooltip_ElegantDragon_Base_Variant3_Tier1.LL_ElegantDragon_Base.png', 47011: 'Tooltip_ElegantDragon_Base_Variant3_Tier2.LL_ElegantDragon_Base.png', 47012: 'Tooltip_ElegantDragon_Base_Variant3_Tier3.LL_ElegantDragon_Base.png', 47013: 'Tooltip_ElegantDragon_Base_Variant4_Tier1.LL_ElegantDragon_Base.png', 47014: 'Tooltip_ElegantDragon_Base_Variant4_Tier2.LL_ElegantDragon_Base.png', 47015: 'Tooltip_ElegantDragon_Base_Variant4_Tier3.LL_ElegantDragon_Base.png', 47016: 'Tooltip_ElegantDragon_Base_Variant5_Tier1.LL_ElegantDragon_Base.png', 47017: 'Tooltip_ElegantDragon_Base_Variant5_Tier2.LL_ElegantDragon_Base.png', 47018: 'Tooltip_ElegantDragon_Base_Variant5_Tier3.LL_ElegantDragon_Base.png', 23016: 'Tooltip_Fairy_Base_Chameleon_Tier1.png', 23017: 'Tooltip_Fairy_Base_Chameleon_Tier2.png', 23018: 'Tooltip_Fairy_Base_Chameleon_Tier3.png', 23001: 'Tooltip_Fairy_Base_Classic_Tier1.png', 23002: 'Tooltip_Fairy_Base_Classic_Tier2.png', 23003: 'Tooltip_Fairy_Base_Classic_Tier3.png', 23013: 'Tooltip_Fairy_Base_ExtraSpicy_Tier1.png', 23014: 'Tooltip_Fairy_Base_ExtraSpicy_Tier2.png', 23015: 'Tooltip_Fairy_Base_ExtraSpicy_Tier3.png', 23007: 'Tooltip_Fairy_Base_Mermaid_Tier1.png', 23008: 'Tooltip_Fairy_Base_Mermaid_Tier2.png', 23009: 'Tooltip_Fairy_Base_Mermaid_Tier3.png', 23022: 'Tooltip_Fairy_Set6UpdateBattlePass_ProgressDay_Tier1.png', 23023: 'Tooltip_Fairy_Set6UpdateBattlePass_ProgressDay_Tier2.png', 23024: 'Tooltip_Fairy_Set6UpdateBattlePass_ProgressDay_Tier3.png', 23004: 'Tooltip_Fairy_Base_Rosebloom_Tier1.png', 23005: 'Tooltip_Fairy_Base_Rosebloom_Tier2.png', 23006: 'Tooltip_Fairy_Base_Rosebloom_Tier3.png', 23020: 'Tooltip_Fairy_Set5RankedRewards_Triumphant_Tier1.png', 23010: 'Tooltip_Fairy_Base_Vampire_Tier1.png', 23011: 'Tooltip_Fairy_Base_Vampire_Tier2.png', 23012: 'Tooltip_Fairy_Base_Vampire_Tier3.png', 23019: 'Tooltip_Fairy_Set5RankedRewards_Victorious_Tier1.png', 30001: 'Tooltip_Fenroar_Base_Classic_Tier1.png', 30002: 'Tooltip_Fenroar_Base_Classic_Tier2.png', 30003: 'Tooltip_Fenroar_Base_Classic_Tier3.png', 30019: 'Tooltip_Fenroar_PrgressDay_PrgressDay1_Tier1.png', 30020: 'Tooltip_Fenroar_PrgressDay_PrgressDay1_Tier2.png', 30021: 'Tooltip_Fenroar_PrgressDay_PrgressDay1_Tier3.png', 30022: 'Tooltip_Fenroar_PrgressDay_PrgressDay2_Tier1.png', 30023: 'Tooltip_Fenroar_PrgressDay_PrgressDay2_Tier2.png', 30024: 'Tooltip_Fenroar_PrgressDay_PrgressDay2_Tier3.png', 30025: 'Tooltip_Fenroar_PrgressDay_PrgressDay3_Tier1.png', 30026: 'Tooltip_Fenroar_PrgressDay_PrgressDay3_Tier2.png', 30027: 'Tooltip_Fenroar_PrgressDay_PrgressDay3_Tier3.png', 30028: 'Tooltip_Fenroar_PrgressDay_PrgressDay4_Tier1.png', 30029: 'Tooltip_Fenroar_PrgressDay_PrgressDay4_Tier2.png', 30030: 'Tooltip_Fenroar_PrgressDay_PrgressDay4_Tier3.png', 30031: 'Tooltip_Fenroar_PrgressDay_PrgressDay5_Tier1.png', 30032: 'Tooltip_Fenroar_PrgressDay_PrgressDay5_Tier2.png', 30033: 'Tooltip_Fenroar_PrgressDay_PrgressDay5_Tier3.png', 30004: 'Tooltip_Fenroar_Base_Variant1_Tier1.png', 30005: 'Tooltip_Fenroar_Base_Variant1_Tier2.png', 30006: 'Tooltip_Fenroar_Base_Variant1_Tier3.png', 30007: 'Tooltip_Fenroar_Base_Variant2_Tier1.png', 30008: 'Tooltip_Fenroar_Base_Variant2_Tier2.png', 30009: 'Tooltip_Fenroar_Base_Variant2_Tier3.png', 30010: 'Tooltip_Fenroar_Base_Variant3_Tier1.png', 30011: 'Tooltip_Fenroar_Base_Variant3_Tier2.png', 30012: 'Tooltip_Fenroar_Base_Variant3_Tier3.png', 30013: 'Tooltip_Fenroar_Base_Variant4_Tier1.png', 30014: 'Tooltip_Fenroar_Base_Variant4_Tier2.png', 30015: 'Tooltip_Fenroar_Base_Variant4_Tier3.png', 30016: 'Tooltip_Fenroar_Base_Variant5_Tier1.png', 30017: 'Tooltip_Fenroar_Base_Variant5_Tier2.png', 30018: 'Tooltip_Fenroar_Base_Variant5_Tier3.png', 18010: 'Tooltip_Gargoyle_BlackMist_Tier1.png', 18011: 'Tooltip_Gargoyle_BlackMist_Tier2.png', 18012: 'Tooltip_Gargoyle_BlackMist_Tier3.png', 18001: 'Tooltip_Gargoyle_Craggle_Tier1.png', 18002: 'Tooltip_Gargoyle_Craggle_Tier2.png', 18003: 'Tooltip_Gargoyle_Craggle_Tier3.png', 18016: 'Tooltip_Gargoyle_Hextech_Tier1.png', 18017: 'Tooltip_Gargoyle_Hextech_Tier2.png', 18018: 'Tooltip_Gargoyle_Hextech_Tier3.png', 18013: 'Tooltip_Gargoyle_Legionnaire_Tier1.png', 18014: 'Tooltip_Gargoyle_Legionnaire_Tier2.png', 18015: 'Tooltip_Gargoyle_Legionnaire_Tier3.png', 18007: 'Tooltip_Gargoyle_Sandbringer_Tier1.png', 18008: 'Tooltip_Gargoyle_Sandbringer_Tier2.png', 18009: 'Tooltip_Gargoyle_Sandbringer_Tier3.png', 18019: 'Tooltip_Gargoyle_Sentinel_Sentinel1_Tier1.png', 18021: 'Tooltip_Gargoyle_Set7RankedRewards_Triumphant_Tier1.LL_Gargoyle_Set7RankedRewards.png', 18004: 'Tooltip_Gargoyle_TrueIce_Tier1.png', 18005: 'Tooltip_Gargoyle_TrueIce_Tier2.png', 18006: 'Tooltip_Gargoyle_TrueIce_Tier3.png', 18020: 'Tooltip_Gargoyle_Set7RankedRewards_Victorious_Tier1.LL_Gargoyle_Set7RankedRewards.png', 7004: 'Tooltip_GemTiger_Fierce_Tier1.png', 7005: 'Tooltip_GemTiger_Fierce_Tier2.png', 7006: 'Tooltip_GemTiger_Fierce_Tier3.png', 7001: 'Tooltip_GemTiger_Jeweled_Tier1.png', 7002: 'Tooltip_GemTiger_Jeweled_Tier2.png', 7003: 'Tooltip_GemTiger_Jeweled_Tier3.png', 7021: 'Tooltip_GemTiger_LunarNewYear_LunarRevel_Tier1.png', 7022: 'Tooltip_GemTiger_LunarNewYear_LunarRevel_Tier2.png', 7023: 'Tooltip_GemTiger_LunarNewYear_LunarRevel_Tier3.png', 7013: 'Tooltip_GemTiger_Reigning_Tier1.png', 7014: 'Tooltip_GemTiger_Reigning_Tier2.png', 7015: 'Tooltip_GemTiger_Reigning_Tier3.png', 7007: 'Tooltip_GemTiger_Shadowgem_Tier1.png', 7008: 'Tooltip_GemTiger_Shadowgem_Tier2.png', 7009: 'Tooltip_GemTiger_Shadowgem_Tier3.png', 7010: 'Tooltip_GemTiger_Skygem_Tier1.png', 7011: 'Tooltip_GemTiger_Skygem_Tier2.png', 7012: 'Tooltip_GemTiger_Skygem_Tier3.png', 7016: 'Tooltip_GemTiger_Sunborne_Tier1.png', 7017: 'Tooltip_GemTiger_Sunborne_Tier2.png', 7018: 'Tooltip_GemTiger_Sunborne_Tier3.png', 7020: 'Tooltip_GemTiger_Set4RankedRewards_Triumphant_Tier1.png', 7019: 'Tooltip_GemTiger_Set4RankedRewards_Victorious_Tier1.png', 1016: 'Tooltip_Ghosty_Black_Tier1.png', 1017: 'Tooltip_Ghosty_Black_Tier2.png', 1018: 'Tooltip_Ghosty_Black_Tier3.png', 1007: 'Tooltip_Ghosty_Blue_Tier1.png', 1008: 'Tooltip_Ghosty_Blue_Tier2.png', 1009: 'Tooltip_Ghosty_Blue_Tier3.png', 1004: 'Tooltip_Ghosty_Fire_Tier1.png', 1005: 'Tooltip_Ghosty_Fire_Tier2.png', 1006: 'Tooltip_Ghosty_Fire_Tier3.png', 1020: 'Tooltip_Ghosty_GalaxiesVictorious_Tier1.png', 1010: 'Tooltip_Ghosty_Green_Tier1.png', 1011: 'Tooltip_Ghosty_Green_Tier2.png', 1012: 'Tooltip_Ghosty_Green_Tier3.png', 1022: 'Tooltip_Ghosty_Dragon_Hauntling1_Tier1.LL_Ghosty_Dragon.png', 1023: 'Tooltip_Ghosty_Dragon_Hauntling1_Tier2.LL_Ghosty_Dragon.png', 1024: 'Tooltip_Ghosty_Dragon_Hauntling1_Tier3.LL_Ghosty_Dragon.png', 1025: 'Tooltip_Ghosty_Dragon_Hauntling2_Tier1.LL_Ghosty_Dragon.png', 1026: 'Tooltip_Ghosty_Dragon_Hauntling2_Tier2.LL_Ghosty_Dragon.png', 1027: 'Tooltip_Ghosty_Dragon_Hauntling2_Tier3.LL_Ghosty_Dragon.png', 1028: 'Tooltip_Ghosty_Dragon_Hauntling3_Tier1.LL_Ghosty_Dragon.png', 1029: 'Tooltip_Ghosty_Dragon_Hauntling3_Tier2.LL_Ghosty_Dragon.png', 1030: 'Tooltip_Ghosty_Dragon_Hauntling3_Tier3.LL_Ghosty_Dragon.png', 1031: 'Tooltip_Ghosty_Dragon_Hauntling4_Tier1.LL_Ghosty_Dragon.png', 1032: 'Tooltip_Ghosty_Dragon_Hauntling4_Tier2.LL_Ghosty_Dragon.png', 1033: 'Tooltip_Ghosty_Dragon_Hauntling4_Tier3.LL_Ghosty_Dragon.png', 1034: 'Tooltip_Ghosty_Dragon_Hauntling5_Tier1.LL_Ghosty_Dragon.png', 1035: 'Tooltip_Ghosty_Dragon_Hauntling5_Tier2.LL_Ghosty_Dragon.png', 1036: 'Tooltip_Ghosty_Dragon_Hauntling5_Tier3.LL_Ghosty_Dragon.png', 1013: 'Tooltip_Ghosty_Purple_Tier1.png', 1014: 'Tooltip_Ghosty_Purple_Tier2.png', 1015: 'Tooltip_Ghosty_Purple_Tier3.png', 1021: 'Tooltip_Ghosty_Sentinel_Sentinel1_Tier1.png', 1001: 'Tooltip_Ghosty_Spooky_Tier1.png', 1002: 'Tooltip_Ghosty_Spooky_Tier2.png', 1003: 'Tooltip_Ghosty_Spooky_Tier3.png', 1019: 'Tooltip_Ghosty_Victorious_Tier1.png', 41001: 'Tooltip_Gloop_Base_Classic_Tier1.png', 41002: 'Tooltip_Gloop_Base_Classic_Tier2.png', 41003: 'Tooltip_Gloop_Base_Classic_Tier3.png', 41025: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel1_Tier1.LL_Gloop_LunarNewYear2023.png', 41026: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel1_Tier2.LL_Gloop_LunarNewYear2023.png', 41027: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel1_Tier3.LL_Gloop_LunarNewYear2023.png', 41028: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel2_Tier1.LL_Gloop_LunarNewYear2023.png', 41029: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel2_Tier2.LL_Gloop_LunarNewYear2023.png', 41030: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel2_Tier3.LL_Gloop_LunarNewYear2023.png', 41031: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel3_Tier1.LL_Gloop_LunarNewYear2023.png', 41032: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel3_Tier2.LL_Gloop_LunarNewYear2023.png', 41033: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel3_Tier3.LL_Gloop_LunarNewYear2023.png', 41034: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel4_Tier1.LL_Gloop_LunarNewYear2023.png', 41035: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel4_Tier2.LL_Gloop_LunarNewYear2023.png', 41036: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel4_Tier3.LL_Gloop_LunarNewYear2023.png', 41037: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel5_Tier1.LL_Gloop_LunarNewYear2023.png', 41038: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel5_Tier2.LL_Gloop_LunarNewYear2023.png', 41039: 'Tooltip_Gloop_LunarNewYear2023_LunarRevel5_Tier3.LL_Gloop_LunarNewYear2023.png', 41004: 'Tooltip_Gloop_Base_Variant1_Tier1.png', 41005: 'Tooltip_Gloop_Base_Variant1_Tier2.png', 41006: 'Tooltip_Gloop_Base_Variant1_Tier3.png', 41007: 'Tooltip_Gloop_Base_Variant2_Tier1.png', 41008: 'Tooltip_Gloop_Base_Variant2_Tier2.png', 41009: 'Tooltip_Gloop_Base_Variant2_Tier3.png', 41010: 'Tooltip_Gloop_Base_Variant3_Tier1.png', 41011: 'Tooltip_Gloop_Base_Variant3_Tier2.png', 41012: 'Tooltip_Gloop_Base_Variant3_Tier3.png', 41013: 'Tooltip_Gloop_Base_Variant4_Tier1.png', 41014: 'Tooltip_Gloop_Base_Variant4_Tier2.png', 41015: 'Tooltip_Gloop_Base_Variant4_Tier3.png', 41016: 'Tooltip_Gloop_Base_Variant5_Tier1.png', 41017: 'Tooltip_Gloop_Base_Variant5_Tier2.png', 41018: 'Tooltip_Gloop_Base_Variant5_Tier3.png', 41019: 'Tooltip_Gloop_Base_Variant6_Tier1.png', 41020: 'Tooltip_Gloop_Base_Variant6_Tier2.png', 41021: 'Tooltip_Gloop_Base_Variant6_Tier3.png', 41022: 'Tooltip_Gloop_Base_Variant7_Tier1.png', 41023: 'Tooltip_Gloop_Base_Variant7_Tier2.png', 41024: 'Tooltip_Gloop_Base_Variant7_Tier3.png', 2001: 'Tooltip_Griffin_Cream_Tier1.png', 2002: 'Tooltip_Griffin_Cream_Tier2.png', 2003: 'Tooltip_Griffin_Cream_Tier3.png', 2016: 'Tooltip_Griffin_Dark_Tier1.png', 2017: 'Tooltip_Griffin_Dark_Tier2.png', 2018: 'Tooltip_Griffin_Dark_Tier3.png', 2004: 'Tooltip_Griffin_Hawk_Tier1.png', 2005: 'Tooltip_Griffin_Hawk_Tier2.png', 2006: 'Tooltip_Griffin_Hawk_Tier3.png', 2013: 'Tooltip_Griffin_Parrot_Tier1.png', 2014: 'Tooltip_Griffin_Parrot_Tier2.png', 2015: 'Tooltip_Griffin_Parrot_Tier3.png', 2010: 'Tooltip_Griffin_Pink_Tier1.png', 2011: 'Tooltip_Griffin_Pink_Tier2.png', 2012: 'Tooltip_Griffin_Pink_Tier3.png', 2023: 'Tooltip_Griffin_DragonSlayer_Silverwing1_Tier1.LL_Griffin_DragonSlayer.png', 2024: 'Tooltip_Griffin_DragonSlayer_Silverwing1_Tier2.LL_Griffin_DragonSlayer.png', 2025: 'Tooltip_Griffin_DragonSlayer_Silverwing1_Tier3.LL_Griffin_DragonSlayer.png', 2026: 'Tooltip_Griffin_DragonSlayer_Silverwing2_Tier1.LL_Griffin_DragonSlayer.png', 2027: 'Tooltip_Griffin_DragonSlayer_Silverwing2_Tier2.LL_Griffin_DragonSlayer.png', 2028: 'Tooltip_Griffin_DragonSlayer_Silverwing2_Tier3.LL_Griffin_DragonSlayer.png', 2029: 'Tooltip_Griffin_DragonSlayer_Silverwing3_Tier1.LL_Griffin_DragonSlayer.png', 2030: 'Tooltip_Griffin_DragonSlayer_Silverwing3_Tier2.LL_Griffin_DragonSlayer.png', 2031: 'Tooltip_Griffin_DragonSlayer_Silverwing3_Tier3.LL_Griffin_DragonSlayer.png', 2032: 'Tooltip_Griffin_DragonSlayer_Silverwing4_Tier1.LL_Griffin_DragonSlayer.png', 2033: 'Tooltip_Griffin_DragonSlayer_Silverwing4_Tier2.LL_Griffin_DragonSlayer.png', 2034: 'Tooltip_Griffin_DragonSlayer_Silverwing4_Tier3.LL_Griffin_DragonSlayer.png', 2035: 'Tooltip_Griffin_DragonSlayer_Silverwing5_Tier1.LL_Griffin_DragonSlayer.png', 2036: 'Tooltip_Griffin_DragonSlayer_Silverwing5_Tier2.LL_Griffin_DragonSlayer.png', 2037: 'Tooltip_Griffin_DragonSlayer_Silverwing5_Tier3.LL_Griffin_DragonSlayer.png', 2019: 'Tooltip_Griffin_StarGuardian_Tier1.png', 2020: 'Tooltip_Griffin_StarGuardian_Tier2.png', 2021: 'Tooltip_Griffin_StarGuardian_Tier3.png', 2022: 'Tooltip_Griffin_Victorious.png', 2007: 'Tooltip_Griffin_Yellow_Tier1.png', 2008: 'Tooltip_Griffin_Yellow_Tier2.png', 2009: 'Tooltip_Griffin_Yellow_Tier3.png', 3016: 'Tooltip_GrumpyLion_Dark_Tier1.png', 3017: 'Tooltip_GrumpyLion_Dark_Tier2.png', 3018: 'Tooltip_GrumpyLion_Dark_Tier3.png', 3007: 'Tooltip_GrumpyLion_Green_Tier1.png', 3008: 'Tooltip_GrumpyLion_Green_Tier2.png', 3009: 'Tooltip_GrumpyLion_Green_Tier3.png', 3013: 'Tooltip_GrumpyLion_IceCream_Tier1.png', 3014: 'Tooltip_GrumpyLion_IceCream_Tier2.png', 3015: 'Tooltip_GrumpyLion_IceCream_Tier3.png', 3020: 'Tooltip_GrumpyLion_KDAKaiSa_KDA1_Tier1.png', 3021: 'Tooltip_GrumpyLion_KDAKaiSa_KDA1_Tier2.png', 3022: 'Tooltip_GrumpyLion_KDAKaiSa_KDA1_Tier3.png', 3023: 'Tooltip_GrumpyLion_KDAKaiSa_KDA2_Tier1.png', 3024: 'Tooltip_GrumpyLion_KDAKaiSa_KDA2_Tier2.png', 3025: 'Tooltip_GrumpyLion_KDAKaiSa_KDA2_Tier3.png', 3026: 'Tooltip_GrumpyLion_Set4Update_LunarBeast_Tier1.png', 3027: 'Tooltip_GrumpyLion_Set4Update_LunarBeast_Tier2.png', 3028: 'Tooltip_GrumpyLion_Set4Update_LunarBeast_Tier3.png', 3029: 'Tooltip_GrumpyLion_Set4Update_LunarRevel2021_Tier1.png', 3030: 'Tooltip_GrumpyLion_Set4Update_LunarRevel2021_Tier2.png', 3031: 'Tooltip_GrumpyLion_Set4Update_LunarRevel2021_Tier3.png', 3010: 'Tooltip_GrumpyLion_Orange_Tier1.png', 3011: 'Tooltip_GrumpyLion_Orange_Tier2.png', 3012: 'Tooltip_GrumpyLion_Orange_Tier3.png', 3001: 'Tooltip_GrumpyLion_Red_Tier1.png', 3002: 'Tooltip_GrumpyLion_Red_Tier2.png', 3003: 'Tooltip_GrumpyLion_Red_Tier3.png', 3019: 'Tooltip_GrumpyLion_Victorious.png', 3004: 'Tooltip_GrumpyLion_Void_Tier1.png', 3005: 'Tooltip_GrumpyLion_Void_Tier2.png', 3006: 'Tooltip_GrumpyLion_Void_Tier3.png', 16010: 'Tooltip_HextechBirb_BlackMist_Tier1.png', 16011: 'Tooltip_HextechBirb_BlackMist_Tier2.png', 16012: 'Tooltip_HextechBirb_BlackMist_Tier3.png', 16007: 'Tooltip_HextechBirb_Chemtech_Tier1.png', 16008: 'Tooltip_HextechBirb_Chemtech_Tier2.png', 16009: 'Tooltip_HextechBirb_Chemtech_Tier3.png', 16013: 'Tooltip_HextechBirb_Legionnaire_Tier1.png', 16014: 'Tooltip_HextechBirb_Legionnaire_Tier2.png', 16015: 'Tooltip_HextechBirb_Legionnaire_Tier3.png', 16016: 'Tooltip_HextechBirb_PetalDancer_Tier1.png', 16017: 'Tooltip_HextechBirb_PetalDancer_Tier2.png', 16018: 'Tooltip_HextechBirb_PetalDancer_Tier3.png', 16004: 'Tooltip_HextechBirb_Petricite_Tier1.png', 16005: 'Tooltip_HextechBirb_Petricite_Tier2.png', 16006: 'Tooltip_HextechBirb_Petricite_Tier3.png', 16021: 'Tooltip_HextechBirb_StarGuardian_StarGuardianTocker_Tier1.LL_HextechBirb_StarGuardian.png', 16022: 'Tooltip_HextechBirb_StarGuardian_StarGuardianTocker_Tier2.LL_HextechBirb_StarGuardian.png', 16023: 'Tooltip_HextechBirb_StarGuardian_StarGuardianTocker_Tier3.LL_HextechBirb_StarGuardian.png', 16001: 'Tooltip_HextechBirb_Tocker_Tier1.png', 16002: 'Tooltip_HextechBirb_Tocker_Tier2.png', 16003: 'Tooltip_HextechBirb_Tocker_Tier3.png', 16020: 'Tooltip_HextechBirb_Set6RankedRewards_Triumphant_Tier1.LL_HextechBirb_Set6RankedRewards.png', 16019: 'Tooltip_HextechBirb_Set6RankedRewards_Victorious_Tier1.LL_HextechBirb_Set6RankedRewards.png', 43001: 'Tooltip_JawDragon_Base_Classic_Tier1.LL_JawDragon_Base.png', 43002: 'Tooltip_JawDragon_Base_Classic_Tier2.LL_JawDragon_Base.png', 43003: 'Tooltip_JawDragon_Base_Classic_Tier3.LL_JawDragon_Base.png', 43004: 'Tooltip_JawDragon_Base_Variant1_Tier1.LL_JawDragon_Base.png', 43005: 'Tooltip_JawDragon_Base_Variant1_Tier2.LL_JawDragon_Base.png', 43006: 'Tooltip_JawDragon_Base_Variant1_Tier3.LL_JawDragon_Base.png', 43007: 'Tooltip_JawDragon_Base_Variant2_Tier1.LL_JawDragon_Base.png', 43008: 'Tooltip_JawDragon_Base_Variant2_Tier2.LL_JawDragon_Base.png', 43009: 'Tooltip_JawDragon_Base_Variant2_Tier3.LL_JawDragon_Base.png', 43010: 'Tooltip_JawDragon_Base_Variant3_Tier1.LL_JawDragon_Base.png', 43011: 'Tooltip_JawDragon_Base_Variant3_Tier2.LL_JawDragon_Base.png', 43012: 'Tooltip_JawDragon_Base_Variant3_Tier3.LL_JawDragon_Base.png', 43013: 'Tooltip_JawDragon_Base_Variant4_Tier1.LL_JawDragon_Base.png', 43014: 'Tooltip_JawDragon_Base_Variant4_Tier2.LL_JawDragon_Base.png', 43015: 'Tooltip_JawDragon_Base_Variant4_Tier3.LL_JawDragon_Base.png', 43016: 'Tooltip_JawDragon_Base_Variant5_Tier1.LL_JawDragon_Base.png', 43017: 'Tooltip_JawDragon_Base_Variant5_Tier2.LL_JawDragon_Base.png', 43018: 'Tooltip_JawDragon_Base_Variant5_Tier3.LL_JawDragon_Base.png', 55001: 'Tooltip_Koala_Base_Classic_Tier1.LL_Koala_Base.png', 55002: 'Tooltip_Koala_Base_Classic_Tier2.LL_Koala_Base.png', 55003: 'Tooltip_Koala_Base_Classic_Tier3.LL_Koala_Base.png', 55004: 'Tooltip_Koala_Base_Variant1_Tier1.LL_Koala_Base.png', 55005: 'Tooltip_Koala_Base_Variant1_Tier2.LL_Koala_Base.png', 55006: 'Tooltip_Koala_Base_Variant1_Tier3.LL_Koala_Base.png', 55007: 'Tooltip_Koala_Base_Variant2_Tier1.LL_Koala_Base.png', 55008: 'Tooltip_Koala_Base_Variant2_Tier2.LL_Koala_Base.png', 55009: 'Tooltip_Koala_Base_Variant2_Tier3.LL_Koala_Base.png', 55010: 'Tooltip_Koala_Base_Variant3_Tier1.LL_Koala_Base.png', 55011: 'Tooltip_Koala_Base_Variant3_Tier2.LL_Koala_Base.png', 55012: 'Tooltip_Koala_Base_Variant3_Tier3.LL_Koala_Base.png', 55013: 'Tooltip_Koala_Base_Variant4_Tier1.LL_Koala_Base.png', 55014: 'Tooltip_Koala_Base_Variant4_Tier2.LL_Koala_Base.png', 55015: 'Tooltip_Koala_Base_Variant4_Tier3.LL_Koala_Base.png', 55016: 'Tooltip_Koala_Base_Variant5_Tier1.LL_Koala_Base.png', 55017: 'Tooltip_Koala_Base_Variant5_Tier2.LL_Koala_Base.png', 55018: 'Tooltip_Koala_Base_Variant5_Tier3.LL_Koala_Base.png', 4019: 'Tooltip_Miner_Astronaut_Tier1.png', 4020: 'Tooltip_Miner_Astronaut_Tier2.png', 4021: 'Tooltip_Miner_Astronaut_Tier3.png', 4028: 'Tooltip_Miner_RPG_Chaos_Tier1.png', 4029: 'Tooltip_Miner_RPG_Chaos_Tier2.png', 4030: 'Tooltip_Miner_RPG_Chaos_Tier3.png', 4013: 'Tooltip_Miner_Dark_Tier1.png', 4014: 'Tooltip_Miner_Dark_Tier2.png', 4015: 'Tooltip_Miner_Dark_Tier3.png', 4010: 'Tooltip_Miner_Green_Tier1.png', 4011: 'Tooltip_Miner_Green_Tier2.png', 4012: 'Tooltip_Miner_Green_Tier3.png', 4001: 'Tooltip_Miner_Grey_Tier1.png', 4002: 'Tooltip_Miner_Grey_Tier2.png', 4003: 'Tooltip_Miner_Grey_Tier3.png', 4025: 'Tooltip_Miner_RPG_Neutral_Tier1.png', 4026: 'Tooltip_Miner_RPG_Neutral_Tier2.png', 4027: 'Tooltip_Miner_RPG_Neutral_Tier3.png', 4022: 'Tooltip_Miner_RPG_Order_Tier1.png', 4023: 'Tooltip_Miner_RPG_Order_Tier2.png', 4024: 'Tooltip_Miner_RPG_Order_Tier3.png', 4007: 'Tooltip_Miner_Rainbow_Tier1.png', 4008: 'Tooltip_Miner_Rainbow_Tier2.png', 4009: 'Tooltip_Miner_Rainbow_Tier3.png', 4004: 'Tooltip_Miner_Red_Tier1.png', 4005: 'Tooltip_Miner_Red_Tier2.png', 4006: 'Tooltip_Miner_Red_Tier3.png', 4016: 'Tooltip_Miner_Yellow_Tier1.png', 4017: 'Tooltip_Miner_Yellow_Tier2.png', 4018: 'Tooltip_Miner_Yellow_Tier3.png', 5010: 'Tooltip_MiniGolem_Dark_Tier1.png', 5011: 'Tooltip_MiniGolem_Dark_Tier2.png', 5012: 'Tooltip_MiniGolem_Dark_Tier3.png', 5001: 'Tooltip_MiniGolem_Grey_Tier1.png', 5002: 'Tooltip_MiniGolem_Grey_Tier2.png', 5003: 'Tooltip_MiniGolem_Grey_Tier3.png', 5013: 'Tooltip_MiniGolem_Ice_Tier1.png', 5014: 'Tooltip_MiniGolem_Ice_Tier2.png', 5015: 'Tooltip_MiniGolem_Ice_Tier3.png', 5004: 'Tooltip_MiniGolem_Lava_Tier1.png', 5005: 'Tooltip_MiniGolem_Lava_Tier2.png', 5006: 'Tooltip_MiniGolem_Lava_Tier3.png', 5007: 'Tooltip_MiniGolem_Moss_Tier1.png', 5008: 'Tooltip_MiniGolem_Moss_Tier2.png', 5009: 'Tooltip_MiniGolem_Moss_Tier3.png', 5016: 'Tooltip_MiniGolem_Spring_Tier1.png', 5017: 'Tooltip_MiniGolem_Spring_Tier2.png', 5018: 'Tooltip_MiniGolem_Spring_Tier3.png', 5019: 'Tooltip_MiniGolem_Anniversary_Variant1_Tier1.png', 31001: 'Tooltip_Nimblefoot_Base_Classic_Tier1.png', 31002: 'Tooltip_Nimblefoot_Base_Classic_Tier2.png', 31003: 'Tooltip_Nimblefoot_Base_Classic_Tier3.png', 31004: 'Tooltip_Nimblefoot_Base_Variant1_Tier1.png', 31005: 'Tooltip_Nimblefoot_Base_Variant1_Tier2.png', 31006: 'Tooltip_Nimblefoot_Base_Variant1_Tier3.png', 31007: 'Tooltip_Nimblefoot_Base_Variant2_Tier1.png', 31008: 'Tooltip_Nimblefoot_Base_Variant2_Tier2.png', 31009: 'Tooltip_Nimblefoot_Base_Variant2_Tier3.png', 31010: 'Tooltip_Nimblefoot_Base_Variant3_Tier1.png', 31011: 'Tooltip_Nimblefoot_Base_Variant3_Tier2.png', 31012: 'Tooltip_Nimblefoot_Base_Variant3_Tier3.png', 31013: 'Tooltip_Nimblefoot_Base_Variant4_Tier1.png', 31014: 'Tooltip_Nimblefoot_Base_Variant4_Tier2.png', 31015: 'Tooltip_Nimblefoot_Base_Variant4_Tier3.png', 31016: 'Tooltip_Nimblefoot_Base_Variant5_Tier1.png', 31017: 'Tooltip_Nimblefoot_Base_Variant5_Tier2.png', 31018: 'Tooltip_Nimblefoot_Base_Variant5_Tier3.png', 22016: 'Tooltip_Pegasus_Arcade_Tier1.png', 22017: 'Tooltip_Pegasus_Arcade_Tier2.png', 22018: 'Tooltip_Pegasus_Arcade_Tier3.png', 22013: 'Tooltip_Pegasus_BlackMist_Tier1.png', 22014: 'Tooltip_Pegasus_BlackMist_Tier2.png', 22015: 'Tooltip_Pegasus_BlackMist_Tier3.png', 22001: 'Tooltip_Pegasus_Classic_Tier1.png', 22002: 'Tooltip_Pegasus_Classic_Tier2.png', 22003: 'Tooltip_Pegasus_Classic_Tier3.png', 22004: 'Tooltip_Pegasus_Crystal_Tier1.png', 22005: 'Tooltip_Pegasus_Crystal_Tier2.png', 22006: 'Tooltip_Pegasus_Crystal_Tier3.png', 22010: 'Tooltip_Pegasus_HighNoon_Tier1.png', 22011: 'Tooltip_Pegasus_HighNoon_Tier2.png', 22012: 'Tooltip_Pegasus_HighNoon_Tier3.png', 22019: 'Tooltip_Pegasus_KDASeraphine_KDA1_Tier1.png', 22020: 'Tooltip_Pegasus_KDASeraphine_KDA1_Tier2.png', 22021: 'Tooltip_Pegasus_KDASeraphine_KDA1_Tier3.png', 22022: 'Tooltip_Pegasus_KDASeraphine_KDA2_Tier1.png', 22023: 'Tooltip_Pegasus_KDASeraphine_KDA2_Tier2.png', 22024: 'Tooltip_Pegasus_KDASeraphine_KDA2_Tier3.png', 22025: 'Tooltip_Pegasus_ProgressDay_ProgressDay1_Tier1.png', 22026: 'Tooltip_Pegasus_ProgressDay_ProgressDay1_Tier2.png', 22027: 'Tooltip_Pegasus_ProgressDay_ProgressDay1_Tier3.png', 22028: 'Tooltip_Pegasus_ProgressDay_ProgressDay2_Tier1.png', 22029: 'Tooltip_Pegasus_ProgressDay_ProgressDay2_Tier2.png', 22030: 'Tooltip_Pegasus_ProgressDay_ProgressDay2_Tier3.png', 22031: 'Tooltip_Pegasus_ProgressDay_ProgressDay3_Tier1.png', 22032: 'Tooltip_Pegasus_ProgressDay_ProgressDay3_Tier2.png', 22033: 'Tooltip_Pegasus_ProgressDay_ProgressDay3_Tier3.png', 22034: 'Tooltip_Pegasus_ProgressDay_ProgressDay4_Tier1.png', 22035: 'Tooltip_Pegasus_ProgressDay_ProgressDay4_Tier2.png', 22036: 'Tooltip_Pegasus_ProgressDay_ProgressDay4_Tier3.png', 22037: 'Tooltip_Pegasus_ProgressDay_ProgressDay5_Tier1.png', 22038: 'Tooltip_Pegasus_ProgressDay_ProgressDay5_Tier2.png', 22039: 'Tooltip_Pegasus_ProgressDay_ProgressDay5_Tier3.png', 22007: 'Tooltip_Pegasus_SugarCone_Tier1.png', 22008: 'Tooltip_Pegasus_SugarCone_Tier2.png', 22009: 'Tooltip_Pegasus_SugarCone_Tier3.png', 6032: 'Tooltip_PenguKnight_Set5LaunchBattlePass_Chaos_Tier1.png', 6033: 'Tooltip_PenguKnight_Set5LaunchBattlePass_Chaos_Tier2.png', 6034: 'Tooltip_PenguKnight_Set5LaunchBattlePass_Chaos_Tier3.png', 6001: 'Tooltip_PenguKnight_Classic_Tier1.png', 6002: 'Tooltip_PenguKnight_Classic_Tier2.png', 6003: 'Tooltip_PenguKnight_Classic_Tier3.png', 6004: 'Tooltip_PenguKnight_Dark_Tier1.png', 6005: 'Tooltip_PenguKnight_Dark_Tier2.png', 6006: 'Tooltip_PenguKnight_Dark_Tier3.png', 6038: 'Tooltip_PenguKnight_Esport_Esport1_Tier1.png', 6007: 'Tooltip_PenguKnight_Ice_Tier1.png', 6008: 'Tooltip_PenguKnight_Ice_Tier2.png', 6009: 'Tooltip_PenguKnight_Ice_Tier3.png', 6025: 'Tooltip_PenguKnight_KDAAkali_KDA1_Tier1.png', 6026: 'Tooltip_PenguKnight_KDAAkali_KDA1_Tier2.png', 6027: 'Tooltip_PenguKnight_KDAAkali_KDA1_Tier3.png', 6028: 'Tooltip_PenguKnight_KDAAkali_KDA2_Tier1.png', 6029: 'Tooltip_PenguKnight_KDAAkali_KDA2_Tier2.png', 6030: 'Tooltip_PenguKnight_KDAAkali_KDA2_Tier3.png', 6054: 'Tooltip_PenguKnight_Dragon_Mythic_Tier1.LL_PenguKnight_Dragon.png', 6055: 'Tooltip_PenguKnight_Dragon_Mythic_Tier2.LL_PenguKnight_Dragon.png', 6056: 'Tooltip_PenguKnight_Dragon_Mythic_Tier3.LL_PenguKnight_Dragon.png', 6035: 'Tooltip_PenguKnight_Set5UpdateBattlePass_Order_Tier1.png', 6036: 'Tooltip_PenguKnight_Set5UpdateBattlePass_Order_Tier2.png', 6037: 'Tooltip_PenguKnight_Set5UpdateBattlePass_Order_Tier3.png', 6016: 'Tooltip_PenguKnight_Owl_Tier1.png', 6017: 'Tooltip_PenguKnight_Owl_Tier2.png', 6018: 'Tooltip_PenguKnight_Owl_Tier3.png', 6010: 'Tooltip_PenguKnight_Rooster_Tier1.png', 6011: 'Tooltip_PenguKnight_Rooster_Tier2.png', 6012: 'Tooltip_PenguKnight_Rooster_Tier3.png', 6031: 'Tooltip_PenguKnight_Ruined_Ruined_Tier1.png', 6019: 'Tooltip_PenguKnight_SpiritBlossomKami_Tier1.png', 6020: 'Tooltip_PenguKnight_SpiritBlossomKami_Tier2.png', 6021: 'Tooltip_PenguKnight_SpiritBlossomKami_Tier3.png', 6022: 'Tooltip_PenguKnight_SpiritBlossomYokai_Tier1.png', 6023: 'Tooltip_PenguKnight_SpiritBlossomYokai_Tier2.png', 6024: 'Tooltip_PenguKnight_SpiritBlossomYokai_Tier3.png', 6039: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy1_Tier1.png', 6040: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy1_Tier2.png', 6041: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy1_Tier3.png', 6042: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy2_Tier1.png', 6043: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy2_Tier2.png', 6044: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy2_Tier3.png', 6045: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy3_Tier1.png', 6046: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy3_Tier2.png', 6047: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy3_Tier3.png', 6048: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy4_Tier1.png', 6049: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy4_Tier2.png', 6050: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy4_Tier3.png', 6051: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy5_Tier1.png', 6052: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy5_Tier2.png', 6053: 'Tooltip_PenguKnight_SpiritFairy_SpiritFairy5_Tier3.png', 6013: 'Tooltip_PenguKnight_Yellow_Tier1.png', 6014: 'Tooltip_PenguKnight_Yellow_Tier2.png', 6015: 'Tooltip_PenguKnight_Yellow_Tier3.png', 40001: 'Tooltip_Piximander_Base_Classic_Tier1.png', 40002: 'Tooltip_Piximander_Base_Classic_Tier2.png', 40003: 'Tooltip_Piximander_Base_Classic_Tier3.png', 40004: 'Tooltip_Piximander_Base_Variant1_Tier1.png', 40005: 'Tooltip_Piximander_Base_Variant1_Tier2.png', 40006: 'Tooltip_Piximander_Base_Variant1_Tier3.png', 40007: 'Tooltip_Piximander_Base_Variant2_Tier1.png', 40008: 'Tooltip_Piximander_Base_Variant2_Tier2.png', 40009: 'Tooltip_Piximander_Base_Variant2_Tier3.png', 40010: 'Tooltip_Piximander_Base_Variant3_Tier1.png', 40011: 'Tooltip_Piximander_Base_Variant3_Tier2.png', 40012: 'Tooltip_Piximander_Base_Variant3_Tier3.png', 40013: 'Tooltip_Piximander_Base_Variant4_Tier1.png', 40014: 'Tooltip_Piximander_Base_Variant4_Tier2.png', 40015: 'Tooltip_Piximander_Base_Variant4_Tier3.png', 40016: 'Tooltip_Piximander_Base_Variant5_Tier1.png', 40017: 'Tooltip_Piximander_Base_Variant5_Tier2.png', 40018: 'Tooltip_Piximander_Base_Variant5_Tier3.png', 40019: 'Tooltip_Piximander_Base_Variant6_Tier1.png', 40020: 'Tooltip_Piximander_Base_Variant6_Tier2.png', 40021: 'Tooltip_Piximander_Base_Variant6_Tier3.png', 40022: 'Tooltip_Piximander_Base_Variant7_Tier1.png', 40023: 'Tooltip_Piximander_Base_Variant7_Tier2.png', 40024: 'Tooltip_Piximander_Base_Variant7_Tier3.png', 46001: 'Tooltip_PupDragon_Base_Classic_Tier1.LL_PupDragon_Base.png', 46002: 'Tooltip_PupDragon_Base_Classic_Tier2.LL_PupDragon_Base.png', 46003: 'Tooltip_PupDragon_Base_Classic_Tier3.LL_PupDragon_Base.png', 46004: 'Tooltip_PupDragon_Base_Variant1_Tier1.LL_PupDragon_Base.png', 46005: 'Tooltip_PupDragon_Base_Variant1_Tier2.LL_PupDragon_Base.png', 46006: 'Tooltip_PupDragon_Base_Variant1_Tier3.LL_PupDragon_Base.png', 46007: 'Tooltip_PupDragon_Base_Variant2_Tier1.LL_PupDragon_Base.png', 46008: 'Tooltip_PupDragon_Base_Variant2_Tier2.LL_PupDragon_Base.png', 46009: 'Tooltip_PupDragon_Base_Variant2_Tier3.LL_PupDragon_Base.png', 46010: 'Tooltip_PupDragon_Base_Variant3_Tier1.LL_PupDragon_Base.png', 46011: 'Tooltip_PupDragon_Base_Variant3_Tier2.LL_PupDragon_Base.png', 46012: 'Tooltip_PupDragon_Base_Variant3_Tier3.LL_PupDragon_Base.png', 46013: 'Tooltip_PupDragon_Base_Variant4_Tier1.LL_PupDragon_Base.png', 46014: 'Tooltip_PupDragon_Base_Variant4_Tier2.LL_PupDragon_Base.png', 46015: 'Tooltip_PupDragon_Base_Variant4_Tier3.LL_PupDragon_Base.png', 46016: 'Tooltip_PupDragon_Base_Variant5_Tier1.LL_PupDragon_Base.png', 46017: 'Tooltip_PupDragon_Base_Variant5_Tier2.LL_PupDragon_Base.png', 46018: 'Tooltip_PupDragon_Base_Variant5_Tier3.LL_PupDragon_Base.png', 14016: 'Tooltip_QiyanaDog_BassQueen_Tier1.png', 14017: 'Tooltip_QiyanaDog_BassQueen_Tier2.png', 14018: 'Tooltip_QiyanaDog_BassQueen_Tier3.png', 14010: 'Tooltip_QiyanaDog_Beatmaker_Tier1.png', 14011: 'Tooltip_QiyanaDog_Beatmaker_Tier2.png', 14012: 'Tooltip_QiyanaDog_Beatmaker_Tier3.png', 14004: 'Tooltip_QiyanaDog_Hardhitter_Tier1.png', 14005: 'Tooltip_QiyanaDog_Hardhitter_Tier2.png', 14006: 'Tooltip_QiyanaDog_Hardhitter_Tier3.png', 14013: 'Tooltip_QiyanaDog_Prodigy_Tier1.png', 14014: 'Tooltip_QiyanaDog_Prodigy_Tier2.png', 14015: 'Tooltip_QiyanaDog_Prodigy_Tier3.png', 14019: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay1_Tier1.png', 14020: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay1_Tier2.png', 14021: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay1_Tier3.png', 14022: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay2_Tier1.png', 14023: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay2_Tier2.png', 14024: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay2_Tier3.png', 14025: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay3_Tier1.png', 14026: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay3_Tier2.png', 14027: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay3_Tier3.png', 14028: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay4_Tier1.png', 14029: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay4_Tier2.png', 14030: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay4_Tier3.png', 14031: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay5_Tier1.png', 14032: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay5_Tier2.png', 14033: 'Tooltip_QiyanaDog_ProgressDay_ProgressDay5_Tier3.png', 14001: 'Tooltip_QiyanaDog_Qiqi_Tier1.png', 14002: 'Tooltip_QiyanaDog_Qiqi_Tier2.png', 14003: 'Tooltip_QiyanaDog_Qiqi_Tier3.png', 14007: 'Tooltip_QiyanaDog_Soloist_Tier1.png', 14008: 'Tooltip_QiyanaDog_Soloist_Tier2.png', 14009: 'Tooltip_QiyanaDog_Soloist_Tier3.png', 10004: 'Tooltip_SGCat_Bubblegum_Tier1.png', 10005: 'Tooltip_SGCat_Bubblegum_Tier2.png', 10006: 'Tooltip_SGCat_Bubblegum_Tier3.png', 10001: 'Tooltip_SGCat_Dango_Tier1.png', 10002: 'Tooltip_SGCat_Dango_Tier2.png', 10003: 'Tooltip_SGCat_Dango_Tier3.png', 10007: 'Tooltip_SGCat_Gingersnap_Tier1.png', 10008: 'Tooltip_SGCat_Gingersnap_Tier2.png', 10009: 'Tooltip_SGCat_Gingersnap_Tier3.png', 10010: 'Tooltip_SGCat_Lemondrop_Tier1.png', 10011: 'Tooltip_SGCat_Lemondrop_Tier2.png', 10012: 'Tooltip_SGCat_Lemondrop_Tier3.png', 10013: 'Tooltip_SGCat_Limeberry_Tier1.png', 10014: 'Tooltip_SGCat_Limeberry_Tier2.png', 10015: 'Tooltip_SGCat_Limeberry_Tier3.png', 10019: 'Tooltip_SGCat_LunarNewYear_LunarRevel1_Tier1.png', 10020: 'Tooltip_SGCat_LunarNewYear_LunarRevel1_Tier2.png', 10021: 'Tooltip_SGCat_LunarNewYear_LunarRevel1_Tier3.png', 10022: 'Tooltip_SGCat_LunarNewYear_LunarRevel2_Tier1.png', 10023: 'Tooltip_SGCat_LunarNewYear_LunarRevel2_Tier2.png', 10024: 'Tooltip_SGCat_LunarNewYear_LunarRevel2_Tier3.png', 10025: 'Tooltip_SGCat_LunarNewYear_LunarRevel3_Tier1.png', 10026: 'Tooltip_SGCat_LunarNewYear_LunarRevel3_Tier2.png', 10027: 'Tooltip_SGCat_LunarNewYear_LunarRevel3_Tier3.png', 10028: 'Tooltip_SGCat_LunarNewYear_LunarRevel4_Tier1.png', 10029: 'Tooltip_SGCat_LunarNewYear_LunarRevel4_Tier2.png', 10030: 'Tooltip_SGCat_LunarNewYear_LunarRevel4_Tier3.png', 10031: 'Tooltip_SGCat_LunarNewYear_LunarRevel5_Tier1.png', 10032: 'Tooltip_SGCat_LunarNewYear_LunarRevel5_Tier2.png', 10033: 'Tooltip_SGCat_LunarNewYear_LunarRevel5_Tier3.png', 10016: 'Tooltip_SGCat_SugarCrash_Tier1.png', 10017: 'Tooltip_SGCat_SugarCrash_Tier2.png', 10018: 'Tooltip_SGCat_SugarCrash_Tier3.png', 11028: 'Tooltip_SGPig_RPG_Chaos_Tier1.png', 11029: 'Tooltip_SGPig_RPG_Chaos_Tier2.png', 11030: 'Tooltip_SGPig_RPG_Chaos_Tier3.png', 11016: 'Tooltip_SGPig_Daystar_Tier1.png', 11017: 'Tooltip_SGPig_Daystar_Tier2.png', 11018: 'Tooltip_SGPig_Daystar_Tier3.png', 11010: 'Tooltip_SGPig_Eclipse_Tier1.png', 11011: 'Tooltip_SGPig_Eclipse_Tier2.png', 11012: 'Tooltip_SGPig_Eclipse_Tier3.png', 11013: 'Tooltip_SGPig_Firecracker_Tier1.png', 11014: 'Tooltip_SGPig_Firecracker_Tier2.png', 11015: 'Tooltip_SGPig_Firecracker_Tier3.png', 11001: 'Tooltip_SGPig_Fuwa_Tier1.png', 11002: 'Tooltip_SGPig_Fuwa_Tier2.png', 11003: 'Tooltip_SGPig_Fuwa_Tier3.png', 11004: 'Tooltip_SGPig_LastWish_Tier1.png', 11005: 'Tooltip_SGPig_LastWish_Tier2.png', 11006: 'Tooltip_SGPig_LastWish_Tier3.png', 11007: 'Tooltip_SGPig_Lovestruck_Tier1.png', 11008: 'Tooltip_SGPig_Lovestruck_Tier2.png', 11009: 'Tooltip_SGPig_Lovestruck_Tier3.png', 11019: 'Tooltip_SGPig_Journey_Fuwa_Tier1.png', 11020: 'Tooltip_SGPig_Journey_Fuwa_Tier2.png', 11021: 'Tooltip_SGPig_Journey_Fuwa_Tier3.png', 11025: 'Tooltip_SGPig_RPG_Neutral_Tier1.png', 11026: 'Tooltip_SGPig_RPG_Neutral_Tier2.png', 11027: 'Tooltip_SGPig_RPG_Neutral_Tier3.png', 11022: 'Tooltip_SGPig_RPG_Order_Tier1.png', 11023: 'Tooltip_SGPig_RPG_Order_Tier2.png', 11024: 'Tooltip_SGPig_RPG_Order_Tier3.png', 12016: 'Tooltip_SGShisa_Corrupted_Tier1.png', 12017: 'Tooltip_SGShisa_Corrupted_Tier2.png', 12018: 'Tooltip_SGShisa_Corrupted_Tier3.png', 12025: 'Tooltip_SGShisa_Set6LaunchBattlePass_Doctor_Tier1.png', 12026: 'Tooltip_SGShisa_Set6LaunchBattlePass_Doctor_Tier2.png', 12027: 'Tooltip_SGShisa_Set6LaunchBattlePass_Doctor_Tier3.png', 12013: 'Tooltip_SGShisa_Firecracker_Tier1.png', 12014: 'Tooltip_SGShisa_Firecracker_Tier2.png', 12015: 'Tooltip_SGShisa_Firecracker_Tier3.png', 12004: 'Tooltip_SGShisa_Heroic_Tier1.png', 12005: 'Tooltip_SGShisa_Heroic_Tier2.png', 12006: 'Tooltip_SGShisa_Heroic_Tier3.png', 12007: 'Tooltip_SGShisa_Littlest_Tier1.png', 12008: 'Tooltip_SGShisa_Littlest_Tier2.png', 12009: 'Tooltip_SGShisa_Littlest_Tier3.png', 12022: 'Tooltip_SGShisa_Journeys_LunarBeast_Tier1.png', 12023: 'Tooltip_SGShisa_Journeys_LunarBeast_Tier2.png', 12024: 'Tooltip_SGShisa_Journeys_LunarBeast_Tier3.png', 12019: 'Tooltip_SGShisa_Journeys_LunarRevel_Tier1.png', 12020: 'Tooltip_SGShisa_Journeys_LunarRevel_Tier2.png', 12021: 'Tooltip_SGShisa_Journeys_LunarRevel_Tier3.png', 12001: 'Tooltip_SGShisa_Shisa_Tier1.png', 12002: 'Tooltip_SGShisa_Shisa_Tier2.png', 12003: 'Tooltip_SGShisa_Shisa_Tier3.png', 12010: 'Tooltip_SGShisa_Sundrop_Tier1.png', 12011: 'Tooltip_SGShisa_Sundrop_Tier2.png', 12012: 'Tooltip_SGShisa_Sundrop_Tier3.png', 15010: 'Tooltip_SennaBunny_Beatmaker_Tier1.png', 15011: 'Tooltip_SennaBunny_Beatmaker_Tier2.png', 15012: 'Tooltip_SennaBunny_Beatmaker_Tier3.png', 15004: 'Tooltip_SennaBunny_Hardhitter_Tier1.png', 15005: 'Tooltip_SennaBunny_Hardhitter_Tier2.png', 15006: 'Tooltip_SennaBunny_Hardhitter_Tier3.png', 15025: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel1_Tier1.LL_SennaBunny_LunarNewYear2023.png', 15026: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel1_Tier2.LL_SennaBunny_LunarNewYear2023.png', 15027: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel1_Tier3.LL_SennaBunny_LunarNewYear2023.png', 15028: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel2_Tier1.LL_SennaBunny_LunarNewYear2023.png', 15029: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel2_Tier2.LL_SennaBunny_LunarNewYear2023.png', 15030: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel2_Tier3.LL_SennaBunny_LunarNewYear2023.png', 15031: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel3_Tier1.LL_SennaBunny_LunarNewYear2023.png', 15032: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel3_Tier2.LL_SennaBunny_LunarNewYear2023.png', 15033: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel3_Tier3.LL_SennaBunny_LunarNewYear2023.png', 15034: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel4_Tier1.LL_SennaBunny_LunarNewYear2023.png', 15035: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel4_Tier2.LL_SennaBunny_LunarNewYear2023.png', 15036: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel4_Tier3.LL_SennaBunny_LunarNewYear2023.png', 15037: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel5_Tier1.LL_SennaBunny_LunarNewYear2023.png', 15038: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel5_Tier2.LL_SennaBunny_LunarNewYear2023.png', 15039: 'Tooltip_SennaBunny_LunarNewYear2023_LunarRevel5_Tier3.LL_SennaBunny_LunarNewYear2023.png', 15001: 'Tooltip_SennaBunny_Melisma_Tier1.png', 15002: 'Tooltip_SennaBunny_Melisma_Tier2.png', 15003: 'Tooltip_SennaBunny_Melisma_Tier3.png', 15007: 'Tooltip_SennaBunny_Popqueen_Tier1.png', 15008: 'Tooltip_SennaBunny_Popqueen_Tier2.png', 15009: 'Tooltip_SennaBunny_Popqueen_Tier3.png', 15013: 'Tooltip_SennaBunny_Prodigy_Tier1.png', 15014: 'Tooltip_SennaBunny_Prodigy_Tier2.png', 15015: 'Tooltip_SennaBunny_Prodigy_Tier3.png', 15016: 'Tooltip_SennaBunny_ShadowBeat_Tier1.png', 15017: 'Tooltip_SennaBunny_ShadowBeat_Tier2.png', 15018: 'Tooltip_SennaBunny_ShadowBeat_Tier3.png', 15019: 'Tooltip_SennaBunny_SpiritBlossomKami_Tier1.png', 15020: 'Tooltip_SennaBunny_SpiritBlossomKami_Tier2.png', 15021: 'Tooltip_SennaBunny_SpiritBlossomKami_Tier3.png', 15022: 'Tooltip_SennaBunny_SpiritBlossomYokai_Tier1.png', 15023: 'Tooltip_SennaBunny_SpiritBlossomYokai_Tier2.png', 15024: 'Tooltip_SennaBunny_SpiritBlossomYokai_Tier3.png', 9016: 'Tooltip_SpiritFox_Eternal_Tier1.png', 9017: 'Tooltip_SpiritFox_Eternal_Tier2.png', 9018: 'Tooltip_SpiritFox_Eternal_Tier3.png', 9004: 'Tooltip_SpiritFox_Fae_Tier1.png', 9005: 'Tooltip_SpiritFox_Fae_Tier2.png', 9006: 'Tooltip_SpiritFox_Fae_Tier3.png', 9025: 'Tooltip_SpiritFox_KDAAhri_KDA1_Tier1.png', 9026: 'Tooltip_SpiritFox_KDAAhri_KDA1_Tier2.png', 9027: 'Tooltip_SpiritFox_KDAAhri_KDA1_Tier3.png', 9028: 'Tooltip_SpiritFox_KDAAhri_KDA2_Tier1.png', 9029: 'Tooltip_SpiritFox_KDAAhri_KDA2_Tier2.png', 9030: 'Tooltip_SpiritFox_KDAAhri_KDA2_Tier3.png', 9010: 'Tooltip_SpiritFox_Mistberry_Tier1.png', 9011: 'Tooltip_SpiritFox_Mistberry_Tier2.png', 9012: 'Tooltip_SpiritFox_Mistberry_Tier3.png', 9007: 'Tooltip_SpiritFox_Monarch_Tier1.png', 9008: 'Tooltip_SpiritFox_Monarch_Tier2.png', 9009: 'Tooltip_SpiritFox_Monarch_Tier3.png', 9001: 'Tooltip_SpiritFox_Moontipped_Tier1.png', 9002: 'Tooltip_SpiritFox_Moontipped_Tier2.png', 9003: 'Tooltip_SpiritFox_Moontipped_Tier3.png', 9019: 'Tooltip_SpiritFox_SpiritBlossomKami_Tier1.png', 9020: 'Tooltip_SpiritFox_SpiritBlossomKami_Tier2.png', 9021: 'Tooltip_SpiritFox_SpiritBlossomKami_Tier3.png', 9022: 'Tooltip_SpiritFox_SpiritBlossomYokai_Tier1.png', 9023: 'Tooltip_SpiritFox_SpiritBlossomYokai_Tier2.png', 9024: 'Tooltip_SpiritFox_SpiritBlossomYokai_Tier3.png', 9013: 'Tooltip_SpiritFox_Untamed_Tier1.png', 9014: 'Tooltip_SpiritFox_Untamed_Tier2.png', 9015: 'Tooltip_SpiritFox_Untamed_Tier3.png', 15: 'Tooltip_TFTAvatar_Set6LaunchBattlePass_Arcane_Tier1.png', 6: 'Tooltip_TFTAvatar_Set5LaunchBattlePass_Chaos_Tier1.png', 1: 'Tooltip_TFT_Avatar_Blue.png', 17: 'Tooltip_TFTAvatar_Set7LaunchBattlePass_Egg_Tier1.LL_TFTAvatar_Set7LaunchBattlePass.png', 18: 'Tooltip_TFTAvatar_HotSpring_HotSpring_Tier1.LL_TFTAvatar_HotSpring.png', 5: 'Tooltip_TFTAvatar_Set4UpdateBattlePass_Journeys_Tier1.png', 14: 'Tooltip_TFTAvatar_Set5UpdateBattlePass_Order_Tier1.png', 16: 'Tooltip_TFTAvatar_Set6UpdateBattlePass_ProgressDay_Tier1.png', 4: 'Tooltip_TFTAvatar_Sprite_Tier1.png', 3: 'Tooltip_TFT_Avatar_StarGuardian.png', 19: 'Tooltip_TFTAvatar_SuperHero_SuperHero1_Tier1.LL_TFTAvatar_SuperHero.png', 2: 'Tooltip_TFT_Avatar_UFO.png', 8007: 'Tooltip_Turtle_Caldera_Tier1.png', 8008: 'Tooltip_Turtle_Caldera_Tier2.png', 8009: 'Tooltip_Turtle_Caldera_Tier3.png', 8004: 'Tooltip_Turtle_Glamorous_Tier1.png', 8005: 'Tooltip_Turtle_Glamorous_Tier2.png', 8006: 'Tooltip_Turtle_Glamorous_Tier3.png', 8001: 'Tooltip_Turtle_Jade_Tier1.png', 8002: 'Tooltip_Turtle_Jade_Tier2.png', 8003: 'Tooltip_Turtle_Jade_Tier3.png', 8013: 'Tooltip_Turtle_Rosebloom_Tier1.png', 8014: 'Tooltip_Turtle_Rosebloom_Tier2.png', 8015: 'Tooltip_Turtle_Rosebloom_Tier3.png', 8019: 'Tooltip_Turtle_SpiritFairy_SpiritFairy1_Tier1.png', 8020: 'Tooltip_Turtle_SpiritFairy_SpiritFairy1_Tier2.png', 8021: 'Tooltip_Turtle_SpiritFairy_SpiritFairy1_Tier3.png', 8022: 'Tooltip_Turtle_SpiritFairy_SpiritFairy2_Tier1.png', 8023: 'Tooltip_Turtle_SpiritFairy_SpiritFairy2_Tier2.png', 8024: 'Tooltip_Turtle_SpiritFairy_SpiritFairy2_Tier3.png', 8025: 'Tooltip_Turtle_SpiritFairy_SpiritFairy3_Tier1.png', 8026: 'Tooltip_Turtle_SpiritFairy_SpiritFairy3_Tier2.png', 8027: 'Tooltip_Turtle_SpiritFairy_SpiritFairy3_Tier3.png', 8028: 'Tooltip_Turtle_SpiritFairy_SpiritFairy4_Tier1.png', 8029: 'Tooltip_Turtle_SpiritFairy_SpiritFairy4_Tier2.png', 8030: 'Tooltip_Turtle_SpiritFairy_SpiritFairy4_Tier3.png', 8031: 'Tooltip_Turtle_SpiritFairy_SpiritFairy5_Tier1.png', 8032: 'Tooltip_Turtle_SpiritFairy_SpiritFairy5_Tier2.png', 8033: 'Tooltip_Turtle_SpiritFairy_SpiritFairy5_Tier3.png', 8010: 'Tooltip_Turtle_Tidepool_Tier1.png', 8011: 'Tooltip_Turtle_Tidepool_Tier2.png', 8012: 'Tooltip_Turtle_Tidepool_Tier3.png', 8016: 'Tooltip_Turtle_Yuletide_Tier1.png', 8017: 'Tooltip_Turtle_Yuletide_Tier2.png', 8018: 'Tooltip_Turtle_Yuletide_Tier3.png', 26004: 'Tooltip_Umbra_BlackMist_Tier1.png', 26005: 'Tooltip_Umbra_BlackMist_Tier2.png', 26006: 'Tooltip_Umbra_BlackMist_Tier3.png', 26013: 'Tooltip_Umbra_BloodMoon_Tier1.png', 26014: 'Tooltip_Umbra_BloodMoon_Tier2.png', 26015: 'Tooltip_Umbra_BloodMoon_Tier3.png', 26025: 'Tooltip_Umbra_RPG_Chaos_Tier1.png', 26026: 'Tooltip_Umbra_RPG_Chaos_Tier2.png', 26027: 'Tooltip_Umbra_RPG_Chaos_Tier3.png', 26001: 'Tooltip_Umbra_Classic_Tier1.png', 26002: 'Tooltip_Umbra_Classic_Tier2.png', 26003: 'Tooltip_Umbra_Classic_Tier3.png', 26007: 'Tooltip_Umbra_FruityTooty_Tier1.png', 26008: 'Tooltip_Umbra_FruityTooty_Tier2.png', 26009: 'Tooltip_Umbra_FruityTooty_Tier3.png', 26016: 'Tooltip_Umbra_Hexgold_Tier1.png', 26017: 'Tooltip_Umbra_Hexgold_Tier2.png', 26018: 'Tooltip_Umbra_Hexgold_Tier3.png', 26022: 'Tooltip_Umbra_RPG_Neutral_Tier1.png', 26023: 'Tooltip_Umbra_RPG_Neutral_Tier2.png', 26024: 'Tooltip_Umbra_RPG_Neutral_Tier3.png', 26019: 'Tooltip_Umbra_RPG_Order_Tier1.png', 26020: 'Tooltip_Umbra_RPG_Order_Tier2.png', 26021: 'Tooltip_Umbra_RPG_Order_Tier3.png', 26028: 'Tooltip_Umbra_PoolParty_Swimming1_Tier1.LL_Umbra_PoolParty.png', 26029: 'Tooltip_Umbra_PoolParty_Swimming1_Tier2.LL_Umbra_PoolParty.png', 26030: 'Tooltip_Umbra_PoolParty_Swimming1_Tier3.LL_Umbra_PoolParty.png', 26031: 'Tooltip_Umbra_PoolParty_Swimming2_Tier1.LL_Umbra_PoolParty.png', 26032: 'Tooltip_Umbra_PoolParty_Swimming2_Tier2.LL_Umbra_PoolParty.png', 26033: 'Tooltip_Umbra_PoolParty_Swimming2_Tier3.LL_Umbra_PoolParty.png', 26034: 'Tooltip_Umbra_PoolParty_Swimming3_Tier1.LL_Umbra_PoolParty.png', 26035: 'Tooltip_Umbra_PoolParty_Swimming3_Tier2.LL_Umbra_PoolParty.png', 26036: 'Tooltip_Umbra_PoolParty_Swimming3_Tier3.LL_Umbra_PoolParty.png', 26037: 'Tooltip_Umbra_PoolParty_Swimming4_Tier1.LL_Umbra_PoolParty.png', 26038: 'Tooltip_Umbra_PoolParty_Swimming4_Tier2.LL_Umbra_PoolParty.png', 26039: 'Tooltip_Umbra_PoolParty_Swimming4_Tier3.LL_Umbra_PoolParty.png', 26040: 'Tooltip_Umbra_PoolParty_Swimming5_Tier1.LL_Umbra_PoolParty.png', 26041: 'Tooltip_Umbra_PoolParty_Swimming5_Tier2.LL_Umbra_PoolParty.png', 26042: 'Tooltip_Umbra_PoolParty_Swimming5_Tier3.LL_Umbra_PoolParty.png', 26010: 'Tooltip_Umbra_Thunderbeast_Tier1.png', 26011: 'Tooltip_Umbra_Thunderbeast_Tier2.png', 26012: 'Tooltip_Umbra_Thunderbeast_Tier3.png'}
    return pet[id]

def Item_K(name):
    item = {
    'TFT_Consumable_NeekosHelp': '챔피언 복제기',
    'TFT_Item_BFSword': 'B.F. 대검', 
    'TFT_Item_Bloodthirster': '피바라기', 
    'TFT_Item_BrambleVest': '덤불 조끼', 
    'TFT_Item_ChainVest': '쇠사슬 조끼', 
    'TFT_Item_SparringGloves': '연습용 장갑',
    'TFT_Item_Deathblade': '죽음의 검',
    'TFT_Item_DragonsClaw': '용의 발톱', 
    'TFT_Item_EmptyBag': '',
    'TFT_Item_ForceOfNature': '전략가의 왕관',
    'TFT_Item_ThiefsGloves': '도적의 장갑',
    'TFT_Item_ThiefsGloves_Empty': '', 
    'TFT_Item_Shroud': '침묵의 장막',
    'TFT_Item_FrozenHeart': '수호자의 맹세', 
    'TFT_Item_GiantsBelt': '거인의 허리띠', 
    'TFT_Item_MadredsBloodrazor': '거인 학살자', 
    'TFT_Item_GuardianAngel': '밤의 끝자락', 
    'TFT_Item_GuinsoosRageblade': '구인수의 격노검',
    'TFT_Item_UnstableConcoction': '정의의 손길', 
    'TFT_Item_HextechGunblade': '마법공학 총검', 
    'TFT_Item_Chalice': '힘의 성배', 
    'TFT_Item_InfinityEdge': '무한의 대검', 
    'TFT_Item_IonicSpark': '이온 충격기',
    'TFT_Item_JeweledGauntlet': '보석 건틀릿', 
    'TFT_Item_LastWhisper': '최후의 속삭임',
    'TFT_Item_LocketOfTheIronSolari': '강철의 솔라리 펜던트',
    'TFT_Item_ArchangelsStaff': '대천사의 지팡이',
    'TFT_Item_Spatula': '뒤집개', 
    'TFT_Item_Quicksilver': '수은', 
    'TFT_Item_Morellonomicon': '모렐로노미콘',
    'TFT_Item_NeedlesslyLargeRod': '쓸데없이 큰 지팡이', 
    'TFT_Item_NegatronCloak': '음전자 망토',
    'TFT_Item_PowerGauntlet': '방패파괴자', 
    'TFT_Item_RabadonsDeathcap': '라바돈의 죽음모자', 
    'TFT_Item_RapidFireCannon': '고속 연사포', 
    'TFT_Item_RecurveBow': '곡궁', 
    'TFT_Item_RedBuff': '태양불꽃 망토', 
    'TFT_Item_Redemption': '구원',
    'TFT_Item_RunaansHurricane': '루난의 허리케인', 
    'TFT_Item_SeraphsEmbrace': '푸른 파수꾼',
    'TFT_Item_SpearOfShojin': '쇼진의 창', 
    'TFT_Item_StatikkShiv': '스태틱의 단검',
    'TFT_Item_GargoyleStoneplate': '가고일 돌갑옷',
    'TFT_Item_TearOfTheGoddess': '여신의 눈물',
    'TFT_Item_TitanicHydra': '즈롯 차원문',
    'TFT_Item_TitansResolve': '거인의 결의',
    'TFT_Item_WarmogsArmor': '워모그의 갑옷',
    'TFT_Item_ZekesHerald': '지크의 전령',
    'TFT_Item_Zephyr': '서풍', 
    'TFT_Consumable_ItemRemover': '자석 제거기',
    'TFT_Consumable_ItemReroller': '재조합기', 
    'TFT_Consumable_ShopReroller': '사기 주사위', 
    'TFT4_Item_OrnnAnimaVisage': '영혼의 형상',
    'TFT4_Item_OrnnDeathsDefiance': '죽음의 저항', 
    'TFT4_Item_OrnnEternalWinter': '영원한 겨울',
    'TFT4_Item_OrnnTheCollector': '황금 징수의 총', 
    'TFT4_Item_OrnnInfinityForce': '무한한 삼위일체',
    'TFT4_Item_OrnnMuramana': '마나자네', 
    'TFT4_Item_OrnnObsidianCleaver': '흑요석 양날 도끼',
    'TFT4_Item_OrnnRanduinsSanctum': '란두인의 성소', 
    'TFT4_Item_OrnnRocketPropelledFist': '로켓 주먹', 
    'TFT4_Item_OrnnZhonyasParadox': '존야의 역설',
    'TFT5_Item_TrapClawRadiant': '의지파괴자',
    'TFT5_Item_BloodthirsterRadiant': '축복받은 피바라기',
    'TFT5_Item_BlueBuffRadiant': '푸른 축복',
    'TFT5_Item_ChaliceOfPowerRadiant': '선의의 성배', 
    'TFT5_Item_IonicSparkRadiant': '집단 충격기', 
    'TFT5_Item_GiantSlayerRadiant': '악마 학살자',
    'TFT5_Item_DragonsClawRadiant': '용의 의지',
    'TFT5_Item_GargoyleStoneplateRadiant': '수호상 돌갑옷',
    'TFT5_Item_LastWhisperRadiant': '영겁의 속삭임',
    'TFT5_Item_HandOfJusticeRadiant': '공정의 주먹',
    'TFT5_Item_FrozenHeartRadiant': '철갑의 서약',
    'TFT5_Item_JeweledGauntletRadiant': '눈부신 건틀릿', 
    'TFT5_Item_GuardianAngelRadiant': '새벽의 서광',
    'TFT5_Item_GuinsoosRagebladeRadiant': '구인수의 심판', 
    'TFT5_Item_HextechGunbladeRadiant': '마법공학 생명검',
    'TFT5_Item_LocketOfTheIronSolariRadiant': '타곤 정상의 펜던트', 
    'TFT5_Item_DeathbladeRadiant': '빛나는 죽음의 검', 
    'TFT5_Item_ZephyrRadiant': '겨울바람',
    'TFT5_Item_MorellonomiconRadiant': '엔젤로노미콘', 
    'TFT5_Item_QuicksilverRadiant': '반짝이는 수은', 
    'TFT5_Item_RabadonsDeathcapRadiant': '라바돈의 초월한 죽음모자',
    'TFT5_Item_RedemptionRadiant': '면죄', 
    'TFT5_Item_RapidFirecannonRadiant': '고속 광자포',
    'TFT5_Item_ThiefsGlovesRadiant': '장난꾸러기의 장갑',
    'TFT5_Item_BrambleVestRadiant': '장미가시 조끼',
    'TFT5_Item_RunaansHurricaneRadiant': '루난의 폭풍', 
    'TFT5_Item_ShroudOfStillnessRadiant': '경외의 장막',
    'TFT5_Item_SpearOfShojinRadiant': '히라나의 창', 
    'TFT5_Item_StatikkShivRadiant': '스태틱의 호의',
    'TFT5_Item_SunfireCapeRadiant': '태양빛 망토',
    'TFT5_Item_TitansResolveRadiant': '거인의 맹세',
    'TFT5_Item_ArchangelsStaffRadiant': '우르프 천사의 지팡이',
    'TFT5_Item_WarmogsArmorRadiant': '워모그의 자부심',
    'TFT5_Item_ZekesHeraldRadiant': '지크의 조화', 
    'TFT5_Item_InfinityEdgeRadiant': '천공의 대검',
    'TFT5_Item_ZzRotPortalRadiant': '즈롯 소환문', 
    'TFT7_Item_ShimmerscaleDeterminedInvestor': '결단력 있는 투자자',
    'TFT7_Item_ShimmerscaleDravensAxe': '드레이븐의 도끼', 
    'TFT7_Item_ShimmerscaleMogulsMail': '거물의 갑옷',
    'TFT7_Item_ShimmerscaleGamblersBlade': '도박꾼의 칼날',
    'TFT7_Item_ShimmerscaleHeartOfGold': '쓸데없이 큰 보석', 
    'TFT7_Item_ShimmerscaleGoldmancersStaff': '황금술사의 지팡이', 
    'TFT7_Item_ShimmerscaleDiamondHands': '다이아몬드 손',
    'TFT8_Item_AnimaSquadEmblemItem': '동물특공대 상징',
    'TFT8_Item_CivilianEmblemItem': '민간인 상징', 
    'TFT8_Item_StarGuardianEmblemItem': '별 수호자 상징',
    'TFT8_Item_InterPolarisEmblemItem': '레이저단 상징', 
    'TFT8_Item_OxForceEmblemItem': '황소부대 상징', 
    'TFT8_Item_UndergroundTheEmblemItem': '지하세계 상징',
    'TFT8_Item_GenAEEmblemItem': '기계유망주 상징', 
    'TFT8_Item_ADMINEmblemItem': '자동방어체계 문장',
    'TFT8_Item_MascotEmblemItem': '마스코트 상징',
    'TFT8_Item_DefenderEmblemItem': '엄호대 상징',
    'TFT8_Item_ReconEmblemItem': '정찰단 상징',
    'TFT8_Item_RenegadeEmblemItem': '무법자 상징',
    'TFT8_Item_BrawlerEmblemItem': '싸움꾼 상징', 
    'TFT8_Item_HackerEmblemItem': '해커 상징', 
    'TFT8_Item_DuelistEmblemItem': '결투가 상징',
    'TFT8_Item_HeartEmblemItem': '선의 상징',
    'TFT8_Item_PranksterEmblemItem': '익살꾼 상징',
    'TFT8_Item_DeadeyeEmblemItem': '특등사수 상징',
    'TFT8_Item_GiantSlayer_GenAE': '과부하_ 오류 // 거인 학살자 ',
    'TFT8_Item_HandOfJustice_GenAE': '비결정적 정의의 손길',
    'TFT8_Item_RapidFireCannon_GenAE': '용수철이 든 고속 연사포',
    'TFT8_Item_Shojin_GenAE': '날뛰는 쇼진의 창',
    'TFT8_Item_Shroud_GenAE': '더 고요한 침묵의 장막',
    'TFT8_Item_Sunfire_GenAE': '과열된 태양불꽃 망토', 
    'TFT8_Item_Warmogs_GenAE': '유도집전형 워모그의 갑옷', 
    'TFT8_Item_ArsenalRedGun': '맹공',
    'TFT8_AdminEffect_Mana': '마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득', 
    'TFT8_Item_ArsenalBlueGun': '황혼파',
    'TFT8_AdminCause_OnCast': '', 
    'TFT8_Item_ArsenalPurpleGun': '속박의 월식', 
    'TFT8_AdminCause_CombatStart': '전투 시작: ', 
    'TFT8_AdminCause_EveryXAttacks': '', 
    'TFT8_AdminCause_EveryXSeconds': '', 
    'TFT8_AdminCause_HealthThreshold': '',
    'TFT8_AdminCause_OnEnemyDeath': '',
    'TFT8_AdminEffect_AttackSpeed': '공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminEffect_GainAP': '주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminEffect_Gold': '@TFTUnitProperty.item:TFT8_Admin_GoldChance@% 확률로 골드 획득',
    'TFT8_AdminEffect_Shield': '체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_Item_ExoPrimeEmblemItem': '메카: 프라임 상징',
    'TFT8_Item_AceEmblemItem': '에이스 상징',
    'TFT_Assist_Gold_5': '5골드',
    'TFT_Assist_Gold_6': '6골드',
    'TFT_Assist_Gold_7': '7골드',
    'TFT_Assist_Gold_8': '8골드',
    'TFT_Assist_Gold_10': '10골드',
    'TFT_Assist_Gold_16': '16골드',
    'TFT8_AdminCause_AllyDeath': '',
    'TFT8_AdminEffect_GainAD': '공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminEffect_Heal': '체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminEffect_PermanentHealth': '최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminEffect_SingleTargetDamage': '자동방어체계 유닛의 현재 대상에게 고정 피해를 입히는 미사일 발사',
    'TFT_Assist_Gold_34': '34골드',
    'TFT_Assist_Gold_18': '18골드',
    'TFT_Assist_Gold_22': '22골드', 
    'TFT_Assist_Gold_54': '54골드',
    'TFT_Assist_Gold_12': '12골드',
    'TFT_Assist_Gold_20': '20골드',
    'TFT_Assist_Gold_24': '24골드',
    'TFT_Assist_Gold_36': '36골드',
    'TFT_Assist_Gold_76': '76골드',
    'TFT_Assist_Gold_30': '30골드',
    'TFT_Assist_Gold_25': '25골드',
    'TFT_Assist_Gold_40': '40골드',
    'TFT_Assist_Gold_100': '100골드',
    'TFT_Assist_Gold_26': '26골드',
    'TFT_Assist_Gold_126': '126골드',
    'TFT_Assist_Gold_44': '44골드',
    'TFT_Assist_Gold_64': '64골드',
    'TFT_Assist_Gold_154': '154골드',
    'TFT8_Item_ChannelerEmblemItem': '주문투척자 상징',
    'TFT_Random_5_Cost': '감옥 탈출!',
    'TFT_Random_Two_Star_4_Cost': '감옥 탈출!',
    'TFT8_Consumable_ExoPrime_PrimeMarker': '프라임 선택기',
    'TFT8_Item_AegisEmblemItem': '방패대 상징',
    'TFT8_AdminCauseEffect_AllyDeath_GainAP': '아군 사망 시 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_PermanentHealth': '체력이 40%일 때 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_OnCast_AttackSpeed': '스킬 사용 시 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_AllyDeath_GainMana': '아군 사망 시 자동방어체계 유닛이 마나 @TFTUnitProperty.trait:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_AllyDeath_Shield': '아군 자동방어체계 유닛 사망 시 최대 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_AllyDeath_AttackSpeed': '아군 사망 시 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_AllyDeath_Heal': '아군 사망 시 자동방어체계 유닛이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_AllyDeath_GainAD': '아군 사망 시 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_AllyDeath_PermanentHealth': '아군 사망 시 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_OnCast_GainAP': '스킬 사용 시 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_OnCast_Mana': '스킬 사용 시 자동방어체계 유닛이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_OnCast_Shield': '스킬 사용 시 자동방어체계 유닛이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_OnCast_Heal': '스킬 사용 시 자동방어체계 유닛이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_OnCast_GainAD': '스킬 사용 시 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_GainAP': '3번째 기본 공격을 할 때마다 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_Mana': '3번째 기본 공격을 할 때마다 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득', 
    'TFT8_AdminCauseEffect_EveryXAttacks_Shield': '3번째 기본 공격을 할 때마다 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_AttackSpeed': '3번째 기본 공격을 할 때마다 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_Heal': '3번째 기본 공격을 할 때마다 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_EveryXAttacks_GainAD': '3번째 기본 공격을 할 때마다 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_EveryXAttacks_PermanentHealth': '3번째 기본 공격을 할 때마다 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_OnKill_GainAP': '처치 시 처치자가 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_OnKill_Mana': '처치 시 처치자가 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득', 
    'TFT8_AdminCauseEffect_OnKill_Shield': '처치 시 처치자가 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득', 
    'TFT8_AdminCauseEffect_OnKill_AttackSpeed': '처치 시 처치자가 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득', 
    'TFT8_AdminCauseEffect_OnKill_Heal': '처치 시 처치자가 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_OnKill_GainAD': '처치 시 처치자가 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득', 
    'TFT8_AdminCauseEffect_OnKill_PermanentHealth': '처치 시 처치자가 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득', 
    'TFT8_AdminCauseEffect_HealthThreshold_GainAP': '체력이 40%일 때 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_Mana': '체력이 40%일 때 자동방어체계 유닛이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_Shield': '체력이 40%일 때 자동방어체계 유닛이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_AttackSpeed': '체력이 40%일 때 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_HealthThreshold_Heal': '체력이 40%일 때 자동방어체계 유닛이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_HealthThreshold_GainAD': '체력이 40%일 때 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_CombatStart_GainAP': '전투 시작: 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_CombatStart_Mana': '전투 시작: 자동방어체계 유닛이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_CombatStart_Shield': '전투 시작: 자동방어체계 유닛이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_CombatStart_AttackSpeed': '전투 시작: 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_CombatStart_GainAD': '전투 시작: 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_CombatStart_PermanentHealth': '전투 시작: 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_GainAP': '5초마다 자동방어체계 유닛이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_Mana': '5초마다 자동방어체계 유닛이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_Shield': '5초마다 자동방어체계 유닛이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_AttackSpeed': '5초마다 자동방어체계 유닛이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_Heal': '5초마다 자동방어체계 유닛이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_EveryXSeconds_GainAD': '5초마다 자동방어체계 유닛이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_EveryXSeconds_PermanentHealth': '5초마다 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_Item_Bloodthirster_GenAE': '톱날 피바라기',
    'TFT8_AdminCauseEffect_OnCast_PermanentHealth': '스킬 사용 시 자동방어체계 유닛이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_Item_IonicSpark_GenAE': '자화 이온 충격기', 'TFT8_AdminCause_CombatStartTeam': '전투 시작: ',
    'TFT8_AdminCause_EveryXSecondsTeam': '전투 시작: ',
    'TFT8_AdminCauseEffect_CombatStartTeam_AttackSpeed': '전투 시작: 아군이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_GainAD': '전투 시작: 아군이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_GainAP': '전투 시작: 아군이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_Mana': '전투 시작: 아군이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_PermHP': '전투 시작: 아군이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT8_AdminCauseEffect_CombatStartTeam_Shield': '전투 시작: 아군이 체력의 @TFTUnitProperty.item:TFT8_Admin_ShieldAmount@%만큼 피해를 흡수하는 보호막 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_AttackSpeed': '5초마다 아군이 공격 속도 @TFTUnitProperty.item:TFT8_Admin_ASAmount@% 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_GainAD': '5초마다 아군이 공격력 @TFTUnitProperty.item:TFT8_Admin_ADGained@% 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_GainAP': '5초마다 아군이 주문력 @TFTUnitProperty.item:TFT8_Admin_APGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_Heal': '5초마다 아군이 체력 @TFTUnitProperty.item:TFT8_Admin_HealAmount@ 회복',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_Mana': '5초마다 아군이 마나 @TFTUnitProperty.item:TFT8_Admin_ManaGained@ 획득',
    'TFT8_AdminCauseEffect_EveryXSecsTeam_PermHP': '5초마다 아군이 최대 체력 @TFTUnitProperty.item:TFT8_Admin_PermanentHealthPerActivation@만큼 영구히 획득',
    'TFT_Item_GrantCompletedAnvil': '완성 아이템 열쇠',
    'TFT_Item_GrantComponentAnvil': '조합 아이템 열쇠',
    'TFT_Item_GrantTomeOfTraits': '특성의 고서', 
    'TFT_Item_GrantCompletedItem1': '완성 아이템 1개',
    'TFT_Item_GrantCompletedItem2': '완성 아이템 @ItemsToGive@개',
    'TFT_Item_GrantCompletedItem3': '완성 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent1': '조합 아이템 1개',
    'TFT_Item_GrantComponent2': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent3': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent4': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent5': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent6': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent7': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent8': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantComponent9': '조합 아이템 @ItemsToGive@개',
    'TFT_Item_GrantOrbs1': '전리품 구 1개',
    'TFT_Item_GrantOrnnAnvil': '오른의 아이템 모루'
    }

    return item[name]

def champ_K(name):
    champ = {
    "TFT8_Kaisa" : "카이사",
    "TFT8_Lux" : "럭스",
    "TFT8_Kayle" : "케일",
    "TFT8_Poppy" : "뽀삐",
    "TFT8_Galio" : "갈리오",
    "TFT8_Rell" : "렐",
    "TFT8_Velkoz" : "벨코즈",
    "TFT8_Nilah" : "닐라",
    "TFT8_Ashe" : "애쉬",
    "TFT8_Yasuo" : "야스오",
    "TFT8_Senna" : "세나",
    "TFT8_Zed" : "제드",
    "TFT8_Lulu" : "룰루",
    "TFT8_Nunu" : "누누",
    "TFT8_Yuumi" : "유미",
    "TFT8_Zoe" : "조이",
    "TFT8_Taliyah" : "탈리야",
    "TFT8_Sivir" : "시비르",
    "TFT8_Gangplank" : "갱플랭크",
    "TFT8_WuKong" : "오공",
    "TFT8_Draven" : "드레이븐",
    "TFT8_Malphite" : "말파이트",
    "TFT8_Nasus" : "나서스",
    "TFT8_Jinx" : "징크스",
    "TFT8_Vayne" : "베인",
    "TFT8_MissFortune" : "미스포츈",
    "TFT8_Chogath" : "초가스",
    "TFT8_Rammus" : "람머스",
    "TFT8_BelVeth" : "벨베스",
    "TFT8_AurelionSol" : "아우렐리온솔",
    "TFT8_Zac" : "자크",
    "TFT8_Mordekaiser" : "모데카이저",
    "TFT8_Leblanc" : "르블랑",
    "TFT8_Sylas" : "사일러스",
    "TFT8_Camille" : "카밀",
    "TFT8_Ezreal" : "이즈리얼",
    "TFT8_Sona" : "소나",
    "TFT8_Ekko" : "에코",
    "TFT8_Sett" : "세트",
    "TFT8_Janna" : "잔나",
    "TFT8_Urgot" : "우르곳",
    "TFT8_Syndra" : "신드라",
    "TFT8_Fiddlesticks" : "피들스틱",
    "TFT8_Blitzcrank" : "블리츠크랭크",
    "TFT8_Renekton" : "레넥톤",
    "TFT8_Vi" : "바이",
    "TFT8_LeeSin" : "리신",
    "TFT8_Riven" : "리븐",
    "TFT8_Jax" : "잭스",
    "TFT8_Sejuani" : "세주아니",
    "TFT8_Soraka" : "소라카",
    "TFT8_Talon" : "탈론",
    "TFT8_Fiora" : "피오라",
    "TFT8_Annie" : "애니",
    "TFT8_Alistar" : "알리스타",
    "TFT8_Viego" : "비에고",
    "TFT8_Samira" : "사미라",
    "TFT8_Aphelios" : "아펠리오스",
    "TFT8_Leona" : "레오나"
    }

    return champ[name]

def Aug_K(name):
    augments = {
    'TFT6_augment_PandorasItem' : '판도라의 아이템',
    'TFT6_Augment_ForceOfNature': '신병',
    'TFT6_Augment_FirstAidKit': '응급처치 키트1',
    'TFT6_Augment_MaxLevel10': '레벨 업!',
    'TFT6_Augment_ItemGrabBag1': '아이템 꾸러미1',
    'TFT6_Augment_ItemGrabBag2': '아이템 꾸러미2',
    'TFT6_Augment_Windfall': '뜻밖의 횡재',
    'TFT6_Augment_GrandGambler': '큰손',
    'TFT6_Augment_CalculatedLoss': '계산된 패배',
    'TFT6_Augment_SalvageBin': '재활용 쓰레기통',
    'TFT6_Augment_SlowAndSteady': '진보의 행진',
    'TFT6_Augment_PortableForge': '휴대용 대장간',
    'TFT6_Augment_HighEndShopping': '품격있는 쇼핑',
    'TFT6_Augment_Diversify1': '단결된 의지1',
    'TFT6_Augment_Diversify2': '단결된 의지2',
    'TFT6_Augment_Diversify3': '단결된 의지3',
    'TFT6_Augment_BandOfThieves2': '도둑 무리2',
    'TFT6_Augment_Featherweights1': '경량급1',
    'TFT6_Augment_Featherweights2': '경량급2',
    'TFT6_Augment_Featherweights3': '경량급3',
    'TFT6_Augment_HyperRoll': '수완가',
    'TFT6_Augment_MetabolicAccelerator': '대사 촉진제',
    'TFT6_Augment_MakeshiftArmor1': '임시변통 방어구1',
    'TFT6_Augment_MakeshiftArmor2': '임시변통 방어구2',
    'TFT6_Augment_Ascension': '초월',
    'TFT6_Augment_BinaryAirdrop': '이중 공중 보급',
    'TFT6_Augment_ClearMind': '맑은 정신',
    'TFT6_Augment_ThriftShop': '현명한 소비',
    'TFT6_Augment_Recombobulator': '대격변 생성기',
    'TFT6_Augment_RadiantRelics': '찬란한 유물',
    'TFT6_Augment_JeweledLotus': '보석 연꽃',
    'TFT6_Augment_VerdantVeil': '신록의 장막',
    'TFT6_Augment_TinyTitans': '꼬마 거인',
    'TFT6_Augment_ComponentGrabBag': '재료 꾸러미',
    'TFT6_Augment_Twins2': '문제가 두 배2',
    'TFT6_Augment_Twins3': '문제가 두 배3',
    'TFT6_Augment_FuturePeepers2': '예견2',
    'TFT6_Augment_TrueTwos': '곱빼기',
    'TFT6_Augment_TriForce1': '3에 깃든 힘1',
    'TFT6_Augment_TriForce2': '3에 깃든 힘2',
    'TFT6_Augment_TriForce3': '3에 깃든 힘3',
    'TFT6_Augment_TheGoldenEgg': '황금 알',
    'TFT7_Augment_ThinkFast': '빠른 판단',
    'TFT7_Augment_Bloodlust1': '전투 훈련',
    'TFT7_Augment_SacrificialPact': '잔혹한 계약',
    'TFT7_Augment_PandorasBench': '판도라의 대기석',
    'TFT7_Augment_AxiomArc2': '원칙의 원형낫2',
    'TFT7_Augment_ClutteredMind': '어수선한 마음',
    'TFT6_Augment_TradeSector': '교환의 장',
    'TFT6_Augment_Distancing': '추방자1',
    'TFT6_Augment_Distancing2': '추방자2',
    'TFT6_Augment_ThreesCompany': '삼총사',
    'TFT7_Augment_UrfsGrabBag2': '우르프의 꾸러미2',
    'TFT7_Augment_LivingForge': '간이 대장간',
    'TFT7_Augment_AFK': '자리 비움',
    'TFT7_Augment_BandOfThieves1': '도둑 무리1',
    'TFT7_Augment_LategameSpecialist': '후반 전문가',
    'TFT7_Augment_Preparation': '준비1',
    'TFT7_Augment_BigFriend': '커다란 친구1',
    'TFT7_Augment_LastStand': '최후의 저항',
    'TFT6_Augment_TargetDummies': '허수아비 전선',
    'TFT7_Augment_CursedCrown': '저주받은 왕관',
    'TFT6_Augment_CyberneticImplants1': '사이버네틱 이식술1',
    'TFT6_Augment_CelestialBlessing1': '천상의 축복1',
    'TFT6_Augment_SecondWind1': '재생의 바람1',
    'TFT6_Augment_CyberneticShell1': '사이버네틱 외피1',
    'TFT6_Augment_CyberneticUplink1': '사이버네틱 통신1',
    'TFT6_Augment_CyberneticImplants3': '사이버네틱 이식술3',
    'TFT6_Augment_CyberneticShell3': '사이버네틱 외피3',
    'TFT6_Augment_CyberneticUplink3': '사이버네틱 통신3',
    'TFT6_Augment_RichGetRicher': '부익부',
    'TFT6_Augment_RichGetRicherPlus': '부익부+',
    'TFT6_Augment_Electrocharge1': '고전압1',
    'TFT6_Augment_LudensEcho1': '루덴의 메아리1',
    'TFT6_Augment_CelestialBlessing2': '천상의 축복2',
    'TFT6_Augment_CelestialBlessing3': '천상의 축복3',
    'TFT6_Augment_SecondWind2': '재생의 바람2',
    'TFT6_Augment_ThrillOfTheHunt1': '사냥의 전율1',
    'TFT6_Augment_ThrillOfTheHunt2': '사냥의 전율2',
    'TFT6_Augment_LudensEcho2': '루덴의 메아리2',
    'TFT6_Augment_LudensEcho3': '루덴의 메아리3',
    'TFT6_Augment_Electrocharge2': '고전압2',
    'TFT6_Augment_Electrocharge3': '고전압3',
    'TFT6_Augment_CyberneticImplants2': '사이버네틱 이식술2',
    'TFT6_Augment_CyberneticShell2': '사이버네틱 외피2',
    'TFT6_Augment_CyberneticUplink2': '사이버네틱 통신2',
    'TFT6_Augment_SunfireBoard': '태양불꽃판',
    'TFT6_Augment_WindfallPlus': '뜻밖의 횡재+',
    'TFT6_Augment_WindfallPlusPlus': '뜻밖의 횡재++',
    'TFT7_Augment_FirstAidKit2': '응급처치 키트2',
    'TFT7_Augment_BigFriend2': '커다란 친구2',
    'TFT7_Augment_Preparation2': '준비2',
    'TFT7_Augment_Preparation3': '준비3',
    'TFT6_Augment_TradeSectorPlus': '교환의 장+',
    'TFT8_Augment_ThreatMaxHealth': '위협 레벨: 최대',
    'TFT8_Augment_AceEmblem': '에이스 문장',
    'TFT8_Augment_AceEmblem2': '에이스 왕관',
    'TFT8_Augment_ADMINEmblem': '자동방어체계 문장',
    'TFT8_Augment_ADMINEmblem2': '자동방어체계 왕관',
    'TFT8_Augment_AnimaSquadEmblem': '동물특공대 문장',
    'TFT8_Augment_AnimaSquadEmblem2': '동물특공대 왕관',
    'TFT8_Augment_BrawlerEmblem': '싸움꾼 문장',
    'TFT8_Augment_BrawlerEmblem2': '싸움꾼 왕관',
    'TFT8_Augment_ChannelerEmblem': '주문투척자 문장',
    'TFT8_Augment_ChannelerEmblem2': '주문투척자 왕관',
    'TFT8_Augment_CivilianEmblem': '민간인 문장',
    'TFT8_Augment_CivilianEmblem2': '민간인 왕관',
    'TFT8_Augment_DeadeyeEmblem': '특등사수 문장',
    'TFT8_Augment_DeadeyeEmblem2': '특등사수 왕관',
    'TFT8_Augment_DefenderEmblem': '엄호대 문장',
    'TFT8_Augment_DefenderEmblem2': '엄호대 왕관',
    'TFT8_Augment_DuelistEmblem': '결투가 문장',
    'TFT8_Augment_DuelistEmblem2': '결투가 왕관',
    'TFT8_Augment_ExoPrimeEmblem': '메카: 프라임 문장',
    'TFT8_Augment_ExoPrimeEmblem2': '메카: 프라임 왕관',
    'TFT8_Augment_GenAETrait2': '기계유망주 영혼',
    'TFT8_Augment_AegisEmblem': '방패대 문장',
    'TFT8_Augment_AegisEmblem2': '방패대 왕관',
    'TFT8_Augment_HackerEmblem': '해커 문장',
    'TFT8_Augment_HackerEmblem2': '해커 왕관',
    'TFT8_Augment_HeartEmblem': '선의 문장',
    'TFT8_Augment_HeartEmblem2': '선의 왕관',
    'TFT8_Augment_InterPolarisEmblem': '레이저단 문장',
    'TFT8_Augment_InterPolarisEmblem2': '레이저단 왕관',
    'TFT8_Augment_MascotEmblem': '마스코트 문장',
    'TFT8_Augment_MascotEmblem2': '마스코트 왕관',
    'TFT8_Augment_OxForceEmblem': '황소부대 문장',
    'TFT8_Augment_OxForceEmblem2': '황소부대 왕관',
    'TFT8_Augment_PranksterEmblem': '익살꾼 문장',
    'TFT8_Augment_PranksterEmblem2': '익살꾼 왕관',
    'TFT8_Augment_ReconEmblem': '정찰단 문장',
    'TFT8_Augment_ReconEmblem2': '정찰단 왕관',
    'TFT8_Augment_RenegadeEmblem': '무법자 문장',
    'TFT8_Augment_RenegadeEmblem2': '무법자 왕관',
    'TFT8_Augment_StarGuardianEmblem': '별 수호자 문장',
    'TFT8_Augment_StarGuardianEmblem2': '별 수호자 왕관',
    'TFT8_Augment_UndergroundTheTrait2': '지하세계 영혼',
    'TFT6_Augment_WoodlandCharm': '숲의 부적',
    'TFT7_Augment_LuckyGloves': '행운의 장갑',
    'TFT7_Augment_ScopedWeapons1': '조준경 부착1',
    'TFT6_Augment_Battlemage1': '전투 마법사1',
    'TFT6_Augment_Battlemage2': '전투 마법사2',
    'TFT6_Augment_Battlemage3': '전투 마법사3',
    'TFT6_Augment_MeleeStarBlade1': '나이프의 날1',
    'TFT6_Augment_MeleeStarBlade2': '나이프의 날2',
    'TFT6_Augment_MeleeStarBlade3': '나이프의 날3',
    'TFT7_Augment_BirthdayPresents': '생일 선물',
    'TFT7_Augment_Consistency': '일관성',
    'TFT8_Augment_AnimaSquadTrait': '동물특공대 심장',
    'TFT8_Augment_StarGuardianTrait': '별 수호자 심장',
    'TFT8_Augment_InterPolarisTrait': '레이저단 심장',
    'TFT8_Augment_OxForceTrait': '황소부대 심장',
    'TFT8_Augment_GenAETrait': '기계유망주 심장',
    'TFT8_Augment_MascotTrait': '마스코트 심장',
    'TFT8_Augment_DefenderTrait': '엄호대 심장',
    'TFT8_Augment_ChannelerTrait': '주문투척자 심장',
    'TFT8_Augment_BrawlerTrait': '싸움꾼 심장',
    'TFT8_Augment_DuelistTrait': '결투가 심장',
    'TFT8_Augment_HeartTrait': '선의 심장',
    'TFT8_Augment_DeadeyeTrait': '특등사수 심장',
    'TFT8_Augment_ReconTrait': '정찰단 심장',
    'TFT8_Augment_RenegadeTrait': '무법자 심장',
    'TFT8_Augment_UndergroundTheTrait': '지하세계 심장',
    'TFT8_Augment_SupersTrait': '우세 심장',
    'TFT8_Augment_SupersTrait2': '우세 영혼',
    'TFT8_Augment_ADMINTrait': '자동방어체계 심장',
    'TFT8_Augment_HackerTrait': '해커 심장',
    'TFT6_Augment_TomeOfTraits1': '고대의 기록 보관소1',
    'TFT7_Augment_TomeOfTraits2': '고대의 기록 보관소2',
    'TFT6_Augment_Traitless2': '다른 태생2',
    'TFT6_Augment_Traitless3': '다른 태생3',
    'TFT6_Augment_FuturePeepers': '예견1',
    'TFT6_Augment_GachaAddict': '황금 티켓',
    'TFT8_Augment_BelVethVoidmother': '공허 어미',
    'TFT8_Augment_AurelionSolImpact': '충격 속도',
    'TFT8_Augment_ChoGathMR': '우주의 방어막',
    'TFT8_Augment_RammusArmor': '중무장 아르마딜로',
    'TFT8_Augment_VelkozFrostburn': '동상',
    'TFT8_Augment_ZacSupersize': '거대화',
    'TFT8_Augment_SonaExile': '전력망',
    'TFT8_Augment_SonaSupport': '암류',
    'TFT8_Augment_AlistarAoEPulverizer': '강타!',
    'TFT8_Augment_JaxASCarry': '가차없는 맹공',
    'TFT8_Augment_SennaASCarry': '면죄',
    'TFT8_Augment_NilahReflection': '나눔의 미덕',
    'TFT8_Augment_ZoeDoubleTrouble': '이중 방울',
    'TFT8_Augment_SennaSupport': '레이저단 진형',
    'TFT8_Augment_AlistarBeefUp': '괴수',
    'TFT8_Augment_RivenReverberation': '반향',
    'TFT8_Augment_AnnieCarry': '반사 방패',
    'TFT8_Augment_AnnieSupport': '불타는 영혼',
    'TFT8_Augment_CamilleCarry': '적응형 방어 체계',
    'TFT8_Augment_LeeSinSupport': '고양',
    'TFT8_Augment_RellSupport': '변화의 철마술',
    'TFT8_Augment_YuumiSupport': '슈우우웅!',
    'TFT8_Augment_ViSupport': '권투 교습',
    'TFT8_Augment_SivirSupport': '끝없는 피자',
    'TFT8_Augment_KaisaStarCrossed': '엇갈린 별',
    'TFT8_Augment_YasuoCarry': '흡수의 바람',
    'TFT8_Augment_LeBlancGlitch': '조준 보정',
    'TFT8_Augment_FioraCarry': '전방의 검사',
    'TFT8_Augment_EzrealSupport': '도굴꾼의 전리품',
    'TFT8_Augment_JinxCarry': '신난다!',
    'TFT8_Augment_MalphiteCarry': '견고',
    'TFT8_Augment_NasusCarry': '쌓고 또 쌓고',
    'TFT8_Augment_DravenCarry': '드레이븐의 리그',
    'TFT8_Augment_KaisaCarry': '다중 사격',
    'TFT8_Augment_GalioCarry': '정의의 주먹',
    'TFT8_Augment_GalioSupport': '안전제일',
    'TFT8_Augment_AurelionSolCarry': '대멸종',
    'TFT8_Augment_JaxSupport': '회피',
    'TFT8_Augment_LuxCarry': '눈부신 특이점',
    'TFT8_Augment_PoppyCarry': '더 크고 튼튼한 방패',
    'TFT8_Augment_ApheliosSupport': '발포 준비 완료',
    'TFT8_Augment_LuxSupport': '빛의 방어막',
    'TFT8_Augment_GangplankSupport': '수금',
    'TFT8_Augment_SylasCarry': '국왕시해자',
    'TFT8_Augment_SylasSupport': '페트리사이트 사슬',
    'TFT8_Augment_SettCarry': '펀치 프로토콜',
    'TFT8_Augment_KayleCarry': '거룩한 승천',
    'TFT8_Augment_KayleSupport': '정의로운 사거리',
    'TFT8_Augment_EkkoSupport': '시공간 붕괴',
    'TFT8_Augment_MordekaiserCarry': '헤비하지 않은 메탈',
    'TFT8_Augment_VelkozSupport': '얼어붙은 땅',
    'TFT8_Augment_SettSupport': '재생형 보호막',
    'TFT8_Augment_TalonCarry': '검의 군주',
    'TFT8_Augment_MissFortuneCarry': '토끼 용병',
    'TFT8_Augment_ChoGathCarry': '에너지 공허',
    'TFT8_Augment_SyndraSupport': '예비전력 강화',
    'TFT8_Augment_RammusCarry': '가시박힌 껍질',
    'TFT8_Augment_LeonaCarry': '완벽한 흑점 폭발',
    'TFT8_Augment_NunuSupport': '퍼지는 웃음',
    'TFT8_Augment_FiddlesticksCarry': '끔찍한 기억',
    'TFT8_Augment_UrgotCarry': '반짝반짝',
    'TFT8_Augment_JannaSupport': '과장된 보도',
    'TFT8_Augment_SamiraCarry': '스타일과 재능',
    'TFT8_Augment_TaliyahSupport': '돌처럼 단단하게',
    'TFT8_Augment_ZedSupport': '약자 멸시',
    'TFT8_Augment_BlitzcrankCarry': '동적 방어',
    'TFT8_Augment_UrgotSupport': '밀물',
    'TFT8_Augment_BlitzcrankSupport': '로켓 손',
    'TFT8_Augment_MordekaiserSupport': '말살',
    'TFT8_Augment_ApheliosCarry': '철갑탄',
    'TFT8_Augment_LuluSupport': '성장 촉진',
    'TFT8_Augment_LeonaSupport': '절정의 일식',
    'TFT8_Augment_SejuaniCarry': '빙하 감옥',
    'TFT8_Augment_SyndraCarry': '압도적인 힘',
    'TFT8_Augment_WukongSupport': '재충전',
    'TFT8_Augment_AsheCarry': '레이저단 집중',
    'TFT8_Augment_AsheSupport': '레이저단 몰입',
    'TFT8_Augment_NilahSupport': '승리의 장막',
    'TFT8_Augment_VayneSupport': '한밤의 서곡',
    'TFT8_Augment_RivenSupport': '금의환향',
    'TFT8_Augment_ZoeSupport': '한숨 잘 시간',
    'TFT8_Augment_LeBlancSupport': '거울 환영',
    'TFT8_Augment_LeeSinCarry': '정화의 방호',
    'TFT8_Augment_YuumiCarry': '포식자의 정확성',
    'TFT8_Augment_FiddlesticksSupport': '완전한 타락',
    'TFT8_Augment_PoppySupport': '굳건한 태세',
    'TFT8_Augment_JannaCarry': '신속한 보도',
    'TFT8_Augment_RenegadePartners': '공범',
    'TFT8_Augment_TaliyahCarry': '바위술사',
    'TFT8_Augment_ZedCarry': '그림자술',
    'TFT8_Augment_SivirCarry': '배달팁',
    'TFT8_Augment_RenektonCarry': '분노의 지배',
    'TFT8_Augment_ViCarry': '무자비한 힘',
    'TFT8_Augment_RenektonSupport': '양떼 도륙',
    'TFT8_Augment_RellCarry': '진형 유지',
    'TFT8_Augment_FioraSupport': '황소의 활력',
    'TFT8_Augment_DravenSupport': '무자비한 칼날',
    'TFT8_Augment_YasuoSupport': '추방자의 기백',
    'TFT8_Augment_NasusSupport': '영혼의 포식자',
    'TFT8_Augment_SorakaSupport': '융화',
    'TFT8_Augment_LuluCarry': '급속 성장',
    'TFT8_Augment_SorakaCarry': '업그레이드: 광란',
    'TFT8_Augment_VayneCarry': '확산 사격',
    'TFT8_Augment_MalphiteSupport': '수호자 영혼',
    'TFT8_Augment_BelVethCarry': '피의 복수',
    'TFT8_Augment_EkkoCarry': '공진',
    'TFT8_Augment_GangplankCarry': '불타는 도탄',
    'TFT8_Augment_JinxSupport': '전부 터져라!',
    'TFT8_Augment_MissFortuneSupport': '총알은 비를 타고',
    'TFT8_Augment_CamilleSupport': '마법공학 응징',
    'TFT8_Augment_WukongCarry': '회전격',
    'TFT8_Augment_SejuaniSupport': '산산조각',
    'TFT8_Augment_ZacSupport': '새총 발사',
    'TFT8_Augment_NunuCarry': '눈 굴러가요',
    'TFT8_Augment_ViegoCarry': '심장을 멈추는 자',
    'TFT8_Augment_SamiraSupport': '무모한 자',
    'TFT8_Augment_TalonSupport': '황소부대의 분노',
    'TFT8_Augment_EzrealCarry': '끓어오르는 주문의 힘'
    }

    return augments[name]

def trait_K(name):
    traits={
        "Set8_AnimaSquad" : "동물 특공대",
        "Set8_Aegis" : "방패대",
        "Set8_Brawler" : "싸움꾼",
        "Set8_Civilian" : "민간인",
        "Set8_Duelist" :"결투가", 
        "Set8_GenAE":"기계유망주",
        "Set8_Heart" :"선의",
        "Set8_Mascot": "마스코트",
        "Set8_OxForce": "황소부대",
        "Set8_StarGuardian": "별 수호자",
        "Set8_Supers" : "우세",
        "Set8_Ace" : "에이스",
        "Set8_Defender" : "엄호대",
        "Set8_ExoPrime": "메카: 프라임",
        "Set8_SpaceCorps":"레이저단",
        "Set8_Channeler":"주문투척자",
        "Set8_Forecaster":"기상캐스터",
        "Set8_Prankster":"익살꾼",
        "Set8_Recon" :"정찰단",
        "Set8_UndergroundThe":"지하세계",
        "Set8_Deadeye":"특등사수",
        "Set8_Renegade":"무법자",
        "Set8_Corrupted":"타락",
        "Set8_Threat":"위협",
        "Set8_Arsenal":"병기고",
        "Set8_Hacker":"해커",
        "Set8_Admin":"자동방어체계",

    }
    return traits[name]


class usersAPI(APIView):
    def get(self,request,sname):
        s_name=''
        for i in sname:
            if i!=' ':
                s_name+=i
        matches=match.objects.filter(Q(Name__name__iexact=s_name))
        serializer=matchSerializer(matches,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request,sname):
        key=getAPIkey()
        
        summonername=sname
        
        response=requests.get(f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonername}?api_key={key}') #데이터 불러오기

        if response.status_code==200: # 정상처리
                print('기다려주세요')
                pass

        elif response.status_code==404:#사용자 이름 못찾음
            if user.objects.filter(name=summonername):
                obj = user.objects.filter(name=summonername)
                obj.delete()
            return Response(status=status.HTTP_404_NOT_FOUND)


        elif response.status_code == 429:
            print('api cost full : infinite loop start')
            start_time = time.time()

            while True: # 429error가 끝날 때까지 무한 루프
                    if response.status_code == 429:
                        print('try 10 second wait time')
                        time.sleep(10)
                        url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonername}?api_key={key}'
                        response = requests.get(url)
                        print(response.status_code)

                    elif response.status_code == 200: #다시 response 200이면 loop escape
                        print('total wait time : ', time.time() - start_time)                            
                        print('recovery api cost')
                        break

        elif response.status_code == 503: # 잠시 서비스를 이용하지 못하는 에러
                    print('service available error')
                    start_time = time.time()

                    while True:
                        if response.status_code == 503 or response.status_code == 429:

                            print('try 10 second wait time')
                            time.sleep(10)
                            url = f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summonername}?api_key={key}'
                            response = requests.get(url)
                            print(response.status_code)

                        elif response.status_code == 200: # 똑같이 response가 정상이면 loop escape
                            print('total error wait time : ', time.time() - start_time)
                            print('recovery api cost')
                            break

        elif response.status_code == 403: # api갱신이 필요
                print('you need api renewal')
                print('break')

        data=response.json()
        name=''
        for i in data["name"]:
            if i!=' ':
                name+=i
        
        puuid=data['puuid']
        level=data['summonerLevel']
        profile_icon=data['profileIconId']
        profileid=f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/profileicon/{profile_icon}.png"
        
        u=user(name=name,Puuid=puuid,Level=level,profile_img=profileid)# 유저 테이블에 puuid 와 이름, level저장
        if u in user.objects.all():
            obj = user.objects.filter(name=name)
            obj.delete()
        u.save()

        
        #match id 가져오기
        response_match=requests.get(f'https://asia.api.riotgames.com/tft/match/v1/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={key}')
        ids=response_match.json() #match id들 가져오기
        
        #foreign key
        s_name=user.objects.filter(Puuid=puuid)
        name=s_name[0]


        # 티어 LP 크롤링
        croll=''
        for i in range(0,len(sname)): # 공백제거
            if sname[i]!=' ':
                croll+=sname[i]
        encode = urllib.parse.quote_plus(croll)
        a=requests.get("https://lolchess.gg/profile/kr/"+encode)
        req=a.text
        soup=bs(req,'html.parser')
        #더블업모드 티어 및 LP
        b=soup.find_all('div','tier-ranked-info__content')[1]
        if b.find('strong'):
            tier=b.find('strong').text
            tier=str(tier).strip()
            LP=b.find('span').text
            LP=LP[:-2]

        else:
            tier=b.find('span').text
            LP=0



        # 통계 모델 만들기
        stat=static(Name=name,Level=level,Tier=tier,LP=LP)
        if stat in static.objects.all():
            obj = static.objects.filter(Name=name)
            obj.delete()
        stat.save()
        

        hero_augment=['TFT8_Augment_BelVethVoidmother', 'TFT8_Augment_AurelionSolImpact', 'TFT8_Augment_ChoGathMR', 'TFT8_Augment_RammusArmor', 'TFT8_Augment_VelkozFrostburn', 'TFT8_Augment_ZacSupersize', 'TFT8_Augment_SonaExile', 'TFT8_Augment_SonaSupport', 'TFT8_Augment_AlistarAoEPulverizer', 'TFT8_Augment_JaxASCarry', 'TFT8_Augment_SennaASCarry', 'TFT8_Augment_NilahReflection', 'TFT8_Augment_ZoeDoubleTrouble', 'TFT8_Augment_SennaSupport', 'TFT8_Augment_AlistarBeefUp', 'TFT8_Augment_RivenReverberation', 'TFT8_Augment_AnnieCarry', 'TFT8_Augment_AnnieSupport', 'TFT8_Augment_CamilleCarry', 'TFT8_Augment_LeeSinSupport', 'TFT8_Augment_RellSupport', 'TFT8_Augment_YuumiSupport', 'TFT8_Augment_ViSupport', 'TFT8_Augment_SivirSupport', 'TFT8_Augment_KaisaStarCrossed', 'TFT8_Augment_YasuoCarry', 'TFT8_Augment_LeBlancGlitch', 'TFT8_Augment_FioraCarry', 'TFT8_Augment_EzrealSupport', 'TFT8_Augment_JinxCarry', 'TFT8_Augment_MalphiteCarry', 'TFT8_Augment_NasusCarry', 'TFT8_Augment_DravenCarry', 'TFT8_Augment_KaisaCarry', 'TFT8_Augment_GalioCarry', 'TFT8_Augment_GalioSupport', 'TFT8_Augment_AurelionSolCarry', 'TFT8_Augment_JaxSupport', 'TFT8_Augment_LuxCarry', 'TFT8_Augment_PoppyCarry', 'TFT8_Augment_ApheliosSupport', 'TFT8_Augment_LuxSupport', 'TFT8_Augment_GangplankSupport', 'TFT8_Augment_SylasCarry', 'TFT8_Augment_SylasSupport', 'TFT8_Augment_SettCarry', 'TFT8_Augment_KayleCarry', 'TFT8_Augment_KayleSupport', 'TFT8_Augment_EkkoSupport', 'TFT8_Augment_MordekaiserCarry', 'TFT8_Augment_VelkozSupport', 'TFT8_Augment_SettSupport', 'TFT8_Augment_TalonCarry', 'TFT8_Augment_MissFortuneCarry', 'TFT8_Augment_ChoGathCarry', 'TFT8_Augment_SyndraSupport', 'TFT8_Augment_RammusCarry', 'TFT8_Augment_LeonaCarry', 'TFT8_Augment_NunuSupport', 'TFT8_Augment_FiddlesticksCarry', 'TFT8_Augment_UrgotCarry', 'TFT8_Augment_JannaSupport', 'TFT8_Augment_SamiraCarry', 'TFT8_Augment_TaliyahSupport', 'TFT8_Augment_ZedSupport', 'TFT8_Augment_BlitzcrankCarry', 'TFT8_Augment_UrgotSupport', 'TFT8_Augment_BlitzcrankSupport', 'TFT8_Augment_MordekaiserSupport', 'TFT8_Augment_ApheliosCarry', 'TFT8_Augment_LuluSupport', 'TFT8_Augment_LeonaSupport', 'TFT8_Augment_SejuaniCarry', 'TFT8_Augment_SyndraCarry', 'TFT8_Augment_WukongSupport', 'TFT8_Augment_AsheCarry', 'TFT8_Augment_AsheSupport', 'TFT8_Augment_NilahSupport', 'TFT8_Augment_VayneSupport', 'TFT8_Augment_RivenSupport', 'TFT8_Augment_ZoeSupport', 'TFT8_Augment_LeBlancSupport', 'TFT8_Augment_LeeSinCarry', 'TFT8_Augment_YuumiCarry', 'TFT8_Augment_FiddlesticksSupport', 'TFT8_Augment_PoppySupport', 'TFT8_Augment_JannaCarry', 'TFT8_Augment_RenegadePartners', 'TFT8_Augment_TaliyahCarry', 'TFT8_Augment_ZedCarry', 'TFT8_Augment_SivirCarry', 'TFT8_Augment_RenektonCarry', 'TFT8_Augment_ViCarry', 'TFT8_Augment_RenektonSupport', 'TFT8_Augment_RellCarry', 'TFT8_Augment_FioraSupport', 'TFT8_Augment_DravenSupport', 'TFT8_Augment_YasuoSupport', 'TFT8_Augment_NasusSupport', 'TFT8_Augment_SorakaSupport', 'TFT8_Augment_LuluCarry', 'TFT8_Augment_SorakaCarry', 'TFT8_Augment_VayneCarry', 'TFT8_Augment_MalphiteSupport', 'TFT8_Augment_BelVethCarry', 'TFT8_Augment_EkkoCarry', 'TFT8_Augment_GangplankCarry', 'TFT8_Augment_JinxSupport', 'TFT8_Augment_MissFortuneSupport', 'TFT8_Augment_CamilleSupport', 'TFT8_Augment_WukongCarry', 'TFT8_Augment_SejuaniSupport', 'TFT8_Augment_ZacSupport', 'TFT8_Augment_NunuCarry', 'TFT8_Augment_ViegoCarry', 'TFT8_Augment_SamiraSupport', 'TFT8_Augment_TalonSupport', 'TFT8_Augment_EzrealCarry']
        

        #match 정보 가져오기
        for matchid in ids:
            response=requests.get(f'https://asia.api.riotgames.com/tft/match/v1/matches/{matchid}?api_key={key}')

            if response.status_code==200:
                pass
            elif response.status_code==429:
                print('대기시간이 초과되었습니다. 잠시 기다려주세요')
                start_time = time.time()

                while True: # 429error가 끝날 때까지 무한 루프
                        if response.status_code == 429:
                            print('try 10 second wait time')
                            time.sleep(10)
                            response=requests.get(f'https://asia.api.riotgames.com/tft/match/v1/matches/{matchid}?api_key={key}')
                            print(response.status_code)

                        elif response.status_code == 200: #다시 response 200이면 loop escape
                            print('total wait time : ', time.time() - start_time)
                            print('recovery api cost')
                            break
            elif response.status_code == 503: # 잠시 서비스를 이용하지 못하는 에러
                    print('service available error')
                    

            elif response.status_code == 403: # api갱신이 필요
                print('you need api renewal')
                print('break')
                    

            data = response.json()
            rank=0
            petID=''
            pet_IMG=''
            game_level=0
            traits={}
            augments={}
            units=[]
            participants=[]
            

            if data["info"]['tft_game_type'] == 'pairs':
                m = match.objects.filter(Matchid = matchid)
                if not m :
                    for i in range(len(data["metadata"]["participants"])):
                        if data["metadata"]["participants"][i] in user.objects.all(): # puuid 닉네임으로 바꾸기
                            obj=user.objects.filter(Puuid=data["metadata"]["participants"][i])
                            participants.append(obj["Name"])
                        else:
                            PUUID=data["metadata"]["participants"][i]
                            response=requests.get(f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/{PUUID}?api_key={key}')
                            if response.status_code==200:
                                
                                namedata=response.json()
                                nickname=''
                                for p in namedata["name"]:
                                    if p!=' ':
                                        nickname+=p
                                playerpuuid=namedata['puuid']
                                level=namedata['summonerLevel']
                                profile_icon=namedata['profileIconId']
                                profileid=f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/profileicon/{profile_icon}.png"
                                u=user(name=nickname,Puuid=playerpuuid,Level=level,profile_img=profileid)# 유저 테이블에 puuid 와 이름, level저장
                                u.save()
                                participants.append(nickname)
                            elif response.status_code==429:
                                print('대기시간이 초과되었습니다. 잠시 기다려주세요')
                                start_time = time.time()

                                while True: # 429error가 끝날 때까지 무한 루프
                                        if response.status_code == 429:
                                            print('try 10 second wait time')
                                            time.sleep(10)
                                            response=requests.get(f'https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-puuid/{PUUID}?api_key={key}')
                                            print(response.status_code)

                                        elif response.status_code == 200: #다시 response 200이면 loop escape
                                            namedata=response.json()
                                            nickname=''
                                            for p in namedata["name"]:
                                                if p!=' ':
                                                    nickname+=p
                                            playerpuuid=namedata['puuid']
                                            level=namedata['summonerLevel']
                                            profile_icon=namedata['profileIconId']
                                            profileid=f"http://ddragon.leagueoflegends.com/cdn/13.3.1/img/profileicon/{profile_icon}.png"
                                            u=user(name=nickname,Puuid=playerpuuid,Level=level,profile_img=profileid)# 유저 테이블에 puuid 와 이름, level저장
                                            u.save()
                                            participants.append(nickname)
                                            break
                 
                    for i in data["info"]['participants']:
                        if puuid == i["puuid"]:
                            if i['placement']<3:
                                rank=1
                            elif i['placement']<5:
                                rank=2
                            elif i['placement']<7:
                                rank=3
                            else:
                                rank=4
                            petID=pet_K(i["companion"]['item_ID'])
                            
                            pet_code=pet_img(i["companion"]['item_ID'])
                            pet_IMG=f"https://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-tactician/{pet_code}"
                            
                            game_level=i['level']


                            tr=i['traits']
                            trait = sorted(tr, key=(lambda x: x['style']),reverse=True)
                            #활성화되어있는 특성만 뽑기
                            for j in trait:
                                if j["tier_current"]>=1:
                                    traits[trait_K(j["name"])]=j["num_units"]
                            

                            for j in i["augments"]:
                                if j in hero_augment:
                                    img=hero_aug(j)
                                    augments[Aug_K(j)]=f"https://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-hero-augment/{img}"
                                else:
                                    img=aug_img(j)
                                    augments[Aug_K(j)]=f"https://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-augment/{img}"


                            for j in i["units"]:
                                dictionary={}
                                character_id=j["character_id"]
                                dictionary["Champion"]=champ_K(j["character_id"])
                                url=f"https://ddragon.leagueoflegends.com/cdn/13.3.1/img/tft-hero-augment/{character_id}.TFT_Set8.png"
                                dictionary["champion_image"]=url
                                item=[]
                                for k in j["itemNames"]:
                                    item.append(Item_K(k))
                                dictionary["items"]=item
                                dictionary["rarity"]=j["rarity"]
                                dictionary["tier"]=j["tier"]
                                units.append(dictionary)

                    
                                

                    s=static.objects.get(Name=name)
                    s.Total_game+=1
                    s.sum_of_rank+=rank
                    if rank==1:
                        s.Win+=1
                        s.Top2+=1
                    elif rank==2:
                        s.Top2+=1
                    s.save()

                    mat=match(Name=name,Matchid=matchid,Rank=rank,PetID=petID,Pet_Img=pet_IMG,Game_level=game_level,Traits=traits,Augments=augments,Units=units,Participant=participants)
                    mat.save()

                    
        
        matches=match.objects.filter(Name=name)
        serializer=matchSerializer(matches,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class statAPI(APIView):
    def get(self,request,sname):
        
        stat=static.objects.filter(Name=sname)
        serializer=statSerializer(stat,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

