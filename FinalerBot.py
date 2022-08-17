import discord as dc
import datetime
import random
import json
import Dinos
import GambleManager
from Token import *


class MyClient(dc.Client):
    # Einloggen
    async def on_ready(self):
        print("Der Bot ist online.")

    # Wenn Nachricht geposted wird
    async def on_message(self, message):

        message_author = message.author.mention.replace("!", "")

        if message.author == client.user:
            return

        # if not message.channel.name == "🌴command-dschungel":
        #     return

        def nutzer_erlaubt():
            with open(f"Datenbank/{message.channel.guild.name}/AAAbanned.txt", mode="r",
                      encoding="utf-8") as banned_users:
                users_banned = []

                for l in banned_users.readlines():
                    users_banned.append(l)

            if message_author in users_banned:
                return False
            else:
                return True

        if message.content.startswith("schnauze Joe"):
            await message.channel.send(":(")

        # KK Emoji
        # anachy
        # KK = "<:KK:914146962935267368>"
        # GAGA
        KK = "<:KK:931914975759458374>"
        # Test
        # KK = ":coin:"


        # Missionen

        mission1 = "**Krokodilfanclub**\nSammel alle drei Krokodildinos. Das sind Baryonyx, Sarco und Kaprosuchus. " \
                   "Die Belohnung ist fresh."

        mission2 = "**Ganz Oben**\nBesitze einen legendären Dino. Die Belohung ist inordnung."

        mission3 = "**Dick und Fett**\nBesitze einen Lystrosaurus und einen Maschops."


        verfugbare_missionen = ["mission1", "mission2", "mission3"]


        # objekt.__class__.__name__ str vom obj erhalten
        # eval(der string des dino Namens)
        # pickle ist wie json, merken


        if message.content.lower().startswith(",basar"):
            await message.delete()

            try:
                with open(f"Datenbank/{message.channel.guild.name}/AAAbasar.txt", mode="r",
                          encoding="utf-8") as bas:
                    description = ""
                    desc_list = []
                    basar_index = 1

                    # Falls Angaben richtig sind, jeweilige Seite ausgeben..
                    try:
                        seite = int(message.content.split(" ")[1]) - 1

                        # ..entseiden sie ist unter null
                        if seite < 0:
                            seite = 0

                    # wenn Angaben falsch sind, seite 1
                    except:
                        seite = 0

                    seiteoderso = seite * 25
                    seiten_index = seiteoderso - 24
                    basar = json.load(bas)

                    # Falls der Basar leer ist
                if not basar["basar"]:
                    description = "Der Basar ist leer!"

                # Falls etwas im Basar ist
                else:

                    # Basar Embed füllen, bzw die description dafür
                    for d in basar["basar"]:
                        for k, v in d.items():
                            basardino = k
                            basardino_formatiert = eval(basardino)
                            desc_list.append(
                                f"**{basar_index}** - {basardino_formatiert.field_name} - {v[0]} {KK} - von {v[1]}\n")  # [-3] weil das der Name mit dem hübschen Emoji ist, v[-1] ist dann der Preis
                            basar_index += 1

                    for e in range(len(desc_list)):
                        try:
                            if seiten_index <= seiteoderso:
                                description += desc_list[e + seiteoderso]
                                seiten_index += 1
                        except:
                            break

                # wenn seite leer, also description nicht gefüllt
                if description == "":
                    description = "Auf dieser Seite befindet sich nichts!"

                embed = dc.Embed(title=f"**Der aktuelle Basar**", colour=dc.Colour(0xbdba6f),
                                 description=description)
                embed.set_footer(text=f"Seite {seite + 1}")

                await message.channel.send(embed=embed)
                print(f"{message.author.name} hat sich den Basar ausgeben lassen.")


            except:
                await message.channel.send(
                    f"**{message.author.name}** so geht das nicht!\n*,basar + auszugebende Seitenzahl*")


        if message.content.lower().startswith(",basitem"):

            with open(f"Datenbank/{message.channel.guild.name}/AAAbasar.txt", mode="r", encoding="utf-8") as bas:
                basar = json.load(bas)

            # Versuchen ob der index gültig ist
            try:
                # index des Dinos finden
                index = message.content.split(" ")[1]
                auszugebener_dino = basar["basar"][int(index) - 1]

                # nicht notwendig aber so werden die sachen unten nicht die ganze Zeit als Fehler angezeigt
                basardino = ""

                # Dino fakten fürs embed erhalten, das geht hier weil pro dic nur ein Dino enthalten ist
                for k, v in auszugebener_dino.items():
                    basardino = k

                basardino_r = eval(basardino)

                # dino senden und Nahcricht löschen
                embed = dc.Embed(title=f"Basargegenstand", colour=basardino_r.color,
                                 description=basardino_r.description)
                embed.set_image(url=basardino_r.picture_url)
                embed.add_field(name=basardino_r.field_name, value=basardino_r.field_value)
                await message.channel.send(embed=embed)

            # Falls der Index / eventuell die ganze Nachricht ungültig ist
            except:
                await message.channel.send(f"Ungültiger Index, **{message.author.name}**!")

            await message.delete()
            print(f"{message.author.name} hat sich einen Gegenstand aus dem Basar angesehen.")


        if message.content.lower().startswith(",selltobasar"):
            await message.delete()

            if True:
                angaben = message.content.split(" ")
                dino_preis = int(angaben[1])

                if dino_preis < 0:
                    dino_preis = 0

                with open(f"Datenbank/{message.channel.guild.name}/AAAbasar.txt", mode="r",
                          encoding="utf-8") as bas:
                    basar = json.load(bas)

                with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="r", encoding="utf-8") as inv:
                    inventar = json.load(inv)

                ausgewahlter_dinoo = inventar[message_author][int(angaben[2]) - 1]  # type str
                ausgewahlter_dino = eval(ausgewahlter_dinoo)
                basarshit_dic = {}
                basarshit_dic[ausgewahlter_dino.variablen_name] = [int(dino_preis), message_author]

                basar["basar"].append(basarshit_dic)
                del inventar[message_author][int(angaben[2]) - 1]

                with open(f"Datenbank/{message.channel.guild.name}/AAAbasar.txt", mode="w",
                          encoding="utf-8") as bas:
                    json.dump(basar, bas)

                with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="w", encoding="utf-8") as inv:
                    json.dump(inventar, inv)

                await message.channel.send(
                    f"**{message.author.name}**, du hast erfolgreich **{ausgewahlter_dino.field_name}** für **{dino_preis}** auf den Basar gestellt!")
                print(f"{message.author.name} hat einen Gegenstand auf den Basar gestellt.")

            else:
                await message.channel.send(
                    f"Ungültige Angaben, **{message.author.name}**!\n*,selltobasar + Preis + Index des Gegnstands aus eurem Inventar*")


        if message.content.lower().startswith(",claim"):
            await message.delete()

            # wenn Angaben richtig
            try:
                gegeben_index = int(message.content.split(" ")[1])

                with open(f"Datenbank/{message.channel.guild.name}/AAAbasar.txt", mode="r",
                          encoding="utf-8") as bas:
                    basar = json.load(bas)

                with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="r", encoding="utf-8") as inv:
                    inventar = json.load(inv)

                objekt = basar["basar"][gegeben_index - 1]  # type dic
                owner = ""
                vari_name = ""

                for k, v in objekt.items():
                    vari_name = k
                    owner = v[-1]

                if owner == message_author:
                    inventar[message_author].append(vari_name)

                    for _, v in objekt.items():
                        del v[0]
                        del v[-1]

                    del basar["basar"][gegeben_index - 1]
                    print(f"{message.author.name} hat sich einen Dino aus dem Basar zurückgeholt.")
                    await message.channel.send(
                        f"**{message.author.name}**, du hast erfolgreich ein Item aus dem Basar abgeholt!")

                else:
                    await message.channel.send(
                        f"Das ist nicht dein Dino **{message.author.name}**, der gehört {owner}")

                with open(f"Datenbank/{message.channel.guild.name}/AAAbasar.txt", mode="w",
                          encoding="utf-8") as bas:
                    json.dump(basar, bas)

                with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="w", encoding="utf-8") as inv:
                    json.dump(inventar, inv)

            # wenn Angaben falsch
            except:
                await message.channel.send(
                    f"Ungültige Eingabe **{message.author.name}**!\n*,claim + Index des vom Basar abzuholenden Gegenstandes*")


        if message.content.lower().startswith(",selltobank"):
            await message.delete()

            try:
                angaben = message.content.split(" ")

                with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="r", encoding="utf-8") as inv:
                    inventar = json.load(inv)

                with open(f"Datenbank/{message.channel.guild.name}/AAAKK.txt", mode="r",
                          encoding="utf-8") as user_kk:
                    kronen_anzahl = json.load(user_kk)

                ausgewahlter_dinoo = inventar[message_author][int(angaben[1]) - 1]  # type str
                ausgewahlter_dino = eval(ausgewahlter_dinoo)
                verkaufbar = True
                verkaufs_preis = 0

                # Geld für die jeweilige rarität hinzufügen
                if ausgewahlter_dino.description == "Ein gewöhnlicher Gegenstand!":
                    kronen_anzahl[message_author] += 30
                    verkaufs_preis = 30

                elif ausgewahlter_dino.description == "Ein ungewöhnlicher Gegenstand!":
                    kronen_anzahl[message_author] += 40
                    verkaufs_preis = 40

                elif ausgewahlter_dino.description == "Ein seltener Gegenstand!":
                    kronen_anzahl[message_author] += 50
                    verkaufs_preis = 50

                elif ausgewahlter_dino.description == "Ein epischer Gegenstand!":
                    kronen_anzahl[message_author] += 70
                    verkaufs_preis = 70

                elif ausgewahlter_dino.description == "Ein legendärer Gegenstand!":
                    kronen_anzahl[message_author] += 100
                    verkaufs_preis = 100

                else:
                    verkaufbar = False
                    await message.channel.send(f"**Dieser Gegenstand ist nicht verkaufbar!**")

                if verkaufbar:
                    del inventar[message_author][int(angaben[1]) - 1]

                    with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="w",
                              encoding="utf-8") as inv:
                        json.dump(inventar, inv)

                    with open(f"Datenbank/{message.channel.guild.name}/AAAKK.txt", mode="w",
                              encoding="utf-8") as user_kk:
                        json.dump(kronen_anzahl, user_kk)

                    await message.channel.send(
                        f"**{message.author.name}**, du hast erfolgreich **{ausgewahlter_dino.field_name}** für **{verkaufs_preis}** verkauft!")
                    print(f"{message.author.name} hat ein Items an die Bank verkauft.")

            except:
                await message.channel.send(
                    f"Ungültige Angaben, **{message.author.name}**!\n*,selltobank + Index des Gegenstandes aus eurem Inventar*")


        if message.content.lower().startswith(",buy"):
            await message.delete()

            try:
                buy_dino_i = int(message.content.split(" ")[1])

                with open(f"Datenbank/{message.channel.guild.name}/AAAbasar.txt", mode="r",
                          encoding="utf-8") as bas:
                    basar = json.load(bas)

                with open(f"Datenbank/{message.channel.guild.name}/AAAKK.txt", mode="r",
                          encoding="utf-8") as user_kk:
                    kronen_anzahl = json.load(user_kk)

                with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="r", encoding="utf-8") as inv:
                    inventar = json.load(inv)

                kaufen_dinoo = basar["basar"][int(buy_dino_i) - 1]  # type dic
                dinoname = ""
                preis = ""
                owner = ""

                # Dino Eigenschaften erhalten, das geht hier weil pro dic nur ein Dino enthalten ist
                for k, v in kaufen_dinoo.items():
                    dinoname = k
                    preis = int(v[0])
                    owner = v[1]

                # Zu class dino umformatieren
                kaufen_dino = eval(dinoname)

                # Wemm der Nutzer genug Kronen hat
                if kronen_anzahl[message_author] >= preis:
                    # Kronen abziehen und owner hinzufügen
                    kronen_anzahl[message_author] -= preis
                    kronen_anzahl[owner] += preis

                    # Dino ins inventar hinzufügen und Preis löschen
                    inventar[message_author].append(kaufen_dino.variablen_name)
                    del basar["basar"][int(buy_dino_i) - 1]

                    await message.channel.send(embed=kaufen_dino.embed())
                    await message.channel.send(
                        f"**{message.author.name}**, du hast erfolgreich **{kaufen_dino.field_name}** für **{preis}** {KK} gekauft!")

                # wenn nicht genug kronen
                else:
                    await message.channel.send(f"{message_author} du hast nicht genug {KK}!")

                # txts wieder auffüllen
                with open(f"Datenbank/{message.channel.guild.name}/AAAbasar.txt", mode="w",
                          encoding="utf-8") as bas:
                    json.dump(basar, bas)

                with open(f"Datenbank/{message.channel.guild.name}/AAAKK.txt", mode="w",
                          encoding="utf-8") as user_kk:
                    json.dump(kronen_anzahl, user_kk)

                with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="w", encoding="utf-8") as inv:
                    json.dump(inventar, inv)

                print(f"{message.author.name} hat sich einen Dino vom Basar gekauft")

            # invalide eingabe
            except:
                await message.channel.send(
                    f"Invalide eingabe **{message.author.name}**. \n*,buy + Index des zu kaufenden Gegenstandes!*")


        # Ich habe vergessen Kommentare beim coden zu schreiben und kein Plan wie ich das beschreiben soll
        if message.content.lower().startswith(",inventar"):
            await message.delete()

            try:
                with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="r", encoding="utf-8") as inv:
                    description = ""
                    desc_list = []
                    inventar_index = 1
                    try:
                        seite = int(message.content.split(" ")[1]) - 1

                        if seite < 0:
                            seite = 0
                    except:
                        seite = 0

                    seiteoderso = seite * 25
                    seiten_index = seiteoderso - 24
                    inventar = json.load(inv)

                if message_author not in inventar:
                    description = "Du hast noch keine Gegenstände besessen!"

                elif not inventar[message_author]:
                    description = "Dein Inventar ist leer!"

                else:
                    for d in inventar[message_author]:
                        dino_obj = eval(d)
                        desc_list.append(f"**{inventar_index}** - {dino_obj.field_name}\n")
                        inventar_index += 1

                    for e in range(len(desc_list)):
                        try:
                            if seiten_index <= seiteoderso:
                                description += desc_list[e + seiteoderso]
                                seiten_index += 1
                        except:
                            break

                if description == "":
                    description = "Auf dieser Seite befindet sich nichts!"

                embed = dc.Embed(title=f"**Inventar von {message.author.name}**", colour=dc.Colour(0xbdba6f),
                                 description=description)
                embed.set_footer(text=f"Seite {seite + 1}")

                await message.channel.send(embed=embed)
                print(f"{message.author.name} hat sich sein Inventar ausgeben lassen.")


            except:
                await message.channel.send(
                    f"**{message.author.name}** so geht das nicht!\n*,inventar + auszugebende Seitenzahl*")


        if message.content.lower().startswith(",invitem"):
            await message.delete()

            with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="r", encoding="utf-8") as inv:
                inventar = json.load(inv)

            # Versuchen ob der index gültig ist
            try:
                # index des Dinos finden
                index = message.content.split(" ")[1]
                auszugebener_dino = inventar[message_author][int(index) - 1]
                obj_auszugebener_dino = eval(auszugebener_dino)

                # dino senden und Nahcricht löschen
                await message.channel.send(embed=obj_auszugebener_dino.embed())

            # Falls der Index / eventuell die ganze Nachricht ungültig ist
            except:
                await message.channel.send(f"Ungültiger Index, **{message.author.name}**!")

            print(f"{message.author.name} hat versucht sich einen Dino aus seinem Inventar angesehen.")


        if message.content.lower() == ",help":
            await message.delete()

            embed = dc.Embed(title="Hilfe zum Bot", colour=dc.Colour(0x221f41),
                             description="**,helpKK**\nErfahrt mehr über Kjell Kronen!\n\n"
                                         "**,helpitems**\nAlles was ihr über Gegenstände wissen müsst!\n\n"
                                         "**,helpbasar**\nAlles zum Basar!\n\n**,vorschlag**\nSchlage features "
                                         "für den Bot vor!")

            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/912362937077891132/925022001121345576/axolotl.jpg")
            embed.set_footer(text=",help", icon_url="https://cdn.discordapp.com/attachments/912362937077891132/914146351548338216/KK_real.png")
            await message.channel.send(embed=embed)
            print("Es wurde ein help Befehl genutzt")


        if message.content.lower() == ",helpkk":
            await message.delete()

            embed = dc.Embed(title="Kjell Kronen", colour=dc.Colour(0xbdba6f),
                             description="**,daily**\nHiermit könnt ihr euch jeden Tag Kronen abholen! Die summe "
                                         "steigert sich alle 5 Tage bis 95 erreicht sind.\n\n**,kk**\nÜberprüft "
                                         "euren Kontostand!")

            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/912362937077891132/914146351548338216/KK_real.png")
            embed.set_footer(text=",helpkk", icon_url="https://cdn.discordapp.com/attachments/912362937077891132/914146351548338216/KK_real.png")
            await message.channel.send(embed=embed)
            print("Es wurde ein help Befehl genutzt")


        if message.content.lower() == ",helpitems":
            await message.delete()

            embed = dc.Embed(title="Gegenstände", colour=dc.Colour(0x126114),
                             description=f"**,gamble**\nGambelt für Items! Es kostet aber 200 {KK}!\n\n**,inventar "
                                         f"*Seitenzahl***\nSchaut welche Items ihr besitzt!\n\n**,invitem *Inventarzahl***"
                                         f"\nGebt euch einen Items aus eurem Inventar aus!\n\n**,raritäten**\n"
                                         f"Erfahrt mehr über die einzelnen Raritäten der Dinos!")

            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/915713506152693872/925347198735097886/dino.png")
            embed.set_footer(text=",helpitems", icon_url="https://cdn.discordapp.com/attachments/912362937077891132/914146351548338216/KK_real.png")
            await message.channel.send(embed=embed)
            print("Es wurde ein help Befehl genutzt")


        if message.content.lower() == ",helpbasar":
            await message.delete()

            embed = dc.Embed(title="Der Basar", colour=dc.Colour(0x6d3619),
                             description="**,basar *Seitenzahl***\nGebt euch den aktuellen Basar aus!\n\n"
                                         "**,selltobasar *Preis* *Inventarzahl***\n"
                                         "Stellt ein Angebot auf den Basar!\n\n**,selltobank *Inventarzahl***\n"
                                         "Verkauft einen Dino an die Bank mit "
                                         "festgelegten Preisen!\n\n**,buy *Basarzahl***\nKauft etwas vom Basar!\n\n"
                                         "**,basitem + *Basarzahl***\nGebt euch einen Dino aus dem Basar "
                                         "aus!\n\n**,claim *Basarzahl***\nHol einen deiner Dinos aus dem "
                                         "Basar wieder zurück!")

            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/912362937077891132/925024725414060052/basar.png")
            embed.set_footer(text=",helpbasar", icon_url="https://cdn.discordapp.com/attachments/912362937077891132/914146351548338216/KK_real.png")
            await message.channel.send(embed=embed)
            print("Es wurde ein help Befehl genutzt")


        # if message.content == ",missionen":
        #     await message.delete()
        #
        #     with open(f"Datenbank/{message.channel.guild.name}/AAAmissionen.txt", mode="r", encoding="utf-8") as mis:
        #         missionen = json.load(mis)
        #
        #     with open(f"Datenbank/{message.channel.guild.name}/AAAmissionen.txt", mode="r", encoding="utf-8") as miss:
        #         missionenE = json.load(miss)
        #
        #     with open(f"Datenbank/{message.channel.guild.name}/AAAKK.txt", mode="r", encoding="utf-8") as user_kk:
        #         kronen_anzahl = json.load(user_kk)
        #
        #     with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="r", encoding="utf-8") as inv:
        #         inventar = json.load(inv)
        #
        #     missionserfolg = False
        #
        #     # Falls noch nie Missionen gehabt
        #     if message_author not in missionen:
        #         zweimaldurchint = 0
        #         missionen[message_author] = []
        #
        #         # 2 mal durchgehen
        #         while zweimaldurchint < 2:
        #
        #             rdm_int = random.randint(0, len(verfugbare_missionen) - 1)
        #             gewahlte_mis = verfugbare_missionen[rdm_int]
        #
        #             # falls mission nicht schon beim ma
        #             if gewahlte_mis not in missionen[message_author]:
        #                 missionen[message_author].append(gewahlte_mis)
        #
        #             # wenn doch schon da ist, neue wählen
        #             else:
        #                 zweimaldurchint -= 1
        #
        #             zweimaldurchint += 1
        #
        #     erfolgstext = f"Herzlichen Glückwunsch, **{message.author.name}**! Du hast **eine Mission " \
        #                   f"abgeschlossen** und gewinnst somit"
        #     kronengewinn = 0
        #
        #     def mission_wieder_hinzufugen(mission):
        #
        #         zweimaldurchint = 0
        #
        #         while zweimaldurchint < 1:
        #             rdm_int = random.randint(0, len(verfugbare_missionen) - 1)
        #             gewahlte_mis = verfugbare_missionen[rdm_int]
        #
        #             if message_author not in missionenE:
        #                 missionenE[message_author] = [mission]
        #
        #             else:
        #                 missionenE[message_author].append(mission)
        #
        #             if gewahlte_mis not in missionen[message_author] and gewahlte_mis not in missionenE[message_author]:
        #                 missionen[message_author].append(gewahlte_mis)
        #
        #             else:
        #                 zweimaldurchint -= 1
        #             zweimaldurchint += 1
        #
        #         missionen[message_author].remove(mission)
        #
        #     if "mission1" in missionen[message_author]:
        #
        #         if "baryonyx" in inventar[message_author]:
        #             if "sarco" in inventar[message_author]:
        #                 if "kaprosuchus" in inventar[message_author]:
        #                     missionserfolg = True
        #                     kronengewinn = 400
        #                     mission_wieder_hinzufugen("mission1")
        #
        #     # soll nur gesendet werden falls keine Mission erfolgreich abgeschlossen wurde
        #     if not missionserfolg:
        #         # Missionen evaluieren
        #         erste_mission = eval(missionen[message_author][0])
        #         zweite_mission = eval(missionen[message_author][1])
        #         description = f"{erste_mission}\n\n{zweite_mission}"
        #
        #         embed = dc.Embed(title=f"Missionen von {message.author.name}", colour=dc.Colour(0x6d3619), description=description)
        #         await message.channel.send(embed=embed)
        #
        #     else:
        #         await message.channel.send(f"{erfolgstext} **{kronengewinn}** {KK}!")
        #         kronen_anzahl[message_author] += kronengewinn
        #
        #     with open(f"Datenbank/{message.channel.guild.name}/AAAKK.txt", mode="w", encoding="utf-8") as user_kk:
        #         json.dump(kronen_anzahl, user_kk)
        #
        #     with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="w", encoding="utf-8") as inv:
        #         json.dump(inventar, inv)
        #
        #     with open(f"Datenbank/{message.channel.guild.name}/AAAmissionen.txt", mode="w", encoding="utf-8") as mis:
        #         json.dump(missionen, mis)
        #
        #     with open(f"Datenbank/{message.channel.guild.name}/AAAmissionenE.txt", mode="w", encoding="utf-8") as miss:
        #         json.dump(missionenE, miss)


        # Anzahl der KK
        if message.content.lower() == ",kk":
            await message.delete()
            print(f"{message.author.name} hat die Anzahl seiner Kjell Kronen angefordert")

            # Kronen Anzahl Laden
            with open(f"Datenbank/{message.channel.guild.name}/AAAKK.txt", mode="r", encoding="utf-8") as user_kk:
                kronen_anzahl = json.load(user_kk)

            # Anzahl ausgeben
            try:
                await message.channel.send(
                    f"**{message.author.name}** hat {kronen_anzahl[message_author]} {KK}")

            # Wenn die Person keine Kronen hat, bzw nicht in die Liste der Leute mit Kronen eingetragen ist
            except:
                await message.channel.send(f"**{message.author.name}** du hast noch keine {KK}")

            print(f"{message.author} hat sich die Anzahl seiner Kjell Kronen ausgeben lassen")


        if message.content.lower() == ",shop":

            await message.delete()
            print(f"{message.author} öffnet den shop")

        async def gamble(message):

            message_author = message.author.mention.replace('!', '')
            KK = ':coin:'

            if message.content.lower() == ",gamble":
                global gewohnliches, ungewohnliches, seltenes, episches, legendares

                await message.delete()
                print(f"{message.author} versucht zu gambeln")

                # Kronenanzahl auslesen
                with open(f"Datenbank/{message.channel.guild.name}/AAAKK.txt", mode="r", encoding="utf-8") as user_kk:

                    kronen_anzahl = json.load(user_kk)

                # Wenn der user genug Kronen hat
                if kronen_anzahl[message_author] > 199:

                    print(f"{message.author} hat erfolgreich gegambelt")

                    # Kronenabziehen und dann gambeln
                    kronen_anzahl[message_author] -= 200

                    # Inventar auslesen
                    with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="r", encoding="utf-8") as inv:

                        inventar = json.load(inv)

                        if message_author not in inventar:
                            inventar[message_author] = []

                    async def inventar_hinzufugen(g_ziehung):

                        # inventar hinzufügen
                        inventar[message_author].append(g_ziehung.variablen_name)

                        await message.channel.send(
                            f"Herzlichen Glückwunsch! Du hast **{g_ziehung.field_name}** gezogen!")

                    gambeled = GambleManager.get_random_dino(message)

                    if gambeled == None:
                        kronen_anzahl[message_author] += 400
                        await message.channel.send(
                            f"Herzlichen Glückwunsch **{message.author.name}**, du hast 400 {KK} "
                            f"erhalten!")

                        return

                    await message.channel.send(embed=gambeled.embed())
                    await inventar_hinzufugen(gambeled)

                    # Neue Kronenanzahl niederschreiben
                    with open(f"Datenbank/{message.channel.guild.name}/AAAKK.txt", mode="w",
                              encoding="utf-8") as user_kk:

                        json.dump(kronen_anzahl, user_kk)

                    # Zum Inventar hinzufügen
                    with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="w", encoding="utf-8") as inv:

                        json.dump(inventar, inv)

                # Wenn der user nicht genug Kronen hat
                else:
                    print(f"{message.author} hat nicht erfolgreich gegambled")
                    await message.channel.send(f"**{message.author.name}** du hast nicht genug {KK} zum Gambeln!")

                gamble(message)


        if message.content.lower() == ",daily":
            if nutzer_erlaubt():
                # Allgemeines
                await message.delete()

                # Wurde es heute schon angefordert?
                with open(f"Datenbank/{message.channel.guild.name}/AAAdailytime.txt",
                          encoding="utf-8") as daily_time:

                    date = json.load(daily_time)

                today = datetime.date.today()
                tdelta = datetime.timedelta(days=1)
                yeday = today - tdelta

                if message_author not in date:
                    date[message_author] = "0"

                # Wenn heute schon abgeholt
                if date[message_author] == str(today):
                    await message.channel.send(
                        f"**{message.author.name}**, du hast deine {KK} heute schon abgeholt!")

                # Wenn heute noch nicht abgeholt
                else:

                    # Kronen Anzahl der Nutzer auslesen
                    with open(f"Datenbank/{message.channel.guild.name}/AAAKK.txt", mode="r") as user_kk:
                        kronen_anzahl = json.load(user_kk)

                    # streak auslesen
                    with open(f"Datenbank/{message.channel.guild.name}/AAAstreak.txt", mode="r") as stre:
                        streak = json.load(stre)

                    # wenn noch nie abgeholt
                    if message_author not in kronen_anzahl:
                        kronen_anzahl[message_author] = int(300)

                    erhalt = 65

                    # Falls das Datum nicht gestern und damit die Streak unterbrochen ist
                    if not date[message_author] == str(yeday):
                        streak[message_author] = 1
                        kronen_anzahl[message_author] += erhalt

                    # Falls das Datum gestern ist und die streak damit läuft
                    else:
                        try:
                            streak[message_author] += 1
                        except:
                            streak[message_author] = 1

                        if streak[message_author] < 4:
                            kronen_anzahl[message_author] += 65
                        elif streak[message_author] < 9:
                            kronen_anzahl[message_author] += 70
                            erhalt = 70
                        elif streak[message_author] < 14:
                            kronen_anzahl[message_author] += 75
                            erhalt = 75
                        elif streak[message_author] < 19:
                            kronen_anzahl[message_author] += 80
                            erhalt = 80
                        elif streak[message_author] < 24:
                            kronen_anzahl[message_author] += 85
                            erhalt = 85
                        elif streak[message_author] < 29:
                            kronen_anzahl[message_author] += 90
                            erhalt = 90
                        else:
                            kronen_anzahl[message_author] += 95
                            erhalt = 95

                    date[message_author] = str(today)

                    # Kronen Anzahl hinzufügen
                    with open(f"Datenbank/{message.channel.guild.name}/AAAKK.txt", mode="w") as user_kk:
                        json.dump(kronen_anzahl, user_kk)

                    # Alte Zeit löschen und aktuallisierte hinschreiben
                    with open(f"Datenbank/{message.channel.guild.name}/AAAdailytime.txt", "w") as daily_time:
                        json.dump(date, daily_time)

                    # Kronen Anzahl der Nutzer auslesen
                    with open(f"Datenbank/{message.channel.guild.name}/AAAstreak.txt", mode="w") as stre:
                        json.dump(streak, stre)

                    print(f"{message.author} hat seine täglichen 65 Kjell Kronen eingefordert")

                    await message.channel.send(
                        f"Glückwunsch **{message.author.name}**, du hast deine täglichen **{erhalt}** {KK} "
                        f"eingefordert! Deine Streak beträgt nun **{streak[message_author]}** :fire:!")


        if message.content.lower() == ",raritäten":
            await message.delete()

            embed = dc.Embed(title="Infos über die Raritäten", colour=dc.Colour(0x6d3619),
                             description=f"**Gewöhnlich {w_b}**\nSie sind für **30** {KK} an die Bank verkaufbar. "
                                         f"Die Wahrscheinlichkeit einen zu ziehen liegt bei **45%**.\n\n**Ungewöhnlich "
                                         f"{g_b}**\nSie sind für **40** {KK} an die Bank verkaufbar. Die "
                                         f"Wahrscheinlichkeit einen zu ziehen liegt bei **25%**.\n\n**Selten "
                                         f"{b_b}**\nSie sind für **50** {KK} an die Bank verkaufbar. "
                                         f"Die Wahrscheinlichkeit einen zu ziehen liegt bei **20%**.\n\n**Episch "
                                         f"{p_b}**\nSie sind für **70** {KK} an die Bank verkaufbar. "
                                         f"Die Wahrscheinlichkeit einen zu ziehen liegt bei **7,5%**.\n\n**Kjell "
                                         f"Kronen {KK}**\nMit einer **2%** chance ziehst du **400** Kjell Kronen anstatt "
                                         f"eines Dinos.\n\n**Legendär "
                                         f"{star}**\nSie sind für **100** {KK} an die Bank verkaufbar. "
                                         f"Die Wahrscheinlichkeit einen zu ziehen liegt bei **0,5%**.\n\n**Sonderrang "
                                         f"{sr}**\nSie sind nicht an die Bank verkaufbar. Man kann sie nicht ziehen, "
                                         f"nur durch Events erhalten. Jedes gibt es nur einmal.")

            await message.channel.send(embed=embed)


        if message.content.lower().startswith(",vorschlag"):
            await message.delete()

            vorschlag = message.content.split("g", maxsplit=1)[1]

            with open(f"Datenbank/{message.channel.guild.name}/AAAvorschläge.txt", mode="a",
                      encoding="utf-8") as vorschlage:
                vorschlage.write(f"{message.author.name} hat vorgeschlagen: {vorschlag}\n\n")

            print(f"{message.author.name} hat etwas erfolgreich vorgeschlagen.")
            await message.channel.send(f"Du hast den Vorschlag erfolgreich eingereicht.")


        # if message.content.lower().startswith(",einreichung-"):
        #     await message.delete()
        #
        #     vorschlag = message.content.split("-", maxsplit=1)[1]
        #
        #     with open(f"Datenbank/{message.channel.guild.name}/AAAeinreichungen.txt", mode="a",
        #               encoding="utf-8") as vorschlage:
        #         vorschlage.write(f"{message.author.name} hat eingereicht: {vorschlag}\n\n")
        #
        #     print(f"{message.author.name} hat etwas erfolgreich eingereicht.")
        #     await message.channel.send(f"Du hast erfolgreich etwas eingereicht.")


        # if message.content.lower().startswith(",vote-"):
        #     await message.delete()
        #
        #     vorschlag = message.content.split("-", maxsplit=1)[1]
        #
        #     with open(f"Datenbank/{message.channel.guild.name}/AAAvotes.txt", mode="a",
        #               encoding="utf-8") as vorschlage:
        #         vorschlage.write(f"{message.author.name} hat gevotet: {vorschlag}\n\n")
        #
        #     print(f"{message.author.name} hat erfolgreich gevotet.")
        #     await message.channel.send(f"Du hast erfolgreich gevotet.")


        if message.content.lower().startswith(",give") and message_author == "<@588407314772525196>":
            await message.delete()

            try:
                angaben = message.content.split(" ")
                zulieferant = angaben[1].replace("!", "")
                verschenktes = angaben[2]

                # Falls Kronen
                try:

                    verschenkte_kronen = int(verschenktes)
                    with open(f"Datenbank/{message.channel.guild.name}/AAAKK.txt", mode="r",
                              encoding="utf-8") as user_kk:
                        kronen_anzahl = json.load(user_kk)
                        try:
                            kronen_anzahl[zulieferant] += verschenkte_kronen
                        except:
                            verschenkte_kronen += 300
                            kronen_anzahl[zulieferant] = verschenkte_kronen

                    with open(f"Datenbank/{message.channel.guild.name}/AAAKK.txt", mode="w",
                              encoding="utf-8") as user_kk:
                        json.dump(kronen_anzahl, user_kk)

                    print(f"Es wurden {zulieferant} erfolgreich {verschenktes} Kronen gegeben")
                    await message.channel.send(
                        f"Du hast erfolgreich {zulieferant} **{verschenktes}** {KK} gegeben!")

                # Falls Dino
                except:

                    # Zum Inventar hinzufügen
                    with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="r",
                              encoding="utf-8") as inv:
                        inventar = json.load(inv)
                        # nur zum Prüfen ob es das Objekt gibt
                        klassen_dino = eval(verschenktes)
                        try:
                            inventar[zulieferant].append(verschenktes)

                        except:
                            inventar[zulieferant] = []
                            inventar[zulieferant].append(verschenktes)

                    with open(f"Datenbank/{message.channel.guild.name}/AAAinv.txt", mode="w",
                              encoding="utf-8") as inv:
                        json.dump(inventar, inv)

                    print(f"Es wurde {zulieferant} erfolgreich {verschenktes} gegeben")
                    await message.channel.send(
                        f"Du hast erfolgreich {zulieferant} **{klassen_dino.field_name}** gegeben!")

            except:
                await message.channel.send(
                    f"So geht das nicht man\n*,give + zu gebende Person + dino variablen Name*")  # das dritte zeichen in der mention ist ein Ausrufezeichen


client = MyClient()
client.run(TOKEN)
