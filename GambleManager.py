from Dinos import Dino
import random

def get_random_dino(message):
    grey = 0x777777
    green = 0x359b15
    blue = 0x1e72e6
    purple = 0x8227da
    yellow = 0xc0b838
    red = 0xa13316

    # pull texte
    gewohnlich_text = "Ein gewöhnlicher Gegenstand!"
    ungewohnlich_text = "Ein ungewöhnlicher Gegenstand!"
    selten_text = "Ein seltener Gegenstand!"
    episch_text = "Ein epischer Gegenstand!"
    legendar_text = "Ein legendärer Gegenstand!"
    sonderrang_text = "Ein Objekt der ganz besonderen Art."

    # hinternamen emojis
    w_b = ":white_circle:"
    g_b = ":green_circle:"
    b_b = ":blue_circle:"
    p_b = ":purple_circle:"
    star = ":star:"
    sr = ":secret:"

    # gewöhnlich

    beelzebufo = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "beelzebufo",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809514506457098/5_beelzebufo_R.jpeg",
                      f"Beelzebufo {w_b}", "Ein sehr großer Frosch.")

    iguanodon = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "iguanodon",
                     "https://cdn.discordapp.com/attachments/915713506152693872/922809515236282428/5_iguanodon_R.jpeg",
                     f"Iguanodon {w_b}", "Schnell und charmant.")

    baryonyx = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "baryonyx",
                    "https://cdn.discordapp.com/attachments/915713506152693872/922809260071591996/5_baryonyx_R.jpeg",
                    f"Baryonyx {w_b}", "Wie ein Krokodil, aber orange.")

    dimorphodon = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "dimorphodon",
                       "https://cdn.discordapp.com/attachments/915713506152693872/922809260419710986/5_dimorphodon_R.jpeg",
                       f"Dimorphodon {w_b}", "Fledermaus mit Flügeln und großer Fresse.")

    glowtail = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "glowtail",
                    "https://cdn.discordapp.com/attachments/915713506152693872/922809260742684742/5_glowtail_R.jpeg",
                    f"Glowtail {w_b}", "Eine Eidechse mit kleinen Flügeln.")

    mesopithecus = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "mesopithecus",
                        "https://cdn.discordapp.com/attachments/915713506152693872/922809261090807808/5_mesopithecus_R.jpeg",
                        f"Mesopithecus {w_b}", "Eine Art Urmensch.")

    plesiosaur = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "plesiosaur",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809261371842570/5_plesiosaur_R.jpeg",
                      f"Plesiosaur {w_b}", "Eine Schildkröte, aber 50 mal größer.")

    troodon = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "troodon",
                   "https://cdn.discordapp.com/attachments/915713506152693872/922809261665439754/5_troodon_R.jpeg",
                   f"Troodon {w_b}", "Eine Mischung aus Vogel und Echse.")

    archaeopteryx = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "archaeopteryx",
                         "https://cdn.discordapp.com/attachments/915713506152693872/922809318208843806/5_archaeopteryx_R.jpeg",
                         f"Archaeopteryx {w_b}", "Vögel mit sehr platten Armen.")

    dilophosaur = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "dilophosaur",
                       "https://cdn.discordapp.com/attachments/915713506152693872/922809318833811456/5_dilophosaur_R.jpeg",
                       f"Dilophosaur {w_b}", "Schlagen, treten, häuten.")

    giantbee = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "giantbee",
                    "https://cdn.discordapp.com/attachments/915713506152693872/922809319299375104/5_giantbee_R.jpeg",
                    f"Giantbee {w_b}", "Mein Lieblingspokemon.")

    megatherium = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "megatherium",
                       "https://cdn.discordapp.com/attachments/915713506152693872/922809319626518548/5_megatherium_R.jpeg",
                       f"Megatherium {w_b}", "Das Urzeit Schnabeltier.")

    pelagornis = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "pelagornis",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809320121466920/5_pelagornis_R.jpeg",
                      f"Pelagornis {w_b}", "Eine Möve mit einer sehr hohen Flügelspannweite.")

    trilobite = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "trilobite",
                     "https://cdn.discordapp.com/attachments/915713506152693872/922809320935133254/5_trilobite_R.jpeg",
                     f"Trilobite {w_b}", "Ein flaches Meeresmonster.")

    cnidaria = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "cnidaria",
                    "https://cdn.discordapp.com/attachments/915713506152693872/922809356351864882/5_cnidaria_R.jpeg",
                    f"Cnidaria {w_b}", "Eine Qualle made by Ufotable.")

    gasbags = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "gasbags",
                   "https://cdn.discordapp.com/attachments/915713506152693872/922809356704157696/5_gasbags_R.jpeg",
                   f"Gasbags {w_b}", "Keine Made, eine Kuh.")

    mammoth = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "mammoth",
                   "https://cdn.discordapp.com/attachments/915713506152693872/922809357148749844/5_mammoth_R.jpeg",
                   f"Mammoth {w_b}", "Behaart wie ein Elefant.")

    pegomastax = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "pegomastax",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809357454942248/5_pegomastax_R.jpeg",
                      f"Pegomastax {w_b}", "Ist das ein Schnabel?")

    titanomyrma = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "titanomyrma",
                       "https://cdn.discordapp.com/attachments/915713506152693872/922809358063108096/5_titanomyrma_R.jpeg",
                       f"Titanomyrma {w_b}", "Eine Termite.")

    chalicotherium = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "chalicotherium",
                          "https://cdn.discordapp.com/attachments/915713506152693872/922809380498460732/5_chalicotherium_R.jpeg",
                          f"Chalicotherium {w_b}", "Die Arme bruder :heart_eyes:")

    gallimimus = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "gallimimus",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809380901093376/5_gallimimus_R.jpeg",
                      f"Gallimimus {w_b}", "Wie ein Strauß.")

    maewing = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "maewing",
                   "https://cdn.discordapp.com/attachments/915713506152693872/922809381245059102/5_maewing_R.jpeg",
                   f"Maewing {w_b}", "Ein normales Schnabeltier. Oder ist es ...")

    parasaur = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "parasaur",
                    "https://cdn.discordapp.com/attachments/915713506152693872/922809381576404992/5_parasaur_R.jpeg",
                    f"Parasaur {w_b}", "Ein wundervoller Pflanzenfresser.")

    titanoboa = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "titanoboa",
                     "https://cdn.discordapp.com/attachments/915713506152693872/922809381828051005/5_titanoboa_R.jpeg",
                     f"Titanoboa {w_b}", "Eine lange Schlange.")

    carbonemys = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "carbonemys",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809408319266816/5_carbonemys_R.jpeg",
                      f"Carbonemys {w_b}", "Wie hieß dieses 8. gen Pokemon nochmal")

    equus = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "equus",
                 "https://cdn.discordapp.com/attachments/915713506152693872/922809408667389962/5_equus_R.jpeg",
                 f"Equus {w_b}", "Das ist nur ein Zebra.")

    leedsichthys = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "leedsichthys",
                        "https://cdn.discordapp.com/attachments/915713506152693872/922809409002963005/5_leedsichthys_R.jpeg",
                        f"Leedsichthys {w_b}", "Ein Riesenwahl.")

    pachy = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "pachy",
                 "https://cdn.discordapp.com/attachments/915713506152693872/922809409304948796/5_pachy_R.jpeg",
                 f"Pachy {w_b}", "Ein Kopf hart wie Stahl.")

    thylacoleo = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "thylacoleo",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809409648857138/5_thylacoleo_R.jpeg",
                      f"Thylacoleo {w_b}", "Der Frankenstein der Säugetiere.")

    bulbdog = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "bulbdog",
                   "https://cdn.discordapp.com/attachments/915713506152693872/922809438237249546/5_bulbdog_R.jpeg",
                   f"Bulbdog {w_b}", "Ein echter Cutie.")

    direbear = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "direbear",
                    "https://cdn.discordapp.com/attachments/915713506152693872/922809438589562880/5_direbear_R.jpeg",
                    f"Direbear {w_b}", "Wie ein Schwarzbär, aber braun.")

    leech = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "leech",
                 "https://cdn.discordapp.com/attachments/915713506152693872/922809438950277120/5_leech_R.jpeg",
                 f"Leech {w_b}", "Ist er 1cm oder 1m lang?")

    onyc = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "onyc",
                "https://cdn.discordapp.com/attachments/915713506152693872/922809439197753384/5_onyc_R.jpeg",
                f"Onyc {w_b}", "Nicht zum Verzehr geeignet.")

    sabertoothsalmon = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "sabertoothsalmon",
                            "https://cdn.discordapp.com/attachments/915713506152693872/922809439495528468/5_sabertoothsalmon_R.jpeg",
                            f"Sabertoothsalmon {w_b}", "Zum Verzehr geeignet.")

    brontosaurus = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "brontosaurus",
                        "https://cdn.discordapp.com/attachments/915713506152693872/922809483409887242/5_brontosaurus_R.jpeg",
                        f"Brontosaurus {w_b}", "Der ikonische Langhals.")

    diplocaulus = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "diplocaulus",
                       "https://cdn.discordapp.com/attachments/915713506152693872/922809483636383765/5_diplocaulus_R.jpeg",
                       f"Diplocaulus {w_b}", "Ein bisschen wie ein Axolotl.")

    kaprosuchus = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "kaprosuchus",
                       "https://cdn.discordapp.com/attachments/915713506152693872/922809483909005372/5_kaprosuchus_R.jpeg",
                       f"Kaprosuchus {w_b}", "Wie ein Krokodil, aber blau.")

    moschops = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "moschops",
                    "https://cdn.discordapp.com/attachments/915713506152693872/922809484198436874/5_moschops_R.jpeg",
                    f"Moschops {w_b}", "Moppelig und nackt.")

    dinopithecus = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "dinopithecus",
                        "https://cdn.discordapp.com/attachments/915713506152693872/922809514972053574/5_dinopithecus_R.jpeg",
                        f"Dinopithecus {w_b}", "Der altmodische Mensch.")

    mosasaurus = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "mosasaurus",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809515479543829/5_mosasaurus_R.jpeg",
                      f"Mosasaurus {w_b}", "Ein Kiefer mächtig wie von zehn Haien.")

    pulmonoscorpius = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "pulmonoscorpius",
                           "https://cdn.discordapp.com/attachments/915713506152693872/922809515697659904/5_pulmonoscorpius_R.jpeg",
                           f"Pulmonoscorpius {w_b}", "'Scorpius' hätte eigentlich auch gereicht.")

    glowbug = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "glowbug",
                   "https://cdn.discordapp.com/attachments/915713506152693872/934770632674148362/5_glowbug_R.jpeg",
                   f"Glowbug {w_b}", "Grün aber nicht giftig.")

    hyaenodon = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "hyaenodon",
                     "https://cdn.discordapp.com/attachments/915713506152693872/934770633185824828/5_hyaenodon_R.jpeg",
                     f"Hyaenodon {w_b}", "Die Weibchen haben Penisse!")

    lymantria = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "lymantria",
                     "https://cdn.discordapp.com/attachments/915713506152693872/934770633643008000/5_lymantria_R.jpeg",
                     f"Lymantria {w_b}", "Eine Flügelspannweite von 2 Metern!")

    lystrosaurus = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "lystrosaurus",
                        "https://cdn.discordapp.com/attachments/915713506152693872/934770744985010206/5_lystrosaurus_R.jpeg",
                        f"Lystrosaurus {w_b}", "Maschops, aber cooler!")

    meganeura = Dino(f"Eigentum von {message.author.name}", grey, gewohnlich_text, "meganeura",
                     "https://cdn.discordapp.com/attachments/915713506152693872/934770745375072296/5_meganeura_R.jpeg",
                     f"Meganeura {w_b}", "Eine Libelle wie sie heute noch vorkommt.")

    # ungewöhnlich

    liopleurodon = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "liopleurodon",
                        "https://cdn.discordapp.com/attachments/915713506152693872/922809259509575700/4_liopleurodon_R.jpeg",
                        f"Liopleurodon {g_b}", "Ein hundert Mann schneller Dino.")

    sabertooth = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "sabertooth",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809259811569684/4_sabertooth_R.jpeg",
                      f"Sabertooth {g_b}", "Eine uralte Katze.")

    ferox = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "ferox",
                 "https://cdn.discordapp.com/attachments/915713506152693872/922809317734879312/4_ferox_R.jpeg",
                 f"Ferox {g_b}", "Mehr Katze als Hund, aber eigentlich Lemur.")

    pteranodon = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "pteranodon",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809317973975071/4_pteranodon_R.jpeg",
                      f"Pteranodon {g_b}", "Der ikonische Flugdinosaurier.")

    dodicurus = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "dodicurus",
                     "https://cdn.discordapp.com/attachments/915713506152693872/922809355156488223/4_dodicurus_R.jpeg",
                     f"Dodicurus {g_b}", "Man nennt ihn auch Keule.")

    ovis = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "ovis",
                "https://cdn.discordapp.com/attachments/915713506152693872/922809355458465813/4_ovis_R.jpeg",
                f"Ovis {g_b}", "Ein, nicht der Ovis.")

    yutryrannus = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "yutryrannus",
                       "https://cdn.discordapp.com/attachments/915713506152693872/922809355869499422/4_yutryrannus_R.jpeg",
                       f"Yutyrannus {g_b}", "Sieht aus wie ein Vogel, es ist aber ein Hurensohn.")

    deinonychus = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "deinonychus",
                       "https://cdn.discordapp.com/attachments/915713506152693872/922809379156283442/4_deinonychus_R.jpeg",
                       f"Deinonychus {g_b}", "Ein Raptor aber als Vogel.")

    oviraptor = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "oviraptor",
                     "https://cdn.discordapp.com/attachments/915713506152693872/922809379743473714/4_oviraptor_R.jpeg",
                     f"Oviraptor {g_b}", "Was zum fick")

    yeti = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "yeti",
                "https://cdn.discordapp.com/attachments/915713506152693872/922809380083216464/4_yeti_R.jpeg",
                f"Yeti {g_b}", "Ich glaube den hat es nicht wirklich gegeben.")

    carnotaurus = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "carnotaurus",
                       "https://cdn.discordapp.com/attachments/915713506152693872/922809407102939156/4_carnotaurus_R.jpeg",
                       f"Carnotaurus {g_b}", "Codename Schenkelquetscher.")

    megalosaurus = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "megalosaurus",
                        "https://cdn.discordapp.com/attachments/915713506152693872/922809407438458941/4_megalosaurus_R.jpeg",
                        f"Megalosaurus {g_b}", "...aber wo sind seine Augen?")

    terrorbird = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "terrorbird",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809407925018664/4_terrorbird_R.jpeg",
                      f"Terrorbird {g_b}", "Gesuchter Kopf der Al-Qaida.")

    arthropluera = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "arthropluera",
                        "https://cdn.discordapp.com/attachments/915713506152693872/922809437423554580/4_arthropluera_R.jpeg",
                        f"Arthropluera {g_b}", "Größer als du willst!")

    megaloceros = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "megaloceros",
                       "https://cdn.discordapp.com/attachments/915713506152693872/922809437754908692/4_megaloceros_R.jpeg",
                       f"Megaloceros {g_b}", "Griechisch für großer (mega) Hurensohn (loceros).")

    sinomacrops = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "sinomacrops",
                       "https://cdn.discordapp.com/attachments/915713506152693872/922809437985603624/4_sinomacrops_R.jpeg",
                       f"Sinomacrops {g_b}", "Ein buntes Flugeichhörnchen.")

    anklyosaurus = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "anklyosaurus",
                        "https://cdn.discordapp.com/attachments/915713506152693872/922809482592006154/4_anklyosaurus_R.jpeg",
                        f"Anklyosaurus {g_b}",
                        "Bekannter Redakteur der Kinderserie 'In einem Reich vor unserer Zeit'.")

    megalania = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "megalania",
                     "https://cdn.discordapp.com/attachments/915713506152693872/922809482860458034/4_megalania_R.jpeg",
                     f"Megalania {g_b}", "Eine Eidechse wie sie heute noch vorkommt.")

    shadowmane = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "shadowmane",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809483116306452/4_shadowmane_R.jpeg",
                      f"Shadowmane {g_b}", "Luxtra ist ganz schön scheiße geworden.")

    achatina = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "achatina",
                    "https://cdn.discordapp.com/attachments/915713506152693872/922809513520808006/4_achatina_R.jpeg",
                    f"Achatina {g_b}", "Eine Weinbergschnecke.")

    mantis = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "mantis",
                  "https://cdn.discordapp.com/attachments/915713506152693872/922809513822814208/4_mantis_R.jpeg",
                  f"Mantis {g_b}", "Größer als heute.")

    sarco = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "sarco",
                 "https://cdn.discordapp.com/attachments/915713506152693872/922809514166734878/4_sarco_R.jpeg",
                 f"Sarco {g_b}", "Wie ein Krokodil, aber- ne. Wie ein Krokodil.")

    compy = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "compy",
                 "https://cdn.discordapp.com/attachments/915713506152693872/934770631516504064/4_compy_R.jpeg",
                 f"Compy {g_b}", "Schwach und unproportional dünn, sowie...")

    pachyrhinosaurus = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "pachyrhinosaurus",
                            "https://cdn.discordapp.com/attachments/915713506152693872/934770631843655770/4_pachyrhinosaurus_R.jpeg",
                            f"Pachyrhinosaurus {g_b}", "Mehr Pachy als Rhinozeros.")

    woollyrhino = Dino(f"Eigentum von {message.author.name}", green, ungewohnlich_text, "woollyrhino",
                       "https://cdn.discordapp.com/attachments/915713506152693872/934770632082718760/4_woollyrhino_R.jpeg",
                       f"Woollyrhino {g_b}", "Ein Horn aus dem man wunderschöne Klaviere bauen kann.")

    # selten

    featherlight = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "featherlight",
                        "https://cdn.discordapp.com/attachments/915713506152693872/922809258666516480/3_featherlight_R.jpeg",
                        f"Featherlight {b_b}", "Ein Vogel mit einem schönen Federkleid.")

    tusoteuthis = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "tusoteuthis",
                       "https://cdn.discordapp.com/attachments/915713506152693872/922809259186606100/3_tusoteuthis_R.jpeg",
                       f"Tusoteuthis {b_b}", "Der Herrscher der Ozeane. Doch stärker als ein Megalodon?")

    basilisk = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "basilisk",
                    "https://cdn.discordapp.com/attachments/915713506152693872/922809317139304468/3_basilisk_R.jpeg",
                    f"Basilisk {b_b}", "Der Herrscher der Schlangen.")

    triceratops = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "triceratops",
                       "https://cdn.discordapp.com/attachments/915713506152693872/922809317441282069/3_triceratops_R.jpeg",
                       f"Triceratops {b_b}", "Ein ikonischer Pflanzenfresser.")

    astrocetus = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "astrocetus",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809354204348436/3_astrocetus_R.jpeg",
                      f"Astrocetus {b_b}", "Im Wolkenmeer unterwegs.")

    therizinosaurus = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "therizinosaurus",
                           "https://cdn.discordapp.com/attachments/915713506152693872/922809354665730078/3_therizinosaurus_R.jpeg",
                           f"Therizinosaurus {b_b}",
                           "Jedes Jahr werden für Thanksgiving mehr als 100 Millionen von ihnen verzehrt.")

    allosaurus = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "allosaurus",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809378099306516/3_allosaurus_R.jpeg",
                      f"Allosaurus {b_b}", "Sieht aus wie aus Lego.")

    spinosaur = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "spinosaur",
                     "https://cdn.discordapp.com/attachments/915713506152693872/922809378518732800/3_spinosaur_R.jpeg",
                     f"Spinosaur {b_b}", "Er ist eigentlich ganz zarm.")

    snowowl = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "snowowl",
                   "https://cdn.discordapp.com/attachments/915713506152693872/922809406725443634/3_snowowl_R.jpeg",
                   f"Snowowl {b_b}", "Eine Majestetische Eule.")

    otter = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "otter",
                 "https://cdn.discordapp.com/attachments/915713506152693872/922809437113163776/3_otter_R.jpeg",
                 f"Otter {b_b}", "Er hat eifach einen Hut digga")

    megalodon = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "megalodon",
                     "https://cdn.discordapp.com/attachments/915713506152693872/922809482185166928/3_megalodon_R.jpeg",
                     f"Megalodon {b_b}", "Der Herrscher der Ozeane. Doch stärker als ein Tusoteuthis?")

    griffin = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "griffin",
                   "https://cdn.discordapp.com/attachments/915713506152693872/922809513139134494/3_griffin_R.jpeg",
                   f"Griffin {b_b}", "Ein Family Guy.")

    astrodelphis = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "astrodelphis",
                        "https://cdn.discordapp.com/attachments/915713506152693872/934770631013171280/3_astrodelphis_R.jpeg",
                        f"Astrodelphis {b_b}", "Eng verwandt mit dem Astrocetus.")

    diplodocus = Dino(f"Eigentum von {message.author.name}", blue, selten_text, "diplodocus",
                      "https://cdn.discordapp.com/attachments/915713506152693872/934770631260667924/3_diplodocus_R.jpeg",
                      f"Diplodocus {b_b}", "Ein weiterer Langhals.")

    # episch

    t_rex = Dino(f"Eigentum von {message.author.name}", purple, episch_text, "t_rex",
                 "https://cdn.discordapp.com/attachments/915713506152693872/922809481870577694/2_rex_R.jpeg",
                 f"T-Rex {p_b}", "So groß wie er ikonisch ist. *Der* Fleischfresser!")

    phoenix = Dino(f"Eigentum von {message.author.name}", purple, episch_text, "phoenix",
                   "https://cdn.discordapp.com/attachments/915713506152693872/922809269622022144/2_phoenix_R.jpeg",
                   f"Phoenix {p_b}", "Ein unsterblicher und majestetischer Vogel.")

    manticore = Dino(f"Eigentum von {message.author.name}", purple, episch_text, "manticore",
                     "https://cdn.discordapp.com/attachments/915713506152693872/922809320012398592/2_manticore_R.jpeg",
                     f"Manticore {p_b}", "Der Frankenstein der Tierwelt.")

    magmasaur = Dino(f"Eigentum von {message.author.name}", purple, episch_text, "magmasaur",
                     "https://cdn.discordapp.com/attachments/915713506152693872/922809356217634846/2_magmasaur_R.jpeg",
                     f"Magmasaur {p_b}", "Der Herr des Feuers.")

    giganotosaurus = Dino(f"Eigentum von {message.author.name}", purple, episch_text, "giganotosaurus",
                          "https://cdn.discordapp.com/attachments/915713506152693872/922809386949287936/2_giganotosaurus_R.jpeg",
                          f"Giganotosaurus {p_b}", "Sogar stärker als der T-Rex.")

    dodo = Dino(f"Eigentum von {message.author.name}", purple, episch_text, "dodo",
                "https://cdn.discordapp.com/attachments/915713506152693872/922809407719489566/2_dodo_R.jpeg",
                f"Dodo {p_b}", "Nimm es, zerknüll es, wirf es.")

    wyvern = Dino(f"Eigentum von {message.author.name}", purple, episch_text, "wyvern",
                  "https://cdn.discordapp.com/attachments/915713506152693872/922809406297628672/2_wyvern_R.jpeg",
                  f"Wyvern {p_b}", "Der legendären Wyvern Queen direkt untergestellt.")

    argentavis = Dino(f"Eigentum von {message.author.name}", purple, episch_text, "argentavis",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809440141455440/2_argentavis_R.jpeg",
                      f"Argentavis {p_b}", "50 mal größer als jeder Adler.")

    titanosaur = Dino(f"Eigentum von {message.author.name}", purple, episch_text, "titanosaur",
                      "https://cdn.discordapp.com/attachments/915713506152693872/922809436844748830/2_titanosaur_R.jpeg",
                      f"Titanosaur {p_b}", "Groß, wirklich sehr sehr groß.")

    raptor = Dino(f"Eigentum von {message.author.name}", purple, episch_text, "raptor",
                  "https://cdn.discordapp.com/attachments/915713506152693872/922809512778412042/2_raptor_R.jpeg",
                  f"Raptor {p_b}", "Schnell, klein, gefährlich.")

    megachelon = Dino(f"Eigentum von {message.author.name}", purple, episch_text, "megachelon",
                      "https://cdn.discordapp.com/attachments/915713506152693872/934770630652473394/2_megachelon_R.jpeg",
                      f"Megachelon {p_b}", "Ein Träger der Scheibe.")

    # legendär

    crystalwyvernqueen = Dino(f"Eigentum von {message.author.name}", yellow, legendar_text,
                              "crystalwyvernqueen",
                              "https://cdn.discordapp.com/attachments/915713506152693872/922809512421888000/1_crystalwyvernqueen_R.png",
                              f"Crystal Wyvern Queen {star}",
                              "Die Mutter der Natur und unvorstellbar mächtig. Ist sie aber stärker als der Reaper?")

    reaper = Dino(f"Eigentum von {message.author.name}", yellow, legendar_text, "reaper",
                  "https://cdn.discordapp.com/attachments/915713506152693872/922809481564413982/1_reaper_R.jpeg",
                  f"Reaper {star}",
                  "Man sagt er sei 10.000 Mann stark. Ist er aber stärker als die Wyvern Queen?")

    # Sonderrang

    nameless = Dino(f"Eigentum von {message.author.name}", red, sonderrang_text, "nameless",
                    "https://cdn.discordapp.com/attachments/915713506152693872/928973604945797170/6_nameless.jpeg",
                    f"??? {sr}", "Keine Ahnung was es ist, aber das Sonderrang Objekt zum Release!")

    gewohnliches = [pulmonoscorpius, mosasaurus, dinopithecus, moschops, kaprosuchus, diplocaulus,
                    brontosaurus, sabertoothsalmon, onyc, leech, direbear, bulbdog, thylacoleo, pachy,
                    leedsichthys, equus, carbonemys, titanoboa, parasaur, maewing, gallimimus,
                    chalicotherium, titanomyrma, pegomastax, mammoth, gasbags, cnidaria, trilobite,
                    pelagornis, megatherium, giantbee, dilophosaur, archaeopteryx, troodon, plesiosaur,
                    mesopithecus, glowtail, dimorphodon, baryonyx, iguanodon, beelzebufo, glowbug,
                    hyaenodon, lymantria, lystrosaurus, meganeura]

    ungewohnliches = [sarco, mantis, achatina, shadowmane, megalania, anklyosaurus, sinomacrops,
                      megaloceros, arthropluera, terrorbird, megalosaurus, carnotaurus, yeti, oviraptor,
                      deinonychus, yutryrannus, ovis, dodicurus, pteranodon, ferox,
                      sabertooth, liopleurodon, compy, pachyrhinosaurus, woollyrhino]

    seltenes = [griffin, megalodon, otter, snowowl, spinosaur, allosaurus, therizinosaurus, astrocetus,
                triceratops, basilisk, tusoteuthis, featherlight, astrodelphis, diplodocus]

    episches = [raptor, titanosaur, argentavis, wyvern, dodo, giganotosaurus, magmasaur, manticore,
                phoenix, t_rex, megachelon]

    legendares = [reaper, crystalwyvernqueen]

    random_int = (random.randint(1, 201))
    # Wemm es gewöhnlich ist
    if random_int in range(1, 91):
        print("Es handelt sich um einen gewöhnlichen Dino.")

        # welcher wurde gezogen?
        return gewohnliches[random.randint(0, len(gewohnliches) - 1)]

    # Wenn es ungewöhnlich ist
    elif random_int in range(91, 141):
        print("Es handelt sich um einen ungewöhnlichen Dino.")

        # welcher wurde gezogen?
        return ungewohnliches[random.randint(0, len(ungewohnliches) - 1)]

    # Wenn es selten ist
    elif random_int in range(141, 181):
        print("Es handelt sich um einen seltenen Dino.")

        # welcher wurde gezogen?
        return seltenes[random.randint(0, len(seltenes) - 1)]

    # Wenn es episch ist
    elif random_int in range(181, 196):
        print("Es handelt sich um einen epischen Dino.")

        # welcher wurde gezogen?
        return episches[random.randint(0, len(episches) - 1)]

    # wenn nur Kronen
    elif random_int in range(196, 200):
        print("Einsatz wurde verdoppelt")

        return None

    # wenn es legendär ist
    elif random_int in range(200, 201):
        print("Es handelt sich um einen legendären Dino.")

        # welcher wurde gezogen?
        return legendares[random.randint(0, len(legendares) - 1)]



