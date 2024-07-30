import wmi

def main():
    status = False
    print("[+] Antivirus check is running .. ")
    AV_Check = [ 
        "MsMpEng.exe", "AdAwareService.exe", "afwServ.exe", "avguard.exe", "AVGSvc.exe", 
        "bdagent.exe", "BullGuardCore.exe", "ekrn.exe", "fshoster32.exe", "GDScan.exe", 
        "avp.exe", "K7CrvSvc.exe", "McAPExe.exe", "NortonSecurity.exe", "PavFnSvr.exe", 
        "SavService.exe", "EnterpriseService.exe", "WRSA.exe", "ZAPrivacyService.exe" 
    ]
    
    c = wmi.WMI()
    process_list = c.Win32_Process()
    
    for process in process_list:
        if process.Name in AV_Check:
            print(f"--AV Found: {process.Name}")
            status = True
            
    if not status:
        print("--AV software is not found!")

if __name__ == "__main__":
    main()

