from kriswarpy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from time import sleep
from datetime import datetime
import time, random, sys, json, codecs, re, os, requests, pytz
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
kris = LINE("email","password")
kris.log("Auth Token : " + str(kris.authToken))
kr = LINE("email","password")
kr.log("Auth Token : " + str(kr.authToken))
kr1 = LINE("email","password")
kr1.log("Auth Token : " + str(kr1.authToken))
kr2 = LINE("email","password")
kr2.log("Auth Token : " + str(kr2.authToken))
kr3 = LINE("email","password")
kr3.log("Auth Token : " + str(kr3.authToken))
kr4 = LINE("email","password")
kr4.log("Auth Token : " + str(kr4.authToken))
print ("LOGIN SUCCESS [KRIS PASUKAN KEMENG CYBER ARMY BOT]")
oepoll = OEPoll(kris)
ownerOpen = codecs.open("owner.json","r","utf-8")
Owner = json.load(ownerOpen)
admin = ["u9cc2323f5b84f9df880c33aa9f9e3ae1","u35459f1e84ad208cc56025c259cb1628"]
krisMID = kris.profile.mid
krMID = kr.profile.mid
kr1MID = kr1.profile.mid
kr2MID = kr2.profile.mid
kr3MID = kr3.profile.mid
kr4MID = kr4.profile.mid
Bots = [krisMID,krMID,kr1MID,kr2MID,kr3MID,kr4MID]
settings = {
    "blacklist":{},
    "Upfoto":False,
    "autoJoinTicket":False,
    "qr":False,
    "pro":False,
    "cancel":False
}
def restart_program():
    backupData()
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    kris.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Makassar")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "tolsember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("Error.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))
    return
def backupData():
    try:
        backup = Owner
        f = codecs.open('owner.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        kris.log("[ERROR] : " + str(error))
        return False
def help():
    with open('help.txt', 'r') as f:
        text = f.read()
    helpMsg = text
    return helpMsg
def command(text):
    krtext = text.lower()
    return krtext
def botpoll(op):
    try:
        if op.type == 0:
            return
        if op.type == 26:
            msg = op.message
            to = msg.to
            if msg.contentType == 1:
                if settings['Upfoto'] == True:
                    path = kris.downloadObjectMsg(msg.id)
                    path = kr.downloadObjectMsg(msg.id)
                    path = kr1.downloadObjectMsg(msg.id)
                    path = kr2.downloadObjectMsg(msg.id)
                    path = kr3.downloadObjectMsg(msg.id)
                    path = kr4.downloadObjectMsg(msg.id)
                    kris.updateProfilePicture(path)
                    kr.updateProfilePicture(path)
                    kr1.updateProfilePicture(path)
                    kr2.updateProfilePicture(path)
                    kr3.updateProfilePicture(path)
                    kr4.updateProfilePicture(path)
                    kr.sendMessage(to,"Update picture success")
                    kr1.sendMessage(to,"Update picture success")
                    kr2.sendMessage(to,"Update picture success")
                    kr3.sendMessage(to,"Update picture success")
                    kr4.sendMessage(to,"Update picture success")
                    settings['Upfoto'] = False
        if op.type in [25,26]:
            msg = op.message
            text = msg.text
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != kris.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if "/ti/g/" in text.lower():
                        if settings["autoJoinTicket"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                    n_links.append(l)
                            for ticket_id in n_links:
                                group = kr.findGroupByTicket(ticket_id)
                                group = kr1.findGroupByTicket(ticket_id)
                                group = kr2.findGroupByTicket(ticket_id)
                                group = kr3.findGroupByTicket(ticket_id)
                                group = kr4.findGroupByTicket(ticket_id)
                                kr.acceptGroupInvitationByTicket(group.id,ticket_id)
                                kr1.acceptGroupInvitationByTicket(group.id,ticket_id)
                                kr2.acceptGroupInvitationByTicket(group.id,ticket_id)
                                kr3.acceptGroupInvitationByTicket(group.id,ticket_id)
                                kr4.acceptGroupInvitationByTicket(group.id,ticket_id)
                                kr.sendMessage(to, "Masuk : %s" % str(group.name))
                                break
        if op.type in [25,26]:
            msg = op.message
            text = msg.text
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != kris.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        try:
                            krtext = command(text)
                            if krtext == "til keys":
                                if sender in Owner:
                                    kris.sendMessage(to, str(help()))
                            elif krtext == "til speed":
                                if sender in Owner:
                                    start = time.time()
                                    kris.sendMessage(to, "Prosses...")
                                    elapsed_time = time.time() - start
                                    kris.sendMessage(to,"%s" % (elapsed_time))
                            elif krtext == "til sp":
                                if sender in Owner:
                                    start = time.time()
                                    kris.sendMessage(to, "Prosses...")
                                    elapsed_time = time.time() - start
                                    kris.sendMessage(to,format(str(elapsed_time)))
                            elif krtext == "til lebet":
                                if sender in Owner:
                                    kris.findAndAddContactsByMid(krMID)
                                    kris.findAndAddContactsByMid(kr1MID)
                                    kris.findAndAddContactsByMid(kr2MID)
                                    kris.findAndAddContactsByMid(kr3MID)
                                    kris.findAndAddContactsByMid(kr4MID)
                                    kris.inviteIntoGroup(msg.to,[krMID,kr1MID,kr2MID,kr3MID,kr4MID])
                                    kr.acceptGroupInvitation(to)
                                    kr1.acceptGroupInvitation(to)
                                    kr2.acceptGroupInvitation(to)
                                    kr3.acceptGroupInvitation(to)
                                    kr4.acceptGroupInvitation(to)
                            elif krtext == "til backup":
                                if sender in Owner:
                                    kris.findAndAddContactsByMid("u35459f1e84ad208cc56025c259cb1628")
                                    kris.findAndAddContactsByMid("u9cc2323f5b84f9df880c33aa9f9e3ae1")
                                    kris.findAndAddContactsByMid(krMID)
                                    kris.findAndAddContactsByMid(kr1MID)
                                    kris.findAndAddContactsByMid(kr2MID)
                                    kris.findAndAddContactsByMid(kr3MID)
                                    kris.findAndAddContactsByMid(kr4MID)
                                    kr.findAndAddContactsByMid("u35459f1e84ad208cc56025c259cb1628")
                                    kr.findAndAddContactsByMid("u9cc2323f5b84f9df880c33aa9f9e3ae1")
                                    kr.findAndAddContactsByMid(krisMID)
                                    kr.findAndAddContactsByMid(kr1MID)
                                    kr.findAndAddContactsByMid(kr2MID)
                                    kr.findAndAddContactsByMid(kr3MID)
                                    kr.findAndAddContactsByMid(kr4MID)
                                    kr1.findAndAddContactsByMid("u35459f1e84ad208cc56025c259cb1628")
                                    kr1.findAndAddContactsByMid("u9cc2323f5b84f9df880c33aa9f9e3ae1")
                                    kr1.findAndAddContactsByMid(krisMID)
                                    kr1.findAndAddContactsByMid(krMID)
                                    kr1.findAndAddContactsByMid(kr2MID)
                                    kr1.findAndAddContactsByMid(kr3MID)
                                    kr1.findAndAddContactsByMid(kr4MID)
                                    kr2.findAndAddContactsByMid("u35459f1e84ad208cc56025c259cb1628")
                                    kr2.findAndAddContactsByMid("u9cc2323f5b84f9df880c33aa9f9e3ae1")
                                    kr2.findAndAddContactsByMid(krisMID)
                                    kr2.findAndAddContactsByMid(krMID)
                                    kr2.findAndAddContactsByMid(kr1MID)
                                    kr2.findAndAddContactsByMid(kr3MID)
                                    kr2.findAndAddContactsByMid(kr4MID)
                                    kr3.findAndAddContactsByMid("u35459f1e84ad208cc56025c259cb1628")
                                    kr3.findAndAddContactsByMid("u9cc2323f5b84f9df880c33aa9f9e3ae1")
                                    kr3.findAndAddContactsByMid(krisMID)
                                    kr3.findAndAddContactsByMid(krMID)
                                    kr3.findAndAddContactsByMid(kr1MID)
                                    kr3.findAndAddContactsByMid(kr2MID)
                                    kr3.findAndAddContactsByMid(kr4MID)
                                    kr4.findAndAddContactsByMid("u35459f1e84ad208cc56025c259cb1628")
                                    kr4.findAndAddContactsByMid("u9cc2323f5b84f9df880c33aa9f9e3ae1")
                                    kr4.findAndAddContactsByMid(krisMID)
                                    kr4.findAndAddContactsByMid(krMID)
                                    kr4.findAndAddContactsByMid(kr1MID)
                                    kr4.findAndAddContactsByMid(kr2MID)
                                    kr4.findAndAddContactsByMid(kr3MID)
                                    kr.sendMessage(to, "Backup done...")
                            elif krtext == "til masuk":
                                if sender in Owner:
                                    try:
                                        kris.findAndAddContactsByMid(krMID)
                                        kris.inviteIntoGroup(to,[krMID])
                                        kr.acceptGroupInvitation(to)
                                        kr.findAndAddContactsByMid(kr1MID)
                                        kr.inviteIntoGroup(to,[kr1MID])
                                        kr1.acceptGroupInvitation(to)
                                        kr1.findAndAddContactsByMid(kr2MID)
                                        kr1.inviteIntoGroup(to,[kr2MID])
                                        kr2.acceptGroupInvitation(to)
                                        kr2.findAndAddContactsByMid(kr3MID)
                                        kr2.inviteIntoGroup(to,[kr3MID])
                                        kr3.acceptGroupInvitation(to)
                                        kr3.findAndAddContactsByMid(kr4MID)
                                        kr3.inviteIntoGroup(to,[kr4MID])
                                        kr4.acceptGroupInvitation(to)
                                    except:
                                        pass
                            elif krtext == "til asup":
                                if sender in Owner:
                                    try:
                                        G = kris.getGroup(to)
                                        G.preventedJoinByTicket = False
                                        kris.updateGroup(G)
                                        Ticket = kris.reissueGroupTicket(to)
                                        kr.acceptGroupInvitationByTicket(to,Ticket)
                                        kr1.acceptGroupInvitationByTicket(to,Ticket)
                                        kr2.acceptGroupInvitationByTicket(to,Ticket)
                                        kr3.acceptGroupInvitationByTicket(to,Ticket)
                                        kr4.acceptGroupInvitationByTicket(to,Ticket)
                                        G = kris.getGroup(to)
                                        G.preventedJoinByTicket = True
                                        kris.updateGroup(G)
                                        Ticket = kris.reissueGroupTicket(to)
                                    except:
                                        pass
                            elif krtext.startswith("til cium "):
                                if sender in Owner:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for x in key["MENTIONEES"]:
                                        targets.append(x["M"])
                                    for target in targets:
                                        if target in Owner:
                                            pass
                                        else:
                                            try:
                                                kr1.sendMessage(to, "Maaf ya izin mencumbu...")
                                                settings["blacklist"][target] = True
                                                kr1.kickoutFromGroup(to,[target])
                                            except:
                                                try:
                                                    kr2.sendMessage(to, "Maaf ya izin merayu...")
                                                    settings["blacklist"][target] = True
                                                    kr2.kickoutFromGroup(to,[target])
                                                except:
                                                    try:
                                                        kr3.sendMessage(to, "Maaf ya izin memadu...")
                                                        settings["blacklist"][target] = True
                                                        kr3.kickoutFromGroup(to,[target])
                                                    except:
                                                        try:
                                                            kr4.sendMessage(to, "Maaf ya izin mengentu...")
                                                            settings["blacklist"][target] = True
                                                            kr4.kickoutFromGroup(to,[target])
                                                        except:
                                                            kr1.sendMessage(to, "LIMIT")
                            elif krtext == "bl":
                                if sender in Owner:
                                    if settings["blacklist"] == {}:
                                        kris.sendMessage(to,"Tidak Ada kontak blacklist")
                                    else:
                                        mc = "Daftar Blacklist "
                                        num=1
                                        ragets = kris.getContacts(settings["blacklist"])
                                        for mi_d in ragets:
                                            mc+="\n%i. %s" % (num, mi_d.displayName)
                                            num=(num+1)
                                        mc+="\n\n Total %i Blacklist " % len(ragets)
                                        kris.sendMessage(to, mc)
                            elif krtext == "cbl":
                                if sender in Owner:
                                    settings["blacklist"] = {}
                                    kr.sendMessage(to,"sukses membersihkan blacklist..!!")
                            elif krtext == "til bot" or krtext == "mybot":
                                if sender in Owner:
                                    kris.sendMessage(to, None, contentMetadata={'mid': krMID}, contentType=13)
                                    kris.sendMessage(to, None, contentMetadata={'mid': kr1MID}, contentType=13)
                                    kris.sendMessage(to, None, contentMetadata={'mid': kr2MID}, contentType=13)
                                    kris.sendMessage(to, None, contentMetadata={'mid': kr3MID}, contentType=13)
                                    kris.sendMessage(to, None, contentMetadata={'mid': kr4MID}, contentType=13)
                            elif krtext == "til absen":
                                if sender in Owner:
                                    kr1.sendMessage(to, " Hadir..!!!")
                                    kr2.sendMessage(to, " Hadir..!!!")
                                    kr.sendMessage(to, " Hadir..!!!")
                                    kr3.sendMessage(to, " Hadir..!!!")
                                    kr4.sendMessage(to, " Hadir..!!!")
                            elif krtext == "til changepp on":
                                if sender in Owner:
                                    settings['Upfoto'] = True
                                    kris.sendMessage(to,"Send Pict For UpPict")
                            elif krtext == "til changepp off":
                                if sender in Owner:
                                    settings['Upfoto'] = False
                                    kris.sendMessage(to,"Send Pict Already Off")
                            elif krtext == "ping":
                                if sender in Owner:
                                    text0 = (" Pong..!!")
                                    kr.sendMessage(to, text0)
                                    text1 = (" Pong..!!")
                                    kr1.sendMessage(to, text1)
                                    text2 = (" Pong..!!")
                                    kr2.sendMessage(to, text2)
                                    text3 = (" Pong..!!")
                                    kr3.sendMessage(to, text3)
                                    text4 = (" Pong..!!")
                                    kr4.sendMessage(to, text4)
                            elif krtext == "til cabut":
                                if sender in Owner:
                                    kris.sendMessage(to, "Hmm..., pamit dah...")
                                    kr1.leaveGroup(msg.to)
                                    kr2.leaveGroup(msg.to)
                                    kr3.leaveGroup(msg.to)
                                    kr4.leaveGroup(msg.to)
                                    kr.leaveGroup(msg.to)
                                    kris.leaveGroup(msg.to)
                            elif krtext == "til kabur":
                                if sender in Owner:
                                    kr.sendMessage(to, "Hmm... di suruh pergi,, Ok lah kalau gitu, pamit...")
                                    kr1.leaveGroup(msg.to)
                                    kr2.leaveGroup(msg.to)
                                    kr3.leaveGroup(msg.to)
                                    kr4.leaveGroup(msg.to)
                                    kr.leaveGroup(msg.to)
                            elif krtext == "til jointicket on":
                                if sender in Owner:
                                    settings["autoJoinTicket"] = True
                                    kris.sendMessage(to,"Join Ticket Set To On")
                            elif krtext == "til jointicket off":
                                if sender in Owner:
                                    settings["autoJoinTicket"] = False
                                    kris.sendMessage(to,"Join Ticket Set To Off")
                            elif krtext == "til on":
                                if sender in Owner:
                                    settings["qr"] = True
                                    settings["pro"] = True
                                    settings["cancel"] = True
                                    kris.sendMessage(to,"til Siap digelitikin => Status On")
                            elif krtext == "til off":
                                if sender in Owner:
                                    settings["qr"] = False
                                    settings["pro"] = False
                                    settings["cancel"] = False
                                    kris.sendMessage(to,"til Siap digelitikin => Status Off")
                            elif krtext == "til restart":
                                if sender in Owner:
                                    kris.sendMessage(msg.to, 'Restarting Prosses..')
                                    print ("Restarting")
                                    restart_program()
                            elif krtext == "til ancur":
                                if sender in Owner:
                                    if msg.toType == 2:
                                        gs = kr.getGroup(msg.to)
                                        gs = kr1.getGroup(msg.to)
                                        gs = kr2.getGroup(msg.to)
                                        gs = kr3.getGroup(msg.to)
                                        gs = kr4.getGroup(msg.to)
                                        time.sleep(0.0002)
                                        targets = []
                                        for g in gs.members:
                                            if targets in g.displayName:
                                                targets.append(g.mid)
                                        if targets == []:
                                            kr.sendMessage(to,"LIMIT.!!!")
                                        else:
                                            for target in targets:
                                                if target not in Bots:
                                                    if target not in Owner:
                                                        try:
                                                            klist=[kr,kr1,kr2,kr3,kr4]
                                                            kicker=random.choice(klist)
                                                            kicker.kickoutFromGroup(to,[target])
                                                            print (to,[g.mid])
                                                        except:
                                                            pass
                            elif krtext.startswith("adminadd @"):
                                if sender in Owner:
                                    print ("[Command]Menambahkan admin")
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for g in key["MENTIONEES"]:
                                        targets.append(g["M"])
                                    for target in targets:
                                        if target in admin:
                                            kris.sendMessage(to, "Sudah Terdaftar di Admin")
                                        else:
                                            for target in targets:
                                                try:
                                                    admin.append(target)
                                                    kris.sendMessage(to,"Admin Ditambahkan")
                                                except Exception as error:
                                                    kris.sendMessage(to, str(error))
                                else:
                                    kris.sendMessage(to,"Perintah Ditolak.")
                                    kris.sendMessage(to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                            elif krtext.startswith("admindell @"):
                                if sender in Owner:
                                    print ("[Command]Menghapus admin")
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key["MENTIONEES"][0]["M"]
                                    targets = []
                                    for g in key["MENTIONEES"]:
                                        targets.append(g["M"])
                                    for target in targets:
                                        if target not in admin:
                                            kr.sendMessage(to, "Belum Terdaftar di Admin")
                                        else:
                                            for target in targets:
                                                try:
                                                    admin.remove(target)
                                                    kris.sendMessage(to,"Admin Dihapus")
                                                except Exception as error:
                                                    kris.sendMessage(to, str(error))
                                else:
                                    kris.sendMessage(to,"Perintah Ditolak.")
                                    kris.sendMessage(to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                            elif krtext == "adminlist":
                                if sender in Owner:
                                    if admin == []:
                                        kris.sendMessage(to,"The Adminlist is empty")
                                    else:
                                        kris.sendMessage(to,"Tunggu...")
                                        mc = "╔═══════════════\n╠❂➣♥ Kris - Cyber Army Bot ♥\n╠❂➣══✪〘 Admin List 〙✪═══\n"
                                        for mi_d in admin:
                                            mc += "╠❂➣✪ " +kris.getContact(mi_d).displayName + "\n"
                                        kris.sendMessage(to,mc + "╠❂➣═══════════════\n╠❂➣✪〘 line://ti/p/~krissthea 〙\n╚═══════════════")
                            elif krtext == "til rejectall":
                                if sender in Owner:
                                    ginvited = kris.getGroupIdsInvited()
                                    ginvited = kr.getGroupIdsInvited()
                                    ginvited = kr1.getGroupIdsInvited()
                                    ginvited = kr2.getGroupIdsInvited()
                                    ginvited = kr3.getGroupIdsInvited()
                                    ginvited = kr4.getGroupIdsInvited()
                                    if ginvited != [] and ginvited != None:
                                        for gid in ginvited:
                                            kris.rejectGroupInvitation(gid)
                                            kr.rejectGroupInvitation(gid)
                                            kr1.rejectGroupInvitation(gid)
                                            kr2.rejectGroupInvitation(gid)
                                            kr3.rejectGroupInvitation(gid)
                                            kr4.rejectGroupInvitation(gid)
                                            kris.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                                            kr.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                                            kr1.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                                            kr2.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                                            kr3.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                                            kr4.sendMessage(to, "Berhasil tolak sebanyak {} undangan".format(str(len(ginvited))))
                                    else:
                                        kr.sendMessage(to, "Tidak ada undangan yang tertunda")
                            elif "changenametil: " in krtext:
                                if sender in Owner:
                                    name = krtext.split(": ")
                                    change = krtext.replace(name[0] + ": ","")
                                    cll0 = kris.getProfile()
                                    cll1 = kr.getProfile()
                                    cll2 = kr1.getProfile()
                                    cll3 = kr2.getProfile()
                                    cll4 = kr3.getProfile()
                                    cll5 = kr4.getProfile()
                                    cll0.displayName = change
                                    cll1.displayName = change
                                    cll2.displayName = change
                                    cll3.displayName = change
                                    cll4.displayName = change
                                    cll5.displayName = change
                                    kris.updateProfile(cll0)
                                    kr.updateProfile(cll1)
                                    kr1.updateProfile(cll2)
                                    kr2.updateProfile(cll3)
                                    kr3.updateProfile(cll4)
                                    kr4.updateProfile(cll5)
                                    kris.sendMessage(to," Update Name Success to " + str(change))
                                    kr.sendMessage(to," Update Name Success to " + str(change))
                                    kr1.sendMessage(to," Update Name Success to " + str(change))
                                    kr2.sendMessage(to," Update Name Success to " + str(change))
                                    kr3.sendMessage(to," Update Name Success to " + str(change))
                                    kr4.sendMessage(to," Update Name Success to " + str(change))
                            elif krtext == "til cek":
                                if sender in Owner:
                                    try:kr.inviteIntoGroup(to, [krMID]);has = "OK"
                                    except:has = "NOT"
                                    try:kr.kickoutFromGroup(to, [krMID]);has1 = "OK"
                                    except:has1 = "NOT"
                                    if has == "OK":sil = "Sehat Jagjag 😎"
                                    else:sil = "Teu Damang 😥"
                                    if has1 == "OK":sil1 = "Sehat Jagjag 😎"
                                    else:sil1 = "Teu Damang 😥"
                                    kr.sendMessage(to, "╔═══════════════\n║❂➣ Pamariosan\n╠═════════════\n║❂➣ Najong : {} \n║❂➣ Ngulem : {}\n╚═════════════".format(sil1,sil))
                                    try:kr1.inviteIntoGroup(to, [kr1MID]);has = "OK"
                                    except:has = "NOT"
                                    try:kr1.kickoutFromGroup(to, [kr1MID]);has1 = "OK"
                                    except:has1 = "NOT"
                                    if has == "OK":sil = "Sehat Jagjag 😎"
                                    else:sil = "Teu Damang 😥"
                                    if has1 == "OK":sil1 = "Sehat Jagjag 😎"
                                    else:sil1 = "Teu Damang 😥"
                                    kr1.sendMessage(to, "╔═══════════════\n║❂➣ Pamariosan\n╠═════════════\n║❂➣ Najong : {} \n║❂➣ Ngulem : {}\n╚═════════════".format(sil1,sil))
                                    try:kr2.inviteIntoGroup(to, [kr2MID]);has = "OK"
                                    except:has = "NOT"
                                    try:kr2.kickoutFromGroup(to, [kr2MID]);has1 = "OK"
                                    except:has1 = "NOT"
                                    if has == "OK":sil = "Sehat Jagjag 😎"
                                    else:sil = "Teu Damang 😥"
                                    if has1 == "OK":sil1 = "Sehat Jagjag 😎"
                                    else:sil1 = "Teu Damang 😥"
                                    kr2.sendMessage(to, "╔═══════════════\n║❂➣ Pamariosan\n╠═════════════\n║❂➣ Najong : {} \n║❂➣ Ngulem : {}\n╚═════════════".format(sil1,sil))
                                    try:kr3.inviteIntoGroup(to, [kr3MID]);has = "OK"
                                    except:has = "NOT"
                                    try:kr3.kickoutFromGroup(to, [kr3MID]);has1 = "OK"
                                    except:has1 = "NOT"
                                    if has == "OK":sil = "Sehat Jagjag 😎"
                                    else:sil = "Teu Damang 😥"
                                    if has1 == "OK":sil1 = "Sehat Jagjag 😎"
                                    else:sil1 = "Teu Damang 😥"
                                    kr3.sendMessage(to, "╔═══════════════\n║❂➣ Pamariosan\n╠═════════════\n║❂➣ Najong : {} \n║❂➣ Ngulem : {}\n╚═════════════".format(sil1,sil))
                                    try:kr4.inviteIntoGroup(to, [kr4MID]);has = "OK"
                                    except:has = "NOT"
                                    try:kr4.kickoutFromGroup(to, [kr4MID]);has1 = "OK"
                                    except:has1 = "NOT"
                                    if has == "OK":sil = "Sehat Jagjag 😎"
                                    else:sil = "Teu Damang 😥"
                                    if has1 == "OK":sil1 = "Sehat Jagjag 😎"
                                    else:sil1 = "Teu Damang 😥"
                                    kr4.sendMessage(to, "╔═══════════════\n║❂➣ Pamariosan\n╠═════════════\n║❂➣ Najong : {} \n║❂➣ Ngulem : {}\n╚═════════════".format(sil1,sil))
                        except Exception as e:
                            print (e)
        if op.type [19,32]:
            if op.param3 in krisMID:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    try:
                        kr.inviteIntoGroup(op.param1,[op.param3])
                        kris.acceptGroupInvitation(op.param1)
                    except:
                        G = kr1.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kr1.updateGroup(G)
                        Ticket = kr1.reissueGroupTicket(op.param1)
                        kris.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = kr1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        kr1.updateGroup(G)
                        Ticket = kr1.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr.inviteIntoGroup(op.param1,[op.param3])
                        kris.acceptGroupInvitation(op.param1)
                        kr.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kr1.inviteIntoGroup(op.param1,[op.param3])
                            kris.acceptGroupInvitation(op.param1)
                            kr1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kr2.inviteIntoGroup(op.param1,[op.param3])
                                kris.acceptGroupInvitation(op.param1)
                                kr2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kr3.inviteIntoGroup(op.param1,[krisMID,krMID,kr1MID,kr2MID])
                                    kris.acceptGroupInvitation(op.param1)
                                    kr3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kr4.inviteIntoGroup(op.param1,[krisMID,krMID,kr1MID,kr2MID,kr3MID])
                                        kris.acceptGroupInvitation(op.param1)
                                        kr4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kr.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kr.updateGroup(G)
                                            Ticket = kr.reissueGroupTicket(op.param1)
                                            kris.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kr.kickoutFromGroup(op.param1,[op.param2])
                                            G = kris.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kris.updateGroup(G)
                                            Ticket = kris.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                G = kr1.getGroup(op.param1)
                                                G.preventedJoinByTicket = False
                                                kr1.updateGroup(G)
                                                Ticket = kr1.reissueGroupTicket(op.param1)
                                                kris.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                kr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                kr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                kr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                kr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                kr1.kickoutFromGroup(op.param1,[op.param2])
                                                G = kris.getGroup(op.param1)
                                                G.preventedJoinByTicket = True
                                                kris.updateGroup(G)
                                                Ticket = kris.reissueGroupTicket(op.param1)
                                            except:
                                                try:
                                                    G = kr2.getGroup(op.param1)
                                                    G.preventedJoinByTicket = False
                                                    kr2.updateGroup(G)
                                                    Ticket = kr2.reissueGroupTicket(op.param1)
                                                    kris.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    kr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    kr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    kr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    kr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    kr2.kickoutFromGroup(op.param1,[op.param2])
                                                    G = kris.getGroup(op.param1)
                                                    G.preventedJoinByTicket = True
                                                    kris.updateGroup(G)
                                                    Ticket = kris.reissueGroupTicket(op.param1)
                                                except:
                                                    try:
                                                        G = kr3.getGroup(op.param1)
                                                        G.preventedJoinByTicket = False
                                                        kr3.updateGroup(G)
                                                        Ticket = kr3.reissueGroupTicket(op.param1)
                                                        kris.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kr3.kickoutFromGroup(op.param1,[op.param2])
                                                        G = kris.getGroup(op.param1)
                                                        G.preventedJoinByTicket = True
                                                        kris.updateGroup(G)
                                                        Ticket = kris.reissueGroupTicket(op.param1)
                                                    except:
                                                        G = kr4.getGroup(op.param1)
                                                        G.preventedJoinByTicket = False
                                                        kr4.updateGroup(G)
                                                        Ticket = kr4.reissueGroupTicket(op.param1)
                                                        kris.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kr4.kickoutFromGroup(op.param1,[op.param2])
                                                        G = kris.getGroup(op.param1)
                                                        G.preventedJoinByTicket = True
                                                        kris.updateGroup(G)
                                                        Ticket = kris.reissueGroupTicket(op.param1)
            if op.param3 in krMID:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    try:
                        kris.inviteIntoGroup(op.param1,[op.param3])
                        kr.acceptGroupInvitation(op.param1)
                    except:
                        G = kris.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kris.updateGroup(G)
                        Ticket = kris.reissueGroupTicket(op.param1)
                        kr.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = kris.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        kris.updateGroup(G)
                        Ticket = kris.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr1.inviteIntoGroup(op.param1,[op.param3])
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                        kr.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kr2.inviteIntoGroup(op.param1,[op.param3])
                            kr2.kickoutFromGroup(op.param1,[op.param2])
                            kr.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kr3.inviteIntoGroup(op.param1,[op.param3])
                                kr3.kickoutFromGroup(op.param1,[op.param2])
                                kr.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kr4.inviteIntoGroup(op.param1,[krMID,kr1MID,kr2MID,kr3MID])
                                    kr4.kickoutFromGroup(op.param1,[op.param2])
                                    kr.acceptGroupInvitation(op.param1)
                                    kr1.acceptGroupInvitation(op.param1)
                                    kr2.acceptGroupInvitation(op.param1)
                                    kr3.acceptGroupInvitation(op.param1)
                                except:
                                    kris.inviteIntoGroup(op.param1,[krMID,kr1MID,kr2MID,kr3MID,kr4MID])
                                    kr.acceptGroupInvitation(op.param1)
                                    kr1.acceptGroupInvitation(op.param1)
                                    kr2.acceptGroupInvitation(op.param1)
                                    kr3.acceptGroupInvitation(op.param1)
                                    kr4.acceptGroupInvitation(op.param1)
                                    kr.kickoutFromGroup(op.param1,[op.param2])
            if op.param3 in kr1MID:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    try:
                        kris.inviteIntoGroup(op.param1,[op.param3])
                        kr1.acceptGroupInvitation(op.param1)
                    except:
                        G = kris.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kris.updateGroup(G)
                        Ticket = kris.reissueGroupTicket(op.param1)
                        kr1.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = kris.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        kris.updateGroup(G)
                        Ticket = kris.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr2.inviteIntoGroup(op.param1,[op.param3])
                        kr2.kickoutFromGroup(op.param1,[op.param2])
                        kr1.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kr3.inviteIntoGroup(op.param1,[op.param3])
                            kr3.kickoutFromGroup(op.param1,[op.param2])
                            kr1.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kr4.inviteIntoGroup(op.param1,[op.param3])
                                kr4.kickoutFromGroup(op.param1,[op.param2])
                                kr1.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kr.inviteIntoGroup(op.param1,[kr1MID,kr2MID,kr3MID,kr4MID])
                                    kr.kickoutFromGroup(op.param1,[op.param2])
                                    kr1.acceptGroupInvitation(op.param1)
                                    kr2.acceptGroupInvitation(op.param1)
                                    kr3.acceptGroupInvitation(op.param1)
                                    kr4.acceptGroupInvitation(op.param1)
                                except:
                                    kris.inviteIntoGroup(op.param1,[krMID,kr1MID,kr2MID,kr3MID,kr4MID])
                                    kr.acceptGroupInvitation(op.param1)
                                    kr1.acceptGroupInvitation(op.param1)
                                    kr2.acceptGroupInvitation(op.param1)
                                    kr3.acceptGroupInvitation(op.param1)
                                    kr4.acceptGroupInvitation(op.param1)
                                    kr1.kickoutFromGroup(op.param1,[op.param2])
            if op.param3 in kr2MID:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    try:
                        kris.inviteIntoGroup(op.param1,[op.param3])
                        kr2.acceptGroupInvitation(op.param1)
                    except:
                        G = kris.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kris.updateGroup(G)
                        Ticket = kris.reissueGroupTicket(op.param1)
                        kr2.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = kris.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        kris.updateGroup(G)
                        Ticket = kris.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr3.inviteIntoGroup(op.param1,[op.param3])
                        kr3.kickoutFromGroup(op.param1,[op.param2])
                        kr2.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kr4.inviteIntoGroup(op.param1,[op.param3])
                            kr4.kickoutFromGroup(op.param1,[op.param2])
                            kr2.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kr.inviteIntoGroup(op.param1,[op.param3])
                                kr.kickoutFromGroup(op.param1,[op.param2])
                                kr2.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kr1.inviteIntoGroup(op.param1,[kr2MID,kr3MID,kr4MID,krMID])
                                    kr1.kickoutFromGroup(op.param1,[op.param2])
                                    kr2.acceptGroupInvitation(op.param1)
                                    kr3.acceptGroupInvitation(op.param1)
                                    kr4.acceptGroupInvitation(op.param1)
                                    kr.acceptGroupInvitation(op.param1)
                                except:
                                    kris.inviteIntoGroup(op.param1,[krMID,kr1MID,kr2MID,kr3MID,kr4MID])
                                    kr.acceptGroupInvitation(op.param1)
                                    kr1.acceptGroupInvitation(op.param1)
                                    kr2.acceptGroupInvitation(op.param1)
                                    kr3.acceptGroupInvitation(op.param1)
                                    kr4.acceptGroupInvitation(op.param1)
                                    kr2.kickoutFromGroup(op.param1,[op.param2])
            if op.param3 in kr3MID:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    try:
                        kris.inviteIntoGroup(op.param1,[op.param3])
                        kr3.acceptGroupInvitation(op.param1)
                    except:
                        G = kris.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kris.updateGroup(G)
                        Ticket = kris.reissueGroupTicket(op.param1)
                        kr3.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = kris.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        kris.updateGroup(G)
                        Ticket = kris.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr4.inviteIntoGroup(op.param1,[op.param3])
                        kr4.kickoutFromGroup(op.param1,[op.param2])
                        kr3.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kr.inviteIntoGroup(op.param1,[op.param3])
                            kr.kickoutFromGroup(op.param1,[op.param2])
                            kr3.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kr1.inviteIntoGroup(op.param1,[op.param3])
                                kr1.kickoutFromGroup(op.param1,[op.param2])
                                kr3.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kr2.inviteIntoGroup(op.param1,[kr3MID,kr4MID,krMID,kr1MID])
                                    kr2.kickoutFromGroup(op.param1,[op.param2])
                                    kr3.acceptGroupInvitation(op.param1)
                                    kr4.acceptGroupInvitation(op.param1)
                                    kr.acceptGroupInvitation(op.param1)
                                    kr1.acceptGroupInvitation(op.param1)
                                except:
                                    kris.inviteIntoGroup(op.param1,[krMID,kr1MID,kr2MID,kr3MID,kr4MID])
                                    kr.acceptGroupInvitation(op.param1)
                                    kr1.acceptGroupInvitation(op.param1)
                                    kr2.acceptGroupInvitation(op.param1)
                                    kr3.acceptGroupInvitation(op.param1)
                                    kr4.acceptGroupInvitation(op.param1)
                                    kr3.kickoutFromGroup(op.param1,[op.param2])
                return
            if op.param3 in kr4MID:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    try:
                        kris.inviteIntoGroup(op.param1,[op.param3])
                        kr4.acceptGroupInvitation(op.param1)
                    except:
                        G = kris.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kris.updateGroup(G)
                        Ticket = kris.reissueGroupTicket(op.param1)
                        kr4.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G = kris.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        kris.updateGroup(G)
                        Ticket = kris.reissueGroupTicket(op.param1)
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr.inviteIntoGroup(op.param1,[op.param3])
                        kr.kickoutFromGroup(op.param1,[op.param2])
                        kr4.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kr1.inviteIntoGroup(op.param1,[op.param3])
                            kr1.kickoutFromGroup(op.param1,[op.param2])
                            kr4.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kr2.inviteIntoGroup(op.param1,[op.param3])
                                kr2.kickoutFromGroup(op.param1,[op.param2])
                                kr4.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kr3.inviteIntoGroup(op.param1,[kr4MID,krMID,kr1MID,kr2MID])
                                    kr3.kickoutFromGroup(op.param1,[op.param2])
                                    kr4.acceptGroupInvitation(op.param1)
                                    kr.acceptGroupInvitation(op.param1)
                                    kr1.acceptGroupInvitation(op.param1)
                                    kr2.acceptGroupInvitation(op.param1)
                                except:
                                    kris.inviteIntoGroup(op.param1,[krMID,kr1MID,kr2MID,kr3MID,kr4MID])
                                    kr.acceptGroupInvitation(op.param1)
                                    kr1.acceptGroupInvitation(op.param1)
                                    kr2.acceptGroupInvitation(op.param1)
                                    kr3.acceptGroupInvitation(op.param1)
                                    kr4.acceptGroupInvitation(op.param1)
                                    kr4.kickoutFromGroup(op.param1,[op.param2])
            if op.param3 in Owner:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    try:
                        kr1.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kr2.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kr3.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                kr4.inviteIntoGroup(op.param1,[op.param3])
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                        kr1.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kr2.kickoutFromGroup(op.param1,[op.param2])
                            kr2.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kr3.kickoutFromGroup(op.param1,[op.param2])
                                kr3.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kr4.kickoutFromGroup(op.param1,[op.param2])
                                    kr4.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    kr.kickoutFromGroup(op.param1,[op.param2])
                                    kr.inviteIntoGroup(op.param1,[op.param3])
            if op.param3 in admin:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    try:
                        kr1.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kr2.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kr3.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                kr4.inviteIntoGroup(op.param1,[op.param3])
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                        kr1.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kr2.kickoutFromGroup(op.param1,[op.param2])
                            kr2.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kr3.kickoutFromGroup(op.param1,[op.param2])
                                kr3.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kr4.kickoutFromGroup(op.param1,[op.param2])
                                    kr4.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    kr.kickoutFromGroup(op.param1,[op.param2])
                                    kr.inviteIntoGroup(op.param1,[op.param3])
        if op.type in [19,32]:
            if settings["pro"] == True:
                if op.param3 not in Bots or op.param3 not in Owner or op.param3 not in admin:
                    if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                        pass
                    else:
                        settings["blacklist"][op.param2] = True
                        try:
                            kr1.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kr2.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kr3.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        kr4.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        kr.kickoutFromGroup(op.param1,[op.param2])
                    return
        if op.type == 17:
            if op.param2 in settings["blacklist"]:
                try:
                    kr.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        kr2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kr3.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kr4.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                kr1.kickoutFromGroup(op.param1,[op.param2])
            return  
        if op.type == 13:
            if op.param3 in krisMID:
                if op.param2 in Owner:
                    kris.acceptGroupInvitation(op.param1)
            if op.param3 in krisMID:
                if op.param2 in Bots:
                    kris.acceptGroupInvitation(op.param1)
            if op.param3 in krMID:
                if op.param2 in Bots:
                    kr.acceptGroupInvitation(op.param1)
            if op.param3 in kr1MID:
                if op.param2 in Bots:
                    kr1.acceptGroupInvitation(op.param1)
            if op.param3 in kr2MID:
                if op.param2 in Bots:
                    kr2.acceptGroupInvitation(op.param1)
            if op.param3 in kr3MID:
                if op.param2 in Bots:
                    kr3.acceptGroupInvitation(op.param1)
            if op.param3 in kr4MID:
                if op.param2 in Bots:
                    kr4.acceptGroupInvitation(op.param1)
            if settings["cancel"] == True:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr.cancelGroupInvitation(op.param1,[op.param3])
                        kr.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kr2.cancelGroupInvitation(op.param1,[op.param3])
                            kr2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kr3.cancelGroupInvitation(op.param1,[op.param3])
                                kr3.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kr4.cancelGroupInvitation(op.param1,[op.param3])
                                    kr4.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    kr1.cancelGroupInvitation(op.param1,[op.param3])
                                    kr1.kickoutFromGroup(op.param1,[op.param2])
                return
            if op.param3 in settings["blacklist"]:
                try:
                    kr1.cancelGroupInvitation(op.param1,[op.param3])
                    kr1.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        kr2.cancelGroupInvitation(op.param1,[op.param3])
                        kr2.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            kr3.cancelGroupInvitation(op.param1,[op.param3])
                            kr3.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            kr4.cancelGroupInvitation(op.param1,[op.param3])
                            kr4.kickoutFromGroup(op.param1,[op.param2])
            return
        if op.type == 11:
            if settings["qr"] == True:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                        G = kr1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        kr1.updateGroup(G)
                    except:
                        try:
                            kr2.kickoutFromGroup(op.param1,[op.param2])
                            kr2.reissueGroupTicket(op.param1)
                            G = kr2.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            kr2.updateGroup(G)
                        except:
                            try:
                                kr3.kickoutFromGroup(op.param1,[op.param2])
                                kr3.reissueGroupTicket(op.param1)
                                G = kr3.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kr3.updateGroup(G)
                            except:
                                try:
                                    kr4.kickoutFromGroup(op.param1,[op.param2])
                                    kr4.reissueGroupTicket(op.param1)
                                    G = kr4.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kr4.updateGroup(G)
                                except:
                                    kr.kickoutFromGroup(op.param1,[op.param2])
                                    kr.reissueGroupTicket(op.param1)
                                    G = kr.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kr.updateGroup(G)
                return
            if op.param3 in settings["blacklist"]:
                if op.param2 in Bots or op.param2 in Owner or op.param2 in admin:
                    pass
                else:
                    settings["blacklist"][op.param2] = True
                    try:
                        kr1.kickoutFromGroup(op.param1,[op.param2])
                        G = kr1.getGroup(op.param1)
                        G.preventedJoinByTicket = True
                        kr1.updateGroup(G)
                    except:
                        try:
                            kr2.kickoutFromGroup(op.param1,[op.param2])
                            kr2.reissueGroupTicket(op.param1)
                            G = kr2.getGroup(op.param1)
                            G.preventedJoinByTicket = True
                            kr2.updateGroup(G)
                        except:
                            try:
                                kr3.kickoutFromGroup(op.param1,[op.param2])
                                kr3.reissueGroupTicket(op.param1)
                                G = kr3.getGroup(op.param1)
                                G.preventedJoinByTicket = True
                                kr3.updateGroup(G)
                            except:
                                try:
                                    kr4.kickoutFromGroup(op.param1,[op.param2])
                                    kr4.reissueGroupTicket(op.param1)
                                    G = kr4.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kr4.updateGroup(G)
                                except:
                                    kr.kickoutFromGroup(op.param1,[op.param2])
                                    kr.reissueGroupTicket(op.param1)
                                    G = kr.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    kr.updateGroup(G)
                return
    except Exception as error:
        kris.log("[ERROR] : " + str(error))
        if op.type == 59:
            print (op)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops != None:
            for op in ops:
               botpoll(op)
               oepoll.setRevision(op.revision)
    except Exception as e:
        print (e)